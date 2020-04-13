package ch02.ex09;

public class Car {
    private final double mpg;  // fuel efficiency, miles/gallon
    private final double fuelCapacity;  // fuel tank capacity
    private double fuel;  // current amount of fuels
    private double distance;  // total distance traveled

    public Car(double mpg, double fuelCapacity) {
        this.mpg = mpg;
        this.fuelCapacity = fuelCapacity;
    }

    public double getFuel() {
        return fuel;
    }

    public double getDistance() {
        return distance;
    }

    public Car addGas(double gallons) {
        if (gallons <= 0) {
            throw new IllegalArgumentException("gallons must be positive: " + gallons);
        } else if (fuel < fuelCapacity) {
            fuel += gallons;
            if (fuel > fuelCapacity) {
                fuel = fuelCapacity;
            }
        }   // else: fuel tank is full, no-op
        return this;
    }

    public Car travelMiles(double miles) {
        if (miles <= 0) {
            throw new IllegalArgumentException("miles must be positive: " + miles);
        }
        if (fuel <= 0) {  // no fuel, no-op
            return this;
        }
        double maxRange = fuel * mpg;
        if (maxRange <= miles) {  // cap at maxRange
            distance += maxRange;
            fuel = 0;
        } else {
            distance += miles;
            fuel -= miles / mpg;  // consume fuel
        }
        return this;
    }

    @Override
    public String toString() {
        return "Car{" +
                "fuel=" + fuel +
                ", distance=" + distance +
                '}';
    }
}
