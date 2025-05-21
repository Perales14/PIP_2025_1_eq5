//Proyecto Pip
#include <Keypad.h>
#include <HardwareSerial.h>

//Sensor de movimiento en escaleras (Sensor PIR)
#define sensor_Pir1 4
#define sensor_Pir2 5

#define led_escaleras 6


//Sensor de luz (Exterior). (LDR)
#define ldr_ext 7  //Cambiar a pin analogicop6

#define led_ext 15


const byte FILAS = 4;
const byte COLUMNAS = 4;

char teclas[FILAS][COLUMNAS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};

// // byte pinesFilas[FILAS] = { 42, 41, 40, 39 };
// byte pinesColumnas[COLUMNAS] = { 38, 37, 36, 35 };
byte pinesFilas[FILAS] = { 39, 40, 41, 42 };  // invertí el orden de filas
byte pinesColumnas[COLUMNAS] = { 35, 36, 37, 38 };  // invertí columnas también si quieres


Keypad teclado = Keypad(makeKeymap(teclas), pinesFilas, pinesColumnas, FILAS, COLUMNAS);

#include <ESP32Servo.h>  //si es con arduino, usar Servo.h
// #include <Servo.h>
#define cerrojo_puerta 18  //Servo, intentar que sea PIN PWM
Servo servoPuerta;
#define abierto 150
#define cerrado 90


// Sensor de temeperautra (LM35)
#define sensor_temperatura 20

// #define abanico12v 21
#define abanico12v 45


// Timbre (boton)
#define boton_timbre 16

#define buzzer_timbre 19
#define frecuenciaTimbre 1000  //cambiar


// Medidor de agua Tinaco (Ultrasonico)
#define echo 48
#define trigger 47

// Sensor de lluvia para tendedero (sensor de agua)
#define sensor_lluvia 3

#define AFUERA 0
#define ADENTRO 1

// Motor lluvia (Motor 2)
#define motor_lluvia_IN3 9
#define motor_lluvia_IN4 46
#define motor_lluvia_ENB 11  // PWM para velocidad

// Tendedero
byte estado_ropa;
unsigned long tendedero_tiempo;

//nivel de agua, tinaco
byte nivel = 0;

//tiempo en general, para hacer impresiones a serial
unsigned long tiempo;

bool buzzerActivo = false;
unsigned long buzzerInicio = 0;
int buzzerEtapa = 0;


void setup() {
  tiempo = millis();
  Serial.begin(115200);
  estado_ropa = AFUERA;


  // movimiento escaleras
  pinMode(sensor_Pir1, INPUT);
  pinMode(sensor_Pir2, INPUT);
  pinMode(led_escaleras, OUTPUT);

  //baja luz exterior
  pinMode(led_ext, OUTPUT);

  servoPuerta.setPeriodHertz(50);  // 50 Hz
  servoPuerta.attach(cerrojo_puerta);
  servoPuerta.write(abierto);

  // Ventilador para alta temperatura
  pinMode(abanico12v, OUTPUT);
  digitalWrite(abanico12v, 0); // el Rele que se esta usando es invertido, por lo que para que este desactivado el fan, debe de estar en H el pin.

  // Boton y buzzer para el timbre
  pinMode(boton_timbre, INPUT_PULLUP);           // Evita ruidos y resistencias externas
  ledcAttachChannel(buzzer_timbre, 2000, 8, 7);  // pone el buzzer del timbre en el canal 7 de PWM
  // ledcAttachChannel
  // //pines para el ultrasonico
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  Serial1.begin(115200, SERIAL_8N1,8, 17);  // Para el traspaso del nivel del tinaco.

  // // Motor lluvia el encargado de ocultar y "desocultar" el tendedero
  pinMode(motor_lluvia_IN3, OUTPUT);
  pinMode(motor_lluvia_IN4, OUTPUT);
  ledcAttachChannel(motor_lluvia_ENB, 1000, 8, 4);  // pone el buzzer del timbre en el canal 4 de PWM
}


String valorSeparado[7];    // Array para almacenar los valores separados (los recibidos por el PC)
int estadoServo = abierto;  // Valor inicial
bool estadomotor_activo = false;


