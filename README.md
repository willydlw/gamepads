# gamepads
This repository provides examples of reading gamepad data in a Linux system. Examples are written in C and python.

## Linux Joystick Input Interfaces
Linux has two different joystick interfaces.
1. /dev/input/jsX maps to the joystick API interface
2. /dev/input/event* maps to the evdev interface.

## Logitech F310, Ubuntu 18.04
1. Testing the gamepad with the Joystick API interface
   -   The button on the back of the controller should be in the X position
   -   Plug the gamepad into a usb port and open up a terminal
   -   Type `lsusb` and you should see similar output: `Bus 001 Device 007: ID 046d:c21d Logitech, Inc. F310 Gamepad [XInput Mode]`
   If you do not see the above, then check the switch on the back is likely not in the X position. 
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

   -   Before running the program, you will need the device information. Type `ls /dev/input` for a listing of input devices.
   
   
      ```
      by-id    event0  event10  event12  event14  event16  event3  event5  event7  event9  mice    mouse1
      by-path  event1  event11  event13  event15  event2   event4  event6  event8  js0     mouse0
      ```
      The joystick devices are listed as jsX, where the X is a placehoder for a number. In the example output above, the device is js0. When running the jstest program, the path /dev/input/js0 is needed.
   -   Type either `jstest /dev/input/js0` or `jstest --normal /dev/input/js0`. The default mode is normal. You will see the joystick output on the screen. Move the thumbsticks and press the buttons to see the range of values.
      ```
      Driver version is 2.1.0.
      Joystick (Logitech Gamepad F310) has 8 axes (X, Y, Z, Rx, Ry, Rz, Hat0X, Hat0Y) and 11 buttons (BtnA, BtnB, BtnX, BtnY, BtnTL, BtnTR, BtnSelect, BtnStart, BtnMode, BtnThumbL, BtnThumbR).
      Testing ... (interrupt to exit)
      Axes:  0:     0  1:    -2  2:-32767  3:     0  4:    -2  5:-32767  6:     0  7:     0 
      Buttons:  0:off  1:off  2:off  3:off  4:off  5:off  6:off  7:off  8:off  9:off 10:off 
      ```

   -   If the program does not run, check the device permissions. Type `ls -l /dev/input/js0` 
   
   
2. Testing the gamepad with the evdev interface
   -   The button on the back of the controller should be in the D (direct input) position
   -   Plug the gamepad into a usb port and type `lsusb` in the terminal. You should see similar output: `Bus 001 Device 014: ID 046d:c216 Logitech, Inc. Dual Action Gamepad`
   -   Find the joystick event number. Type `ls -l /dev/input/by-id/` and look for an ouput similar to `lrwxrwxrwx 1 root root 10 May  9 17:39 usb-Logitech_Logitech_Dual_Action_BBECCB89-event-joystick -> ../event16'
   -   Type `evtest` and it will list input devices and their event numbers, similar to the output below.
   ```
   No device specified, trying to scan all of /dev/input/event*
   Not running as root, no devices may be available.
   Available devices:
   /dev/input/event16:	Logitech Logitech Dual Action
   Select the device event number [0-16]: 
   ```
   Enter the event number, 16 in this example and press the enter key. You will then see a listing of event codes and values. Press the gamepad buttons and thumbsticks to see the full range.
   
 
 
 A thorough and much better explanation of joysticks in Linux is found [here](https://wiki.archlinux.org/index.php/Gamepad).
