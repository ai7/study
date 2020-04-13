// Why can't you implement a Java method that swaps the content of two
// int variables? Instead, write a method that swaps the content of
// two IntHolder objects. (Look up this rather obscure class in the
// API documentation.) Can you swap the contents of two Integer
// objects?

// Note:
//   can't swap int parameter because java params are passed by value,
//   so inside the function we are changing the copy of the reference,
//   the caller's variable reference is unchanged.
//
//   IntHolder is simply a wrapper class with a public .value instance
//   variable, so can use it to swap.
//
//   Cannot swap 2 Integer, as Integer is immutable.

package ch02.ex04;

// import org.omg.CORBA.IntHolder;  // removed in JDK11

public class Exercise04 {

    static class IntHolder {
        int value;  // public, no getter/setter
        IntHolder() {}
        IntHolder(int initial) {
            value = initial;
        }
    }

    public static void main(String[] args) {
        IntHolder a = new IntHolder(12);
        IntHolder b = new IntHolder(32);
        swap(a, b);
        System.out.println(a.value + ", " + b.value);
    }

    // swap the content of two int holder objects.
    // notice that .value is public, easy to use
    static void swap(IntHolder x, IntHolder y) {
        int t = x.value;
        x.value = y.value;
        y.value = t;
    }
}
