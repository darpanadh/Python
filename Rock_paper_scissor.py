# Write a program to simulate a game of Rock, Paper, Scissors.  
# The game will prompt the player to choose rock, paper, or scissors by typing 'r', 
# 'p', or 's'. The computer will randomly select its choice. The game will then display 
# both choices using emojis and determine the winner based on the rules. 
# Optional Enhancements 
# • Modify the game so that the first player (or computer) to win two out of three 
# rounds is declared the overall winner. This adds a competitive aspect to the 
# game. 
# • Keep a tally of how many times the player wins, loses, or ties with the 
# computer. Display these statistics at the end of the game. 
# • Add an option for two players to play against each other, taking turns to input 
# their choices. The program should then determine the winner based on their 
# inputs.

# import random

# ch=('r','p','s')
# comp=random.choice(ch)

# while True:
#     user=input("Rock,paper or scissor? (r/p/s) ").lower()
    
#     if (user not in ch):
#         print("Invalid choice")
        
#     else:
#         emoji={'r':'👊', 'p':'📃','s':'✂️'}

#         print(f"You choose {emoji[user]}  ")
#         print(f"Computer choose {emoji[comp]}  ")  
        
#         if (user == comp):
#             print("Draw")
        
#         elif ((user =='r' and comp=='s') or 
#                 (user=='p' and comp=='r') or
#                 (user=='s'and comp=='p')):
#                     print("You win")
#         else:
#             print("Computer win")


#         while True:
#             again=input("Want to play again?(y/n) : ").lower()
            
#             if (again == 'n'):
#                 exit()
            
#             elif (again == 'y'):
#                 break
            
#             else:
#                 print("Enter valid choice : y/n")


#modifications

import random


user_win=0
comp_win=0
draw=0

def play_game():
    ch=('r','p','s')
    comp=random.choice(ch)
    global user_win, comp_win, draw #defined global variable to access them across all the code not only wih in function only
    user=input("Rock,paper or scissor? (r/p/s) ").lower()

    if (user not in ch):
        print("Invalid choice")
        
    else:
        emoji={'r':'👊', 'p':'📃','s':'✂️'}

        print(f"You choose {emoji[user]}  ")
        print(f"Computer choose {emoji[comp]}  ")  
        
        if (user == comp):
            print("Draw")
            draw+=1
        
        elif ((user =='r' and comp=='s') or 
                (user=='p' and comp=='r') or
                (user=='s'and comp=='p')):
                    print("You win")
                    user_win+=1
                    
        else:
            print("Computer win")
            comp_win+=1


user1_win=0
user2_win=0
draw1=0

def two_play():
    ch=('r','p','s') 
    global user1_win, user2_win, draw1
    
    user1=input("Player 1: Rock,paper or scissor? (r/p/s) ").lower()
    user2=input("Player 2: Rock,paper or scissor? (r/p/s) ").lower()

    if (user1 not in ch or user2 not in ch):
        print("Invalid choice")
        
    else:
        emoji={'r':'👊', 'p':'📃','s':'✂️'}

        print(f"User1 choose {emoji[user1]}  ")
        print(f"User2 choose {emoji[user2]}  ")  
        
        if (user1 == user2):
            print("Draw")
            draw1+=1
        
        elif ((user1 =='r' and user2=='s') or 
                (user1=='p' and user2=='r') or
                (user1=='s'and user2=='p')):
                    print("User1 wins")
                    user1_win+=1
                    
        else:
            print("User2 wins")
            user2_win+=1
            



def play_again():
    while True:
        again=input("Want to play again?(y/n) : ").lower()
        
        if (again == 'n'):
            exit()
        
        elif (again == 'y'):
            break
        
        else:
            print("Enter valid choice : y/n")

mode=input("Enter (c) to play with computer \n Enter (p) to play with friend ").lower()

while True:

    if (mode == 'c'):
        play_game()
        print("User : ",user_win)
        print("Computer: ",comp_win)
        print("Draw : ",draw)
        
        if (comp_win ==2):
            print("Computer won the overall game")
            user_win = comp_win = draw = 0
        elif (user_win ==2):
            print("Congrats!! You won the overall game")
            user_win = comp_win = draw = 0
            
        play_again()
    
    elif (mode == 'p'):
        two_play()
        print("User1 : ",user1_win)
        print("User2 : ",user2_win)
        print("Draw : ",draw1)
        play_again()
        
    
        if (user1_win==2):
            print("User1 won the overall game")
            user1_win=user2_win=draw1=0
            
        elif (user2_win==2):
            print("User2 won the overall game")
            user1_win=user2_win=draw1=0
    
    else:
        print("Invalid mode. Choose (c/p) ")
        mode=input("Enter (c) to play with computer \n Enter (p) to play with friend ").lower()
        continue
