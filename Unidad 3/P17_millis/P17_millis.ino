long m;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  m = millis();
  int nm = m/1000;
  Serial.println(String(nm)+" "+String(m));
  delay(1000);
}
