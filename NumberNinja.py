import random
# Displays the interface
def game_interface():
    print("\nWelcome to the Guessing Game!")
    print("This game picks a random number between 1 and 100.")
    print("Try to guess the number.\n")
    print("""Game Menu
    1. Start
    2. Exit""")
def play_game():
    number = random.randint(1, 100)
    attempts = 0
#Loop continues until the choosen number is entered
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print(" Please enter a valid number.")
            continue
        attempts += 1
        
        # Out of range check
        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100.")
            continue

        # Check guess
        if guess == number:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
        # Help's you if you're closer
        elif abs(guess - number) <= 5 and abs(guess - number)>2:
            if guess < number:
                print("Low, but really close!")
            else:
                print("High, but really close!")
        # Help's you if you're very closer
        elif abs(guess - number) <= 2:
            if guess < number:
                print("Low, but really close! Just a bit higher...")
            else:
                print("High, but really close! Just a bit lower...")
        elif guess > number:
            print("The number you guessed is Too high!")
        else:
            print("The number you guessed is Too low!")
# I just made this to recieve different exit messages each time 
exit_messages=["Closing the game, but not the challenge.",
               "Every exit is just a pause. See you again!",
               "One step closer to mastering the numbers!",
               "The game rests... until you return.",
               "You leave now, but the secret number stays waiting."]

# This makes the user uses until they choose exit
def main():
    while True:
        game_interface()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter 1 or 2.")
            continue

        if choice == 1:
            play_game()
        elif choice == 2:
            print(random.choice(exit_messages))
            break
        else:
            print("Invalid choice! Enter 1 or 2.")
main()
