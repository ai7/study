// Implement a class Queue, an unbounded queue of strings. Provide
// methods add, adding at the tail, and remove, removing at the head
// of the queue. Store elements as a linked list of nodes. Make Node a
// nested class. Should it be static or not?

// Note:
//   it should be static, because no reason to go from Node back to
//   the queue object.
//
//   return this in add() and remove(), chaining is fun!

package ch02.ex16;

import java.util.ArrayList;
import java.util.List;

public class Exercise16 {

    public static class Queue {
        List<Node> elements = new ArrayList<>();

        public Queue add(String s) {
            elements.add(new Node(s));
            return this;
        }

        public Queue remove() {
            if (elements.size() > 0) {
                elements.remove(0);
            }
            return this;
        }

        public static class Node {
            String value;

            public Node(String value) {
                this.value = value;
            }
        }
    }

    public static void main(String[] args) {
        Queue myqueue = new Queue();
        myqueue.add("first").add("second").remove();
        // only second remaining.
    }
}
