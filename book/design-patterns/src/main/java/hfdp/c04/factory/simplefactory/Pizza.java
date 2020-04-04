/**
 * 
 */
package hfdp.c04.factory.simplefactory;

import java.util.ArrayList;

/**
 * This is the base pizza that all other pizzas inherit from, used by
 * factorymethod as well.
 */
public abstract class Pizza {

    // adding public so we can override them in different packages here
    public String name;
    public String dough;
    public String sauce;
    public ArrayList<String> toppings = new ArrayList<String>();
    
    public void prepare() {
	System.out.println("Preparing " + name);
	System.out.println("Tossing dough ...");
	System.out.println("Adding sauce ...");
	System.out.println("Adding toppings:");
	for (int i = 0; i < toppings.size(); i++) {
	    System.out.println("   " + toppings.get(i));
	}
    }
    
    public void bake() {
	System.out.println("Bake for 25 minutes at 350");
    }
    public void cut() {
	System.out.println("Cutting the pizza into diagonal slices");
    }
    public void box() {
	System.out.println("Place pizza in official PizzaStore box");
    }

    public String getName() {
	return name;
    }
}
