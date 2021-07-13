from datetime import datetime

origin_list = [0 for i in range(12)]
copied_list = []
month_list = []
date = "2021.03.21"

if "일" in date:
    origin_list[datetime.today().month - 1] += 1  # 한달 이내에 작성된 리뷰
else:
    origin_list[int(date.split('.')[1]) - 1] += 1

copied_list = origin_list
copied_list.sort(reverse=True)  # 월별로 1씩 증가시킨 리스트를 내림차순으로 정렬

print(copied_list)

month_1 = origin_list.index(copied_list[0]) + 1
month_2 = origin_list.index(copied_list[1]) + 1
month_3 = origin_list.index(copied_list[2]) + 1

month_list.append(month_1)
if month_2 not in month_list:
    month_list.append(month_2)
if month_3 not in month_list:
    month_list.append(month_3)

for i in range(len(month_list)):
    print(f"{month_list[i]}월 ", end='')