// Provide an iterator - an object that yields the elements of the queue in
// turn - for the queue of the preceding class. Make Iterator a nested class
// with methods next() and hasNext(). Provide a method iterator() of the Queue
// class that yields a Queue.Iterator. Should Iterator be static or not?

// Note:
//   iterator should NOT be static because it needs access to the parent
//   queue!
//
//   as inner class have direct access to out class instance
//   variables, the iterator just need to keep track of an index and
//   access the outer class's element at that index.

// done with chapter2 exercise! 4/13/2019, 6:09pm.

package ch02.ex17;

public class Answer {

    public static void main(String[] args) {
        Queue myqueue = new Queue();
        myqueue.add("first").add("second").add("raymond").add("kaboon");
        Queue.Iterator it = myqueue.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }
        myqueue.remove();
        it = myqueue.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }

    }

}
