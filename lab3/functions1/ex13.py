#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
#This is how it should work when run in a termini
import random
count = 0
print("Hello! What is your name?")
name = input()
print("Well, " +name+ ", I am thinking of a number between 1 and 20.")
num = random.randint(1, 20)
while True:
    print("Take a guess.")
    user_num = int(input())
    count +=1
    if user_num < num:
        print("Your guess is too low.")
    elif user_num > num:
        print("Your guess is too high.")
    else:
        print("Good job, KBTU! You guessed my number in " + str(count) + " guesses!")
        break
