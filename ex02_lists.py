#list
actors_list = ['Vasya', 'Petya', 'Loshad', 2, True]

if 'Vasya' in actors_list:
    print('Vasya here')

actors_list.append(10)
print(10 in actors_list)

print(actors_list[1])

#kortege
moscow = (12, 19, 10)
piter = (30, 10)
rostov = (23, 15)

#dict
dicto = {'2' : 'dva',
         '3' : 'tri',
         '10' : 'desyat'}
print(dicto['2'])

n = 3
if str(n) in dicto:
    d =  dicto[str(n)]
    print(d);
else:
    print('Not found')

###
locations = [moscow, piter, rostov, dicto]
if moscow in locations:
   print(12 in moscow)


