from django.db import models


class Ranking(models.Model):
    ranking_name = models.CharField(max_length=50)
    ranking_img = models.ImageField(default=0)
    ranking_score = models.PositiveIntegerField(default=0)


class FashionScore_trench_coat(models.Model):
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


class FashionScore_coat(models.Model):
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


class FashionScore_padded_jacket(models.Model):
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


class FashionScore_military(models.Model):
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


class FashionScore_blazer(models.Model):
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


class FashionScore_leather_jacket(models.Model):
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


class FashionScore_fur_jacket(models.Model):
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


class FashionScore_short_sleeve_jacket(models.Model):
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


class FashionScore_long_sleeve_jacket(models.Model):
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


class FashionScore_shirt(models.Model):
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


class FashionScore_blouse(models.Model):
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


class FashionScore_neat(models.Model):
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


class FashionScore_hoodie(models.Model):
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


class FashionScore_sweat_shirt(models.Model):
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


class FashionScore_denim_pants(models.Model):
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


class FashionScore_mini_skirt(models.Model):
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


class FashionScore_skirt(models.Model):
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


class FashionScore_slacks(models.Model):
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


class FashionScore_short_pants(models.Model):
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


class FashionScore_sports_wear(models.Model):
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


class FashionScore_leggings(models.Model):
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


class FashionScore_sports_shoes(models.Model):
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


class FashionScore_sandal(models.Model):
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


class FashionScore_heel(models.Model):
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


class FashionScore_loafers(models.Model):
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


class FashionScore_walker(models.Model):
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


class FashionScore_dress(models.Model):
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


class FashionScore_back_pack(models.Model):
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


class FashionScore_tote_bag(models.Model):
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


class FashionScore_clutch_bag(models.Model):
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


class FashionScore_shoulder_bag(models.Model):
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


class FashionScore_eco_bag(models.Model):
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


class FashionScore_musinsa_coat(models.Model):
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


class FashionScore_musinsa_padded_jacket(models.Model):
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


class FashionScore_musinsa_military(models.Model):
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


class FashionScore_musinsa_blazer(models.Model):
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


class FashionScore_musinsa_leather_jacket(models.Model):
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


class FashionScore_musinsa_fur_jacket(models.Model):
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


class FashionScore_musinsa_short_sleeve_jacket(models.Model):
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


class FashionScore_musinsa_long_sleeve_jacket(models.Model):
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


class FashionScore_musinsa_shirt(models.Model):
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


class FashionScore_musinsa_blouse(models.Model):
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


class FashionScore_musinsa_neat(models.Model):
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


class FashionScore_musinsa_hoodie(models.Model):
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


class FashionScore_musinsa_sweat_shirt(models.Model):
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


class FashionScore_musinsa_denim_pants(models.Model):
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


class FashionScore_musinsa_mini_skirt(models.Model):
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


class FashionScore_musinsa_skirt(models.Model):
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


class FashionScore_musinsa_slacks(models.Model):
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


class FashionScore_musinsa_short_pants(models.Model):
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


class FashionScore_musinsa_sports_wear(models.Model):
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


class FashionScore_musinsa_leggings(models.Model):
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


class FashionScore_musinsa_sports_shoes(models.Model):
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


class FashionScore_musinsa_sandal(models.Model):
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


class FashionScore_musinsa_heel(models.Model):
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


class FashionScore_musinsa_loafers(models.Model):
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


class FashionScore_musinsa_walker(models.Model):
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


class FashionScore_musinsa_dress(models.Model):
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


class FashionScore_musinsa_back_pack(models.Model):
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


class FashionScore_musinsa_tote_bag(models.Model):
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


class FashionScore_musinsa_clutch_bag(models.Model):
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


class FashionScore_musinsa_shoulder_bag(models.Model):
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


class FashionScore_musinsa_eco_bag(models.Model):
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


class FashionScore_seoulstore_coat(models.Model):
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


class FashionScore_seoulstore_padded_jacket(models.Model):
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


class FashionScore_seoulstore_military(models.Model):
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


class FashionScore_seoulstore_blazer(models.Model):
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


class FashionScore_seoulstore_leather_jacket(models.Model):
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


