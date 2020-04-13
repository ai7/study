package ch02.ex16;

import java.util.ArrayList;
import java.util.List;

public class Queue {
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

