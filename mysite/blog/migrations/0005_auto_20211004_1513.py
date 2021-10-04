# Generated by Django 3.2.6 on 2021-10-04 20:13

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0004_alter_blog_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='etiquetas',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='comment',
            name='nombre',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
