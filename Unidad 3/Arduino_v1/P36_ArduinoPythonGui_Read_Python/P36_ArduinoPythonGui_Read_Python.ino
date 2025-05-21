int valor;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(A0);
  Serial.println("Valor "+String(valor));
  delay(100);
}
