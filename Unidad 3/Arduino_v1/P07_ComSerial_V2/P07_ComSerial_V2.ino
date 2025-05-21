int led = 13;

void setup() {
  Serial.begin(9600);
}

byte var=0;

void loop() {
  // put your main code here, to run repeatedly:
  var += 1;
  Serial.println(var);
  delay(100);
}