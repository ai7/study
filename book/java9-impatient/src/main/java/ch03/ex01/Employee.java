package ch03.ex01;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class Employee implements Measurable {

    private final double salary;

    @Override
    public double getMeasure()
    {
        return salary;
    }
}