void loop() {

  // Este IF, es para apagar el motor del tendedero siempre al tiempo que es, que no haya tiempo de mas, pues si no, despues de tanto movimeinto, generara un desfase grande
  if (estadomotor_activo) {
    
    // si esta activo, ver si pasaron los 3.7 Segundos para apagarse
    if (millis() - tendedero_tiempo > 3700) {
      digitalWrite(motor_lluvia_IN3, LOW);
      digitalWrite(motor_lluvia_IN4, LOW);
      ledcWrite(motor_lluvia_ENB, 0);  // Le mandas el nuevo valor (0-255)
      estadomotor_activo = false;
    }
  }

  if (millis() - tiempo >= 250) {
    lecturas();
    tiempo += 250;
  }

  if (Serial.available() > 0) {
    recibir();
    acciones();
  }

  actualizarBuzzer();  // Aquí actualizamos el estado del buzzer si está activo
}



//recibe los datos de la PC, para actuar despues segun lo que se reciba
void recibir() {
  if (Serial.available()) {
    String linea = Serial.readStringUntil('\n');  // Leer todo hasta salto de línea
    int index = 0;
    int start = 0;

    for (int i = 0; i < linea.length(); i++) {
      if (linea[i] == '-' || i == linea.length() - 1) {
        int end = (linea[i] == '-') ? i : i + 1;
        if (index < 7) {
          valorSeparado[index] = linea.substring(start, end);
          index++;
        }
        start = i + 1;
      }
    }
  }
}

void acciones() {
  // valor separado estara conformado de esta forma:
  // valorSeparado[] tendrá la siguiente estructura:

    // valorSeparado[0] - pir: Para encender o apagar las escaleras segun su valor (0,1)
    // valorSeparado[1] - ldr: Para encender o apagar el exterior segun su valor (0,1)
    // valorSeparado[2] - boton_matriz: saber si abrir o no la puerta del proche trasero
    // valorSeparado[3] - temperatura: encender o no el abanico (12v)
    // valorSeparado[4] - timbre: para hacer sonar el buzzer
    // valorSeparado[5] - distancia: pues para mostrarla en la pantalla i2c
    // valorSeparado[6] - lluvia: para quitar el tendedero

  escaleras(valorSeparado[0].toInt());  //segun lo que reciba, enciende o apaga las escaleras

  exterior(valorSeparado[1].toInt());  //segun lo que reciba, enciende o apaga el exterior

  abrir_porche(valorSeparado[2].toInt());  //abre porche solo si es necesario

  abanico(valorSeparado[3].toInt());  //enciende el abanico de 12v

  buzzer(valorSeparado[4].toInt());  //hace sonar el buzzer

  pantalla(valorSeparado[5].toInt());  // muestra el % de agua que queda en el recipiente.

  tendedero(valorSeparado[6].toInt());  //se encarga de quitar la "ropa" (ocultarla/taparla) de la lluvia xd
}


long tiempoescaleras;  // para que cuando no haya movimiento y reciba 0 tarde 5 segundos mas en apagarse
void escaleras(int valor) {
  if (valor == 1) {
    tiempoescaleras = millis() / 1000;  // Guardamos el tiempo actual en segundos
    digitalWrite(led_escaleras, HIGH);
  } else if ((millis() / 1000) - tiempoescaleras > 5) {
    digitalWrite(led_escaleras, LOW);
  }
}

int tiempoexterior = 0;  // Variable para contar el tiempo en segundos (int)

void exterior(int valor) {
  if (valor == 1) {
    tiempoexterior = millis() / 1000;  // Guardamos el tiempo actual en segundos
    digitalWrite(led_ext, HIGH);       // Encendemos el LED exterior
  } else if ((millis() / 1000) - tiempoexterior > 5) {
    digitalWrite(led_ext, LOW);  // Apagamos el LED exterior después de 5 segundos
  }
}

void abanico(int valor){
  if(valor==0){//lo apaga, entonces "enciende" el rele, osea corta el paso.
    digitalWrite(abanico12v, 0);
    Serial.println("enciendeabanico");
  }
  else{
    digitalWrite(abanico12v, 1);
    Serial.println("apga abanico");
  }
}

void abrir_porche(int valor) {
  if (valor == 1) {
    estadoServo = abierto;
  } else {
    estadoServo = cerrado;
  }
  servoPuerta.write(estadoServo);
}

void buzzer(int valor) {
  if (valor == 1 && !buzzerActivo) {
    buzzerActivo = true;
    buzzerInicio = millis();
    buzzerEtapa = 0;
  }
}

