package hfdp.c02.Observer;

import java.util.Observable;

/**
 * This is the Subject in Observer pattern, implemented using Java
 * Observable.
 *
 * Observers are added to subject, and when data changes Subject
 * notifies listed observers.
 */

public class WeatherData extends Observable {
    
    private float temperature;
    private float humidity;
    private float pressure;
    
    public WeatherData() { }
    
    public void measurementsChanged() {
	setChanged();
	notifyObservers();
    }
    
    public void setMeasurements(float temperature, float humidity, float pressure) {
	this.temperature = temperature;
	this.humidity = humidity;
	this.pressure = pressure;
	measurementsChanged();
    }

    public float getTemperature() {
	return temperature;
    }
    public float getHumidity() {
	return humidity;
    }
    public float getPressure() {
	return pressure;
    }
    
}
