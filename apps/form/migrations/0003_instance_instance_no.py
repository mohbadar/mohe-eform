# Generated by Django 2.2.4 on 2020-06-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20200607_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='instance_no',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
