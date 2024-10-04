import java.util.Scanner;
import java.util.Random;

public class BullsAndCowsGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int[] secretCode = new int[4]; // generate a random 4-digit code
        for (int i = 0; i < 4; i++) {
            secretCode[i] = random.nextInt(10);
        }

        int attempts = 0;

        while (true) {
            System.out.println("Enter a 4-digit code:");
            String userInput = scanner.next();

            if (userInput.length() != 4) {
                System.out.println("Invalid input. Please enter a 4-digit code.");
                continue;
            }

            int[] userInputArray = new int[4];
            for (int i = 0; i < 4; i++) {
                userInputArray[i] = userInput.charAt(i) - '0';
            }

            int bulls = 0;
            int cows = 0;

            for (int i = 0; i < 4; i++) {
                if (userInputArray[i] == secretCode[i]) {
                    bulls++;
                } else if (isDigitInCode(userInputArray[i], secretCode)) {
                    cows++;
                }
            }

            System.out.println("Bulls: " + bulls);
            System.out.println("Cows: " + cows);

            attempts++;

            if (bulls == 4) {
                System.out.println("Congratulations! You cracked the code in " + attempts + " attempts.");
                break;
            }
        }
    }

    public static boolean isDigitInCode(int digit, int[] code) {
        for (int i = 0; i < 4; i++) {
            if (code[i] == digit) {
                return true;
            }
        }
        return false;
    }
}