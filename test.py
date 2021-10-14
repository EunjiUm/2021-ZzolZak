product_list = ['trench_coat',
                'coat',
                'padded_jacket',
                'military',
                'blazer',
                'leather_jacket',
                'fur_jacket',
                'short_sleeve_jacket',
                'long_sleeve_jacket',
                'shirt',
                'blouse',
                'neat',
                'hoodie',
                'sweat_shirt',
                'denim_pants',
                'mini_skirt',
                'skirt',
                'slacks',
                'short_pants',
                'sports_wear',
                'leggings',
                'sports_shoes',
                'sandal',
                'heel',
                'loafers',
                'walker',
                'dress',
                'back_pack',
                'tote_bag',
                'clutch_bag',
                'shoulder_bag',
                'eco_bag', ]
company_list = ["musinsa", "seoulstore", "ssf"]
for i in range(1,len(product_list)):
    word = "elif keyword == \""+ product_list[i]+"\":\n\tmusinsa_review_list = Review_musinsa_"+ product_list[i]+".objects.all()\n\tseoulstore_review_list = Review_seoulstore_"+ product_list[i]+".objects.all()\n\tssf_review_list = Review_ssf_"+ product_list[i]+".objects.all()\n\tsent_value = SentValue_"+ product_list[i]+".objects.values()\n\tsent_list = SentScore_"+ product_list[i]+".objects.all()\n\tJan = FashionScore_"+ product_list[i]+"[0]['Jan']\n\tFeb = FashionScore_"+ product_list[i]+"[0]['Feb']\n\tMar = FashionScore_"+ product_list[i]+"[0]['Mar']\n\tApr = FashionScore_"+ product_list[i]+"[0]['Apr']\n\tMay = FashionScore_"+ product_list[i]+"[0]['May']\n\tJune = FashionScore_"+ product_list[i]+"[0]['June']\n\tJuly = FashionScore_"+ product_list[i]+"[0]['July']\n\tAug = FashionScore_"+ product_list[i]+"[0]['Aug']\n\tSep = FashionScore_"+ product_list[i]+"[0]['Sep']\n\tOct = FashionScore_"+ product_list[i]+"[0]['Oct']\n\tNov = FashionScore_"+ product_list[i]+"[0]['Nov']\n\tDec = FashionScore_"+ product_list[i]+"[0]['Dec']\n\tmonth_1 = FashionScore_"+ product_list[i]+"[0]['month_1']\n\tmonth_2 = FashionScore_"+ product_list[i]+"[0]['month_2']\n\tmonth_3 = FashionScore_"+ product_list[i]+"[0]['month_3']\n\tpositive_value = sent_value[0]['positive_value']\n\tnegative_value = sent_value[0]['negative_value']\n\tneutral_value = sent_value[0]['neutral_value']\n\tcontext = {\n\t'Jan': Jan,\n\t'Feb': Feb,\n\t'Mar': Mar,\n\t'Apr': Apr,\n\t'May': May,\n\t'June': June,\n\t'July': July,\n\t'Aug': Aug,\n\t'Sep': Sep,\n\t'Oct': Oct,\n\t'Nov': Nov,\n\t'Dec': Dec,\n\t'keyword': keyword,\n\t'musinsa_review_list': musinsa_review_list,\n\t'seoulstore_review_list': seoulstore_review_list,\n\t'ssf_review_list': ssf_review_list,\n\t'month_1': month_1,\n\t'month_2': month_2,\n\t'month_3': month_3,\n\t'positive_value': positive_value,\n\t'negative_value': negative_value,\n\t'neutral_value': neutral_value,\n\t'sent_list': sent_list\n\t}\n\treturn render(request, 'index/data.html', context)"
    word1 = "elif product == \""+ product_list[i]+"\":\n\tfor i in range(len(year)):\n\t\treviewDate[i] = FashionScore_musinsa_"+ product_list[i]+"[period][year[i]] + FashionScore_seoulstore_"+ product_list[i]+"[period][year[i]] + FashionScore_ssf_"+ product_list[i]+"[period][year[i]]"
    word2 = "\tcopied_list = sorted(reviewDate, reverse=True)\n\tmonth_1 = reviewDate.index(copied_list[0]) + 1\n\tmonth_2 = reviewDate.index(copied_list[1]) + 1\n\tmonth_3 = reviewDate.index(copied_list[2]) + 1\n\tFashionScore_coat(\n\tJan=reviewDate[0],\n\tFeb=reviewDate[1],\n\tMar=reviewDate[2],\n\tApr=reviewDate[3],\n\tMay=reviewDate[4],\n\tJune=reviewDate[5],\n\tJuly=reviewDate[6],\n\tAug=reviewDate[7],\n\tSep=reviewDate[8],\n\tOct=reviewDate[9],\n\tNov=reviewDate[10],\n\tDec=reviewDate[11],\n\tmonth_1=month_1,\n\tmonth_2=month_2,\n\tmonth_3=month_3,\n\t).save()"
    print(word1)
    print(word2)