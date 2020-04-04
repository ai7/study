package hfdp.c02.Observer;

/**
 * Test code with main function
 */

public class WeatherStation {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	WeatherData weatherData = new WeatherData();
	
	// constructor registers self with subject weatherData
	CurrentConditionsDisplay cDisp = new CurrentConditionsDisplay(weatherData);

	// additional display here
	// StatisticsDisplay sDisp = new StatisticsDisplay(weatherData);
	ForecastDisplay fDisp = new ForecastDisplay(weatherData);
	
	weatherData.setMeasurements(80, 65,  30.4f);
	weatherData.setMeasurements(82, 70,  29.2f);
	weatherData.setMeasurements(78, 90,  29.2f);
    }

}
