package ch02.ex10;

import java.util.ArrayList;
import java.util.Random;

public class RandomNumbers {

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
