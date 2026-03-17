import random, sys

print ("ROCK, PAPER, SCICSORS")

wins = 0
losses = 0 
ties =0
#main game loop
while True:
    print(f'{wins} wins, {losses} losses, {ties} ties')

    while True: #palyer input loop
        print("Choose (r)ock (p)aper, (s)cissors, or (q)uit")
        choice = input("Pick either r, p, s, or q,")

        if choice == "q":
            sys.exit()


        if choice == 'r' or choice == 'p' or choice == "s":
            break
        print('type of of r s p q')

    if choice == "r":
        print("Rock versus ")
        
    elif choice == "s":
        print('Scissors versus ')

    elif choice == "p":
        print('Paper versus ')

    move_number = random.randint(1,3)
    if move_number == 1:
        computerchoice = 'r'
        print("Rock")
    elif move_number == 2:
        computerchoice = 's'
        print ("Scissors")
    else:
        move_number == 3
        computerchoice = 'p'
        print("Paper")

    if choice == computerchoice:
        print ('this is a tie game')
        ties = ties + 1
    elif choice == 'r' and computerchoice == 's':
        print('you win rock beats scissors')
        wins = wins + 1
    elif choice == 's' and computerchoice == 'p':
        print('you win scissors beats paper')
        wins = wins +1
    elif choice == "p" and computerchoice == 'r':
        print ('you win paper beats rock')
        wins = wins +1
        
