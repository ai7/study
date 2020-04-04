package hfdp.c06.command;

class GarageDoor {
    public void up() {
	System.out.println("Garage door is Up");
    }
    public void down() {
	System.out.println("Garage door is Down");
    }
    public void stop() {
	System.out.println("Garage door is Stopped");
    }
    public void lightOn() {
	System.out.println("Garage door light is On");
    }
    public void lightOff() {
	System.out.println("Garage door light is Off");
    }
}

public class GarageDoorOpenCommand implements Command {

    GarageDoor garageDoor;
    
    public GarageDoorOpenCommand(GarageDoor garageDoor) {
	// TODO Auto-generated constructor stub
	this.garageDoor = garageDoor;
    }

    @Override
    public void execute() {
	// TODO Auto-generated method stub
	garageDoor.lightOn();
    }

}
