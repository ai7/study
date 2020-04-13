package ch03.ex08;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Answer {
    public static void luckySort(ArrayList<String> strings, Comparator<String> comp) {
        if (strings == null || strings.size() < 2) {
            return;
        }
        int i = 0;
        while (!isSorted(strings, comp)) {
            System.out.printf("[%d] shuffling\n", ++i);
            Collections.shuffle(strings);
        }
        System.out.printf("Shuffled %d times\n", i);
    }

    static boolean isSorted(ArrayList<String> strings, Comparator<String> comp) {
        for (int i = 0; i < strings.size() - 1; i++) {
            if (comp.compare(strings.get(i), strings.get(i+1)) > 0) {
                // false if element i > i+1, same is ok.
                return false;
            }
        }
        return true;
    }
}
