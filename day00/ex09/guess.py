import sys
import random

print("""
Welcome to the \"Guess the number game\".
You have to guess a number between 1 and 99.
To exit, enter \"exit\"
    """)

guess = "0"
attempt = 1
answer = random.randint(1, 99)

while 1:
    print("\n***Please enter a number between 1 and 99:***")
    guess = input()
    if guess == "exit":
        print("Thanks for playing. Goodbye")
        exit()
    if not guess.isdigit():
        print("This is not a number. Try again")
    elif int(guess) < answer:
        print("Too low !")
    elif int(guess) > answer:
        print("Too high")
    else:
        if answer == 42:
            print("Marvin the robot congratulates you for finding \
the answer to the universe")
        else:
            print("Well done you guessed the number.\n")
        if attempt == 1:
            print("You got it on your first try!!!")
        else:
            print("You have won in %d attempts!" % attempt)
        break
    attempt += 1
