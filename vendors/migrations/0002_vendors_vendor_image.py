# Generated by Django 4.2.3 on 2023-08-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='vendor_image',
            field=models.ImageField(default='/', upload_to='media/'),
        ),
    ]