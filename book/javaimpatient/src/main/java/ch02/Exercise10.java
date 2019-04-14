// In the RandomNumbers class, provide two static methods
// randomElement that get a random element from an array or array list
// of integers. (Return zero if the array or array list is empty). Why
// coulnd't you make these methods into instance methods of int[] or
// ArrayList<Integer>?

// Note:
//   use the already defined nextInt() to return an index between
//   0 to A.length - 1.

package ch02;

import java.util.ArrayList;
import java.util.Random;

public class Exercise10 {

    static class RandomNumbers {

        private static Random generator = new Random();

        // return [low, high] inclusive
        public static int nextInt(int low, int high) {
            return low + generator.nextInt(high - low + 1);
        }

        public static int randomElement(int[] A) {
            if (A.length == 0) {
                return 0;
            }
            int idx = nextInt(0, A.length - 1);
            return A[idx];
        }

        public static Integer randomElement(ArrayList<Integer> A) {
            if (A.size() == 0) {
                return 0;
            }
            int idx = nextInt(0, A.size() - 1);
            return A.get(idx);
        }
    }

    public static void main(String[] args) {
        int[] A = {0, 1};
        for (int i = 0; i < 10; i++) {
            System.out.println(RandomNumbers.randomElement(A));
        }
    }
}
