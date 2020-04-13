package ch01.ex03;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.Random;

public class AnswerTest {

    private static final Random generator = new Random();

    @Test
    public void testMax3() {

        for (int i = 0; i < 100; i++) {
            int a = generator.nextInt();
            int b = generator.nextInt();
            int c = generator.nextInt();
            assertEquals(Answer.threeMax(a, b, c),
                    Answer.threeMax2(a, b, c));
        }
    }
}
