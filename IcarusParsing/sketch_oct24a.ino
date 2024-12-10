#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>




#include <SPI.h>

#include <RH_RF95.h>

#define RFM95_CS 9 // 0
//#define RFM95_RST 9
#define RFM95_INT 2 // 2
#define RF95_FREQ 915.0

// Singleton instanttttttttttttttttttttttttttttttce of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

// if using the Moteino board, initilize it as an arduino uno



// Create instance of the radio

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

void setup() {
  Serial.begin(9600);
  
  if(!accel.begin()) {
    Serial.println("No ADXL345 sensor detected.");
    while(1);
  }

  //pinMode(RFM95_RST, OUTPUT);
  //digitalWrite(RFM95_RST, HIGH);

  Serial.begin(9600);
  while (!Serial) delay(1);
  delay(100);

  Serial.println("Arduino LoRa TX Test!");

  // manual reset
  //digitalWrite(RFM95_RST, LOW);
  //delay(10);
  //digitalWrite(RFM95_RST, HIGH);
  //delay(10);

  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }
  Serial.println("LoRa radio init OK!");

  // Set frequency
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  Serial.print("Set Freq to: "); Serial.println(RF95_FREQ);
  
  // Set transmitter power
  rf95.setTxPower(23, false);
}

int16_t packetnum = 0;  // packet counter, we increment per xmission

void loop() {
  sensors_event_t event;
  accel.getEvent(&event);

  Serial.println("Sending to rf95_server");
  // Send a message to rf95_server

  char radiopacket[60];
  char xbuffer[10];    dtostrf(event.acceleration.x, 7, 2, xbuffer);
  char ybuffer[10];    dtostrf(event.acceleration.y, 7, 2, ybuffer);
  char zbuffer[10];    dtostrf(event.acceleration.z, 7, 2, zbuffer);
  char pbuffer[10];    itoa(packetnum++, pbuffer, 10);
  
  snprintf(radiopacket, 60, "~Icarus~ (N,X,Y,Z) {%s,%s,%s,%s}", pbuffer, xbuffer, ybuffer, zbuffer);
  
  Serial.print("Sending "); Serial.println(radiopacket);
  radiopacket[59] = 0;
  
  Serial.println("Sending...");
  delay(10);
  rf95.send((uint8_t *)radiopacket, 60);

  Serial.println("Waiting for packet to complete..."); 
  delay(10);
  rf95.waitPacketSent();
  // Now wait for a reply
  /*uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);

  Serial.println("Waiting for reply...");
  if (rf95.waitAvailableTimeout(1000))
  { 
    // Should be a reply message for us now   
    if (rf95.recv(buf, &len))
   {
      Serial.print("Got reply: ");
      Serial.println((char*)buf);
      Serial.print("RSSI: ");
      Serial.println(rf95.lastRssi(), DEC);    
    }
    else
    {
      Serial.println("Receive failed");
    }
  }
  else
  {
    Serial.println("No reply, is there a listener around?");
  }*/
  
  delay(50);
}
