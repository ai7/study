// Write a program that prints a lottery combination, pkcking six
// distinct numbers between 1 and 49. To pick six distinct numbers,
// start with an array list filled with 1...49. Pick a random index,
// and remove the element. Repeat six times. Print the result in
// sorted order.

// Note: pick a random element and swap with end of array, repeat for
//       size n-1.

package ch01;

import java.util.Arrays;
import java.util.Random;

public class Exercise13 {

    static Random rand = new Random();

    // swap array element at index i and j
    static void swap(int[] A, int i, int j) {
        int t = A[i];
        A[i] = A[j];
        A[j] = t;
    }

    // pick n distinct numbers from 1...range.
    static int[] lottery(int range, int n) {
        // create array 1....range
        int[] A = new int[range];
        for (int i = 0; i < range; i++) {
            A[i] = i + 1;
        }
        int[] retval = new int[n];
        // pick n random elements from array.
        for (int i = 0; i < n; i++) {
            int k = rand.nextInt(range);
            retval[i] = A[k];  // store element at index k
            swap(A, k, range-1);  // put k at end of array
            range -= 1;  // decrement range
        }
        Arrays.sort(retval);
        return retval;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(lottery(10, 10)));
        for (int i = 0; i < 10; i++) {
            System.out.println(Arrays.toString(lottery(49, 6)));
        }
    }
}
