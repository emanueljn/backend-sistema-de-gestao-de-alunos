# Generated by Django 4.2.16 on 2024-09-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_alter_endereco_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=30),
        ),
    ]
