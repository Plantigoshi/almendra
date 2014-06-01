#include "aJSON.h"

#define rain_sen 8
#define red 9
#define green 10
#define blue 11

int moisture = 0;
bool rain = false;
float solar_volt = 0;
bool light = 0;
float temp = 0;

bool rand_color = true;

double timer = micros();

void setup() 
{
	Serial.begin(115200);
	pinMode(rain_sen,INPUT);
	pinMode(red,OUTPUT);
	pinMode(green,OUTPUT);
	pinMode(blue,OUTPUT);
}

void loop() 
{
	if(Serial.available())
	{
		char cmd = Serial.read();
		switch (cmd) 
		{
		    case 'G':
		    	measurement();
		    	Report();
		      	rand_color = true;
		      	break;
		    case 'R':
		    	setColor(255,0,0);
		    	rand_color = false;
		    	break;
		    case 'T':
		    	setColor(0,0,255);
		    	rand_color = false;
		}
		while(Serial.available())
		{
			Serial.read();
		}
	}
	if(rand_color && (micros() - timer > 5000000))
	{
		timer = micros();
		setColor(random(0,255),random(0,255),random(0,255));
	}
}

void setColor(uint8_t r,uint8_t g,uint8_t b)
{
	analogWrite(red,255-r);
	analogWrite(green,255-g);
	analogWrite(blue,255-b);
}

void measurement()
{
	moisture = map(analogRead(A0),0,900,0,100);
	rain = digitalRead(rain_sen);
	solar_volt = analogRead(A1)*(5.0/1023);
	light = (analogRead(A2)>800);
	temp = random(24,27);//(5.0 * analogRead(A3) * 100.0) / 1024;	
}

void Report()
{
	aJsonObject *json_report = aJson.createObject();

	aJson.addNumberToObject(json_report,"Hum",moisture);
	aJson.addNumberToObject(json_report,"Rain",rain);
	aJson.addNumberToObject(json_report,"SolarVolt",solar_volt);
	aJson.addNumberToObject(json_report,"light",light);
	aJson.addNumberToObject(json_report,"Temp",temp);

	char* report = aJson.print(json_report);
	aJson.deleteItem(json_report);
  	Serial.println(report);
  	free(report);
  	Serial.flush();
}