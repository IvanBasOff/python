import re
l = "Красивое лучше, чем уродливае"
matches = re.findall("красивое", l, re.IGNORECASE)
print(matches)

line = '123?34 hey?'
m = re.findall('\d', line, re.IGNORECASE)
print(m)

#echo Two too | grep -i T[wo]o
