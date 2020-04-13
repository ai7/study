package ch01.ex02;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.Random;

public class AnswerTest {

    private static final Random generator = new Random();

    @Test
    public void testNormalize() {

        for (int i = 0; i < 10; i++) {
            int v = generator.nextInt();
            assertEquals(Answer.normalizeAngle(v, 360),
                    Math.floorMod(v, 360));
            assertEquals(Answer.normalizeAngle(-v, 360),
                    Math.floorMod(-v, 360));
        }
    }
}
