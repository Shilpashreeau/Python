#Write a program that asks five times to guess the lucky number.
import random
num=random.randint(1,10)

counter=1
while counter<=5:
    guess=int(input("guess the number"))
    counter=counter+1
    if guess==num:
        print("good guess")
        break
    else:
        print("try again")   
    continue
print("game over")
        

