#for

name = "test"
for ch in name:
    print(ch)
#
lis = ["123", "456", "789"]
for ch in lis:
    print(ch)
#
lis2 = ("aaa", "bbb", "ccc")
for ch in lis2:
    print(ch)
#
people = {"first" : "yes",
          "second" : "no"}
for ch in people:
    print(ch)
#
tv = ["list", "test", "hex"]
i = 0
for sh in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)
#

# range

for i in range(1, 11):
    if i == 3:
        continue
    print(i)
    
# WHILE
x=10
while x > 0:
    print('{}'.format(x))
    x -= 1
    if x == 7:
        x -= 1
        continue
    if x < 5:
        break

#
print('------------------')
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)

print(list3)
    

