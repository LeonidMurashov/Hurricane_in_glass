int incomingByte = 0;   // переменная для хранения полученного байта
String pong = "";

void setup() {
    Serial.begin(9600); // устанавливаем последовательное соединение
} 
 
void loop() {
    if (Serial.available() > 0) 
    {
        while(Serial.available() > 0)
        {
          pong +=  char(Serial.read());
          delay(70);
        }
        Serial.println(pong);
        pong = "";
    }
}

