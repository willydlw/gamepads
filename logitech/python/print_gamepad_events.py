''' Print gamepad events if Logitech F710 or F310 is connected'''
import evdev 

# read list of connected input event devices
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

found = False 

# loop throught the device list until Logitech gamepad is found
# or all elements in list have been read
for device in devices:
    
	print(device.fn, device.name, device.phys)

	if device.name == 'Logitech Gamepad F710' or device.name == 'Logitech Gamepad F310':
		gamePad = evdev.InputDevice(device.fn)
		found = True 
		break

if found:
	print("\nPrinting gamepad events\n")
	for event in gamePad.read_loop():
		print(event)
else:
	print("Device not found")
