package ch03.ex02;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

@RunWith(MockitoJUnitRunner.class)
public class SolutionTest {

    private Employee[] workers = new Employee[] {
            new Employee("John Doe", 100),
            new Employee("John Doe 2", 95),
            new Employee("John Doe 3", 74),
            new Employee("John Doe 4", 123),
            new Employee("John Doe 5", 57),
            new Employee("John Doe 6", 100),
    };

    @Test
    public void test_Average() {
        // act
        Measurable largest = Solution.largest(workers);
        // verify
        Employee e = (Employee) largest;
        System.out.println("Largest salary: " + e.getName());
        assertEquals("John Doe 4", e.getName());
    }
}
