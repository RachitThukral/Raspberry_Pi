/******************************************************************************
simple-demo.ino
simple demo of using LP55231 to control 9 LEDs.
Byron Jacquot @ SparkFun Electronics
October 12, 2016
https://github.com/sparkfun/SparkFun_LP55231_Arduino_Library

The simplest demo of LP55231 functionality.  Initializes the chip, then
sequentially turn on each of the 9 channels.

Resources:

Development environment specifics:
Written using Arduino 1.6.5

This code is released under the [MIT License](http://opensource.org/licenses/MIT).

Please review the LICENSE.md file included with this example. If you have any questions
or concerns with licensing, please contact techsupport@sparkfun.com.

Distributed as-is; no warranty is given.
******************************************************************************/

//#include <Wire.h>
#include "lp55231.h"
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <time.h>
#include <sys/types.h>
#include <unistd.h>
#include <iostream>


//Lp55231 ledChip;
static Lp55231Engines ledChip(0x32);

static const uint16_t program[] =
{
  // Engine one
  0x9D02, // 0 map direct
  0x18ff, // 1 ramp up
  0x19ff, // 2 ramp dn
  0xa000, // 3 loop to 0

  // Engine two
  0x9D03, // 4 map direct
  0x18ff, // 5 ramp up
  0x19ff, // 6 ramp dn
  0x1d00, // 7 wait...
  0x9D04, // 8 map direct
  0x18ff, // 9 ramp up
  0x19ff, // a ramp dn
  0xa000, // b loop to 4

  // Engine three
  0x9d09, // c map direct
  0x04ff, // d ramp up
  0x05ff, // e ramp dn
  0xa001 // f loop to d (skip map instr...)
};

int main(int argc, char *argv[]){
	//wiringPiSetupSys();
	printf("start\n");
	printf("%d\n",argc);
	for(int i=0; i<argc; i++){
		printf("%s\n",(argv[i]));}
	ledChip.Begin();
	ledChip.Enable();
	if(atoi(argv[1])==1){
		printf("%d\n",atoi(argv[1]));
		ledChip.SetChannelPWM(atoi(argv[2]), atoi(argv[3]));
	}
	else if(atoi(argv[1])==2){
		printf("%d\n",atoi(argv[1]));
		ledChip.AssignChannelToMasterFader(atoi(argv[2]), 0);
		ledChip.AssignChannelToMasterFader(atoi(argv[3]), 0);
		ledChip.AssignChannelToMasterFader(atoi(argv[4]), 0);
		
		ledChip.SetLogBrightness(atoi(argv[2]), true);
		ledChip.SetLogBrightness(atoi(argv[3]), true);
		ledChip.SetLogBrightness(atoi(argv[4]), true);
		
		ledChip.SetDriveCurrent(atoi(argv[2]), 0xff);
		ledChip.SetDriveCurrent(atoi(argv[3]), 0xff);
		ledChip.SetDriveCurrent(atoi(argv[4]), 0xff);
		
		ledChip.SetChannelPWM(atoi(argv[2]),0x80);
		ledChip.SetChannelPWM(atoi(argv[3]),0x40);
		ledChip.SetChannelPWM(atoi(argv[4]),0xff);
	}
	else if(atoi(argv[1])==3){
		printf("%d\n",atoi(argv[1]));
		ledChip.SetMasterFader(0, atoi(argv[5]));
	}
	else if(atoi(argv[1])==4 || atoi(argv[1])==5){
		for(uint8_t i = 0; i < 9; i++){
			ledChip.SetLogBrightness(i, true);
			ledChip.SetDriveCurrent(i, 111);
		}

		if(ledChip.LoadProgram(program, (sizeof(program)/2))==0){
			//Serial.
			printf("Program loaded?\n");
			if(ledChip.VerifyProgram(program, (sizeof(program)/2))){
				//Serial.
				printf("program verifies\n");
			}
		}
		else
		{
			//Serial.
			printf("Program didn't load?\n");
		}
		if(atoi(argv[1])==4){
			ledChip.SetEngineEntryPoint(0, 0);
			ledChip.SetEnginePC(0, 0);
			ledChip.SetEngineEntryPoint(1, 4);
			ledChip.SetEnginePC(1, 4);
			ledChip.SetEngineEntryPoint(2, 0x0c);
			ledChip.SetEnginePC(2, 0x0c);
			ledChip.SetEngineModeFree(0);
			ledChip.SetEngineModeFree(1);
			//ledChip.setEngineModeStep(2);
			ledChip.SetEngineModeFree(2);
			// Tried "once" mode, but it's not very useful...
		}
		else if(atoi(argv[1])==5){
			ledChip.SetEngineEntryPoint(0, 0);
			ledChip.SetEnginePC(0, 0);
			ledChip.SetEngineEntryPoint(1, 4);
			ledChip.SetEnginePC(1, 4);
			ledChip.SetEngineEntryPoint(2, 0x0c);
			ledChip.SetEnginePC(2, 0x0c);
			ledChip.SetEngineModeFree(0);
			ledChip.SetEngineModeFree(1);
			//ledChip.setEngineModeStep(2);
			ledChip.SetEngineModeFree(2);
			// Tried "once" mode, but it's not very useful...
		}
		ledChip.SetEngineRunning(0);
		ledChip.SetEngineRunning(1);
		ledChip.SetEngineRunning(2);
	}

	return 0;
}