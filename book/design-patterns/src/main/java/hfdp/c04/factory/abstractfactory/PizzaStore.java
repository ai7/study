package hfdp.c04.factory.abstractfactory;

/**
 * A framework for pizzastore using the factory method
 */
public abstract class PizzaStore {
    
    public Pizza orderPizza(String type) {
	Pizza pizza;
	
	pizza = createPizza(type);
	
	pizza.prepare();
	pizza.bake();
	pizza.cut();
	pizza.box();
	
	return pizza;
    }

    // method concrete pizzastore override
    abstract Pizza createPizza(String type);
}
