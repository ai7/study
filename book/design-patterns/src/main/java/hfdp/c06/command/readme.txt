                      Head First Design Pattern
                              Chapter 6
                           Command Pattern

Command is a simple interface

LightOnCommand is a concrete class implements Command
- contains a receiver (Light object) that is set in constructor.
- execute() simply is light.on()

SimpleRemoteControl is an object that calls setCommand() to assign
command obj to buttons, and when button is pressed calls slot.execute()

RemoteControlTest is just a test driver.


 