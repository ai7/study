package ch01.ex03;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.Random;

public class Ex03Test {

    private static final Random generator = new Random();

    @Test
    public void testMax3() {

        for (int i = 0; i < 100; i++) {
            int a = generator.nextInt();
            int b = generator.nextInt();
            int c = generator.nextInt();
            assertEquals(Exercise03.threeMax(a, b, c),
                    Exercise03.threeMax2(a, b, c));
        }
    }
}
