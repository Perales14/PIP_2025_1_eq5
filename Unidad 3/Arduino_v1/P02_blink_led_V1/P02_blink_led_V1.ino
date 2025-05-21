int led = 9;
void setup() {
  
}

void loop() {
  // put your main code here, to run repeatedly:
  //delay(ms)
  digitalWrite(led,1);
  delay(500);
  digitalWrite(led,0);
  delay(500);
}