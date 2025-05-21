int valor;
int led = 13;
void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(A0);
  Serial.println("1Valor "+String(valor));

  if(Serial.available()>0){
   int v = Serial.readString().toInt();
   digitalWrite(led,v);
   Serial.println("9999");
  //  analogWrite(led,v);
  }
  delay(100);
}