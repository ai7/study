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

    public static void main(String[] args) {
        Point p = new Point(3, 4).translate(1,3).scale(0.5);
        System.out.println(p);
    }
}
