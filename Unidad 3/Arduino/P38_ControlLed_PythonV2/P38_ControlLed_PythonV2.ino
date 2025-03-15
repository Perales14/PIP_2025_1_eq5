int leds[] = {10,11,12};
String valor; //de xyz, 000,001,010,011,100,101,110,111

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for (int i = 0; i<3;i++){
    pinMode(leds[i],OUTPUT);
  }
  Serial.setTimeout(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    valor = Serial.readString();
    for (int i=0;i<3;i++){
      
      digitalWrite(leds[i],valor.charAt(i));
      digitalWrite(12,1);
    }
  
  }
  delay(250);
  
}
