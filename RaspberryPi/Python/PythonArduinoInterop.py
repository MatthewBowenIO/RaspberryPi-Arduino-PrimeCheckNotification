import serial
import threading

'''
Run 'ls /dev/tty*' without the Arduino plugged into your pi, then run it again with it plugged in.
You should see a new /dev/tty device. Replace '/dev/ttyACM0' with that value.
'''
ser = serial.Serial('/dev/ttyACM0', 9600)

def isPrime(x):
    # Fermat test
    if (x > 1):
        for time in range(3):
                randomNumber = random.randint(2, x)-1
                if ( pow(randomNumber, x-1, x) != 1 ):
                    return False
                return True
        else:
            return False

def isPrimeTestTwo(x):
    # Miller Rabin test
    if x == 2:
        return True
        elif x == 1 or x % 2 == 0:
            return False
        
        oddPartOfNumber = x - 1
        timesTwoDividNumber = 0
        
        while oddPartOfNumber % 2 == 0:
            oddPartOfNumber = oddPartOfNumber / 2
                timesTwoDividNumber = timesTwoDividNumber + 1
    
        for time in range(3):
            while True:
                randomNumber = random.randint(2, x)-1
                    if randomNumber != 0 and randomNumber != 1:
                        break
            
                randomNumberWithPower = pow(randomNumber, oddPartOfNumber, x)
                
                if (randomNumberWithPower != 1) and (randomNumberWithPower != x - 1):
                    iterationNumber = 1
                        
                        while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != x - 1):
                            randomNumberWithPower = pow(randomNumberWithPower, 2, x)
                                iterationNumber = iterationNumber + 1
                        
                        if (randomNumberWithPower != (x - 1)):
                            return False
        return True

'''
We start main in a background thread so we can listen for 'exit' terminal input from the user 
input to stop the script and send the 'stop' command to the Arduino.
'''
def main():
    ser.write('0') # We listen for 0 to start the lights on the Arduino.
	ittr = 0
	while True:
		ittr += 1
		if isPrime(ittr) and isPrimeTestTwo(ittr):
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

		
