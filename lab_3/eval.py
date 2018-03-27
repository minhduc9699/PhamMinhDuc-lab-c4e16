# from calc import *
#
# x = float(input('x = '))
# op = input('operation (+,-,*,/): ')
# y = float(input('y = '))
#
# result = -9999
#
# if op == '+':
#     result = plus(x, y)
# elif op == '-':
#     result = minus(x, y)
# elif op == '*':
#     result = mutiply(x, y)
# elif op == '/':
#     result = divide(x,y)
#
# print(result)

def calc(x, op, y):
    # x = float(input('x = '))
    # op = input('operation (+,-,*,/): ')
    # y = float(input('y = '))

    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    else:
        result = x / y
    return result
