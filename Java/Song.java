package Java;

// Non Pronanun
// 10/5/2021
//CSE 142
//TA: Eric Von Carlos Latham II
//Take Home Assignment 1
//This program will print the lyrics to the song an 
//old lady who swallowed a fly using only one println statement
//for each line to reduce redundancy.



public class Song {
    // TODO: Your Code Here
    //this is the main method which will print out the song.
    public static void main(String[] arg){
        verseOne();
        verseTwo();
        verseThree();
        verseFour();
        verseFive();
        verseSix();
        verseSeven();
    }

    //this will print out the first verse of the song.
    public static void verseOne(){
        System.out.println("There was an old woman who swallowed a fly.");
        swallowedFly();
    }

    //this will print out the second verse of the song.
    public static void verseTwo(){
        System.out.println("There was an old woman who swallowed a spider,");
        System.out.println("That wriggled and iggled and jiggled inside her.");
        swallowedSpider();
    }

    //this will print out the third verse of the song.
    public static void verseThree(){
        System.out.println("There was an old woman who swallowed a bird,");
        System.out.println("How absurd to swallow a bird.");
        swallowedBird();
    }

    //this will print out the fourth verse of the song.
    public static void verseFour(){
        System.out.println("There was an old woman who swallowed a cat,");
        System.out.println("Imagine that to swallow a cat.");
        swallowedCat();
    }

    //this will print out the fifth verse of the song.
    public static void verseFive(){
        System.out.println("There was an old woman who swallowed a dog,");
        System.out.println("What a hog to swallow a dog.");
        swallowedDog();
    }

    //this will print out the sixth verse of the song.
    public static void verseSix(){
        System.out.println("There was an old woman who swallowed a raccoon.");
        System.out.println("Who would swallow a raccoon,");
        swallowedRaccoon();
    }

    //this will print out the seventh verse of the song.
    public static void verseSeven(){
        System.out.println("There was an old woman who swallowed a horse,");
        System.out.println("She died of course.");
    }

    //this line will print the redundant part of the song starting
    //from swallowing the spider
    public static void swallowedSpider(){
        System.out.println("She swallowed the spider to catch the fly,");
        swallowedFly();
    }

    //this line will print out the final part of 
    //the redundant part of the song
    public static void swallowedFly(){    
        System.out.println("I don't know why she swallowed that fly,");
        System.out.println("Perhaps she'll die.");
        System.out.println();
    }

    //this line will printout the redundant part 
    //starting from bird swallowing the spider
    public static void swallowedBird(){
        System.out.println("She swallowed the bird to catch the spider,");
        swallowedSpider();
    }

    //this line will printout the redundant
    //part starting from cat swallowing the bird.
    public static void swallowedCat(){
        System.out.println("She swallowed the cat to catch the bird,");
        swallowedBird();
    }

    //this will printout the redundant part of the 
    //song starting from swallowing the dog.
    public static void swallowedDog(){
        System.out.println("She swallowed the dog to catch the cat,");
        swallowedCat();
    }

    //this will print out the redundant part of the song 
    //starting from swallowing the raccoon.
    public static void swallowedRaccoon(){
        System.out.println("She swallowed the raccoon to catch the dog,");
        swallowedDog();
    }
}
