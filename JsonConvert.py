import json

file = open('C:/무신사_미니원피스.txt', 'r', encoding='utf-8')
lines = file.readlines()
reviews = []
for line in lines:
    reviews.append(line)
file.close()

M = dict(zip(range(1, len(reviews) + 1), reviews))
json.dumps(M)

json_val = json.dumps(M, indent="\t", ensure_ascii=False)

print(json_val)
