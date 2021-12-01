import java.io.*;
import java.util.*;

// I completed part 2 in Java since I am more confortable with it, I am going to learn more about the different types of 
// lists in python tonight to be prepared for tomorrow's challenge.

public class Day1P2 {
    public static void main(String[] args) throws FileNotFoundException {
        
        // Creating new file object to be read
        File lst = new File("C:\\Users\\12268\\Desktop\\AdventOfCode\\AdventOfCode\\src\\input.txt");

        ArrayList<Integer> list = new ArrayList<Integer>(); // Array list to store file data
        Scanner read = new Scanner(lst); // Scanner to read file

        while (read.hasNextInt()) // Adds all lines to list!
        {
            list.add(read.nextInt());
        }

        int numberOfIncreases = 0; // Count for number of sum increases
        for (int i = 3; i < list.size(); i++) {
            numberOfIncreases += list.get(i) > list.get(i - 3) ? 1 : 0; // If true, 1 will return, false if 0. 
        }

        System.out.println(numberOfIncreases); // Printing solution
    }
}
