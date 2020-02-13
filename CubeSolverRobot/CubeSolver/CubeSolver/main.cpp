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


#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include "Cube.h"

void Timer_init();
void Uart_Init();
unsigned char Uart_Receive();
void Uart_trans(unsigned char data);
void Uart_trans_string(char *data);
void readData();
void cameraFunc();


int main(void)
{
	/* servo */
	DDRB = 0xFF;	// Timer (PB05, 06, 07 => OC1ABC) 
	PORTB = 0x00;
	DDRE = 0xFF;	// Timer (PE03 => OC3A)
	PORTE = 0x00;
	DDRC = 0xFF;	// StepMotor
	
	init();
	
    while (1) 
    {
		// cube_init();
		while(Uart_Receive() != 'I'){
			// 'I'가 들어올 때 까지 대기
		}
		cameraFunc();
		readData();	// 공식 받고 실행
		// motor realse		
    }
}

void Timer_init()
{
	// Timer/Counter 1, 3 (A,B,C / A) 사용
	TCCR1A = (1 << COM1A1) | (1 << WGM11) | (1 << COM1B1) | (1<< COM1C1);	// Clear OCnA on Compare match, Fast PWM
	TCCR1B = (1 <<WGM13) | (1 <<CS11) | (1 << CS10);	// 분주비 64
	TCCR3A = (1 << COM3A1) | (1 << WGM31);
	TCCR3B = (1 << WGM32) | (1 << WGM33) | (1 << CS31) | (1 << CS32)
	ICR1 = 4999;
	ICR3 = 4999;
	OCR1A = 375;	// 0 dgree
	OCR1B = 375;
	OCR1C = 375;
	OCR3A = 375;
	TCNT1 = 0x00;
	TCNT3 = 0x00;
}

void init()
{
	Timer_init()
	Uart_Init()
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
		str[i] = Uart_Receive()
	}
	str[i] = '\0'
}
void Uart_trans(unsigned char data)
{
	while(!(UCSR1A & (1<<UDRE1)));
	UDR1 = data;
}

void Uart_trans_string(char *data)
{
	for(int i = 0; data[i] == '\n'; i++)
		Uart_trans(data[i])
}

// 문자열을 읽고 해당하는 동작 수행
void readData()
{
	char solution[400];	// 공식을 받을 변수
	char c1, c2;
	
	Uart_Receive_string(solution);
	
	for(int i = 0; solution[i] != '\n', i+= 2){
		c1 = solution[i];
		c2 = solution[i + 1];
		
		if (c1 == 'U' && c2 =='o')
			U();
		//...
	}
}

void cameraFunc()
{
	int i = 0;
	while(1){
		if(i == 5)
			break;
		if(Uart_Receive()=='I'){			
			switch (i)
			{
				case 0:
				// 그립 안보이게
					i++;
					break;
				case 1:
					i++;
					break;
				case 2:
					i++;
					break;
				case 3:
					i++;
					break;
				case 4:
					i++
					break;
			}
		}
	}
}