class FashionScore_seoulstore_fur_jacket(models.Model):
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


class FashionScore_seoulstore_short_sleeve_jacket(models.Model):
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


class FashionScore_seoulstore_long_sleeve_jacket(models.Model):
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


class FashionScore_seoulstore_shirt(models.Model):
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


class FashionScore_seoulstore_blouse(models.Model):
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


class FashionScore_seoulstore_neat(models.Model):
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


class FashionScore_seoulstore_hoodie(models.Model):
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


class FashionScore_seoulstore_sweat_shirt(models.Model):
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


class FashionScore_seoulstore_denim_pants(models.Model):
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


class FashionScore_seoulstore_mini_skirt(models.Model):
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


class FashionScore_seoulstore_skirt(models.Model):
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


class FashionScore_seoulstore_slacks(models.Model):
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


class FashionScore_seoulstore_short_pants(models.Model):
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


class FashionScore_seoulstore_sports_wear(models.Model):
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


class FashionScore_seoulstore_leggings(models.Model):
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


class FashionScore_seoulstore_sports_shoes(models.Model):
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


class FashionScore_seoulstore_sandal(models.Model):
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


class FashionScore_seoulstore_heel(models.Model):
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


class FashionScore_seoulstore_loafers(models.Model):
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


class FashionScore_seoulstore_walker(models.Model):
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


class FashionScore_seoulstore_dress(models.Model):
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


class FashionScore_seoulstore_back_pack(models.Model):
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


class FashionScore_seoulstore_tote_bag(models.Model):
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


class FashionScore_seoulstore_clutch_bag(models.Model):
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


class FashionScore_seoulstore_shoulder_bag(models.Model):
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


class FashionScore_seoulstore_eco_bag(models.Model):
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


class FashionScore_ssf_coat(models.Model):
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


class FashionScore_ssf_padded_jacket(models.Model):
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


class FashionScore_ssf_military(models.Model):
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


class FashionScore_ssf_blazer(models.Model):
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


class FashionScore_ssf_leather_jacket(models.Model):
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


class FashionScore_ssf_fur_jacket(models.Model):
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


class FashionScore_ssf_short_sleeve_jacket(models.Model):
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


class FashionScore_ssf_long_sleeve_jacket(models.Model):
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


class FashionScore_ssf_shirt(models.Model):
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


class FashionScore_ssf_blouse(models.Model):
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


class FashionScore_ssf_neat(models.Model):
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


class FashionScore_ssf_hoodie(models.Model):
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


class FashionScore_ssf_sweat_shirt(models.Model):
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


class FashionScore_ssf_denim_pants(models.Model):
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


class FashionScore_ssf_mini_skirt(models.Model):
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


class FashionScore_ssf_skirt(models.Model):
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


class FashionScore_ssf_slacks(models.Model):
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


class FashionScore_ssf_short_pants(models.Model):
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


class FashionScore_ssf_sports_wear(models.Model):
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


class FashionScore_ssf_leggings(models.Model):
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


class FashionScore_ssf_sports_shoes(models.Model):
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


class FashionScore_ssf_sandal(models.Model):
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


class FashionScore_ssf_heel(models.Model):
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


class FashionScore_ssf_loafers(models.Model):
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


class FashionScore_ssf_walker(models.Model):
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


class FashionScore_ssf_dress(models.Model):
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


class FashionScore_ssf_back_pack(models.Model):
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


class FashionScore_ssf_tote_bag(models.Model):
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


class FashionScore_ssf_clutch_bag(models.Model):
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


class FashionScore_ssf_shoulder_bag(models.Model):
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


