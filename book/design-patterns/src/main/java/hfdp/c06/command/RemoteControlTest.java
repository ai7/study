package hfdp.c06.command;

public class RemoteControlTest {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	SimpleRemoteControl remote = new SimpleRemoteControl();
	
	Light light = new Light();
	LightOnCommand lightOn = new LightOnCommand(light);
	
	GarageDoor garageDoor = new GarageDoor();
	GarageDoorOpenCommand garageOpens = new GarageDoorOpenCommand(garageDoor);
	
	remote.setCommand(lightOn);
	remote.buttonWasPressed();
	
	remote.setCommand(garageOpens);
	remote.buttonWasPressed();
    }

}
