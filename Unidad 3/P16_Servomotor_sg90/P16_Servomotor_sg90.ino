  int pot = A0;
#include <Servo.h>
  Servo serv;
void setup() {
  // put your setup code here, to run once:
  serv.attach(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  int v = analogRead(pot);
  v = map(v,0,1023,0,180);
  serv.write(v);
  delay(30);


}
