import random
# randnum = random.randint(1,100)

# inp = -1
# guesses = 0
# while(inp != randnum):
    
#     inp = int(input("Guess the Number: "))
#     guesses += 1

#     if (inp > randnum):
#         print("write lower number please!", end="\n\n")
#         # guesses += 1
#     elif(inp < randnum):
#         print("write higher number please!", end="\n\n")
#         # guesses += 1

#     if (guesses >= 7):
#         break

# print(f"You have successfully guessed the correct number {randnum}", end="\n")
# print(f"Number of Guesses made by user: {guesses}")


difficulty = input("Select Difficulty Level: easy, medium, hard: ").lower()


#Diffuclty Criteria

if (difficulty == "easy"):
    randnum = random.randint(1,100)
    max_guesses = 10

elif(difficulty == "medium"):
    randnum = random.randint(1,500)
    max_guesses = 5

elif(difficulty == "hard"):
    randnum = random.randint(1, 1000)
    max_guesses = 3
else:
    print("Failed")

#Basic Game

inp = -1
guesses = 0
user_guesses = [] #Storing Guesses

print(f"You have maximum {max_guesses} guesses. Best Of Luck\n")

while(inp != randnum) and guesses < max_guesses:
    
    inp = int(input("Guess the Number: "))
    guesses += 1

    if (inp > randnum):
        print("write lower number please!", end="\n\n")
        # guesses += 1
    elif(inp < randnum):
        print("write higher number please!", end="\n\n")
        # guesses += 1

#Result
if inp == randnum:
    print(f"WOHOO🎉! Succesful Attempt. The number was {randnum}")
else:
    print(f"❌ Out of guesses! The correct number was {randnum}")

print(f"You have successfully guessed the correct number {randnum}", end="\n")
print(f"Number of Guesses made by user: {guesses}")