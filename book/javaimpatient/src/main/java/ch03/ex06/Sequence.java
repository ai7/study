package ch03.ex06;

public interface Sequence<T> {
    default boolean hasNext() { return true; }
    T next();
}
