with open("data/" + "seoulstore" + "_" + "short_pants" + ".txt", 'r', encoding='utf-8') as f:
    list_file = []
    for line in f:
        list_file.append(line.replace('\n', ''))

# 중복된 리뷰 제거
list_file = list(set(list_file))
origin_list=[0]*12
for txt in list_file:
    if len(txt) >= 5:
        if txt[-1] != ')':
            continue
        elif txt[-5] == '0':
            continue
        if txt[-3].isdigit() and txt[-4].isdigit():
            origin_list[int(txt[-4]+txt[-3])-1]+=1
        elif txt[-3].isdigit() and not txt[-4].isdigit():
            origin_list[int(txt[-3])-1]+=1
print(origin_list)