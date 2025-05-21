int dEncendido = 1000;
int dApagado = 500;
int led = 13;
void setup() {
  pinMode(led,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led,1);
  delay(dEncendido);
  digitalWrite(led,0);
    delay(dApagado);
}