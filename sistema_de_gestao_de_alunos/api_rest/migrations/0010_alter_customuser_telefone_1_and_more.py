# Generated by Django 4.2.16 on 2024-10-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0009_alter_historico_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='telefone_1',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefone_2',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