class FashionScore_ssf_eco_bag(models.Model):
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
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_coat(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_padded_jacket(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_military(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_blazer(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_leather_jacket(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_fur_jacket(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_short_sleeve_jacket(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_long_sleeve_jacket(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_shirt(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_blouse(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_neat(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_hoodie(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_sweat_shirt(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_denim_pants(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_mini_skirt(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_skirt(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_slacks(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_short_pants(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_sports_wear(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_leggings(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_sports_shoes(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_sandal(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_heel(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_loafers(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_walker(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_dress(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_back_pack(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_tote_bag(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_clutch_bag(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_shoulder_bag(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentScore_eco_bag(models.Model):
    word = models.CharField(max_length=200)
    value = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=200)


class SentValue_trench_coat(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_coat(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_padded_jacket(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_military(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_blazer(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_leather_jacket(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_fur_jacket(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_short_sleeve_jacket(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_long_sleeve_jacket(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_shirt(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_blouse(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_neat(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_hoodie(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_sweat_shirt(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_denim_pants(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_mini_skirt(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_skirt(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_slacks(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_short_pants(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_sports_wear(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_leggings(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_sports_shoes(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_sandal(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_heel(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_loafers(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_walker(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_dress(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_back_pack(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_tote_bag(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_clutch_bag(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_shoulder_bag(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class SentValue_eco_bag(models.Model):
    positive_value = models.PositiveIntegerField(default=0)
    neutral_value = models.PositiveIntegerField(default=0)
    negative_value = models.PositiveIntegerField(default=0)


class Review_musinsa_trench_coat(models.Model):
    review = models.TextField()


class Review_seoulstore_trench_coat(models.Model):
    review = models.TextField()


class Review_ssf_trench_coat(models.Model):
    review = models.TextField()


class Review_musinsa_coat(models.Model):
    review = models.TextField()


class Review_seoulstore_coat(models.Model):
    review = models.TextField()


class Review_ssf_coat(models.Model):
    review = models.TextField()


class Review_musinsa_padded_jacket(models.Model):
    review = models.TextField()


class Review_seoulstore_padded_jacket(models.Model):
    review = models.TextField()


class Review_ssf_padded_jacket(models.Model):
    review = models.TextField()


class Review_musinsa_military(models.Model):
    review = models.TextField()


class Review_seoulstore_military(models.Model):
    review = models.TextField()


class Review_ssf_military(models.Model):
    review = models.TextField()


class Review_musinsa_blazer(models.Model):
    review = models.TextField()


class Review_seoulstore_blazer(models.Model):
    review = models.TextField()


class Review_ssf_blazer(models.Model):
    review = models.TextField()


class Review_musinsa_leather_jacket(models.Model):
    review = models.TextField()


class Review_seoulstore_leather_jacket(models.Model):
    review = models.TextField()


class Review_ssf_leather_jacket(models.Model):
    review = models.TextField()


class Review_musinsa_fur_jacket(models.Model):
    review = models.TextField()


class Review_seoulstore_fur_jacket(models.Model):
    review = models.TextField()


class Review_ssf_fur_jacket(models.Model):
    review = models.TextField()


class Review_musinsa_short_sleeve_jacket(models.Model):
    review = models.TextField()


class Review_seoulstore_short_sleeve_jacket(models.Model):
    review = models.TextField()


class Review_ssf_short_sleeve_jacket(models.Model):
    review = models.TextField()


class Review_musinsa_long_sleeve_jacket(models.Model):
    review = models.TextField()


class Review_seoulstore_long_sleeve_jacket(models.Model):
    review = models.TextField()


class Review_ssf_long_sleeve_jacket(models.Model):
    review = models.TextField()


class Review_musinsa_shirt(models.Model):
    review = models.TextField()


class Review_seoulstore_shirt(models.Model):
    review = models.TextField()


class Review_ssf_shirt(models.Model):
    review = models.TextField()


class Review_musinsa_blouse(models.Model):
    review = models.TextField()


class Review_seoulstore_blouse(models.Model):
    review = models.TextField()


class Review_ssf_blouse(models.Model):
    review = models.TextField()


class Review_musinsa_neat(models.Model):
    review = models.TextField()


class Review_seoulstore_neat(models.Model):
    review = models.TextField()


class Review_ssf_neat(models.Model):
    review = models.TextField()


class Review_musinsa_hoodie(models.Model):
    review = models.TextField()


class Review_seoulstore_hoodie(models.Model):
    review = models.TextField()


class Review_ssf_hoodie(models.Model):
    review = models.TextField()


class Review_musinsa_sweat_shirt(models.Model):
    review = models.TextField()


class Review_seoulstore_sweat_shirt(models.Model):
    review = models.TextField()


class Review_ssf_sweat_shirt(models.Model):
    review = models.TextField()


class Review_musinsa_denim_pants(models.Model):
    review = models.TextField()


class Review_seoulstore_denim_pants(models.Model):
    review = models.TextField()


class Review_ssf_denim_pants(models.Model):
    review = models.TextField()


class Review_musinsa_mini_skirt(models.Model):
    review = models.TextField()


class Review_seoulstore_mini_skirt(models.Model):
    review = models.TextField()


class Review_ssf_mini_skirt(models.Model):
    review = models.TextField()


class Review_musinsa_skirt(models.Model):
    review = models.TextField()


class Review_seoulstore_skirt(models.Model):
    review = models.TextField()


class Review_ssf_skirt(models.Model):
    review = models.TextField()


class Review_musinsa_slacks(models.Model):
    review = models.TextField()


class Review_seoulstore_slacks(models.Model):
    review = models.TextField()


class Review_ssf_slacks(models.Model):
    review = models.TextField()


class Review_musinsa_short_pants(models.Model):
    review = models.TextField()


class Review_seoulstore_short_pants(models.Model):
    review = models.TextField()


class Review_ssf_short_pants(models.Model):
    review = models.TextField()


class Review_musinsa_sports_wear(models.Model):
    review = models.TextField()


class Review_seoulstore_sports_wear(models.Model):
    review = models.TextField()


class Review_ssf_sports_wear(models.Model):
    review = models.TextField()


class Review_musinsa_leggings(models.Model):
    review = models.TextField()


class Review_seoulstore_leggings(models.Model):
    review = models.TextField()


class Review_ssf_leggings(models.Model):
    review = models.TextField()


class Review_musinsa_sports_shoes(models.Model):
    review = models.TextField()


class Review_seoulstore_sports_shoes(models.Model):
    review = models.TextField()


class Review_ssf_sports_shoes(models.Model):
    review = models.TextField()


class Review_musinsa_sandal(models.Model):
    review = models.TextField()


class Review_seoulstore_sandal(models.Model):
    review = models.TextField()


class Review_ssf_sandal(models.Model):
    review = models.TextField()


class Review_musinsa_heel(models.Model):
    review = models.TextField()


class Review_seoulstore_heel(models.Model):
    review = models.TextField()


class Review_ssf_heel(models.Model):
    review = models.TextField()


class Review_musinsa_loafers(models.Model):
    review = models.TextField()


class Review_seoulstore_loafers(models.Model):
    review = models.TextField()


class Review_ssf_loafers(models.Model):
    review = models.TextField()


class Review_musinsa_walker(models.Model):
    review = models.TextField()


class Review_seoulstore_walker(models.Model):
    review = models.TextField()


class Review_ssf_walker(models.Model):
    review = models.TextField()


class Review_musinsa_dress(models.Model):
    review = models.TextField()


class Review_seoulstore_dress(models.Model):
    review = models.TextField()


class Review_ssf_dress(models.Model):
    review = models.TextField()


class Review_musinsa_back_pack(models.Model):
    review = models.TextField()


class Review_seoulstore_back_pack(models.Model):
    review = models.TextField()


class Review_ssf_back_pack(models.Model):
    review = models.TextField()


class Review_musinsa_tote_bag(models.Model):
    review = models.TextField()


class Review_seoulstore_tote_bag(models.Model):
    review = models.TextField()


class Review_ssf_tote_bag(models.Model):
    review = models.TextField()


class Review_musinsa_clutch_bag(models.Model):
    review = models.TextField()


class Review_seoulstore_clutch_bag(models.Model):
    review = models.TextField()


class Review_ssf_clutch_bag(models.Model):
    review = models.TextField()


class Review_musinsa_shoulder_bag(models.Model):
    review = models.TextField()


class Review_seoulstore_shoulder_bag(models.Model):
    review = models.TextField()


class Review_ssf_shoulder_bag(models.Model):
    review = models.TextField()


class Review_musinsa_eco_bag(models.Model):
    review = models.TextField()


class Review_seoulstore_eco_bag(models.Model):
    review = models.TextField()


class Review_ssf_eco_bag(models.Model):
    review = models.TextField()
