/**
 * 
 */
package hfdp.c03.Decorator;

/**
 * This is the base Beverage class that actual beverage
 * and condiments inherit from
 */
public abstract class Beverage {
    String description = "Unknown Beverage";
    
    public String getDescription() {
	return description;
    }
    
    public abstract double cost();
}
