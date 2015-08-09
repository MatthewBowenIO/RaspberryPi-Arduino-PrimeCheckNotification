bool isCheckingPrimes = false;
char serialRead = '|';

void setup() {
  Serial.begin(9600);
  Serial.println("Starting...");
  
  for(int i = 0; i <= 9; i++) {
    pinMode(i, OUTPUT);
  }

  pinMode(12, OUTPUT);

  flashLights();
}

void loop() {
  if(Serial.available()) {
    serialRead = Serial.read();
    if(serialRead == '0') {
      isCheckingPrimes = true; //Notification from Raspberry Pi that it is starting to check for primes.
    } else if (serialRead == '1') {
      isCheckingPrimes = false; //Notification from Raspberry Pi that it is stopping it's prime checks.
      shutoffAllLights();
    } else if (serialRead == '2') {
      flashLights(); //Notification from Raspberry Pi that it has found a prime.  
    }
  }

  if(isCheckingPrimes) {
    shutoffAllLights();
  
    digitalWrite(random(0, 9), HIGH);
    delay(50); 
    }
}

void flashLights() {
  turnOnAllLights();

  notifyOfPrime();
  delay(25);

  shutoffAllLights();
}

void turnOnAllLights() {
  for(int f = 0; f <= 9; f++) {
    digitalWrite(f, HIGH);
  }
}

void notifyOfPrime() {
  int pitch = map(2048, 2048, 0, 50, 4000);
  tone(12, pitch, 20);  
}

void shutoffAllLights() {
  for(int i = 0; i <= 9; i++) {
    digitalWrite(i, LOW);
  }
}
