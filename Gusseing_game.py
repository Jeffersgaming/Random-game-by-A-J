import random

def guessing_game():
    print("***********GUESSING GAME**********")
    print("Think of a number between 1 & 100")
    print("Try to guess the number!!!")

    target_number = random.randint(1, 100)
    ampts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            ampts += 1

            if guess < target_number:
                print("This is too low guess.. Try little higher")
            elif guess > target_number:
                print("This is too high guess.. Try little lower")
            else:
                print(f"Congratulations!!! You guessed it right in {ampts} attempts :) ")
                break
        except ValueError:
            print("Please enter a valid number please...")

if __name__ == "__main__":
    guessing_game()
