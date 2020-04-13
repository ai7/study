// Write a program that reads in two integers between 0 and
// 429_696_7295, stores them in int variables, and computes and
// displays their unsigned sum, difference, product, quotient, and
// reminder. Do not convert them to long values.

// Note: +, -, * using regular operation, make sure first number is
//       larger (as unsigned). Division was a bit tricky. Cast to long
//       and then calculated.

package ch01.ex07;

import util.Input;

public class Answer {

    public static void main(String[] args) {
        int[] A = Input.readInts(2);
        calcResult(A[0], A[1]);
    }

    // interpreted as unsigned, is the first number smaller?
    // if so, we need to swap order before arithmetic
    static boolean firstSmaller(int a, int b) {
        if (a < 0 && b < 0) {  // if both are negative
            // as unsigned in, the smaller negative number
            // is also the smaller number as unsigned-int.
            return a < b;
        } else if (a < 0) {  // a is negative b is positive
            // in unsigned int, a is larger
            return false;
        } else if (b < 0) {  // a is positive, b is negative
            // in unsigned int, b is larger
            return true;
        } else {  // both are positive
            return a < b;
        }
    }

    // +, -, * will work as is, according to page 12 of book.
    // just need to interpret result as unsigned.
    static String calcSum(int a, int b) {
        return Integer.toUnsignedString(a + b);
    }
    static String calcDifference(int a, int b) {

        return Integer.toUnsignedString(a - b);
    }
    static String calcProduct(int a, int b) {
        return Integer.toUnsignedString(a * b);
    }

    // need to return string rather than int since quotient or reminder
    // may be larger than max positive int.
    static String[] calcDivide(int a, int b) {
        // ok we'll use library function
        int q = Integer.divideUnsigned(a, b);
        // not sure how to calculate reminder, since % for -1, -4
        // no matter how to arrange and flip sign, won't return 3.
        long r = Integer.toUnsignedLong(a) % Integer.toUnsignedLong(b);
        String[] retval = new String[] {
                Integer.toString(q),
                Long.toString(r) };
        return retval;
    }

    static void calcResult(int a, int b) {
        if (firstSmaller(a, b)) {
            int t = a;  // swap a <--> b
            a = b;
            b = t;
        }
        System.out.printf("Input: %d (%s), %d (%s)\n",
                a, Integer.toUnsignedString(a),
                b, Integer.toUnsignedString(b));
        System.out.printf("sum:  %s\n", calcSum(a, b));
        System.out.printf("diff: %s\n", calcDifference(a, b));
        System.out.printf("prod: %s\n", calcProduct(a, b));

        if (b == 0) {
            System.out.println("div: / by 0");
        } else if (a == 0) {
            System.out.println("div: 0");
        } else {
            // now do divide which is a bit troublesome
            String[] result = calcDivide(a, b);
            System.out.printf("div: %s reminder %s\n", result[0], result[1]);
        }

    }

}
