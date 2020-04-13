package ch03.ex10;

// note: join() not wait() to wait for thread to finish

public class Answer {
    public static void runTogether(Runnable... tasks) {
        for (Runnable r: tasks) {
            Thread t = new Thread(r);
            t.start();
        }
    }

    public static void runInOrder(Runnable... tasks) throws InterruptedException {
        for (Runnable r: tasks) {
            Thread t = new Thread(r);
            t.start();
            t.join();  // wait for task to finish
        }
    }
}
