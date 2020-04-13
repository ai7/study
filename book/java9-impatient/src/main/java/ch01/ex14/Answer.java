// Write a program that reads a 2 dimensional array of integers and
// determine whether it is a magic square (that is, whether the sum of
// all rows, all columns, and the diagonals is the same). Accept lines
// of input that you break up into individual integers, and stop when
// the user enters a blank line. For example, with the input
//   16 3 2 13
//   5 10 11 8
//   9 6 7 12
//   4 15 14 1
//   (blank line)
// your program should respond affirmatively.

// Note: a bit mechanical, but the various check function is easy to
//       write. The readMatrix function is a bit tricky, as if using
//       regular int[][] we need to know the # of rows ahead of time
//       so we can allocate it, so asked for number of rows.
//
//       if don't want to ask for rows, have to use an ArrayList and
//       convert back to int[][]?

package ch01.ex14;

import java.util.ArrayList;
import java.util.Arrays;

import util.Input;

public class Answer {

    static boolean checkRow(int[][] M, int v) {
        for (int r = 0; r < M.length; r++) {  // also: "for (int[] R: M)"
            int sum = 0;  // sum up each row
            for (int c = 0; c < M[r].length; c++) {
                sum += M[r][c];
            }
            if (sum != v) {  // check if equal to target
                return false;
            }
        }
        return true;
    }

    static boolean checkColumn(int[][] M, int v) {
        for (int c = 0; c < M[0].length; c++) {
            int sum = 0;
            for (int r = 0; r < M.length; r++) {
                sum += M[r][c];
            }
            if (sum != v) {
                return false;
            }
        }
        return true;
    }

    static boolean checkDiag(int[][] M, final int v) {
        int cols = M[0].length;
        int sum = 0;
        int sum2 = 0;

        // check top left to bottom right diag
        for (int i = 0; i < M.length; i++) {
            sum  += M[i][i];  // top left -> bottom right
            sum2 += M[i][cols - i - 1];  // top right -> bottom left
        }

        return (sum == v && sum2 == v);
    }

    static boolean checkMatrix(int[][] M) {
        int v = Arrays.stream(M[0]).sum();
        if (!checkRow(M, v)) return false;
        if (!checkColumn(M, v)) return false;
        if (!checkDiag(M, v)) return false;
        return true;
    }

    static int[][] readMatrix() {
        // now get the matrix data
        System.out.println("Enter matrix, blank line to end:");
        ArrayList<int[]> M = new ArrayList<>();
        while (true) {
            int[] A = Input.readManyInts(null);
            if (A == null) break;
            M.add(A);
        }
        // validate matrix dimension
        for (int[] row: M) {
            if (row.length != M.size()) {
                System.out.printf("Bad matrix, expect %d fields, got %d\n",
                        M.size(), row.length);
                return null;
            }
        }

        int[][] retval = new int[M.size()][];
        return M.toArray(retval);
    }

    static void printMatrix(int[][] M) {
        for (int[] r: M) {
            System.out.println(Arrays.toString(r));
        }
    }

    public static void main(String[] args) {
        int[][] M = readMatrix();
        if (M != null) {
            printMatrix(M);
            System.out.println(checkMatrix(M));
        }
    }
}
