# gamepads
## Logitech F310, Ubuntu 18.04
1. Setting up the joystick
   -   The button on the back of the controller should be in the X position
   -   Plug the gamepad into a usb port and open up a terminal
   -   Type `lsusb` and you should see similar output: `Bus 001 Device 007: ID 046d:c21d Logitech, Inc. F310 Gamepad [XInput Mode]`
   If you do not see the above, then check the switch on the back is likely not in the X position. If you see `Bus 001 Device 008: ID 046d:c216 Logitech, Inc. Dual Action Gamepad`, then the switch is in the D (direct input) position.
   -   With the switch in the X position, you can use the jstest program to verify the controller works. To install jstest, type `sudo apt install joystick`. Now type `jstest` and press the enter key. The output provides the following choices:
   ```
   Usage: jstest [<mode>] <device>
   Modes:
   --normal           One-line mode showing immediate status
   --old              Same as --normal, using 0.x interface
   --event            Prints events as they come in
   --nonblock         Same as --event, in nonblocking mode
   --select           Same as --event, using select() call
```

   
