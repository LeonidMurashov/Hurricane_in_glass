#include <SoftwareSerial.h>
#include <DFPlayer_Mini_Mp3.h>
void setup () {
    Serial.begin (9600);
    mp3_set_serial (Serial);    
    mp3_set_volume (25);
    delay (100);
    mp3_play ();
    delay (100);
}
void loop () {        
    mp3_next (); // Следующий трек
    delay (10000); // пуза 10 секунд
}
