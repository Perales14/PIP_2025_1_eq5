int led = 13;
int dEncendido = 500;
int dApagado = 50;
void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  // input  = sensores, en si entrada de datos
  // output = actuadores, cosas que cambian el entorno, led, bocinas, etc
} 

void loop() {

  digitalWrite(led,1);
  delay(dEncendido);
  digitalWrite(led,0);
  delay(dApagado);

}
