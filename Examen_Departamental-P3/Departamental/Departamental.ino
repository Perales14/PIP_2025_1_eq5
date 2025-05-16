const int pinTMP = A0;  // TMP36
const int pinLDR = A1;  // LDR

// Pines actuadores
const int relePin = 2;
const int motorIN1 = 7;
const int motorIN2 = 8;
const int motorPWM = 5;

String inputString = "";

void setup() {
  Serial.begin(9600);
  pinMode(relePin, OUTPUT);
  pinMode(motorIN1, OUTPUT);
  pinMode(motorIN2, OUTPUT);
  pinMode(motorPWM, OUTPUT);
}

void loop() {
  float temp = leerTMP();
  int ldr = analogRead(pinLDR);

  Serial.print(temp);
  Serial.print(",");
  Serial.println(ldr);

  while (Serial.available()) {
    // char c = Serial.read();
    String a = Serial.readString();
    if (a.length() >0) {
      inputString = a;
      procesarComando(inputString);
      inputString = "";
    } 
  }

  delay(1000);
}


float leerTMP() {
  int rawTMP = analogRead(pinTMP);
  float voltageTMP = rawTMP * (5.0 / 1023.0);
  return (voltageTMP - 0.5) * 100.0;
}

void procesarComando(String comando) {
  int focoEstado = comando.indexOf("L:") != -1 ? comando.substring(comando.indexOf("L:") + 2, comando.indexOf("T:")).toInt() : 0;
  int motorEstado = comando.indexOf("T:") != -1 ? comando.substring(comando.indexOf("T:") + 2).toInt() : 0;

  digitalWrite(relePin, focoEstado);

  switch (motorEstado) {
    case 0:
      motor(0);
      break;
    case 1:
      motor(1);
      break;
    case 2:
      motor(2);
      break;
  }
}

void motor(int direccion) {
  if (direccion == 0) {
    digitalWrite(motorIN1, 0);
    digitalWrite(motorIN2, 0);
    analogWrite(motorPWM, 0);
  } else if (direccion == 1) {
    digitalWrite(motorIN1, 1);
    digitalWrite(motorIN2, 0);
    analogWrite(motorPWM, 200);
  } else if (direccion == 2) {
    digitalWrite(motorIN1, 0);
    digitalWrite(motorIN2, 1);
    analogWrite(motorPWM, 200);
  }
}
