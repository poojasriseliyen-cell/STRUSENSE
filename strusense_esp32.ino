/* STRUSENSE firmware scaffold — NOT hardware-validated.
   Select the actual sensor and install its library before use.
   This placeholder only confirms serial setup; it does NOT read a sensor.
*/
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("STRUSENSE scaffold: sensor driver not configured");
  Serial.println("Do not treat these messages as sensor measurements.");
}

void loop() {
  // TODO: initialize the selected accelerometer/vibration sensor.
  // TODO: read calibrated measurements and print timestamp + axis values.
  delay(1000);
}
