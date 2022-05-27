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
    company = CompanySerializer(read_only=True)

    class Meta:
        model = CompanyInfo
        fields = ['company','company_name','language','tag']
        depth = 1


class CompanyRetrieveSerializer(CompanyBaseSerializer):
    class Meta:
        model = CompanyInfo
        fields = ['company_name']


class CompanyPOSTSerializer(CompanyBaseSerializer):
    company = CompanySerializer()

    class Meta:
        model = CompanyInfo
        fields = ['company','company_name','language','tag']
        depth = 1
    
    def validate_company(self, value):
        return Company.objects.get(id=value)

    def create(self, validated_data):
        tags = validated_data.pop('tag')
        company = validated_data.pop('company')
        company, created = Company.objects.get_or_create(company['company'])


        companyinfo = CompanyInfo.objects.create(company=company,**validated_data)

        for tag in tags:
            tag, created = Tag.objects.get_or_create(tag['name'])
            companyinfo.tag.add(tag)
        return companyinfo
