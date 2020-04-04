package hfdp.c04.factory.factorymethod;

import hfdp.c04.factory.simplefactory.Pizza;

// class to simplify tree
class CaliforniaStyleCheesePizza extends Pizza { }
class CaliforniaStylePepperoniPizza extends Pizza { }
class CaliforniaStyleClamPizza extends Pizza { }
class CaliforniaStyleVeggiePizza extends Pizza { }

public class CaliforniaPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
	// TODO Auto-generated method stub
	if (type.equals("cheese")) {
	    return new CaliforniaStyleCheesePizza();
	} else if (type.equals("pepperoni")) {
	    return new CaliforniaStylePepperoniPizza();
	} else if (type.equals("clam")) {
	    return new CaliforniaStyleClamPizza();
	} else if (type.equals("veggie")) {
	    return new CaliforniaStyleVeggiePizza();
	} else {
	    return null;
	}
    }

}
