// Using only the conditional operator, write a program that reads 3
// integers and prints the largest. Repeat with Math.max.

// Note: carefully crafted if statements. Much simpler if Math.max(),

package ch01.ex03;

import util.Input;

public class Answer {

    // using only conditional operators
    static int threeMax(int a, int b, int c) {
        if (a > b) {
            if (b > c) {
                return a;
            } else {  // b <= c
                if (a > c) {
                    return a;
                } else {
                    return c;
                }
            }
        } else {  // a <= b
            if (b > c) {
                return b;
            } else {  // b <= c
                return c;
            }
        }
    }

    static int threeMax2(int a, int b, int c) {
        return Math.max(Math.max(a, b), c);
    }

    public static void main(String[] args) {
        int[] A = Input.readInts(3);
        System.out.printf("max: %d, %d\n",
                threeMax(A[0], A[1], A[2]),
                threeMax2(A[0], A[1], A[2]));
    }

}
