# Generated by Django 4.2.16 on 2024-10-13 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0010_alter_customuser_telefone_1_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='historico',
            unique_together=set(),
        ),
    ]
