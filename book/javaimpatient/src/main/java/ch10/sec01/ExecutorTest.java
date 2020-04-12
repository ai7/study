package ch10.sec01;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorTest {

    public static void main(String[] args) {
        Runnable hellos = () -> {
            for (int i = 0; i < 1000; i++) {
                System.out.println("Hello " + (i + 1));
            }
        };
        Runnable goodbyes = () -> {
            for (int i = 0; i < 1000; i++) {
                System.out.println("Goodbye " + (i + 1));
            }
        };

        ExecutorService executor = Executors.newCachedThreadPool();
        executor.execute(hellos);
        executor.execute(goodbyes);
    }

}
