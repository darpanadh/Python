# import random

# while True:
#     choice=input("Roll the dice? (y/n): ").lower()
#     if choice =='y':
#         d1= random.randint(1,6)
#         d2= random.randint(1,6)
#         print(f"({d1},{d2})")
#         # print("(",d1," ,",d2,")")

#     elif choice =='n':
#         print("Thanks for playing..")
#         break
#     else:
#         print("Invalid Choice")



#modifications
#modified so that user can specify number of dices

import random

count=0
while True:
    choice=input("Roll the dice? (y/n): ").lower()
    if choice =='y':
        no=int(input("No of dices?: "))
        count+=no
        i=0
        data=[]
        for i in range(1,no+1):
            dice=random.randint(1,6)
            data.append(dice)   #append one item to the end of list
            
        print(data)


    elif choice =='n':
        print("Thanks for playing..")
        print("No of dices rolled = ",count)
        break
    else:
        print("Invalid Choice")