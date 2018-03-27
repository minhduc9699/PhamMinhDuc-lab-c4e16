from random import randint, choice
from eval import calc
level = 1
playing = True
while playing:
    x = randint(1, 10)
    y = randint(1, 10)
    err = randint(-1, 1)
    op = ['+', '-', '*', '/']
    ran_op = choice(op)


    result = calc(x, ran_op, y) + err



    print('{0} {1} {2} = {3}'.format(x, ran_op ,y, result))

    answer = input('(Y/N)? ').upper()


    if (err == 0 and answer == 'Y') or (err != 0 and answer == 'N'):
        print('yayyy')
        level += 1
    elif (err == 0 and answer == 'N') or (err != 0 and answer == 'Y' ):
        print(''' you're wrong ''')
        break
