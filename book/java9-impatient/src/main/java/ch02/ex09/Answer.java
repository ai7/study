// Implement a class Car that models a car traveling along the x-axis,
// consuming gas as it moves. Provide methods to drive by a given
// number of miles, to add a given number of gallons to the gas tank,
// and to get the current distance from the origin and fuel level.
// Specify the fuel efficiency (in miles/gallon) in the constructor.
// Should this be an immutable class? Why or why not?

// Note:
//   should not be immutable. gallons in tank is a state that should
//   change as the car is moving.
//
//   only tricky part is cap fuel capacity during add fuel, and cap
//   distance based on available fuel at travel.

package ch02.ex09;

public class Answer {

    public static class Car {
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

    public static void main(String[] args) {
        Car mycar = new Car(20, 21.7);
        mycar.addGas(10).travelMiles(100).addGas(10).travelMiles(300);
        System.out.println(mycar);
    }
}
