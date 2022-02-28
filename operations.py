# T1 and T2 
# Write a program in Python to perform the following operator based task:
val=input({'addition':'1',"subtraction":'2','multiply':'3','division':'4','average':'5'})
x=int(input("number1"))
y=int(input("number2"))

if val=='1':
            
            rsult=x+y
            print(rsult)
elif val=='2':
            rslt=x-y
            print(rslt)
elif val=='3':
            rslt=x*y
            print(rslt)
elif val=='4':
            rslt=x/y
            print(rslt)
elif val=='5':
    a=int(input("number3"))
    b=int(input("number4"))
    rslt=(a+b+x+y)/4 
    print(rslt)      

if rslt<0:
    print("negative")    

        
