import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password:
1. Letters (A-Z, a-z)
2. Digits (0-9)
3. Special characters (!, @, #, etc.)
4. Exit''')

characterList = ""

while True:
    choice = int(input("Pick a number (1-4): "))
    if choice == 1:
        characterList += string.ascii_letters
    elif choice == 2:
        characterList += string.digits
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        if characterList:
            break
        else:
            print("Select at least one character set before exiting!")
    else:
        print("Invalid choice. Please pick 1, 2, 3, or 4.")

if characterList:
    password = ''.join(random.choice(characterList) for _ in range(length))
    print("Your random password is:", password)
