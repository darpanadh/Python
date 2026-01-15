# Write a program to have the computer randomly select a number between 1 and 
# 100, and then prompt the player to guess the number. The program should give 
# hints if the guess is too high or too low.

# Optional Enhancements 
# • Allow the user to specify the minimum and maximum values for the number 
# range before the game starts. This gives the player more control over the 
# difficulty level. 
# • Implement a feature that limits the number of guesses a player can make. If 
# the player runs out of attempts, the game should end, and the correct number 
# should be revealed. 
# • Add a feature that keeps track of the fewest attempts it took to guess the 
# number correctly. The program should display this "best score" at the end of 
# each game.


# import random
# num=random.randint(1,100)   

# while True:   
#     try:
#         guess=int(input("Enter your guess: "))
        
    
#         if (guess == num):
#             print("Congrats! Your guess is correct..")
#             break
            
#         elif (guess>num):
#             print("Too high...")
            
#         else:
#             print("TOo low...")
            
#     except ValueError:
#         print("Enter the valid number")
            


#modified
# import random

# min=int(input("Enter the minimum value of your number range: "))
# max=int(input("Enter the maximum value of your number range: "))
# attempt=10
# num=random.randint(min,max)   

# while True:
#         try:
#             while attempt !=0:
#                 guess=int(input("Enter your guess: "))
                
#                 if (guess == num):
#                     print("Congrats! Your guess is correct..")
#                     exit()
                    
#                 elif (guess>num):
#                     print("Too high...")
                    
#                 else:
#                     print("Too low...")
            
#                 attempt-=1
#                 print("Attempts left= ",attempt)
            
#             print("Ran out of attempts..")   
#             break
        
#         except ValueError:  #prevent program being stopped after error occurs due to invalid input character 
#             print("Enter the valid number")




#Final code

import random

high_score=[] 

def play_game():
    
    attempt=10
    min_=int(input("Enter the minimum value of your number range: "))
    max_=int(input("Enter the maximum value of your number range: "))
    num=random.randint(min_,max_) 
    
    while attempt !=0:
        try:
            guess=int(input("Enter your guess: "))
        
        except ValueError:  #prevent program being stopped after error occurs due to invalid input character 
            print("Enter the valid number")
            continue
                    
        if (guess == num):
            print("Congrats! Your guess is correct..")
            used_attempt=10-attempt+1
            high_score.append(used_attempt)
            print("Your score: ",used_attempt)
            print("HighScore(Minimum attempt)= ",min(high_score)) #show the minimum number of attempt used
            return
            
        elif (guess>num):
            print("Too high...")
            
        else:
            print("Too low...")
            
        attempt-=1
        print("Attempts left= ",attempt)
        
        
        
        if (attempt == 0):
            print("Ran out of attempts.")
            print("The actual number is = ",num)
            
            
def play_again():
    while True:
        choice =input("Do you want to play game again?(y/n):").lower()
        if choice =='y':
            return True 
        
        elif choice =='n':
            return False
        
        else:
            print("Invalid choice")
            
    
while True:
    play_game()
    
    if not play_again():
        print("Thanks for playing...")
        break
    




