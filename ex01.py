def sqr(a, b = 2):
    '''very important
    function
    '''
    return a ** 2 + b

num = input('Enter number: ')

try:
    print(sqr(int(num)))
except (ZeroDivisionError, ValueError):
    print('Wrong input')

print("test".replace('e', 'o'))
