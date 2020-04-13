package ch02.ex06;

public class Point {
    private double x;  // not final, need to modify
    private double y;

    public Point() { }  // no-arg constructor

    public Point(double x, double y) {  // regular constructor
        this.x = x;
        this.y = y;
    }

    public double getX() {  // getters
        return x;
    }

    public double getY() {  // getters
        return y;
    }

    public Point translate(double x, double y) {
        this.x += x;
        this.y += y;
        return this;
    }

    public Point scale(double f) {
        this.x *= f;
        this.y *= f;
        return this;
    }

    @Override
    public String toString() {
        return "Point(" + x + ", " + y + ")";
    }
}
