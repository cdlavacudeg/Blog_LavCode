# Generated by Django 3.2.6 on 2021-10-01 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210929_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comentarios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comment'),
        ),
    ]