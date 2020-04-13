// Repeat the preceding exercise, but now make translate and scale
// into mutators.

// Note:
//   just set instance variables and return this.

package ch02.ex06;

public class Answer {

    public static void main(String[] args) {
        Point p = new Point(3, 4).translate(1,3).scale(0.5);
        System.out.println(p);
    }
}
