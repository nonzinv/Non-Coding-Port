package Java;

// Non Pronanun
// 10/10/2021
// CSE142
// TA: Eric Von Carlos Latham II
// Take Home Assignment 2
// This program will print out the space needle in ASCII art
// using for loops.

public class SpaceNeedle {
    // TODO: Your Code Here
    //this line is used for scaling the size of the space needle.
    public static final int SIZE = 4;

    //this is the main method, it draws the spaceneedle by calling the other methods.
    public static void main(String[] args){
        thinTube();
        headTop();
        headBase();
        thinTube();
        middleSec();
        headTop();
    }

    //this method draws the space in front of and the || part of the space needle.
    public static void thinTube(){
        for(int row = 0; row < SIZE; row++){
            for(int space = 0; space < 3 * SIZE; space++){
                System.out.print(" ");
            }
            System.out.println("||");
        }
    }

    //this method draws the top of the head and the base of the spaceneedle.
    public static void headTop(){
        for(int row = 0; row < SIZE; row++){
            for(int space = 0; space < -3 * row + (SIZE * 3 - 3); space++){
                System.out.print(" ");
            }
            System.out.print("__/");
            for(int colons = 0; colons < 3 * row; colons++){
                System.out.print(":");
            }
            for(int line = 0; line < 2; line++){
                System.out.print("|");
            }
            for(int colon = 0; colon < 3 * row; colon++){
                System.out.print(":");
            }
            System.out.println("\\__");
        }
        System.out.print("|");
        for(int row = 0; row < SIZE; row++){
            for(int quo = 0; quo < 6 * SIZE && row < 1; quo++){
                System.out.print("\"");
            }
        }
        System.out.println("|");
    }
    
    //this method draws the base of the head for the space needle.
    public static void headBase(){
        for(int row = 0; row < SIZE; row++){
            for(int space = 0; space < 2 * row; space++){
                System.out.print(" ");
            }
            System.out.print("\\_");
            for(int tri = 0; tri < -2 * row + (2 * SIZE + SIZE - 1); tri++){
                System.out.print("/\\");
            }
            System.out.println("_/");
        }
    }

    //this method draws the tall middle section of the spaceneedle.
    public static void middleSec(){
        for(int row = 0; row < SIZE * SIZE; row++){
            for(int space = 0; space < 2 * SIZE + 1; space++){
                System.out.print(" ");
            }
            System.out.print("|");
            for(int mod = 0; mod < SIZE - 2; mod++){
                System.out.print("%");
            }
            System.out.print("||");
            for(int mods = 0; mods < SIZE - 2; mods++){
                System.out.print("%");
            }
            System.out.println("|");
        }
    }
}