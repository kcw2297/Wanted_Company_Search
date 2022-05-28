"""
    BaseSerializer안에 현재 CompanyInfo의 필드를 담았습니다.
    이후 확장성을 고려해 다음 serializer를 만들시 상속을 할 예정입니다.
"""

from rest_framework import serializers
from company.models import Tag, Company, CompanyInfo


class TagSerializer(serializers.ModelSerializer):
    """
        BaseSerializer의 nested할 목적입니다
    """
    class Meta:
        model = Tag
        fields = ['id','name']


class CompanySerializer(serializers.ModelSerializer):
    """
        one-to-many relationship인 경우, 해당 필드의 serializer가 필요합니다.
    """
    class Meta:
        model = Company
        fields = ['id']


class CompanyBaseSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    company = CompanySerializer()

    class Meta:
        model = CompanyInfo
        fields = ['company','company_name','language','tag']
        depth = 1


class CompanyRetrieveSerializer(CompanyBaseSerializer):
    class Meta:
        model = CompanyInfo
        fields = ['company_name']


class CompanyPOSTSerializer(CompanyBaseSerializer):
    company = serializers.IntegerField(write_only=True)
  
    class Meta:
        model = CompanyInfo
        fields = ['company', 'company_name', 'language', 'tag']
        depth = 1

    def create(self, validated_data):

        tags = validated_data.pop('tag')
        company = validated_data.pop('company')

        company, _ = Company.objects.get_or_create(id=company)

        """
            companyinfo = CompanyInfo.objects.create(company_id=company, **validated_data)
            다음과 같이 instance대신에 연결하는 FK값으로 주어줘도 됩니다 
            이때 company는 위의 obj을 지우고, validated.pop한 숫자입니다
        """
        companyinfo = CompanyInfo.objects.create(company=company, **validated_data)

        for tag in tags:
            tag, _ = Tag.objects.get_or_create(name=tag['name'])
            companyinfo.tag.add(tag)

        return companyinfo

class CompanyDetailSerializer(CompanyBaseSerializer):
    tag = TagSerializer(read_only=True, many=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = CompanyInfo
        fields = ['company','company_name', 'language', 'tag']
        depth = 1
