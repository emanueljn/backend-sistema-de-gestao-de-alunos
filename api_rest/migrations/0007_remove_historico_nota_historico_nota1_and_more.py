# Generated by Django 4.2.16 on 2024-10-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0006_customuser_data_inscricao_alter_professor_disciplina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historico',
            name='nota',
        ),
        migrations.AddField(
            model_name='historico',
            name='nota1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historico',
            name='nota2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historico',
            name='nota3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historico',
            name='nota4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historico',
            name='nota_final',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='disciplina',
            field=models.CharField(choices=[('MT', 'Matemática'), ('PT', 'Português'), ('HI', 'História'), ('GE', 'Geografia'), ('FI', 'Física'), ('QU', 'Química'), ('BI', 'Biologia')], max_length=2),
        ),
    ]