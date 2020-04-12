package ch03.ex02;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class Employee implements Measurable {

    @Getter
    private final String name;

    private final double salary;

    @Override
    public double getMeasure()
    {
        return salary;
    }
}
