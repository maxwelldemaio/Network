# Generated by Django 3.0.8 on 2020-08-05 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20200804_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]