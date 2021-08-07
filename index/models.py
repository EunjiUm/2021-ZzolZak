from django.db import models

class FashionScore(models.Model):
    Jan = models.PositiveIntegerField(default=0)
    Feb = models.PositiveIntegerField(default=0)
    Mar = models.PositiveIntegerField(default=0)
    Apr = models.PositiveIntegerField(default=0)
    May = models.PositiveIntegerField(default=0)
    June = models.PositiveIntegerField(default=0)
    July = models.PositiveIntegerField(default=0)
    Aug = models.PositiveIntegerField(default=0)
    Sep = models.PositiveIntegerField(default=0)
    Oct = models.PositiveIntegerField(default=0)
    Nov = models.PositiveIntegerField(default=0)
    Dec = models.PositiveIntegerField(default=0)

    month_1 = models.PositiveIntegerField(default=0)
    month_2 = models.PositiveIntegerField(default=0)
    month_3 = models.PositiveIntegerField(default=0)

class SentScore(models.Model):
    name = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)

class SentValue(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)

class Ranking(models.Model):
    ranking_name = models.CharField(max_length=50)
    ranking_img = models.ImageField(default=0)
    ranking_score = models.PositiveIntegerField(default=0)
