package ch03.ex09;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class Greeter implements Runnable {

    private final int n;
    private final String target;

    @Override
    public void run() {
        for (int i = 0; i < n; i++) {
            System.out.printf("[%d] Hello, %s\n", i+1, target);
        }
    }
}
