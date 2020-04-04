/**
 * 
 */
package hfdp.c03.Decorator;

/**
 * Base decorator class. Extend from Beverage as we want the
 * wrapper to be the same type as the beverage
 *
 */
public abstract class CondimentDecorator extends Beverage {
    public abstract String getDescription();
}
