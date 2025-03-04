int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;
int led5 = 10;

void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);
}

void loop() {
    // Encender LEDs en una dirección
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    digitalWrite(led4, LOW);
    digitalWrite(led5, LOW);

    digitalWrite(led1, HIGH);
    delay(200);
    digitalWrite(led1, LOW);
    delay(200);

    digitalWrite(led2, HIGH);
    delay(200);
    digitalWrite(led2, LOW);
    delay(200);

    digitalWrite(led3, HIGH);
    delay(200);
    digitalWrite(led3, LOW);
    delay(200);

    digitalWrite(led4, HIGH);
    delay(200);
    digitalWrite(led4, LOW);
    delay(200);

    digitalWrite(led5, HIGH);
    delay(200);
    digitalWrite(led5, LOW);
    delay(200);

    // Encender LEDs en la otra dirección
    digitalWrite(led4, HIGH);
    delay(200);
    digitalWrite(led4, LOW);
    delay(200);

    digitalWrite(led3, HIGH);
    delay(200);
    digitalWrite(led3, LOW);
    delay(200);

    digitalWrite(led2, HIGH);
    delay(200);
    digitalWrite(led2, LOW);
    delay(200);

    digitalWrite(led1, HIGH);
    delay(200);
    digitalWrite(led1, LOW);
    delay(200);
}
