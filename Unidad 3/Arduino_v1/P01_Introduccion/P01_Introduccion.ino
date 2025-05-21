int led = 13;
void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  // INPUT --> sensores
  //OUTPUT --> Actuadores
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, 1); //1, true, High
}