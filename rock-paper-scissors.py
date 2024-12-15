import random

def play():
    # Prompt user for input
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    
    # Validate input
    if user not in ['r', 'p', 's']:
        print("Invalid choice. Please enter 'r', 'p', or 's'.")
        return
    
    # Computer makes a random choice
    computer = random.choice(['r', 'p', 's'])
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    print(f"You chose {choices[user]}, and the computer chose {choices[computer]}.")
    
    # Determine the result
    if user == computer:
        print("It's a tie!")
    elif (user == 'r' and computer == 's') or \
         (user == 's' and computer == 'p') or \
         (user == 'p' and computer == 'r'):
        print("You won!")
    else:
        print("You lost!")

# Start the game
play()
