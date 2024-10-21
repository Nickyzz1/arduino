int azul = 3;
int laranja = 5;
int pot = A5;
int tempo = 0;

void setup() {
  Serial.begin(9600);
  pinMode(azul, OUTPUT);
  pinMode(laranja, OUTPUT);
  pinMode(pot, INPUT);
}

void loop() { 
  tempo = map(analogRead(pot), 0, 1023, 10, 100);
  Serial.println(tempo);

  // Fade out do LED laranja e fade in do LED azul
  for (int i = 0, j = 255; i <= 255; i += 10, j -= 10) {
    analogWrite(azul, i);      // Aumenta o azul
    analogWrite(laranja, j);   // Diminui o laranja
    delay(tempo);
  }
  
  // Fade in do LED laranja e fade out do LED azul
  for (int i = 255, j = 0; i >= 0; i -= 10, j += 10) {
    analogWrite(azul, i);      // Diminui o azul
    analogWrite(laranja, j);   // Aumenta o laranja
    delay(tempo);
  }
}
