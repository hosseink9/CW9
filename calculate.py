from operation.division import div
from operation.addition import addition
from operation.multi import multi
from operation.subtraction import sub

def cal(a,b,c):
                
    if b=="+" :
        addition(a,c)
    elif b=="-" :
        sub(a,c)
    elif b=="*":
        multi(a,c)
    elif b=="/" :
        div(a,c)
    else:
        print("your input is wrong please try again")
        

print("Welcome")
while True:
    number1=int(input('Please enter your number one\nExit (e)\n'))
    if number1=="e":
        break
    operation=input("Please enter your operation (+,-,*,/)\n")
    number2=int(input('Please enter your number two\n'))
    cal(number1,operation,number2)
    
