package Java;

// Non Pronanun
// 18/10/2021
// TA: Eric Von Carlos Latham II
// Take Home Assigment 3
// This program uses the input given by the
// user and encrypts the word using a key which
// is also given by the user.

import java.util.*;

public class EncryptionMachine {
    // these are the constants used in the program.
    public static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
    public static final int SHIFT = 3;

    // this is the main method of the code, which calls other methods
    // of the program.
    public static void main(String[] args){
        Scanner console = new Scanner(System.in);
        input();
        enterKey(console);
        encryptWords(console);
        outro();
    }

    // this method gives directions to the user
    // and takes in the user's input and calls the encrypt
    // method.
    public static void input(){
        System.out.println("Welcome to the CSE142 Encryption Machine!");
        System.out.println("The program lets you encrypt a message");
        System.out.println("with a key so your recipient can decrypt.");
        System.out.println(); 
    }

    // this method asks for the key to the program's encryption.
    // the parameter is the input from the user.
    public static void enterKey(Scanner console){
        System.out.println("Encrypted messages use a shared keyword to decrypt.");
        System.out.print("  Enter key: ");
        String input = console.next();
        encrypt(input);
        System.out.println();
    }

    // this method encrypts the words that the user inputs depending
    // on how many words the user wants to input.
    // the parameter used is the input from the user.
    public static void encryptWords(Scanner console){
        System.out.print("How many words are in your message? ");
        int numWords = console.nextInt();
        for(int wnum = 0; wnum < numWords; wnum++){
            System.out.print("  Next word: ");
            String w = console.next();
            encrypt(w);
        }
    }
        
    // this method encrypts the word by wrapping the alphabet
    // and adding the SHIFT to the index. 
    // the parameter that is passed into the method is the word we want to encrypt.
    public static void encrypt(String word){
        String encrypted = "";
        for(int spot = 0; spot < word.length(); spot++){
            char letter = word.charAt(spot);
            int letterIndex = ALPHABET.indexOf(letter);
            letter = ALPHABET.charAt((letterIndex + SHIFT) % ALPHABET.length());
            encrypted += letter;
        }
        System.out.println("    \""+ word +"\" has been encrypted to: " + encrypted);
        encrypted = "";
    }

    // this method is the outro of the program.
    public static void outro(){
        System.out.println();
        System.out.println("Message fully encrypted. Happy secret messaging!");
    }
}
