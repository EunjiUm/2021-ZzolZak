# Generated by Django 3.1.3 on 2021-08-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='musinsa_shirt',
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
                ('month_1', models.PositiveIntegerField(default=0)),
                ('month_2', models.PositiveIntegerField(default=0)),
                ('month_3', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('value', models.PositiveIntegerField(default=0)),
                ('group', models.CharField(max_length=200)),
                ('positive_value', models.PositiveIntegerField(default=0)),
                ('neutral_value', models.PositiveIntegerField(default=0)),
                ('negative_value', models.PositiveIntegerField(default=0)),
                ('review', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='FashionScore',
        ),
        migrations.DeleteModel(
            name='Ranking',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='SentScore',
        ),
        migrations.DeleteModel(
            name='SentValue',
        ),
    ]
