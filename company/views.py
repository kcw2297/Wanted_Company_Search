from company.models import Company, CompanyInfo ,Tag
from company.serializers import CompanyBaseSerializer, CompanyRetrieveSerializer, CompanyPOSTSerializer, \
    CompanyDetailSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class APICRUDView():
    def get_queryset(self):
        # language = self.request.headers['x-wanted-language"'] # 이 부분은 배포시 사용됩니다
        language = self.request.headers['Accept-Language'][0:2] # 이 부분은 테스트 목적입니다
        objs = CompanyInfo.objects.filter(language__icontains=language)
        return objs
    
    def get_serializer_class(self):
        param = self.request.query_params.get('query', None)
        if param:
            return CompanyRetrieveSerializer
        if self.request.method == 'POST':
            return CompanyPOSTSerializer
        if self.request.method == 'GET':
            return CompanyDetailSerializer
        return CompanyBaseSerializer

    def get_object(self,name):
        objs = self.get_queryset()
        try:
            objs = objs.get(company_name=name)
            return objs
        except:
            raise ValueError


class CompanyListCreate(APIView, APICRUDView):
    """
        Methods = ['GET', 'POST']
        parameter: query=회사이름 (추가시 해당 회사만 반환)
    """
    
    def get(self, request):
        objs = self.get_queryset()
        param = request.query_params.get('query', None)

        if param:
            objs = objs.filter(company_name__icontains=param).values('company_name')

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
            추가하는 데이터:
            company, company_name, language, tag
        """ 
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyRetrieve(APIView, APICRUDView):
    """
        Method = ['GET']
    """
    def get(self, request, name):
        objs = self.get_object(name)
        
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(objs)

        return Response(serializer.data, status=status.HTTP_200_OK)
