// Improve the average method so that it is called with at least one
// parameter.

// Note: just use vararg after 1st parameter, trivial.

package ch01.ex16;

public class Answer {

    static double average(double x, double... values) {
        for (double v: values) {
            x += v;
        }
        return x / (values.length + 1);
    }

    public static void main(String[] args) {
        System.out.println(average(1));
        System.out.println(average(1, 2));
        System.out.println(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
    }
}
