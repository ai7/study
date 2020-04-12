package ch03.ex05;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class SolutionTest {

    @Test
    public void test_ConstantSequence() {
        // act
        IntSequence x = IntSequence.constant(7);
        // verify
        for (int i = 0; i < 100; i++) {
            assertTrue(x.hasNext());
            assertEquals(7, x.next());
        }
    }
}
