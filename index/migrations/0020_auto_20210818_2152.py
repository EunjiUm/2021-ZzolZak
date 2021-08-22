# Generated by Django 3.1.3 on 2021-08-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20210818_2124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ranking_pants',
            new_name='Ranking_shirt',
        ),
        migrations.DeleteModel(
            name='Ranking_accessory',
        ),
        migrations.RemoveField(
            model_name='fashionscore_shirt',
            name='score',
        ),
        migrations.AddField(
            model_name='fashionscore_musinsa_shirt',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]