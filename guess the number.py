import random
print('WELCOME TO THE GUESS THE NUMBER GAME'.center(125))
n=int(input('CHOOSE YOUR LEVEL OUT OF 2: '.center(50)))
d=''
while d!='NO':
    if n==1:
        print('RANGE FOR CHOOSING THE NUMBER IS 1 TO 100'.center(50))
        a=random.randint(1,100)
        b=0
        while a!=b:
            c=int(input('GUESS THE NUMBER: '.center(50)))
            b=c
            if b>a:
                if b-a<10:
                   print("****IT WAS TOO CLOSE****".center(50))
                elif b-a>=10 and b-a<=20:
                    print("****CLOSE****".center(50))
                else:
                    print("****FAR AWAY****".center(50))
            if a>b:
                if a-b<10:
                    print("****IT WAS TOO CLOSE****".center(50))
                if a-b>=10 and a-b<=20:
                    print("****CLOSE****".center(50))
                if a-b>20:
                    print("****FAR AWAY****".center(50))
            if a==b:
              print('THATS A WIN🥳🥳'.center(50))
              g=input('DO YOU WANT TO PLAY AGAIN: '.center(50))
              d=g
    if n==2:
        print('RANGE FOR CHOOSING THE NUMBER IS 1 TO 200 AND NUMBER OF CHANCES ARE 10'.center(50))
        p=random.randint(1,100)
        q=0
        while q!=10:
            q+=1
            o=int(input('GUESS THE NUMBER: '.center(50)))
            if o>p:
                if o-p<10:
                   print("****IT WAS TOO CLOSE****".center(50))
                elif o-p>=10 and o-p<=20:
                    print("****CLOSE****".center(50))
                else:
                    print("****FAR AWAY****".center(50))
            if p>o:
                if p-o<10:
                    print("****IT WAS TOO CLOSE****".center(50))
                if p-o>=10 and p-o<=20:
                    print("****CLOSE****".center(50))
                if p-o>20:
                    print("****FAR AWAY****".center(50))
            if p==o:
              print('THATS A WIN🥳🥳'.center(50))
              f=input('DO YOU WANT TO PLAY AGAIN: '.center(50))
              d=f
              break
        else:
            print('BETTER LUCK NEXT TIME🤷‍♂️🤷‍♂️')
            f=input('DO YOU WANT TO PLAY AGAIN: '.center(50))
            d=f