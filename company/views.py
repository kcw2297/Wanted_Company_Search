from company.models import Company, CompanyInfo ,Tag
from company.serializers import CompanySerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Q

class CompanyAuto(APIView):
    """
        paramater로 query를 받고 해당하는 company를 필터링합니다.
        이후 company_name 필드만 queryset으로 받습니다. 만약 없다면
        None을 반환합니다.
    """
    def get_queryset(self):
        """
            미완성 xxxx
            parameter를 받고 필터링한 값을 반환합니다
        """
        # language = self.request.headers['x-wanted-language"']
        language = self.request.headers['Accept-Language'][0:2]

        param = self.request.query_params.get("query",None)
        if param:
            """
                param을 기준으로 전체 queryset에서 필터링한다
            """
            queryset = Company.objects.filter(company_name__icontains=param) 
            
            queryset = queryset.filter(language=language)
            
            return queryset
        
        return None

    def get_serializer(self):
        return CompanySerializer

    def get(self, request):
        """
            queryset을 가지고 직렬화를 한 후 response합니다. 만약 값이 없다면,
            에러메시지를 보냅니다.
        """
        

        objs = self.get_queryset()    
        serializer = CompanySerializer(objs)
        if serializer.is_valid():
            return Response(serializer.data, status=200)

        return Response({'error message': 'No company has found'})
        
