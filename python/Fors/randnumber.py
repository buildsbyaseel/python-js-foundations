import random

secretnumber= random.randint(1,20)
print('I am thinking of a random number between 1-20')

for guesses_taken in range(1,5):
    guess = int(input('take a guess what number i am thinking of? you only have 4 tries.'))

    if guess < secretnumber:
        print('your guess it not high enough')
    elif guess > secretnumber:
        print('your guess is too high')
    else:
        break
if guess == secretnumber:
    print(f'wow you guessed it in {guesses_taken} tries You win')
else:
    print(f'you lost insert cash to try again, the correct answer was {secretnumber}')