void actualizarBuzzer() {
  if (!buzzerActivo) return;

  unsigned long ahora = millis();

  switch (buzzerEtapa) {
    case 0: 
      ledcWriteNote(buzzer_timbre, NOTE_C, 5);
      if (ahora - buzzerInicio > 300) {
        buzzerInicio = ahora;
        buzzerEtapa++;
      }
      break;
    case 1:
      ledcWriteNote(buzzer_timbre, NOTE_E, 5);
      if (ahora - buzzerInicio > 300) {
        buzzerInicio = ahora;
        buzzerEtapa++;
      }
      break;
    case 2:
      ledcWriteNote(buzzer_timbre, NOTE_G, 5);
      if (ahora - buzzerInicio > 300) {
        buzzerInicio = ahora;
        buzzerEtapa++;
      }
      break;
    case 3:
      ledcWriteNote(buzzer_timbre, NOTE_C, 6);
      if (ahora - buzzerInicio > 500) {
        buzzerInicio = ahora;
        buzzerEtapa++;
      }
      break;
    default:  
      ledcWrite(buzzer_timbre, 0);
      buzzerActivo = false;
      break;
  }
}

void pantalla(int valor) {
  if (nivel == valor) {
    Serial1.println(valor);
    nivel = valor;
  }
}

void tendedero(int valor) {
  if (estadomotor_activo) {
    return;  //no hace nada pues se esta moviendo
  }
  if (estado_ropa == AFUERA && valor == 1) {
    tendedero_tiempo = millis();
    digitalWrite(motor_lluvia_IN3, 1);
    digitalWrite(motor_lluvia_IN4, 0);
    ledcWrite(motor_lluvia_ENB, 180);  // Le mandas el nuevo valor (0-255)
    estado_ropa = ADENTRO;
    estadomotor_activo = true;
  } else if (estado_ropa == ADENTRO && valor == 0) {
    tendedero_tiempo = millis();
    digitalWrite(motor_lluvia_IN3, 1);
    digitalWrite(motor_lluvia_IN4, 0);
    // digitalWrite(motor_lluvia_IN3, LOW);
    // digitalWrite(motor_lluvia_IN4, HIGH);
    ledcWrite(motor_lluvia_ENB, 180);  // Le mandas el nuevo valor (0-255)
    estado_ropa = AFUERA;
    estadomotor_activo = true;
  }
}


void lecturas() {
  // Sensores de movimiento
  int pir1 = digitalRead(sensor_Pir1);
  int pir2 = digitalRead(sensor_Pir2);

  int ldr = analogRead(ldr_ext);
  // Revisado

  char key = teclado.getKey();
  String tecla = String(key);
  if (tecla == "") {
    tecla = "N";
  }


  // Boton a manera de timbre
  int timbre = !digitalRead(boton_timbre);

  // Sensor de agua para verificar si esta ""lloviendo"", ver si se puede complementar con un dht11
  int lluvia = digitalRead(sensor_lluvia);


  // Lectura del sensor de temperatura
  int temperatura = leerTemperatura();

  // Lectura de distancia (sensor ultrasónico)
  int distancia = medirDistancia();
  // Serial1.println(distancia);

  // Ahora mandamos todo junto
  String datos_sensores = datos(pir1, pir2, ldr, tecla, temperatura, timbre, distancia, lluvia);
  Serial.println(datos_sensores);
}

// Función para leer el sensor de temperatura
int leerTemperatura() {

  int valor = analogRead(sensor_temperatura);
  float voltaje = valor * (3.3 / 4095.0);  //si se utiliza un ESP32, se cambiara a 3.3 en ves de 5, y de 1023 a 4096 (por que su ADC es de 10 bits)
  float temperatura = voltaje * 100.0;     // 10 mV por grado => 100 para Celsius

  return temperatura;
}

// Función para medir la distancia del ultrasónico
int medirDistancia() {
  digitalWrite(trigger, LOW);
  unsigned long tiempoInicio = micros();
  while (micros() - tiempoInicio < 2)
    ;  // Espera 2 microsegundos

  digitalWrite(trigger, HIGH);
  tiempoInicio = micros();
  while (micros() - tiempoInicio < 10)
    ;  // Espera 10 microsegundos

  digitalWrite(trigger, LOW);

  long duracion = pulseIn(echo, HIGH, 38000);  //el 38000 es la duracion MAXIMA del puslso, es lo maximo que "soporta" el ultrasonico, hacerle mas no tiene sentido y genera que la ejecucion sea mas lenta.
  int distancia = duracion * 0.034 / 2;        // Distancia en cm
  
  return distancia;
}

String datos(int pir1, int pir2, int ldr, String boton_matriz, int temperatura, int timbre, int distancia, int lluvia) {
  if (lluvia ==0){
    lluvia = 1;
  }
  else{
    lluvia = 0;
  }
  String cadena = "";
  cadena += String(pir1) + "-" + String(pir2) + "-" + String(ldr) + "-" + boton_matriz + "-" + String(temperatura) + "-" + String(timbre) + "-" + String(distancia) + "-" + String(lluvia);

  return cadena;
}