# Generated by Django 2.0.2 on 2020-06-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Form Name', max_length=255, unique=True)),
                ('code', models.CharField(db_index=True, help_text='Form Code', max_length=255, unique=True)),
                ('worflow', models.TextField(db_index=True, help_text='Form Workflow Json Field', max_length=255, unique=True)),
                ('structure', models.TextField(db_index=True, help_text='Form Structure Json Field', max_length=255, unique=True)),
                ('tenant', models.ForeignKey(on_delete='cascade', to='tenant.Tenant')),
            ],
        ),
    ]