int IR = A0;
int reading;

void setup() {
  Serial.begin(9600);
}

void loop() {
  reading = analogRead(IR);

  Serial.println(reading);

  delay(1000);
}
