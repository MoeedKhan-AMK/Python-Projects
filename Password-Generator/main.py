#Password Generator

#importing modules, strings and random

import string
import random

#using input for length

length = int(input("How many Characters You want in your password?: "))

print('''Select Password Critiera from below:
1. Digits
2. Letters
3. Special Characters
4. Exit ''')

CharacterList = ""

while True:
    select = int(input("Pick a number from above: "))

    if select == 1:
        CharacterList += string.digits
    elif select == 2:
        CharacterList += string.ascii_letters
    elif select == 3:
        CharacterList += string.punctuation
    elif select == 4:
        break
    else:
        print("Invalid Input")
        continue

password = []

for i in range (length):
    randomCharacter = random.choice(CharacterList)
    password.append(randomCharacter)

print("The Password is: "+"".join(password))

#Added feature to save password in a text file
with open("Password.txt", "w") as file:
    file.write("".join(password))
print("Password saved in Password.txt file")
