int pot = A0;
int led = 6;

void setup() {
  // put your setup code here, to run once:

} 

void loop() {
  // put your main code here, to run repeatedly:
  int v = analogRead(pot);

  v = map(v,0,1023,0,255); 

  analogWrite(led,v); 

}
