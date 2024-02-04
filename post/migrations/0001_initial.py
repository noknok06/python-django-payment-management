# Generated by Django 3.2.9 on 2024-02-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_partner', models.CharField(max_length=30, verbose_name='契約先')),
                ('category', models.CharField(blank=True, max_length=30, verbose_name='案件分類')),
                ('title', models.CharField(max_length=30, verbose_name='案件名')),
                ('description', models.TextField(blank=True, verbose_name='契約内容')),
                ('contract_period_st', models.DateField(blank=True, verbose_name='契約開始日')),
                ('contract_period_fi', models.DateField(blank=True, verbose_name='契約終了日')),
                ('contract_method', models.CharField(blank=True, choices=[('１回', '１回'), ('毎月', '毎月'), ('まとめて', 'まとめて')], max_length=20, verbose_name='支払方法')),
                ('approval_flg', models.BooleanField(verbose_name='稟議有無')),
                ('approval_data', models.CharField(blank=True, max_length=300, verbose_name='稟議')),
                ('order_date', models.DateField(blank=True, verbose_name='発注日')),
                ('recording_date', models.DateField(blank=True, verbose_name='計上日')),
                ('status', models.IntegerField(choices=[(0, '見積依頼済'), (1, '見積確認中'), (2, '発注済'), (3, '計上済')], max_length=20, verbose_name='ステータス')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
            ],
        ),
    ]
