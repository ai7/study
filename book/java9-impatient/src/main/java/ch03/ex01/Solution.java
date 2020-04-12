package ch03.ex01;

public class Solution
{
    // compute the average of a list of measurable objects
    public static double average(Measurable[] objects) {
        double sum = 0;
        for (final Measurable object : objects) {
            sum += object.getMeasure();
        }
        return sum / objects.length;
    }
}
