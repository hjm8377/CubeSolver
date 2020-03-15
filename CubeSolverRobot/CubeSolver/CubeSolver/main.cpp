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
#include <util/delay.h>
#include <avr/interrupt.h>
//#include "Cube.h"
#include "Stepper.h"
#include "Servo.h"

void init();
void Uart_Init();
unsigned char Uart_Receive();
void Uart_trans(unsigned char data);
void Uart_trans_string(char *data);
void readData();
void motor_init();
void cameraFunc();


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



void Uart_Init()
{
	UCSR1A = 0x00;
	UCSR1B = (1 << RXEN1) | (1 <<TXEN1);
	UCSR1C = (1 << UCSZ11) | (1 << UCSZ10);
	
	UBRR1H = 0;
	UBRR1L = 8;	//115200
}

unsigned char Uart_Receive()
{
	while(!(UCSR1A & (1<<RXC1)));
	return UDR1;
}

void Uart_Receive_string(char *str)
{
	int i = 0;
	for(int i = 0; Uart_Receive() != '\n'; i++){
		str[i] = Uart_Receive();
	}
	str[i] = '\0';
}
void Uart_trans(unsigned char data)
{
	while(!(UCSR1A & (1<<UDRE1)));
	UDR1 = data;
}

void Uart_trans_string(char *data)
{
	for(int i = 0; data[i] == '\n'; i++)
		Uart_trans(data[i]);
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

void motor_init()
{
	OCR1A = 375;
	OCR1B = 375;
	OCR1C = 375;
	OCR3A = 375;
}

void cameraFunc()
{
	
	step_multi(F, B, -90);
	
}