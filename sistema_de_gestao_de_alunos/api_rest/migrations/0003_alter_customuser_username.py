# Generated by Django 4.2.16 on 2024-09-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_customuser_full_name_endereco_cep_endereco_uf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='Anonymous', max_length=255, unique=True),
        ),
    ]
