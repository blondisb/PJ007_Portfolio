# Generated by Django 3.2.16 on 2022-12-30 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mo_projects',
            name='image',
            field=models.ImageField(upload_to='App_Portfolio/images'),
        ),
    ]
