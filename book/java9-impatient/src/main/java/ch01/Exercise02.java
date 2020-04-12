// Write a program that reads an integer angle (which may be positive
// or negative) and normalize it to a value between 0 and 359 degrees.
// Try it first with the % operator, then with floorMod.

// Note: If not using floorMod(), need to use % twice (with add) to
//       overcome the possible negative values.

package ch01;

import util.Input;

class Exercise02 {

    public static void main(String[] args) {
        int v = Input.readInt("Enter an angle: ");
        System.out.printf("%d = %d, %d\n", v,
                normalizeAngle(v, 360),
                Math.floorMod(v, 360));  // handles negative correctly
    }

    // % will return negative result, which is unfortunate
    // so need to handle it explicitly, a hassle.
    static int normalizeAngle(int v, int n) {
        // while (v < 0) v += 360;  // not very efficient
        // return v % 360
        return ((v % n) + n) % n;
    }
}
