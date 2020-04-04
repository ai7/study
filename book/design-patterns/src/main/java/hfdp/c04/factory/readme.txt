                      Head First Design Pattern
                              Chapter 4
                           Factory Pattern

The infamous factory pattern

==============
Simple Factory
==============

Not really a pattern, more of a programming idiom.

A simple factory class with a method that creates various kind of
pizza.

Client that uses this factory compose a factory as member variable,
and calls createPizza() method on that memory variable whenever a
pizza is needed.

==============
Factory Method
==============

This pattern defines an interface for creating an object, but lets
subclasses decide which class to instantiate. Factory Method lets a
class defer instantiation to subclasses.

PizzaStore is a client with an abstract method createPizza() that
concrete store such as NYPizzaStore overrides.

NYPizzaStore create specific type of NY style pizza.

================
Abstract Factory
================

This pattern provides an interface for creating families of related or
dependent objects without specifying their concrete classes.

PizzaIngredientFactory is an interface that defines methods to create
various objects. This is the base factory class.

NYPizzaIngredientFactory is an concrete class that implements
PizzaIngredientFactory interface and implements methods to create
objects that have NY flavor.

ChicagoPizzaIngredientFactory is defined similarily.

PizzaStore is a base Store class that operates on a generic Pizza
object. it has abstract method createPizza() that child class will
implement.

NYPizzaStore is a concrete Pizza, and it implements the createPizza()
method by using a specific/concrete ingredient factory. All other
behaviors are implemented by the base Store class. So the purpose of
this class is to simply override createPizza() with NYstyle factory.


