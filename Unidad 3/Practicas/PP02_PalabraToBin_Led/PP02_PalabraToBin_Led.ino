byte numero;
#include <WiFi.h>
bool residuo;
String valor;
String palabra;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for(int i = 0; i<8;i++){
    pinMode(i+2,OUTPUT);
  }
}

void mostrarbinario(int n){
  // int numero = n.toInt();
  
  numero = n;
  for(int i = 0; i<5;i++){
    residuo = numero%2;
    digitalWrite(i+8,residuo);
    numero = numero/2;
  }

}
void apagar(){
  digitalWrite(8,0);
  digitalWrite(9,0);
  digitalWrite(10,0);
  digitalWrite(11,0);
  digitalWrite(12,0);
  digitalWrite(13,0);
  // digitalWrite(8,0);
  // digitalWrite(9,0);
  
}
void loop() {
  // put your main code here, to run repeatedly:
  palabra = "";
  valor = "";
  if (Serial.available()>0){  
    palabra = Serial.readString();
    palabra.toUpperCase();
    
    Serial.println(palabra);
    for (int i = 0; i+1<palabra.length(); i++) {
      Serial.println(int(palabra.c_str()[i]));
      mostrarbinario(int(palabra.c_str()[i]));
      delay(5000);
      apagar();
      delay(300);
    }
    apagar();
  }
  // delay(1000);

}

