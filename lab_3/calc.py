def plus(x, y):
    equal = x + y
    return equal


def minus(x, y):
    equal = x - y
    return equal


def mutiply(x, y):
    equal = x * y
    return equal


def divide(x, y):
    equal = x / y
    return equal

x = float(input('x = '))
op = input('operation (+,-,*,/): ')
y = float(input('y = '))

result = -9999

if op == '+':
    result = plus(x, y)
elif op == '-':
    result = minus(x, y)
elif op == '*':
    result = mutiply(x, y)
elif op == '/':
    result = divide(x,y)
    


print('{0} {1} {2} = {3}'.format(x, y, op, result))
