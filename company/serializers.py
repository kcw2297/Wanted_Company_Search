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
        fields = ['name']


class CompanySerializer(serializers.ModelSerializer):
    """
        one-to-many relationship인 경우, 해당 필드의 serializer가 필요합니다.
    """
    class Meta:
        model = Company
        fields = ['id']


class BaseSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = CompanyInfo
        fields = ['company','company_name','language','tag']