# Generated by Django 5.1 on 2024-10-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='category',
            field=models.CharField(blank=True, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time')], max_length=50, null=True),
        ),
    ]
