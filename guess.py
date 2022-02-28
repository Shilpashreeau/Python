#Write a program such that it asks users to “guess the lucky number”. If the correct number is
#guessed the program stops, otherwise it continues forever. modified with yes or no conditions

import random
guess=None
num=random.randint(1,5)
while guess!=num:

    guess=int(input("guess the lucky number\n"))
    if guess==num:
        print("good guess")
        break
    else:
        answer=input("do you want to continue? yes or no\n")
        if answer=='yes':
         continue
        elif answer=='no':
            print("ok stopping")
        break

        
       
    
    




    
