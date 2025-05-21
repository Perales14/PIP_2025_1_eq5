int valores[3] = { 0, 0, 0 };
int sensores[3] = { A0, A1, A2 };
int leds[3] = { 8, 10, 12 };
void setup() {
  // pinMode(led, OUTPUT);
  for (int i = 0; i < 3; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(100);
}

String cadena;
String valor;
int led;
int encendido;
void loop() {
  cadena = "";

  if (Serial.available()) {
    String valor = Serial.readString();
    led = String(valor.charAt(0)).toInt();
    encendido =  String(valor.charAt(1)).toInt();;
    digitalWrite(leds[led-1],encendido);
  }

  for (int i = 0; i < 3; i++) {
    valores[i] = analogRead(sensores[i]);
    cadena += String(valores[i]) + "-";
  }

  Serial.println(cadena);
  delay(100);
}
