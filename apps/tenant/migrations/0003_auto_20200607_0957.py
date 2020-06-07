# Generated by Django 2.2.4 on 2020-06-07 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_auto_20200607_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='center',
        ),
        migrations.AddField(
            model_name='center',
            name='template',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenant.Template'),
        ),
    ]