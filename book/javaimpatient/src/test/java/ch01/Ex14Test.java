package ch01;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.Random;

public class Ex14Test {

    @Test
    public void testPerfectMatrix() {
        int[][] M = {
                {16, 3, 2, 13},
                {5,10, 11, 8},
                {9, 6, 7, 12},
                {4, 15, 14, 1}
        };
        assertTrue(Exercise14.checkMatrix(M));
    }
}
