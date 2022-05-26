from company.models import Company, CompanyInfo ,Tag
from company.serializers import BaseSerializer, RetrieveSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CompanyListCreate(APIView):
    """
        미완성: serializer 에러
        Methods = ['GET', 'POST']
        Get: param을 받을 경우 해당 값 반환, 없으면 전체 반환
    """
    def get_queryset(self):
        # language = self.request.headers['x-wanted-language"'] # 이 부분은 배포시 사용됩니다
        language = self.request.headers['Accept-Language'][0:2] # 이 부분은 테스트 목적입니다

        objs = CompanyInfo.objects.filter(language__icontains=language)
        return objs


    def get_serializer(self, param=None):
        if param:
            return RetrieveSerializer
        return BaseSerializer


    def get(self, request):
        objs = self.get_queryset()
        param = request.query_params.get('query', None)

        if param:
            objs = objs.filter(company_name__icontains=param).values('company_name')


        serializer = self.get_serializer(param)
        serializer = serializer(data=objs)

        """
            수정 필요!
            validation에서 False가 나옴
        """
        if serializer.is_valid():
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def post(self, request):
        """
            에러 발생!
            'property' object has no attribute 'copy'
        """
        serializer = self.get_serializer()
        serializer = serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyRetrieve(APIView):
    def get_queryset(self):
        # language = self.request.headers['x-wanted-language"'] # 이 부분은 배포시 사용됩니다
        language = self.request.headers['Accept-Language'][0:2] # 이 부분은 테스트 목적입니다

        objs = CompanyInfo.objects.filter(language__icontains=language)
        return objs


    def get(self, request, pk):
        """
            미완성
        """
        objs = self.get_queryset()
        objs = objs.objects.filter(company_name=pk)


        serializer = BaseSerializer(data=objs)

        if serializer.is_valid():
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)