from django.db import models


class Ranking(models.Model):
    ranking_name = models.CharField(max_length=50)
    ranking_img = models.ImageField(default=0)
    ranking_score = models.PositiveIntegerField(default=0)

class FashionScore_trench_coat(models.Model):
    # 패션 지수
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

class FashionScore_musinsa_trench_coat(models.Model):
    # 패션 지수
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
    ranking_score = models.PositiveIntegerField(default=0)

class FashionScore_seoulstore_trench_coat(models.Model):
    # 패션 지수
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
    ranking_score = models.PositiveIntegerField(default=0)

class FashionScore_ssf_trench_coat(models.Model):
    # 패션 지수
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
    ranking_score = models.PositiveIntegerField(default=0)

class SentScore_trench_coat(models.Model):
    # 감성어
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentValue_trench_coat(models.Model):
    # 긍정/부정/중립 점수
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class Review_musinsa_trench_coat(models.Model):
    review = models.TextField()
    date = models.CharField(max_length=50)


class Review_seoulstore_trench_coat(models.Model):
    review = models.TextField()
    date = models.CharField(max_length=50)


class Review_ssf_trench_coat(models.Model):
    review = models.TextField()
    date = models.CharField(max_length=50)
