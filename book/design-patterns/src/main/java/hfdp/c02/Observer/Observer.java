package hfdp.c02.Observer;

/**
 * Observer interface if we were to implement it ourselves
 */

public interface Observer {
    public void update(float temp, float humidity, float pressure);
}
