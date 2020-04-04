                      Head First Design Pattern
                              Chapter 1
                           Strategy Pattern

This chapter demonstrates alternative to inheritance for extending and
reusing existing code.

Duck is the parent class, containing interfaces to fly/quack behavior.
It uses delegation function to perform fly/quack on the interfaces
implemented by various fly/quack classes.

Actual duck are implemented by classes inherited from Duck.

This achieves good reuse, provides very flexible fly/quack behavior
for various new ducks without code changes.

5/30/2015
