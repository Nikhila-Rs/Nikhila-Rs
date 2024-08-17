# Hangman Game

import random
words = ["milk", "banana", "nuts", "dates", "berries"]
word_to_guess = random.choice(words)
guessed_letters = ["_"] * len(word_to_guess)
lives = 6
print("Welcome to Hangman smoothie version!")
print("You have", lives, "lives.")
while lives > 0:
    print(" ".join(guessed_letters))
    letter = input("Guess a letter: ")
    if letter in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == letter:
                guessed_letters[i] = letter
    else:
        lives -= 1
        print("Incorrect! You have", lives, "lives left.")
    if "_" not in guessed_letters:
        print("Congratulations! You won!")
        break

if lives == 0:
    print("Game over! The word was", word_to_guess)
