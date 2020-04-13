// Write a program that prints the smallest and largest positive
// double values. Hint: lookup Math.nextUp in the Java API.

// Note: use Math.nextUp() Math.nextDown() from both ends.
//       print value using %s.

package ch01.ex04;

public class Exercise04 {

    // smallest positive double
    static double smallestDouble() {
        return Math.nextUp(0.0);
    }

    // largest positive double
    static double largestDouble() {
        return Math.nextDown(Double.POSITIVE_INFINITY);
    }

    public static void main(String[] args) {
        // printf with %f/$e won't format it with max digits
        // print() or %s seem to do a better at printing these extreme values.
        System.out.printf("%s, %s\n", smallestDouble(), largestDouble());
    }
}
