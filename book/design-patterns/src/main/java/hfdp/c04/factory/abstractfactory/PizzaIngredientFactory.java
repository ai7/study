package hfdp.c04.factory.abstractfactory;

class Dough {}
class Sauce {}
class Cheese {}
class Veggies {}
class Pepperoni {}
class Clams {}

public interface PizzaIngredientFactory {
    public Dough createDough();
    public Sauce createSauce();
    public Cheese createCheese();
    public Veggies[] createVeggies();
    public Pepperoni createPepperoni();
    public Clams createClam();
}
