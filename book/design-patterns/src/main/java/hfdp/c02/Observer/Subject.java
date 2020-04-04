package hfdp.c02.Observer;

/**
 * Subject interface if we were to implement it ourselves
 */
public interface Subject {
    public void registerObserver(Observer o);
    public void removeObserver(Observer o);
    public void notifyObservers();
}
