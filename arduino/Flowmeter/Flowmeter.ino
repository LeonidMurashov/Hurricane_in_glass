volatile int  flow_frequency;
unsigned int  l_hour;
unsigned char flowmeter = 2;
// Пин к которому подключен сенсор.
unsigned long currentTime;
unsigned long cloopTime;

// Only 2, 3 pin on Arduino Nano

void flow ()
{
  flow_frequency++;
}
  
  void setup()
  {
    pinMode(flowmeter, INPUT);
    Serial.begin(9600);
    attachInterrupt(digitalPinToInterrupt(3), flow, RISING);
    sei();  
    currentTime = millis();
    cloopTime = currentTime;
  } 
    
  void loop ()
  {  
    currentTime = millis();  
    if(currentTime >= (cloopTime + 1000)) 
    {    
      cloopTime = currentTime;  
      l_hour = (flow_frequency * 60.0 / 7.5);   
      flow_frequency = 0;                   
      Serial.print(l_hour, DEC);              
      Serial.println(" L/hour");  
    }
  }

