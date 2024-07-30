import random

def get_comp_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter your choice (snake,water, or gun): ").lower()
        if user_input in ['snake', 'water', 'gun']:
            return user_input
        else:
            print("Invalid choice. Please choose snake, water, or gun.")

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'snake' and comp_choice == 'gun') or \
         (user_choice == 'gun' and comp_choice == 'water') or \
         (user_choice == 'water' and comp_choice == 'snake'):
        return "You win!"
    else:
        return "Computer wins!!"

def play_game():
    print("Snake-Water-Gun Game")
    
    user_choice = get_user_choice()
    comp_choice = get_comp_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    
    result = determine_winner(user_choice, comp_choice)
    print(result)

if __name__ == "__main__":
    play_game()
