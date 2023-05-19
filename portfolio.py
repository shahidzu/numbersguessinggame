import random # Import random library to generate random integers

# List of prime numbers upto 100
list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Function to generate randomly selected number from the above list
def rand_num(list):
    target = random.choice(list)
    return target

# This Function displays welcome message and asks for user name
def users_name():
    print("\n--------------- Welcome to Number Guessing Game! -------------")
    print("In this two player game, Least attempts determine the Winner!\n")
    while True:   
        name1 = input("Player 1: Enter your name: ")
        print(name1.title(),", Let's Play!\nSelect an option below:\n")
        winnings()
        name2 = input("Player 2: Enter your name: ")
        print(name2.title(),"Let's Play!\nSelect an option below:\n")
        winnings()
    return 

# This function lets user selects number range or given prime list number upto 100.
# It guides the user in the direction of target as well as prints the number of attempts, once the user select the target.
def winnings():
    users_selection = int(input("1. Select a range of numbers (Enter '1')  \n2. Prime numbers from 1 to 100  (Enter '2')\n"))
    count = 0
    if users_selection == 1:
        lower = int(input("Enter Lower bound: ")) 
        upper = int(input("Enter Upper bound: "))
        if lower >= 0 and upper >= 0 and upper >= lower:
            target = random.randint(lower, upper)
            #print(target)    
        else:   
           print("Invalid Entry") 
           #print(target) 
        
    elif users_selection  == 2:   
        target = rand_num(list)
        #print(target)
    else:
        target = 'NA'
        print("Invalid selection.")

    while target != 'NA':
        guess = int(input( "Guess a number: "))
        count += 1

        if guess == target:
            print("\nCongratulations, you guessed it correctly! It took you",count,"attempt(s).\n")
            '''exit = input("Would you like to exit the game? Enter 'yes'")
            if exit == 'yes':'''
            break

        elif guess > target:
            print("Select a lower number.")
            continue

        elif guess < target:
            print("Select a higher number.")
            continue
        
#Begin the game by calling users_name funtion
users_name()

