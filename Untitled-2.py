#!/usr/bin/python3
#Guess the Number

## add a way to play again
## handle input error in the beginning


import random
def main():
    number_range = int(input("Choose an upper guess range: "))
    random_number = random.randint(1, number_range)
    count = 1
    try:
        guess = int(input(f'I\'m thinking of a number between 1 and {str(number_range)}. Guess which number I\'m thinking of! '))
    except ValueError:
        print("That's not an integer! Enter a whole number.")
        main()


    while guess != random_number:
        if guess > random_number:
            print('You guessed too high! Try again.')
            count += 1
            try:
                guess = int(input(
                    f'I\'m thinking of a number between 1 and {str(number_range)}. Guess which number I\'m thinking of! '))
            except ValueError:
                print("That's not an integer! Enter a whole number.")
                guess = int(input(
                    f'I\'m thinking of a number between 1 and {str(number_range)}. Guess which number I\'m thinking of! '))
        if guess < random_number:
            print('You guessed too low! Try again.')
            count += 1
            try:
                guess = int(input(
                    f'I\'m thinking of a number between 1 and {str(number_range)}. Guess which number I\'m thinking of! '))
            except ValueError:
                print("That's not an integer! Enter a whole number.")
                guess = int(input(
                    f'I\'m thinking of a number between 1 and {str(number_range)}. Guess which number I\'m thinking of!'))
    print(f'You got it! It only took {str(count)} tries')
    Play_again()


def Play_again():
    play_again = input('Do you want to play again? y/n ')
    if play_again.lower() == 'y':
        main()
    if play_again.lower() == 'n':
        print('Thanks for playing!')
        exit()
    else:
        Play_again()
main()

