# Generated by Django 4.2.16 on 2024-10-23 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0011_alter_historico_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='cadastrado_no_ensino_medido',
            field=models.BooleanField(default=False),
        ),
    ]
