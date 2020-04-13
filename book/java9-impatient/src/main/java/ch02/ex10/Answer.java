// In the RandomNumbers class, provide two static methods
// randomElement that get a random element from an array or array list
// of integers. (Return zero if the array or array list is empty). Why
// coulnd't you make these methods into instance methods of int[] or
// ArrayList<Integer>?

// Note:
//   use the already defined nextInt() to return an index between
//   0 to A.length - 1.

package ch02.ex10;

public class Answer {

    public static void main(String[] args) {
        int[] A = {0, 1};
        for (int i = 0; i < 10; i++) {
            System.out.println(RandomNumbers.randomElement(A));
        }
    }
}
