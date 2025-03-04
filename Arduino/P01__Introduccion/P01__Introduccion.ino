int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  // input  = sensores, en si entrada de datos
  // output = actuadores, cosas que cambian el entorno, led, bocinas, etc
} 

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led,1);


}
