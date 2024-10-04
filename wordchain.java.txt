import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class WordChainGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> wordList = new ArrayList<>();
        System.out.println("Welcome to Word Chain Game!");
        System.out.println("Enter a starting word:");
        String startingWord = scanner.next();
        wordList.add(startingWord);
        while (true) {
            System.out.println("Enter a word that starts with the last letter of the previous word:");
            String userInput = scanner.next();
        if (userInput.length() < 1) {
                System.out.println("Invalid input. Please enter a valid word.");
                continue;
            }
        String lastLetter = wordList.get(wordList.size() - 1).substring(wordList.get(wordList.size() - 1).length() - 1);
            if (userInput.substring(0, 1).equalsIgnoreCase(lastLetter)) {
                wordList.add(userInput);
                System.out.println("Word added to the chain!");
            } else {
                System.out.println("OOPS CHAIN BREAKED! The word must start with the last letter of the previous word.");
            }
        }
    }
}