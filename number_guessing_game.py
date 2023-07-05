import random
n = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
tries = 1
while True:
    if guess > n:
        print("Oops! Your guess is bigger than the correct answer. Try again.")
    elif guess < n:
        print("Oops! Your guess is lower than the correct answer. Try again")
    else:
        print("Congratulations! You've guessed correctly! You guessed it in {} tries".format(tries))
        break
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
