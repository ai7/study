package hfdp.c02.Observer;

import java.util.Observable;
import java.util.Observer;

/**
 * This is an Observer in the Observer pattern, implemented to the
 * java Observer interface.
 */

public class CurrentConditionsDisplay implements Observer, DisplayElement {

    private Observable observable;
    private float temperature;
    private float humidity;
    
    public CurrentConditionsDisplay(Observable observable) {
	this.observable = observable;
	observable.addObserver(this);
    }
    
    @Override
    public void update(Observable obs, Object arg1) {
	// TODO Auto-generated method stub
	if (obs instanceof WeatherData) {
	    WeatherData weatherData = (WeatherData) obs;
	    this.temperature = weatherData.getTemperature();
	    this.humidity = weatherData.getHumidity();
	    display();
	}
    }
    
    @Override
    public void display() {
	System.out.println("Current conditions: " + temperature
		+ "F degrees and " + humidity + "% humidity");
    }
}
