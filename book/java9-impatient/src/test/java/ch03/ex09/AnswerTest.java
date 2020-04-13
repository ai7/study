package ch03.ex09;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class AnswerTest {
    @Test
    public void test_RunGreeter() {
        Answer.runGreeter(10);
    }
}
