                      Head First Design Pattern
                              Chapter 2
                           Observer Pattern

The observer pattern, a very popular and useful pattern involving a
subject and one or more observers (listeners). When the subject's
state changes, the listeners are updated automatically.

Implemented using Java build-in Observable/Observer support.

WeatherData is the subject, aka Observable object. It inherits from
Observable which is a Java Class. It calls setChanged() and
notifyObserver() method from parent class when appropriate.

CurrentConditionsDisplay is an Observer, implementing the Java
Observer interface. In the constructor it adds self as a listener to
the subject. It implements the update() method that the subject will
call when subject's data changes.

DisplayElement is an interface that all Display will implement, so we
have a consistent interface to all and future ones.

Subject/Observer are interfaces that we could implement IF we were to
not use Java's build-in Observable support.

6/1/2015


Java Notes
==========

@override
        hint for compiler so if you mistype the method name, the
        compiler can warn you that no such method exists.
32.5f
        float literal, not double
