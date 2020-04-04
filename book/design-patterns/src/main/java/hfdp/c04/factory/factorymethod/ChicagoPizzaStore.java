package hfdp.c04.factory.factorymethod;

import hfdp.c04.factory.simplefactory.Pizza;

// class to simplify tree
class ChicagoStyleCheesePizza extends Pizza { 
    public ChicagoStyleCheesePizza() {
	name = "Chicago Style Deep Dish Cheese Pizza";
	dough = "Extra Thick Crust Dough";
	sauce = "Plum Tomato Sauce";
	toppings.add("Shredded Mozzarella Cheese");
    }
    @Override
    public void cut() {
	System.out.println("Cutting the pizza into square slices");
    }
}
class ChicagoStylePepperoniPizza extends Pizza { }
class ChicagoStyleClamPizza extends Pizza { }
class ChicagoStyleVeggiePizza extends Pizza { }

public class ChicagoPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
	// TODO Auto-generated method stub
	if (type.equals("cheese")) {
	    return new ChicagoStyleCheesePizza();
	} else if (type.equals("pepperoni")) {
	    return new ChicagoStylePepperoniPizza();
	} else if (type.equals("clam")) {
	    return new ChicagoStyleClamPizza();
	} else if (type.equals("veggie")) {
	    return new ChicagoStyleVeggiePizza();
	} else {
	    return null;
	}
    }

}
