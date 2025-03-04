int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  // input  = sensores, en si entrada de datos
  // output = actuadores, cosas que cambian el entorno, led, bocinas, etc
} 

void loop() {
  //delay(ms) para ""detener el arduino ms Tiempo"""
  delay(500);
  digitalWrite(led,1);
  delay(500);
  digitalWrite(led,0);
  
}
