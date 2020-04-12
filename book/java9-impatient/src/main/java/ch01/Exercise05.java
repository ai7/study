// What happens when you cast a double to an int that is larger than
// the largest possible int value? Try it out.

// Note: left bits are dropped?

package ch01;

public class Exercise05 {
    public static void main(String[] args) {
        // left bits are dropped?
        int x = (int) 1234567890234.0;
        System.out.println(x);
    }
}
