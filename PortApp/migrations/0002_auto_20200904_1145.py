# Generated by Django 3.0.8 on 2020-09-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
