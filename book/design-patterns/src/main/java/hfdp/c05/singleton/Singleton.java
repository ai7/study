package hfdp.c05.singleton;

public class Singleton {

    private static Singleton uniqueInstance;
    
    private Singleton() { }  // disallow new
    
    // simple implementation, not thread safe
    public static Singleton getInstance1() {
	if (uniqueInstance == null) {
	    uniqueInstance = new Singleton();
	}
	return uniqueInstance;
    }

    // synchronized method, slower
    public static synchronized Singleton getInstance2() {
	if (uniqueInstance == null) {
	    uniqueInstance = new Singleton();
	}
	return uniqueInstance;
    }

    // double-checked locking
    public static Singleton getInstance3() {
	if (uniqueInstance == null) {
	    synchronized(Singleton.class) {
		if (uniqueInstance == null) {
		    uniqueInstance = new Singleton();
		}
	    }
	}
	return uniqueInstance;
    }
    
}
