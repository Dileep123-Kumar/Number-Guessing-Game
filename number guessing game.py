# NUMBER GUESSING GAME:
import random

secret_number= random. randint(1,10)

name=input("Enter your Name: ")
print(f"Welcome {name} to the Number Guessing Game")
print("1) Play \n2) Exit")
choice=int(input("Pleas press the for play game or leave the game...."))
score=0

while True:
    if choice == 1:
        guess = int(input("Enter your number (1-10): "))
        if guess < secret_number:
            print("your number is low.please! Try again.....")
        elif guess > secret_number:
            print("Your number is high.please Try again.....")
        else:
            print("Congratulations! you won")
            score+=1
        print("Score: ",score)
    elif choice == 0:
        break
    else:
        print("Invalid entry")
