'''
Rock-Paper-Scissors Game Rules:
1. r => rock, p => paper, s => scissors
2. Rock beats Scissors, Scissors beats Paper, Paper beats Rock
'''
import random   #importing random module

computer = random.choice(['r', 'p', 's'])  #Computer will randomly choose between rock, paper, or scissors


user = input("Enter Your Choice (r, p, s): ")       #Will take input from user.

variable_Dict = {'r': 1, 'p': 2, 's': 3}    #Mapping user input to numbers using dictionary

num = variable_Dict.get(user)  # fetch user input from dictionary

print(f"Computer chose: {computer}, You chose: {user}")

#Win-Lose Condition

if(computer == user):
    print("It's a Tie!")
else:
    if(computer == 'r' and user == 'p'): 
        print("You Win!")

    elif(computer == 'r' and user == 's'):
        print("You Lose!")

    elif(computer == 'p' and user == 'r'):
        print("You Lose!")

    elif(computer == 'p' and user == 's'):
        print("You Win!")

    elif(computer == 's' and user == 'p'):
        print("You Lose!")

    elif(computer == 's' and user == 'r'):
        print("You Win!")

    else:
        print("Invalid Error")