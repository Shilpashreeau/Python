
#Write a program that accepts a string as an input from the user and calculate the number of digits
#and letters.

str=input("enter the string\n")
count=dig=0
for i in str:
    
    if i.isalpha():
        count+=1
    elif i.isdigit():
        dig+=1
# do we have function to check spl characters as well??

    else:
        continue
print("number of letters", count)
print("the number of digits", dig)



