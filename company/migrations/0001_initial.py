# Generated by Django 4.0.4 on 2022-05-25 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='태그 이름')),
            ],
            options={
                'db_table': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=127, verbose_name='회사 이름')),
                ('language', models.CharField(max_length=2, verbose_name='정보 언어')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='회사')),
                ('tag', models.ManyToManyField(to='company.tag', verbose_name='연관 태그')),
            ],
            options={
                'db_table': 'CompanyInfo',
            },
        ),
    ]