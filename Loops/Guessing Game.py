import random

n = 20
randomno = random.random()
# print(randomno)
to_be_guessed = int(n * randomno) + 1
# print(guessed)
guess = 0
while guess != to_be_guessed:
    guess = int(input("Enter your Guessing No"))

    if guess > 0:
        if guess > to_be_guessed:
            print("THe no is too large")
        elif guess < to_be_guessed:
            print("The no is too Small")
    else:
        print("Sorry You out of game")
        break
else:
    print("Congratulation you made it")
