# Generated by Django 3.2.6 on 2021-09-06 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
