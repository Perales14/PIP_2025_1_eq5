byte numero;
bool residuo;
String valor;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for(int i = 0; i<8;i++){
    pinMode(i+2,OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = "";
  if (Serial.available()>0){  
    
    numero = Serial.readString().toInt();
    for(int i = 0; i<6;i++){
      residuo = numero%2;
      digitalWrite(i+8,residuo);
      valor = " " + String(residuo) + valor;
      // valor = valor + " " + String(residuo);
      numero = numero/2;
    }
    Serial.println(valor);
  }
  delay(1000);

}
