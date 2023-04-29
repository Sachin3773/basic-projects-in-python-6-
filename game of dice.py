import random as r
print('🎲 WELCOME TO THE GAME OF DICE 🎲'.center(120))
d='c'
while d!='no':
    if d=='c':
      t=int(input('Enter number of faces for the dice: '.center(20)))
    s=input('Press enter to roll the dice: ')
    a=r.randint(1,t)
    if a<=(t//2):
      print('Aww its a')
      print('-----')
      print('|',a,'|')
      print('-----')
      print('😥')
    elif a==t:
       print('Yeah its the highest')
       print('-----')
       print('|',a,'|')
       print('-----')
       print('🥳😍')
    else:
       print('Its a')
       print('-----')
       print('|',a,'|')
       print('-----')
       print('😃')
    e=input('Do you want to roll again (yes or no) or change number of face (press c): '.center(20))
    d=e