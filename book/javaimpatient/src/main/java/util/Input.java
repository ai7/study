package util;

import java.util.Scanner;

public class Input {

    private static final Scanner in = new Scanner(System.in);

    private Input() {}

    // get one integer from stdin, consume newline
    public static int readInt(String prompt) {
        if (prompt != null) System.out.print(prompt);
        int v = in.nextInt();
        in.nextLine();  // consume the newline
        return v;
    }

    public static int[] readManyInts(String prompt) {
        if (prompt != null) System.out.print(prompt);

        // get input line, return if empty
        String line = in.nextLine();
        line = line.trim();
        if (line.isEmpty()) return null;

        // split into int[]
        String[] A = line.trim().split("\\s+");
        int[] X = new int[A.length];
        for (int i = 0; i < X.length; i++) {
            X[i] = Integer.parseInt(A[i]);
        }

        return X;
    }

    /**
     * Read n integers from stdin
     * @param prompt  intro prompt to use
     * @param n  number of integers to read
     * @return  array of integers read.
     */
    public static int[] readInts(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException(String.format("n must be positive: %d", n));
        }
        // print a suitable prompt
        if (n == 1) {
            System.out.print("Enter a number: ");
        } else {
            System.out.print(String.format("Enter %d numbers: ", n));
        }

        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = in.nextInt();
        }

        return A;
    }

    public static String readLine(String prompt) {
        if (prompt != null && !prompt.isEmpty()) {
            System.out.print(prompt);
        }
        return in.nextLine();
    }
}
