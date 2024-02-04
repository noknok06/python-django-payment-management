# Generated by Django 3.2.9 on 2024-02-04 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_contract_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contract_partner',
            field=models.ForeignKey(blank=True, db_column='契約先', null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.company'),
        ),
    ]