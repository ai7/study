package hfdp.c06.command;

/**
 * simple client that have setCommand() and action() method
 */
public class SimpleRemoteControl {

    Command slot;

    public SimpleRemoteControl() { 
	// TODO Auto-generated constructor stub
    }

    public void setCommand(Command command) {
	this.slot = command;
    }
    
    public void buttonWasPressed() {
	slot.execute();
    }
}
