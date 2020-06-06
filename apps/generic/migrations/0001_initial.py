# Generated by Django 2.0.2 on 2020-06-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Name')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('phone', models.CharField(db_index=True, max_length=13, unique=True, verbose_name='Phone')),
                ('message', models.TextField(verbose_name='Message')),
                ('tenant', models.ForeignKey(blank=True, on_delete='cascade', to='tenant.Tenant')),
            ],
        ),
    ]
