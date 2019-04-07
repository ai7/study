package ch01;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.Random;

public class Ex02Test {

    private static final Random generator = new Random();

    @Test
    public void testNormalize() {

        for (int i = 0; i < 10; i++) {
            int v = generator.nextInt();
            assertEquals(Exercise02.normalizeAngle(v, 360),
                    Math.floorMod(v, 360));
            assertEquals(Exercise02.normalizeAngle(-v, 360),
                    Math.floorMod(-v, 360));
        }
    }
}
