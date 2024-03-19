import random

name = input("Enter your name: ")
print("Good luck", name)
print("Welcome To The Guessing Game!")

number_to_guess = random.randint(1, 100)

guesses = []
turns_left = 10

while turns_left > 0:

    for i in range(1, 101):
        if i in guesses:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print()

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Invalid input. Please enter a number between 1 and 100.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

    if guess == number_to_guess:
        print("You win!")
        print("You guessed the number", number_to_guess, "in", 10 - turns_left, "guesses.")
        break
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")

    turns_left -= 1


    guesses.append(guess)

if turns_left == 0:
    print("You lose.")
    print("The correct number was", number_to_guess)