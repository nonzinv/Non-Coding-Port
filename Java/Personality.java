package Java;

// Non Pronanun
// 11/21/2021
// CSE 142
// TA: Eric Von Carlos Latham II
// Take Home Assignment 7
// This program takes in a file with the content of a Keirsey test and processes
// the results and prints the distribution of answers and the personality
// type into another file.

import java.util.*;
import java.io.*;

public class Personality {
    // TODO: Your Code Here
    public static final int DIMENSIONS = 4; 
    // this is the main method, it calls other methods to process the file 
    // and it prints the results into the output file.
    public static void main(String[] args) throws FileNotFoundException{
        Scanner console = new Scanner(System.in);
        introduction();
        System.out.print("input file name? ");
        Scanner input = new Scanner(new File(console.nextLine()));
        System.out.print("output file name? ");
        PrintStream output = new PrintStream(console.nextLine());
        while(input.hasNextLine()){
            String name = input.nextLine();
            String response = input.nextLine().toLowerCase();
            int[] numA = countTraits(response, 'a');
            int[] numB = countTraits(response, 'b');
            int[] percentB = getPercent(numA, numB);
            String personality = getPerson(percentB);
            output.println(name + ": " + Arrays.toString(percentB) + " = " + personality);
        }
    }

    // this method prints out the introduction of the program.
    public static void introduction(){
        System.out.println("This program processes a file of answers to the");
        System.out.println("Keirsey Temperament Sorter. It converts the");
        System.out.println("various A and B answers for each person into");
        System.out.println("a sequence of B-percentages and then into a");
        System.out.println("four-letter personality type.");
        System.out.println();
    }

    // this method counts the number of each answer in each of the categories
    // of the trait. This method uses the String of responses and the char we want
    // to find as the parameters and it returns an array of the results.
    public static int[] countTraits(String ans, char opt){
        int[] result = new int[DIMENSIONS];
        for(int i = 0; i < ans.length(); i++){
            if(ans.charAt(i) == opt){
                int index = ((i % 7) + 1)/2;
                result[index]++;
            }
        }
        return result;
    }
    
    // this method calculates the percent of 'b' answers in each section of the
    // traits. this method uses two int arrays as parameters, and it returns the
    // int array of the percentage of 'b' answers.
    public static int[] getPercent(int[] a, int[] b){
        int[] result = new int[DIMENSIONS];
        for(int i = 0; i < b.length; i++){
            double bSection = b[i];
            double percent = (bSection/(a[i]+b[i])) * 100;
            result[i] = (int)Math.round(percent);
        }
        return result;
    }
    
    // this method uses the percent calculated into determining the personality trait
    // of each person. This method uses the int array percentB as the parameter and it 
    // returns a string of personality trait as an output.
    public static String getPerson(int[] percentB){
        String result = "";
        String[] typeI = {"E", "S", "T", "J"};
        String[] typeII = {"I", "N", "F", "P"};
        for(int i = 0; i < percentB.length; i++){
            if(percentB[i] < 50){
                result += typeI[i] + "";
            } else if(percentB[i] > 50){
                result += typeII[i] + "";
            } else {
                result += "X";
            }
        }
        return result;
    }
}



    


