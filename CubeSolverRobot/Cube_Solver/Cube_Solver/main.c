/*
 * CubeSolver.cpp
 *
 * Created: 2020-02-01 오후 4:05:22
 * Author : hjm33
 */ 

// step motor 4개
// servo motor 4개

/*  step motor => 17HS3430
    CurrentLimit = Vref(V) * 2
    전류 제한 = 전압 * 2
    정격 전류 0.4A => 전압 = 200mV
    1.8 degree / 1 step
*/

/*  step motor driver => a4988
	** 드라이버에 전원이 들어왔을때 모터 연결/분리 X
	필요 핀 수 2 (step, dir)
	dir high 시계
	(step = high
	delay
	step = low
	delay) => 1step
*/

/* servo motor => MG90S
*/
#define F_CPU 16000000UL

#include <avr/io.h>

#include "Stepper.h"
#include "Servo.h"
#include "Serial.h"
#include "mainFunc.h"
//#include "Cube.h"



int main(void)
{	
	init();
	
    while (1) 
    {
		while(PIND0 != 1);
		motor_init();
		// cube_init();
		while(Uart_Receive() != 'S'){// 'S'가 들어올 때 까지 대기
		}
		cameraFunc();
		readData();	// 공식 받고 실행
		// motor realse		
    }
}

