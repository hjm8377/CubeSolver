/*
 * Servo.c
 *
 * Created: 2020-03-14 오후 4:36:48
 *  Author: hjm33
 */ 

#include "Servo.h"

void Timer_init()
{
	// Timer/Counter 1, 3 (A,B,C / A) 사용
	TCCR1A = (1 << COM1A1) | (1 << WGM11) | (1 << COM1B1) | (1<< COM1C1);	// Clear OCnA on Compare match, Fast PWM
	TCCR1B = (1 <<WGM13) | (1 <<CS11) | (1 << CS10);	// 분주비 64
	TCCR3A = (1 << COM3A1) | (1 << WGM31);
	TCCR3B = (1 << WGM32) | (1 << WGM33) | (1 << CS31) | (1 << CS32);
	ICR1 = 4999;
	ICR3 = 4999;
	OCR1A = 375;	// 0 dgree F
	OCR1B = 375;	// R
	OCR1C = 375;	// B
	OCR3A = 375;	// L
	TCNT1 = 0x00;
	TCNT3 = 0x00;
}

void Servo(int servo_num, int OCR)
{
	
}
