# Generated by Django 3.2.6 on 2021-09-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210908_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(blank=True, max_length=90, unique=True),
        ),
    ]