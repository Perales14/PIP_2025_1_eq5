int pot = A0;

int led1 = 6;
int led2 = 7;
int led3 = 8;
int led4 = 9;
int led5 = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int v = analogRead(pot);
  v = map(v, 0, 1023, 1,6);
  
  digitalWrite(led1, 0);
  digitalWrite(led2, 0);
  digitalWrite(led3, 0);
  digitalWrite(led4, 0);
  digitalWrite(led5, 0);

  

  switch(v){
    case 1:
    Serial.println(index);
      digitalWrite(led1,1);
      break;
    case 2:
    Serial.println(index);
      digitalWrite(led2,1);
      break;
    case 3:
    Serial.println(index);
      digitalWrite(led3,1);
      break;
    case 4:
    Serial.println(index);
      digitalWrite(led4,1);
      break;
    case 5:
    Serial.println(index);
      digitalWrite(led5,1);
      break;
    
  }

  delay(100);
}
