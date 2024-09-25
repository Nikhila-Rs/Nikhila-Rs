#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int number, guess, attempts = 0;
    const int MAX_NUMBER = 100;
    srand(time(0));
    number = rand() % MAX_NUMBER + 1; 
 printf("Welcome to the Number Guessing Game!\n");
    printf("I've chosen a number between 1 and %d. Can you guess it?\n", MAX_NUMBER);11
    
    do {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        attempts++;

        if (guess > number) {
            printf("Too high! Try again.\n");
        } else if (guess < number) {
            printf("Too low! Try again.\n");
        } else {
            printf("Congratulations! You guessed the number in %d attempts.\n", attempts);
        }
    } while (guess != number);

    return 0;
}

