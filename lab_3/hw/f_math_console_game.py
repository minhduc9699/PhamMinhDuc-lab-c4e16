from random import randint, choice
from eval import calc
level = 1
playing = True
print('\n')
print('*'*20 ,'Welcome to Fmath game', '*'*20)
print('\n')
start = input('Pess Enter to play')
while playing:
    if level < 4:
        x = randint(1, 10)
        y = randint(1, 10)
        err = randint(-1, 1)
        op = ['+']
        ran_op = choice(op)
    elif level <= 8:
        if level == 4:
            print('level up!!')
        x = randint(1, 20)
        y = randint(1, 20)
        err = randint(-1, 1)
        op = ['+', '-']
        ran_op = choice(op)
    elif level >= 12:
        if level == 12:
            print('level up!!!')
        x = randint(1, 30)
        y = randint(1, 30)
        err = randint(-1, 1)
        op = ['+', '-', '*', '/']
        ran_op = choice(op)
        if level == 20:
            print('Win cmnr!!')
            break



    result = calc(x, ran_op, y) + err



    print('*'*20,'{0} {1} {2} = {3}'.format(x, ran_op ,y, result), '*'*20)

    answer = input('(Y/N)?').upper()


    if (err == 0 and answer == 'Y') or (err != 0 and answer == 'N'):
        print('yayyy')
        level += 1
    elif (err == 0 and answer == 'N') or (err != 0 and answer == 'Y' ):
        print(''' you're wrong ''')
        break
