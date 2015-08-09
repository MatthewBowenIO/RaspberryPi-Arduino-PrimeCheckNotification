import serial
import threading

'''
Run 'ls /dev/tty*' without the Arduino plugged into your pi, then run it again with it plugged in.
You should see a new /dev/tty device. Replace '/dev/ttyACM0' with that value.
'''
ser = serial.Serial('/dev/ttyACM0', 9600)

# Very simple prime check. Returns bool value for true or false.
def isPrime(x):
	return all(x % i for i in xrange(2, x))

'''
We start main in a background thread so we can listen for 'exit' terminal input from the user 
input to stop the script and send the 'stop' command to the Arduino.
'''
def main():
    ser.write('0') # We listen for 0 to start the lights on the Arduino.
	ittr = 0
	while True:
		ittr += 1
		if isPrime(ittr):
            ser.write('2') # We listen for 2 to tell the Arduino to notify of a prime.
			print(str(ittr))

thread = threading.Thread(target=main)
thread.daemon = True
thread.start()

# Listen for user input of 'exit'. Could be cleaner.
while True:
	exitSignal = raw_input('')
	if exitSignal == 'exit':
        ser.write('1') # We listen for 1 to deactivate the lights on the Arduino.
		raise SystemExit(0)

		
