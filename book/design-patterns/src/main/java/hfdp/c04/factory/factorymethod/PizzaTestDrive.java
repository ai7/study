package hfdp.c04.factory.factorymethod;

import hfdp.c04.factory.simplefactory.Pizza;

/**
 * Tester class
 */
public class PizzaTestDrive {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	PizzaStore nyStore = new NYPizzaStore();
	PizzaStore chicagoStore = new ChicagoPizzaStore();
	
	Pizza pizza = nyStore.orderPizza("cheese");
	System.out.println("Ethan ordered a " + pizza.getName() + "\n");

	pizza = chicagoStore.orderPizza("cheese");
	System.out.println("Ethan ordered a " + pizza.getName() + "\n");
    }

}
