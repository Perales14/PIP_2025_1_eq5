void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

byte var = 5;

void loop() {
  // put your main code here, to run repeatedly:
  var += 1;
  Serial.println(var);
  delay(10);
}
