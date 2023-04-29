import random
l3=[chr(i) for i in range(65,91)]
l1=[chr(i) for i in range(97,123)]
l2=[i for i in range(10)]
l=l1+l2+l3
print('IT IS PASSWORD GENERATOR'.center(120))
a=input('generate password yes or no: '.center(20))
s=''
d=''
while d!='no':
    if a=='yes':
        n=random.choice([8,12])
        for i in range(n):
            if n==8:
              b=random.choice(l)
              s=s+str(b)
            else:
               b=random.choice(l)
               s=s+str(b)
        if s.isalpha() or s.isdigit():
               s=''
               continue
        else:
               print(s)
               s=''
    d=input('want to generate password again yes or no: '.center(20))