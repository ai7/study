// Write a program that computes the factorial n! = 1 x 2 x ... x n,
// using BigInteger. Compute the factorial of 1000.

// Note: standard factorial code.

package ch01;

import java.math.BigInteger;

import util.Input;

public class Exercise06 {

    static BigInteger factorial(int n) {
        BigInteger v = BigInteger.valueOf(1);
        for (int i = 2; i <= n; i++) {
            v = v.multiply(BigInteger.valueOf(i));
        }
        return v;
    }

    public static void main(String[] args) {
        int n = Input.readInt("Enter a number: ");
        BigInteger v = factorial(n);
        System.out.println(v);
    }

}
