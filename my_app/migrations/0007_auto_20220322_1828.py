# Generated by Django 3.2.7 on 2022-03-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20220322_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors_location',
            name='id',
        ),
        migrations.RemoveField(
            model_name='doctors_location',
            name='location',
        ),
        migrations.AddField(
            model_name='doctor',
            name='location_id',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='area',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='building_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='city',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='clinic_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='latitude',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='location_id',
            field=models.CharField(default='', max_length=100000000000, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='longitude',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='pin_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctors_location',
            name='state',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
