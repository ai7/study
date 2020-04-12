package ch03.sec04;

import java.util.Arrays;
import java.util.Comparator;

public class LambdaTest {

    public static void main(String[] args) {
        String[] A = { "john", "doe", "kafman", "another person" };

        Arrays.sort(A, (String x, String y) -> { return x.length() - y.length(); });
   }

}
