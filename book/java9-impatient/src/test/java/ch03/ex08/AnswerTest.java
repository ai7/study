package ch03.ex08;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Comparator;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class AnswerTest {
    @Test
    public void test_LuckySort() {
        // setup
        ArrayList<String> A = new ArrayList<>();
        A.add("test 1");
        A.add("2nd string");
        A.add("raymond");
        A.add("kaboon");
        // act
        Answer.luckySort(A, Comparator.naturalOrder());
        System.out.println(A);
        // verify
        assertTrue(Answer.isSorted(A, Comparator.naturalOrder()));
    }

    @Test
    public void test_LuckySort2() {
        // setup
        ArrayList<String> A = new ArrayList<>();
        A.add("test 1");
        A.add("2nd string");
        A.add("raymond");
        A.add("kaboon");
        // act
        Answer.luckySort(A, Comparator.reverseOrder());
        System.out.println(A);
        // verify
        assertTrue(Answer.isSorted(A, Comparator.reverseOrder()));
    }

}
