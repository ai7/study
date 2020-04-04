package hfdp.c04.factory.factorymethod;

import hfdp.c04.factory.simplefactory.Pizza;

// small classes to simplify tree view
class NYStyleCheesePizza extends Pizza { 
    public NYStyleCheesePizza() {
	name = "NY Style Sauce and Cheese Pizza";
	dough = "Thin Crust Dough";
	sauce = "Marinara Sauce";
	toppings.add("Grated Reggiano Cheese");
    }
}
class NYStylePepperoniPizza extends Pizza { }
class NYStyleClamPizza extends Pizza { }
class NYStyleVeggiePizza extends Pizza { }

/**
 * A concrete client that implements abstract factory method
 * defined in parent class to create concrete pizza objects.
 */
public class NYPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
	// TODO Auto-generated method stub
	if (type.equals("cheese")) {
	    return new NYStyleCheesePizza();
	} else if (type.equals("pepperoni")) {
	    return new NYStylePepperoniPizza();
	} else if (type.equals("clam")) {
	    return new NYStyleClamPizza();
	} else if (type.equals("veggie")) {
	    return new NYStyleVeggiePizza();
	} else {
	    return null;
	}
    }

}
