def add(a,b):
    print("The sum is :",a+b)

def sub(a,b):
    print("The subtraction is: ",a-b)

def mul(a,b):
    print("The multiplication is:",a*b)

def div(a,b):
    if (b==0):
        print("Division by 0 is not allowed")
    else:
        print("The division is:",a/b)

while True:
    try:
        a=int(input(("Enter the first number:")))
        b=int(input(("Enter the second number:")))
    
    except ValueError:
        print("Enter valid number")
        continue
    
    choice=input(("(sum(s),subtraction(b),multiply(m),division(d) )")).lower()
    
    if (choice == 's'):
        add(a,b)
        
    elif (choice == 'b'):
        sub(a,b)
    
    elif (choice == 'm'):
        mul(a,b)
    
    elif (choice == 'd'):
        div(a,b)
    
    else:
        print("Enter valid choice")
    
    while True:
        again=input("Do you want to use the calculator again? (y/n) ").lower()
        
        if (again == 'y'):
            break
        
        elif (again =='n'):
            print("Thanks for using the calculator...")
            exit()
        
        else:
            print("Enter valid y/n")