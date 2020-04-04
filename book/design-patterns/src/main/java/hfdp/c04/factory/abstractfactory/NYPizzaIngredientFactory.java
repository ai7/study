package hfdp.c04.factory.abstractfactory;

// simple concrete classes
class ThinCrustDough extends Dough {}
class MarinaraSauce extends Sauce {}
class ReggianoCheese extends Cheese {}
class SlicedPepperoni extends Pepperoni {}
class FreshClams extends Clams {}

class Garlic extends Veggies {}
class Onion extends Veggies {}
class Mushroom extends Veggies {}
class RedPepper extends Veggies {}

public class NYPizzaIngredientFactory implements PizzaIngredientFactory {

    @Override
    public Dough createDough() {
	// TODO Auto-generated method stub
	return new ThinCrustDough();
    }

    @Override
    public Sauce createSauce() {
	// TODO Auto-generated method stub
	return new MarinaraSauce();
    }

    @Override
    public Cheese createCheese() {
	// TODO Auto-generated method stub
	return new ReggianoCheese();
    }

    @Override
    public Veggies[] createVeggies() {
	// TODO Auto-generated method stub
	Veggies veggies[] = { new Garlic(), new Onion(), new Mushroom(), new RedPepper() }; 
	return veggies;
    }

    @Override
    public Pepperoni createPepperoni() {
	// TODO Auto-generated method stub
	return new SlicedPepperoni();
    }

    @Override
    public Clams createClam() {
	// TODO Auto-generated method stub
	return new FreshClams();
    }

}
