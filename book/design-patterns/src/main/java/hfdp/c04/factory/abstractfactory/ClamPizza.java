package hfdp.c04.factory.abstractfactory;

public class ClamPizza extends Pizza {
    
    PizzaIngredientFactory ingredientFactory;
    
    public ClamPizza(PizzaIngredientFactory ingredientFactory) {
	this.ingredientFactory = ingredientFactory;
    }

    @Override
    void prepare() {
	// TODO Auto-generated method stub
	System.out.println("Preparing " + name);
	dough = ingredientFactory.createDough();
	sauce = ingredientFactory.createSauce();
	cheese = ingredientFactory.createCheese();
	clam = ingredientFactory.createClam();
    }
}
