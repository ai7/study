// Section 1.5.3, "String Comparison" (page 25) has an example of
// two strings s and t so that s.equals(t) but s != t. Come up with a
// different example that don't use substring).

// Note: easy, just find another string that have same content but
//             different object reference, such as when
//             .toLowerCase() is called on a string.

package ch01.ex09;

public class Exercise09 {
    public static void main(String[] args) {
        // string operation generates a new string, which have
        // content same as another string, but different address.
        String s = "this";
        String t = "THIS".toLowerCase();
        assert(s.equals(t) && s != t);
    }
}
