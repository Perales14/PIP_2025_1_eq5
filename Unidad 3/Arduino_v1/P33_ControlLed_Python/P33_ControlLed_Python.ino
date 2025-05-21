int led = 6;
int valor; 
void setup() {
  pinMode(led, OUTPUT);
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}


void loop() {
  // put your main code here, to run repeatedly:
 if(Serial.available()>0){
  valor = Serial.readString().toInt();
  digitalWrite(led, valor);
 }
  delay(100);
}
