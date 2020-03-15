/*
 * Serial.h
 *
 * Created: 2020-03-14 오후 5:09:58
 *  Author: hjm33
 */ 


#ifndef SERIAL_H_
#define SERIAL_H_

#include <avr/io.h>
#include <avr/interrupt.h>

void Uart_Init();
unsigned char Uart_Receive();
void Uart_Receive_string(char *str);
void Uart_trans(unsigned char data);
void Uart_trans_string(char *data);


#endif /* SERIAL_H_ */