// Write a program that reads a string and prints all of its
// nonempty substrings.

// Note: split sentense by whitespace using regex?

package ch01;

import java.util.Arrays;

import util.Input;

public class Exercise08 {
    public static void main(String[] args) {
        String line = Input.readLine("Enter some text: ");
        String[] A = line.split("\\s+");
        System.out.println(Arrays.toString(A));
    }
}
