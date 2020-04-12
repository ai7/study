package ch03.ex04;

// note: anonymous inner class that implements the interface,
//   capturing the `values` vararg input parameter, neat!

import java.util.NoSuchElementException;

public interface IntSequence {
    boolean hasNext();
    int next();

    static IntSequence of(int... values) {
        // returns anonymous inner class, yeah!
        return new IntSequence() {
            private int i = 0;  // current index

            @Override
            public boolean hasNext() {
                return i < values.length;
            }

            @Override
            public int next() {
                if (i < values.length) {
                    return values[i++];
                } else {
                    throw new NoSuchElementException("No more elements");
                }
            }
        };
    }
}
