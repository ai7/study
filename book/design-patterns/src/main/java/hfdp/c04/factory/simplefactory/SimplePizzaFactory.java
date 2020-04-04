package hfdp.c04.factory.simplefactory;

//class to simplify tree
class CheesePizza extends Pizza { }
class PepperoniPizza extends Pizza { }
class ClamPizza extends Pizza { }
class VeggiePizza extends Pizza { }

/**
 * Simple class with method to create various pizza
 */
public class SimplePizzaFactory {
    
    // paramitized method 
    public Pizza createPizza(String type) {
	Pizza pizza = null;
	
	if (type.equals("cheese")) {
	    pizza = new CheesePizza();
	} else if (type.equals("pepperoni")) {
	    pizza = new PepperoniPizza();
	} else if (type.equals("clam")) {
	    pizza = new ClamPizza();
	} else if (type.equals("veggie")) {
	    pizza = new VeggiePizza();
	}
	return pizza;
    }

}
