# Generated by Django 3.1.3 on 2021-08-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20210818_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='FashionScore_ssf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jan', models.PositiveIntegerField(default=0)),
                ('Feb', models.PositiveIntegerField(default=0)),
                ('Mar', models.PositiveIntegerField(default=0)),
                ('Apr', models.PositiveIntegerField(default=0)),
                ('May', models.PositiveIntegerField(default=0)),
                ('June', models.PositiveIntegerField(default=0)),
                ('July', models.PositiveIntegerField(default=0)),
                ('Aug', models.PositiveIntegerField(default=0)),
                ('Sep', models.PositiveIntegerField(default=0)),
                ('Oct', models.PositiveIntegerField(default=0)),
                ('Nov', models.PositiveIntegerField(default=0)),
                ('Dec', models.PositiveIntegerField(default=0)),
                ('ranking_score', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review_seoulstore_shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='FashionScore_shirt',
            new_name='FashionScore',
        ),
        migrations.RenameModel(
            old_name='FashionScore_ssf_shirt',
            new_name='FashionScore_musinsa',
        ),
        migrations.RenameModel(
            old_name='FashionScore_musinsa_shirt',
            new_name='FashionScore_seoulstore',
        ),
        migrations.RenameField(
            model_name='fashionscore_musinsa',
            old_name='score',
            new_name='ranking_score',
        ),
        migrations.RenameField(
            model_name='fashionscore_seoulstore',
            old_name='score',
            new_name='ranking_score',
        ),
    ]
