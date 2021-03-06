# Generated by Django 3.2.7 on 2022-04-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0040_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='familiy_code',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_a_priimary_member',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='media-files/patients_profile_images'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(max_length=2000, primary_key=True, serialize=False),
        ),
    ]
