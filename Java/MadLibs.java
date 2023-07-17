package Java;

// Non Pronanun
// 11/14/2021
// CSE 142
// TA: Eric Von Carlos Latham II
// Take Home Assignment 6
// This program plays a game of Madlibs,
// the user can input in words to modify a 
// story.

import java.io.*;
import java.util.*;

public class MadLibs {
    // this is the main method. It first prints out the introduction, then it prompts
    // the menu of the program. The menu asks for the user input, which when valid will call
    // their respective methods. It will continue to run unless the user chooses to quit. 
    public static void main(String[] args)throws FileNotFoundException{
        Scanner sc = new Scanner(System.in);
        introduction();
        boolean play = true;
        while(play){
            System.out.print("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ");
            String input = sc.nextLine();
            if(input.toLowerCase().equals("c")){
                Scanner read = new Scanner(inputName(sc));
                createFile(sc, read);
                System.out.println();
            }
            if(input.toLowerCase().equals("v")){
                Scanner view = new Scanner(inputName(sc));
                viewFile(view);
                System.out.println();
            }
            if(input.toLowerCase().equals("q")){
                play = false;
                System.out.println();
            }
        }
    }

    // this method prints out the introduction of the program.
    public static void introduction(){
        System.out.println("Welcome to the game of Mad Libs.");
        System.out.println("I will ask you to provide various words");
        System.out.println("and phrases to fill in a story.");
        System.out.println("The result will be written to an output file.");
        System.out.println();
    }

    // this method asks for the fileName and will repeat if an invalid
    // fileName is inputted. it uses the scanner keyboard as the parameter
    // and it returns a file.
    public static File inputName(Scanner sc){
        System.out.print("Input file name: ");
        String input = sc.nextLine();
        File inFile = new File(input);
        while(!inFile.exists()){
            System.out.print("File not found. Try again: ");
            input = sc.nextLine();
            inFile = new File(input);
        }
        return inFile;
    }

    // this method will read the file that is passed into the parameter and
    // it creates a new file that users can rewrite the story with certain words.
    // it takes the scanner both file and keyboard as the input, and prints out
    // a statement at the end.
    public static void createFile(Scanner sc, Scanner inputFile)throws FileNotFoundException{
        System.out.print("Output file name: ");
        String fileName = sc.nextLine();
        System.out.println();
        PrintStream output = new PrintStream(fileName);
        while(inputFile.hasNextLine()){
            String line = inputFile.nextLine();
            Scanner word = new Scanner(line);
            while(word.hasNext()){
                String words = word.next();
                if(words.startsWith("<") && words.endsWith(">")){
                    words = words.substring(1, words.length()-1);
                    words = words.replace("-", " ");
                    String aOrAn = vowelCheck(words);
                    System.out.print("Please type " + aOrAn + " " + words + ": ");
                    words = sc.nextLine();
                    output.print(words + " ");
                } else {
                    output.print(words + " ");
                } 
            }
            output.println();
        }
        System.out.println("Your mad-lib has been created!");
    }

    // this method allows users to view a file that already exists by printing it out.
    // this method takes uses scanner file as the input.
    public static void viewFile(Scanner inputFile)throws FileNotFoundException{
        System.out.println();
        while(inputFile.hasNextLine()){
                String words = inputFile.nextLine();
                System.out.println(words);
        }
    }

    // this method checks whether or a word starts with a vowel or not
    // which determines whether 'a' or 'an' will be used. it uses string check as
    // an input and returns a string.
    public static String vowelCheck(String check){
        if(check.toLowerCase().startsWith("a") || check.toLowerCase().startsWith("e") 
        || check.toLowerCase().startsWith("i") || check.toLowerCase().startsWith("o")
        || check.toLowerCase().startsWith("u")){
            return "an";
        } else {
            return "a";
        }
    }
}
