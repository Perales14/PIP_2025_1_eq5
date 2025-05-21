int valores[3]={0,0,0};
int sensores[]= {A0,A1,A2};
int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);
}
String cadena;
void loop() {
  // put your main code here, to run repeatedly:
  cadena= "";
  for (int i=0; i<3; i++){
    valores[i] = analogRead(sensores[i]);
    cadena += String(valores[i])+"-";
  }
  Serial.println(cadena);

  if(Serial.available()>0){
   int v = Serial.readString().toInt();
   digitalWrite(led,v);
  }
  delay(100);
}