import random

secret_number= random.randint(1,20)
print("I am thinking of a number 1-20")

for guesses in range (1,5):
    print('guess the number')
    guess= int(input(''))

    if guess < secret_number:
        print ('the number you chose was too low')
    elif guess > secret_number:
        print('the number you chose was too high')
    else:
        break

if guess == secret_number:
    print(f'NICE You go it within {guesses} tries')
else:
    print(f'better luck next time the correct number was {secret_number}')

    
"""psuedo 
we import the random module
and we start by creating the secret number variable which we use the random.randomint() to randomly select a number 
and print we are thinking of a number

we start our 4 loop which gives the use 4 tries to guess
get the guess variable from user make sure its a number
and our if statement
id number is < or > than the secret number we tell them its wrong 
our else means if its not higher or lower they must have got the right number so we break from the loop in case its like the 2 try and then 
if guess is the number we tell them its rigfht
else its wrong 






"""








"""
guess the number 1-20 
secret number generate it 
number thats guessed 
print hello guess the number im thinking of 1-20 u get 4 tries
if the guess is < secret number print wrong
if guess is > secret number print wrong 
if guess is == to secret number break and print u got it right"""