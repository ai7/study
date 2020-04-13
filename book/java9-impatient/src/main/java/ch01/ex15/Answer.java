// Write a program that stores Pascal's triangle up to a given n in an
// ArrayList<ArrayList<Integer>>.

// Note: initializing an ArrayList row with element is slightly
//       non-trivial, since we can't set pos x directly as we can only
//       add elements gradually. ArrayList initial size doesn't
//       actually create empty element, obviously. We need to do it
//       ourselves.

package ch01.ex15;

import java.util.ArrayList;

import util.Input;

public class Answer {

    static ArrayList<ArrayList<Integer>> pascalTriangle(int n) {
        ArrayList<ArrayList<Integer>> M = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            // create rows and initial elements
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    row.add(1);
                } else {
                    row.add(0);
                }
            }
            // now compute the middle elements
            for (int j = 1; j < i; j++) {
                row.set(j, M.get(i-1).get(j-1) + M.get(i-1).get(j));
            }
            // attach row to list
            M.add(row);
        }
        return M;
    }

    public static void main(String[] args) {
        int n = Input.readInt("pascal triangle size: ");
        ArrayList<ArrayList<Integer>> M = pascalTriangle(n);
        for (ArrayList<Integer> v: M) {
            System.out.println(v.toString());
        }
    }
}
