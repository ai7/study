/**
 * 
 */
package hfdp.c04.factory.simplefactory;

/**
 * PizzaStore using the simple factory
 */
public class PizzaStore {
    SimplePizzaFactory factory;
    
    // constructor that takes factory
    public PizzaStore(SimplePizzaFactory factory) {
	this.factory = factory;
    }

    // order specific type of pizza using stored factory
    public Pizza orderPizza(String type) {
	Pizza pizza;
	
	pizza = factory.createPizza(type);  // use factory
	
	pizza.prepare();
	pizza.bake();
	pizza.cut();
	pizza.box();
	
	return pizza;
    }
}
