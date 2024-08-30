import random

guesses = 0

print('WELCOME TO NUMBER GUESSER GAME!\n')

while True:
    userRange = input('Please type a number to decide range: 0 - ')
    if userRange.isdigit():
        userRange = int(userRange)
        if userRange <= 0:
            print('Please enter a number greater than 0.')
            continue
        else:
            print(f'Okay! Now a random number is generated between 0 to {userRange}')
            randNumber = random.randint(0, userRange)
            break
    else:
        print('Please enter a numerical value only.')
        continue

while True:
    guess = input('Enter your guess: ')
    if guess.isdigit():
        guess = int(guess)
        if guess != randNumber:
            if guess < randNumber:
                print('Try A Higher Value.')
            else:
                print('Try A Lower Value.')
            guesses = guesses + 1
            continue
        elif guess == randNumber:
            print('Well Done! You have guessed it correctly')
            break
    else:
        print('Only numerical digits are counted as a guess. Enter again.')

print(f'You have completed the challenge in {guesses} guesses!\n')
