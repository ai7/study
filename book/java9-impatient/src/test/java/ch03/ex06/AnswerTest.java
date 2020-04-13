package ch03.ex06;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

import java.math.BigInteger;

@RunWith(MockitoJUnitRunner.class)
public class AnswerTest {

    @Test
    public void test_SquareSequence() {
        // act
        Sequence<BigInteger> x = new SquareSequence();
        // verify
        for (int i = 1; i <= 100; i++) {
            assertTrue(x.hasNext());
            assertEquals(BigInteger.valueOf(i)
                            .multiply(BigInteger.valueOf(i)),
                    x.next());
        }
    }
}
