# Generated by Django 3.2.7 on 2022-03-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0021_doctor_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_profile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(default='', upload_to='media-files/doctors_profile_images'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='signature_image',
            field=models.ImageField(default='', upload_to='media-files/doctors_signature_images'),
        ),
    ]
