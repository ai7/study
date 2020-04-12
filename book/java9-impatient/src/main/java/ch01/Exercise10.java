// Write a program that produces a random string of letters and digits
// by generating a random long value and printing it in base36.

// Note: this is basically itoa() for base64. which Long.toString()
//       can also handle given a radix 2-36, interesting.

package ch01;

import java.util.Random;

public class Exercise10 {

    // base36 alphabet
    static String alphabet = "0123456789abcdefghijklmnopqrstuvwxyz";

    // this is basically itoa but base36
    static String base36(long v) {
        StringBuffer buf = new StringBuffer();
        while (v > 0) {
            long r = v % 36;
            buf.append(alphabet.charAt((int) r));  // append to right
            v /= 36;
        }
        return buf.reverse().toString();  // reverse string
    }

    public static void main(String[] args) {
        Random rand = new Random();
        long v = rand.nextLong();
        if (v < 0) v = -v;
        System.out.printf("%d: %s, [%s]\n", v, base36(v),
                Long.toString(v, 36));  // radix 2-36. ;)
    }
}
