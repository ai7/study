package hfdp.c04.factory.abstractfactory;

/**
 * This is the base pizza that all other pizzas inherit from, used by
 * factorymethod as well.
 */
public abstract class Pizza {

    String name;
    Dough dough;
    Sauce sauce;
    Veggies veggies[];
    Cheese cheese;
    Pepperoni pepperoni;
    Clams clam;
    
    abstract void prepare();  // collect ingredients from pizza
    
    public void bake() {
	System.out.println("Bake for 25 minutes at 350");
    }
    public void cut() {
	System.out.println("Cutting the pizza into diagonal slices");
    }
    public void box() {
	System.out.println("Place pizza in official PizzaStore box");
    }

    void setName(String name) {
	this.name = name;
    }
    String getName() {
	return name;
    }
    
    public String toString() {
	// code to print pizza here
	return "Not yet implemented";
    }
}
