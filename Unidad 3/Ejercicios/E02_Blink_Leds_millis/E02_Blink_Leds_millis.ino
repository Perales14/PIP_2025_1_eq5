const int ledPin = 13;
unsigned long previousMillis = 0;   
const unsigned long interval = 500; 

bool ledState = false; 

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Cambiar el estado del LED
    ledState = !ledState;

    if (ledState) {
      digitalWrite(ledPin, HIGH);
    } else {
      digitalWrite(ledPin, LOW);
    }
  }
}
