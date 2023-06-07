#include <Wire.h>
#include <SoftwareSerial.h>

SoftwareSerial BT(10,11);
byte message;
int counter = 0;
int input_pin = A1;
int input_value;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  BT.begin(9600);
}

void loop() {
  // Serial.println(analogRead(A0));
  input_value = analogRead(input_pin);
  // byte output_value = map(input_value, 0, 511, 0, 127);
  byte output_value = map(input_value, 0, 800, 0, 127);
  // output_value = map(output_value, 50, 170, 0, 255);
  BT.write(output_value);
  Serial.println(output_value);
  // delay(2);
}
