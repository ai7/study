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

    public static void main(String[] args) {
        Car mycar = new Car(20, 21.7);
        mycar.addGas(10).travelMiles(100).addGas(10).travelMiles(300);
        System.out.println(mycar);
    }
}
