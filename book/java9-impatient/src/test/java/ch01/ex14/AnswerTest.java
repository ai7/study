package ch01.ex14;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class AnswerTest {

    @Test
    public void testPerfectMatrix() {
        int[][] M = {
                {16, 3, 2, 13},
                {5,10, 11, 8},
                {9, 6, 7, 12},
                {4, 15, 14, 1}
        };
        assertTrue(Answer.checkMatrix(M));
    }
}
