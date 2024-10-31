const int buzzerPin = 8;

;void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Som de porco "oinc oinc oinc"
  for (int i = 0; i < 3; i++) { // Repetir 3 vezes
    tone(buzzerPin, 110);
    delay(120);
    tone(buzzerPin, 174); // Frequência 400 Hz
    delay(50);
    tone(buzzerPin, 138);
    delay(30);
    noTone(buzzerPin);    // Para o som
    delay(100);           // Curta pausa
  }
  
  delay(2000); // Pausa maior antes de repetir
}
