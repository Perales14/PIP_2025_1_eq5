int v;

void setup() {
  v = 0;  
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Valor: " + String(v));
  v += 1;
  delay(100);
}

