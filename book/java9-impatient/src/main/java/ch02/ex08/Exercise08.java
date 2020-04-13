// In the preceding exercise, providing the constructors and getter
// methods of the Point class was rather repetitive. Most IDEs have
// shortcuts for writing boilerplate code. What does your IDE offer?

// Note:
//   enter class, and instance variables first, then cmd-n, can select
//   constructors, getters, setters, toString, etc.

package ch02.ex08;

public class Exercise08 {

    public static class Point {  // manually
        private double x;  // manually
        private double y;  // manually

        public Point() {
        }

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double getX() {
            return x;
        }

        public double getY() {
            return y;
        }

        @Override
        public String toString() {
            return "Point{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }

}
