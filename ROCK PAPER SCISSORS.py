import random
l=['rock','paper','scissors']
print('WELCOME TO ROCK PAPER SCISSORS GAME')
n=int(input('ENTER 1 FOR SINGLE ROUND AND ENTER 2 FOR BEST OF ROUNDS: '))
m=''
while m!='no':
    a=random.choice(l)
    if n==1:
        s=input('ENTER YOUR MOVE: ')
        if (a=='rock' and s=='paper') or (a=='paper' and s=='scissors') or (a=='scissors' and s=='rock'):
            print('YOU WIN')
            o=input('do you want to play again: ')
            m=o
        elif a==s:
            print('DRAW')
            o=input('do you want to play again: ')
            m=o
        else:
            print('YOU LOSE')
            o=input('do you want to play again: ')
            m=o
    if n==2:
        e=int(input('how many rounds you want: '))
        f=0
        g=0
        while e:
            a=random.choice(l)
            s=input('ENTER YOUR MOVE: ')
            if (a=='rock' and s=='paper') or (a=='paper' and s=='scissors') or (a=='scissors' and s=='rock'):
                print('win')
                f+=1
            else:
                print('lose')
                g+=1
            e-=1
        if g>f:
            print('YOU LOSE')
            o=input('do you want to play again: ')
            m=o
        elif f>g:
            print('YOU WIN')
            o=input('do you want to play again: ')
            m=o
        else:
            print('DRAW')
            o=input('do you want to play again: ')
            m=o