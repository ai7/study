package ch02.ex17;

import java.util.LinkedList;
import java.util.List;

public class Queue {
    List<Node> elements = new LinkedList<>();

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

    public Iterator iterator() {
        return new Iterator();
    }

    public static class Node {
        String value;

        public Node(String value) {
            this.value = value;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "value='" + value + '\'' +
                    '}';
        }
    }

    // implementing an iterator, wow!!
    class Iterator {
        private int i = 0;

        public Node next() {
            return elements.get(i++);
        }
        public boolean hasNext() {
            return i < elements.size();
        }
    }
}
