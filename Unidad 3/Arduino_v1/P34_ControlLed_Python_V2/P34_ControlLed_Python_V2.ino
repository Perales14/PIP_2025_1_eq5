int led[] = {10,11,12};
String valor; 
void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i<3; i++){
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  // put your main code here, to run repeatedly:
 if(Serial.available()>0){
  valor = Serial.readString();
  for (int i=0; i<3;i++){
  digitalWrite(led[i], valor.charAt(i)-'0');
  }
 }
  delay(100);
}
