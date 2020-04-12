// Write a program that reads an integer and print it in binary,
// octal, and hexadecimal. Print the reciprocal as a hexadecimal
// floating-point number.

// Note: use correct printf() formatter for oct, hex.
//       Integer.toBinaryString() for binary.

package ch01;

import util.Input;

class Exercise01 {

    public static void main(String[] args) {
        int v = Input.readInt("Enter a number: ");
        printNum(v);
    }

    static void printNum(int v) {
        // using < for previous params.
        System.out.printf("dec: %d, oct: %<#o, hex: %<#x, bin: %s\n",
                          v, Integer.toBinaryString(v))
                .printf("  reciprocal: %a\n", 1.0/v);
    }
}
