package ch03.ex01;

import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class AnswerTest {

    double[] salaries = { 100, 101, 103, 105 };
    private Employee[] workers;

    @Before
    public void setUp() throws Exception
    {
        // need boxed() to convert from DoubleStream to Stream<Double>
        workers = Arrays.stream(salaries)
                .boxed()
                .map(Employee::new)
                .toArray(Employee[]::new);
    }

    @Test
    public void test_Average() {
        // act
        double average = Answer.average(workers);
        // verify
        assertEquals(Arrays.stream(salaries)
                        .average()
                        .orElse(Double.NaN),
                average, 0.001);
    }
}
