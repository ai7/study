package ch03.ex04;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class AnswerTest {

    @Test
    public void test_IntSequence() {
        // act
        IntSequence s = IntSequence.of(1,2,3,4);
        // verify
        assertNotNull(s);
        assertTrue(s.hasNext());
        assertEquals(1, s.next());
        assertTrue(s.hasNext());
        assertEquals(2, s.next());
        assertTrue(s.hasNext());
        assertEquals(3, s.next());
        assertTrue(s.hasNext());
        assertEquals(4, s.next());
        assertFalse(s.hasNext());
    }
}
