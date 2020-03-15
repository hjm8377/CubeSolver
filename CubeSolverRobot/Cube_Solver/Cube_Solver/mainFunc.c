/*
 * mainFunc.c
 *
 * Created: 2020-03-14 오후 5:13:02
 *  Author: hjm33
 */ 
#include "mainFunc.h"

void init()
{
	/* servo */
	DDRB = 0xFF;	// Timer (PB05, 06, 07 => OC1ABC) 
	PORTB = 0x00;
	DDRE = 0xFF;	// Timer (PE03 => OC3A)
	PORTE = 0x00;
	DDRC = 0xFF;	// StepMotor    7 6   5 4   3 2   1 0
					//				d.s / d.s / d.s / d.s
					//              L     B     R     F 
	PORTC = 0x00;
	DDRD = 0x00;	//스위치
	
	Timer_init();
	Uart_Init();
	sei();
}

void motor_init()
{
	OCR1A = 375;
	OCR1B = 375;
	OCR1C = 375;
	OCR3A = 375;
}

void cameraFunc()
{
	servo(F, 500);
	servo(B, 500);
	step_multi(F, B, -90);
	my_delay(Delay_Speed);
	servo(F, 375);
	servo(B, 375);
	my_delay(Delay_Speed);
	servo(R, 500);
	servo(L, 500);
	while(Uart_Receive() != 'N');
	
	servo(R, 375);
	servo(L, 375);
	servo(F, 500);
	servo(B, 500);
	step_multi(F, B, 90);
	my_delay(Delay_Speed);
	step_multi(R, L, 90);
}

// 문자열을 읽고 해당하는 동작 수행
void readData()
{
	char solution[400];	// 공식을 받을 변수
	char c1, c2;
	
	Uart_Receive_string(solution);
	
	for(int i = 0; solution[i] != '\n'; i+= 2){
		c1 = solution[i];
		c2 = solution[i + 1];
		
		//if (c1 == 'U' && c2 =='o')
		
		//...
	}
}