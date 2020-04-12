package ch03.ex05;

// note: supply a lambda that implements an interface utializing
//   interface's default method, so only one method to implement, neat!

public interface IntSequence {
    default boolean hasNext() { return true; }
    int next();

    static IntSequence constant(int v) {
        return () -> v;  // so simple
    }
}
