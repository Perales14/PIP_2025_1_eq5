int pot = A0;
int led =6;

void setup() {
  // put your setup code here, to run once:

}
    
void loop() {
  // put your main code here, to run repeatedly:
  int v= analogRead(pot); //0-255
  v=v/4;
  analogWrite(led, v); //0-255
  delay(10);
}


