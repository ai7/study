// Implement an immutable class Point that describes a point in the
// plane. Provide a constructor to set it to a specific point, a
// no-arg constructor to set it to the origin, and a method getX,
// getY, translate, and scale. The translate method moves the point by
// a given amount in x- and y-direction. The scale method scales both
// coordinates by a given factor. Implements these methods so that
// they return new points with the results. For example,
//
// Point p = new Point(3, 4).translate(1,3).scale(0.5);
//
// Should set p to a point with coordinates (2, 3.5)

package ch02.ex05;

public class Answer {

    /**
     * A point in the plane.
     */
    public static class Point {
        private final double x;  // immutable, set via constructor
        private final double y;

        /**
         * The no-arg constructor.
         */
        public Point() {
            x = 0;
            y = 0;
        };

        /**
         * Create a point at specific location.
         * @param x  x coordinate
         * @param y  y coordinate
         */
        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        /**
         * Get the x-coordinate
         * @return  x-coordinate.
         */
        public double getX() {  // getters
            return x;
        }

        /**
         * Get the y-coordinate.
         * @return  y-coordinate.
         */
        public double getY() {  // getters
            return y;
        }

        /**
         * shift point by specified x,y amount.
         * @param x  amount to shift in x direction
         * @param y  amount to shift in y direction
         * @return  new point.
         */
        public Point translate(double x, double y) {
            return new Point(this.x + x, this.y + y);
        }

        /**
         * scale point by specified amount.
         * @param f  amount to scale in x/y dimension
         * @return  new point.
         */
        public Point scale(double f) {
            return new Point(this.x * f,this.y * f);
        }

        /**
         * String representation.
         * @return  string
         */
        @Override
        public String toString() {
            return "Point(" + x + ", " + y + ")";
        }
    }

    public static void main(String[] args) {
        Point p = new Point(3, 4).translate(1,3).scale(0.5);
        System.out.println(p);
    }
}
