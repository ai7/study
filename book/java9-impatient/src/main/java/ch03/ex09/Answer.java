package ch03.ex09;

public class Answer {
    public static void runGreeter(int n) {
        // create 2 threads with distinct greeter
        Thread x = new Thread(new Greeter(n, "Greeter A"));
        Thread y = new Thread(new Greeter(n, "Greeter B"));
        // start threads
        x.start();
        y.start();
    }
}
