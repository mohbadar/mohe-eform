# Generated by Django 2.2.5 on 2019-09-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(editable=False, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Page Title'),
        ),
        migrations.AlterField(
            model_name='pagecategory',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Category Name'),
        ),
    ]
