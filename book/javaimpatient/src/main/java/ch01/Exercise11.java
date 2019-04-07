// Write a program that reads a line of text and prints all characters
// that are not ASCII, together with their unicode values.

// Note: iterate through string, print out any char > 127 using
//       printf() %c and %x.

package ch01;

import util.Input;

public class Exercise11 {

    public static void main(String[] args) {
        String line = Input.readLine("Input line: ");
        printNonAscii(line);
    }

    static void printNonAscii(String line) {
        System.out.println("Non ASCII chars:");
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c > 127) {
                // %c works for unicoce char, but %x need int, not char.
                System.out.printf("  %c: %#x\n", c, (int) c);
            }
        }
    }
}
