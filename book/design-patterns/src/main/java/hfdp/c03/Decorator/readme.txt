                      Head First Design Pattern
                              Chapter 3
                          Decorator Pattern

A wrapper pattern. Very neat!

========
Beverage
========

Beverage is the abstract base class.

DarkRoast/Decaf/Espresso/HouseBlend is concrete coffee class derived
from beverage.

CondimentDecorator is the base class for all decorators, derived from
Beverage as we want decorated class to be the same type.

Mocha/Soy/Whip are actual concrete decorators. These have a member
variable holding a pointer to an actual beverage (hence wrapping), and
implements certain methods that are delegated to beverage plus custom
behavior.

This is relatively straightforward, but interesting remifications. One
can decorate classes dynamically at runtime, compare to inheritence
which is a behavior obtained only at compile time.

=======
Java IO
=======

Uses decorator for many classes.

LowerCaseInputStream is our own decorator class that extends
FilterInputStream and lower cases chars.

InputTest contains main that illustrates how this is used. Neat
example of creating all these wrapped classes in one shot.
