
int ledPin = 13;
int cameraPin =  8;
int exposureTime = 10000; // in ms
int recoveryTime = 3000; // in ms

void setup() {                
  // initialize the digital pin as an output.
  pinMode(ledPin, OUTPUT);  
  pinMode(cameraPin, OUTPUT);
  
  Serial.begin(6900);
}


void loop() {
  
 while (Serial.available() == 0) {
 }
  if (Serial.read() == 83){
  digitalWrite(cameraPin, HIGH);   
  delay(exposureTime);              
  digitalWrite(cameraPin, LOW);    
  delay(recoveryTime);             
  }
}
