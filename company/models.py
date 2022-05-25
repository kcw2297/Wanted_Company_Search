"""
    Model 설계:
    개별 company안에 언어별 다른 정보가 포함되어 있습니다.
    이를 구현하기 위해서 company와 companyinfo로 나누어 관리하였습니다. tag또한 언어별로 나누어
    있지만, 테이블 추가 및 join이 많아져 성능 저하를 고려하여서, companyinfo 안에 manytomany로 묶었습니다.
"""

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='태그 이름')

    class Meta:
        db_table = 'Tag'

    def __str__(self):
        return str(self.name)


class Company(models.Model):

    class Meta:
        db_table = 'Company'

    def __str__(self):
        return str(self.company_name)


class CompanyInfo(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='회사')
    company_name = models.CharField(max_length=127, verbose_name='회사 이름')
    language = models.CharField(max_length=2, verbose_name='정보 언어')
    tag = models.ManyToManyField('Tag', verbose_name='연관 태그')

    class Meta:
        db_table = 'CompanyInfo'

    def __str__(self):
        return str(self.company_name)