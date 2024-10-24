import random
import time

def number_sequence_game():
    sequence = []
    round_number = 1

    while True:
        
        new_number = random.randint(1, 9)
        sequence.append(new_number)

        print(f"Round {round_number}:")
        print("Remember this sequence:")
        print(" ".join(map(str, sequence)))
        time.sleep(2)  
        print("\033c", end="")  

        
        player_input = input("Enter the sequence (space-separated): ")
        player_sequence = list(map(int, player_input.split()))

        if player_sequence == sequence:
            print("Correct! Moving to the next round.")
            round_number += 1
        else:
            print("Wrong sequence! Game over.")
            print(f"The correct sequence was: {' '.join(map(str, sequence))}")
            break


if __name__ == "__main__":
    number_sequence_game()
