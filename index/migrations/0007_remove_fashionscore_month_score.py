# Generated by Django 3.1.3 on 2021-08-07 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_fashionscore_month_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fashionscore',
            name='month_score',
        ),
    ]
