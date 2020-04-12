// cast is needed to convert from Measurable to Employee class.
// good use of comparingDouble and field extractor.

package ch03.ex02;

import java.util.Arrays;
import java.util.Comparator;

public class Solution
{
    // compute the average of a list of measurable objects
    public static Measurable largest(Measurable[] objects) {
        return Arrays.stream(objects)
                .max(Comparator.comparingDouble(Measurable::getMeasure))
                .orElse(null);
    }
}
