package hfdp.c02.Observer;

import java.util.Observable;
import java.util.Observer;

/**
 * Exercise, similar to CurrentConditionsDisplay.java
 */

public class ForecastDisplay implements Observer, DisplayElement {

    private float currentPressure = 29.92f;  // float, not double
    private float lastPressure;
    
    public ForecastDisplay(Observable observable) {
	observable.addObserver(this);
    }
    
    @Override
    public void update(Observable obs, Object arg1) {
	// TODO Auto-generated method stub
	if (obs instanceof WeatherData) {
	    WeatherData weatherData = (WeatherData) obs;
	    lastPressure = currentPressure;
	    currentPressure = weatherData.getPressure();
	    display();
	}
    }
    
    @Override
    public void display() {
	if (currentPressure == lastPressure) {
	    System.out.println("Forecast: More of the same");
	} else if (currentPressure > lastPressure) {
	    System.out.println("Forecast: Improving weather on the way!");
	} else {
	    System.out.println("Forecast: Watch out for cooler, rainy weather");
	}
    }
}
