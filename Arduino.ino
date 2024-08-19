#include <NewPing.h>
#include <Servo.h>


#define TRIG_PIN 7
#define ECHO_PIN 6
#define MAX_DISTANCE 200 

Servo servo1; 
Servo servo2; 

NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE);

bool displayUltrasonic = false; 

void setup()
{
  Serial.begin(9600);
  servo1.attach(9);
  servo2.attach(10);

  servo1.write(0);
  servo2.write(0);
  delay(1000);
}

void loop()
{
  if (Serial.available())
  {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (input == "rst")
    {
      servo1.write(0);
      servo2.write(0);
      delay(1000);
    }
    else if (input.startsWith("s1"))
    {
      int angle = input.substring(2).toInt();
      if (angle >= 0 && angle <= 180)
      {
        servo1.write(angle);
      }
    }
    else if (input.startsWith("s2"))
    {
      int angle = input.substring(2).toInt();
      if (angle >= 0 && angle <= 180)
      {
        servo2.write(angle);
      }
    }
    else if (input == "uss")
    {
      displayUltrasonic = true; 
    }
    else if (input == "ussext")
    {
      displayUltrasonic = false; 
    }
    else if (input == "runfunc") {
      scanServoAndMeasure();
    }
  }

  if (displayUltrasonic)
  {
    unsigned int distance = sonar.ping_cm();
    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
    delay(100); 
  }
}

void scanServoAndMeasure() {
  Serial.println("Mapping Started");  
  for (int angle2 = 0; angle2 <= 45; angle2 += 5) {
    servo2.write(angle2);
    delay(300);
    for (int angle1 = 30; angle1 <= 150; angle1++) {
      servo1.write(angle1);
      delay(300);  
      unsigned int distance = sonar.ping_cm();
      Serial.print(angle2);
      Serial.print(",");
      Serial.print(angle1);
      Serial.print(",");
      Serial.println(distance);
    }
    servo1.write(0);  
    delay(300);  
  }
  Serial.println("Mapping Finished");
}