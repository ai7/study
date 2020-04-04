package hfdp.c06.command;

class Light {
    public void on() {
	System.out.println("Light is On");
    }
}

public class LightOnCommand implements Command {

    Light light;  // this is the receiver that will do work
    
    public LightOnCommand(Light light) {
	// TODO Auto-generated constructor stub
	this.light = light; 
    }

    @Override
    public void execute() {
	// TODO Auto-generated method stub
	light.on();
    }

}
