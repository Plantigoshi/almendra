#include <aJSON.h>

char* messaje="{\"Name\" : \"Hola\", \"Values\" :[1.5,2.5,3.5], \"state\": true}";
float* output;


void setup() 
{
	Serial.begin(115200);	
}

void loop() 
{
	aJsonObject* msg= aJson.parse(messaje);
	//|Serial.println(aJson.print(msg));
	aJsonObject* Vals=aJson.getObjectItem(msg, "Values");
	aJsonObject* Name=aJson.getObjectItem(msg, "Name");
	aJsonObject* state=aJson.getObjectItem(msg, "state");
        //Serial.println(aJson.print(Vals));
        output=aJson.getFloatArray(Vals);
        for(int i=0;i<3;i++)
       {
         Serial.println(output[i]);
       } 
       while(1)
       {
         ;
       }
}
