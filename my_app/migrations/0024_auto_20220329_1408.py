# Generated by Django 3.2.7 on 2022-03-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0023_auto_20220329_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc_loc',
            name='id',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doc_loc',
            name='doc_id',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]