const int potPinUno = 34;
const int potPinDos = 33;
int EMGValue1 = 0;
int EMGValue2 = 0;

// The setup routine runs once when you press reset:
void setup() {
  // Initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
}

// The loop routine runs over and over again forever:
void loop() {

  EMGValue1 = analogRead(potPinUno);
  EMGValue2 = analogRead(potPinDos);
  // Write the signal points, followed by the terminator "Carriage Return" and "Linefeed".
  //Serial.print("0");
  Serial.print(EMGValue1);
  Serial.print(" ");
  //Serial.print("1");
  Serial.println(EMGValue2);
  //Serial.write(13);
  //Serial.write(10);
  //delay(50);
}


/*// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 


// variable for storing the potentiometer value
int potValue = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  // Reading potentiometer value
  potValue = analogRead(potPin);
  Serial.println(potValue);
  delay(50);
}*/
