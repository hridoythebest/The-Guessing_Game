import random
import colorama

colorama.init()

def main():
    """This is the main function."""

    # Generate a random number between 1 and 10.
    number = random.randint(1, 10)

    # Get the user's guess.
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? Enter Number :  "))

    # Check if the user guessed correctly.
    if guess == number:
        print(colorama.Fore.GREEN + "Congratulations! You guessed correctly!" + colorama.Fore.RESET)
        print(colorama.Fore.GREEN + "The number I was thinking of was " + str(number) + colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "Sorry, you guessed incorrectly. The number I was thinking of was " + str(number) + colorama.Fore.RESET)
        print(colorama.Fore.RED + "Try again next time!" + colorama.Fore.RESET)

if __name__ == "__main__":
    main()
