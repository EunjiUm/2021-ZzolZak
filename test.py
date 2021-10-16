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
    word = "elif keyword == \""+ product_list[i]+"\":\n\t\tmusinsa_review_list = Review_musinsa_"+ product_list[i]+".objects.all()\n\t\tseoulstore_review_list = Review_seoulstore_"+ product_list[i]+".objects.all()\n\t\tssf_review_list = Review_ssf_"+ product_list[i]+".objects.all()\n\t\tsent_value = SentValue_"+ product_list[i]+".objects.values()\n\t\tsent_list = SentScore_"+ product_list[i]+".objects.all()\n\t\tJan = FashionScore_"+ product_list[i]+"[0]['Jan']\n\t\tFeb = FashionScore_"+ product_list[i]+"[0]['Feb']\n\t\tMar = FashionScore_"+ product_list[i]+"[0]['Mar']\n\t\tApr = FashionScore_"+ product_list[i]+"[0]['Apr']\n\t\tMay = FashionScore_"+ product_list[i]+"[0]['May']\n\t\tJune = FashionScore_"+ product_list[i]+"[0]['June']\n\t\tJuly = FashionScore_"+ product_list[i]+"[0]['July']\n\t\tAug = FashionScore_"+ product_list[i]+"[0]['Aug']\n\t\tSep = FashionScore_"+ product_list[i]+"[0]['Sep']\n\t\tOct = FashionScore_"+ product_list[i]+"[0]['Oct']\n\t\tNov = FashionScore_"+ product_list[i]+"[0]['Nov']\n\t\tDec = FashionScore_"+ product_list[i]+"[0]['Dec']\n\t\tmonth_1 = FashionScore_"+ product_list[i]+"[0]['month_1']\n\t\tmonth_2 = FashionScore_"+ product_list[i]+"[0]['month_2']\n\t\tmonth_3 = FashionScore_"+ product_list[i]+"[0]['month_3']\n\t\tpositive_value = sent_value[0]['positive_value']\n\t\tnegative_value = sent_value[0]['negative_value']\n\t\tneutral_value = sent_value[0]['neutral_value']\n\t\tcontext = {\n\t\t'Jan': Jan,\n\t\t'Feb': Feb,\n\t\t'Mar': Mar,\n\t\t'Apr': Apr,\n\t\t'May': May,\n\t\t'June': June,\n\t\t'July': July,\n\t\t'Aug': Aug,\n\t\t'Sep': Sep,\n\t\t'Oct': Oct,\n\t\t'Nov': Nov,\n\t\t'Dec': Dec,\n\t\t'keyword': keyword,\n\t\t'musinsa_review_list': musinsa_review_list,\n\t\t'seoulstore_review_list': seoulstore_review_list,\n\t\t'ssf_review_list': ssf_review_list,\n\t\t'month_1': month_1,\n\t\t'month_2': month_2,\n\t\t'month_3': month_3,\n\t\t'positive_value': positive_value,\n\t\t'negative_value': negative_value,\n\t\t'neutral_value': neutral_value,\n\t\t'sent_list': sent_list\n\t\t}\n\t\treturn render(request, 'index/data.html', context)"
    word1 = "elif product == \""+ product_list[i]+"\":\n\t\tfor i in range(len(year)):\n\t\t\treviewDate[i] = FashionScore_musinsa_"+ product_list[i]+"[period][year[i]] + FashionScore_seoulstore_"+ product_list[i]+"[period][year[i]] + FashionScore_ssf_"+ product_list[i]+"[period][year[i]]"
    word2 = "\tcopied_list = sorted(reviewDate, reverse=True)\n\t\tmonth_1 = reviewDate.index(copied_list[0]) + 1\n\t\tmonth_2 = reviewDate.index(copied_list[1]) + 1\n\t\tmonth_3 = reviewDate.index(copied_list[2]) + 1\n\t\tFashionScore_" + product_list[i] + "(\n\t\tJan=reviewDate[0],\n\t\tFeb=reviewDate[1],\n\t\tMar=reviewDate[2],\n\t\tApr=reviewDate[3],\n\t\tMay=reviewDate[4],\n\t\tJune=reviewDate[5],\n\t\tJuly=reviewDate[6],\n\t\tAug=reviewDate[7],\n\t\tSep=reviewDate[8],\n\t\tOct=reviewDate[9],\n\t\tNov=reviewDate[10],\n\t\tDec=reviewDate[11],\n\t\tmonth_1=month_1,\n\t\tmonth_2=month_2,\n\t\tmonth_3=month_3,\n\t\t).save()"
    word3 = "elif product == \""+ product_list[i]+"\":\n\tSentValue_"+ product_list[i]+"(\n\t\tpositive_value=positive_value,\n\t\tnegative_value=negative_value,\n\t\tneutral_value=neutral_value,\n\t).save()\n\tnodes = []\n\tfor i in range(top_word_count):\n\t\tnode = dict()\n\t\tnode['word'] = word_list[i]\n\t\tnode['value'] = frequency_list[i]\n\t\tnode['group'] = group_list[i]\n\t\tnodes.append(node)\n\tSentScore_"+ product_list[i]+"(\n    \tword=nodes[i]['word'],\n\t    value=nodes[i]['value'],\n\t    group=nodes[i]['group'],\n\t).save()"
    print(word3)