# Generated by Django 3.0.7 on 2020-06-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='student_image',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to=''),
        ),
    ]
