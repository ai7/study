package ch03.ex10;

import org.junit.Test;

public class AnswerTest {
    @Test
    public void test_runTogether() {
        Answer.runTogether(new ch03.ex09.Greeter(10, "Greeter A"),
                new ch03.ex09.Greeter(10, "Greeter B"),
                new ch03.ex09.Greeter(10, "Greeter C"),
                new ch03.ex09.Greeter(10, "Greeter D"));
    }

    @Test
    public void test_runInOrder() throws InterruptedException {
        Answer.runInOrder(new ch03.ex09.Greeter(10, "Greeter A"),
                new ch03.ex09.Greeter(10, "Greeter B"),
                new ch03.ex09.Greeter(10, "Greeter C"),
                new ch03.ex09.Greeter(10, "Greeter D"));
    }
}
