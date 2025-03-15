String respuesta;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}


void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>=0 ){//Devuelve cuantos bytes hay en el buffer de entrada!
    // Que comentario pongo
    respuesta = Serial.readString();//lee todos los caracteres que le sean posible
    //hasta alcanzar el tiempo limite (timeout). por defecto timeout = 1 segundo
    Serial.println(respuesta);
  }
}
