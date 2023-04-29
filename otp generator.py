import random
l3=[chr(i) for i in range(65,91)]
l1=[chr(i) for i in range(97,123)]
l2=[i for i in range(10)]
l=l1+l2+l3
print('IT IS AN OTP GENERATOR'.center(120))
a=input('generate otp yes or no: '.center(20))
l4=[]
s=''
d=''
while d!='no':
    if a=='yes':
        n=random.choice([4,6])
        for i in range(n):
            if n==4:
              b=random.randint(1,9)
              s=s+str(b)
            else:
               b=random.choice(l)
               s=s+str(b)
        if n==4:
           print(s)
           s=''
        else:
            if s.isalpha() or s.isdigit():
               s=''
               continue
            else:
               print(s)
               s=''
    d=input('want to generate otp again yes or no: '.center(20))