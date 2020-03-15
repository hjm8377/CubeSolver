/*
 * Uart.h
 *
 * Created: 2020-03-14 오후 3:07:29
 *  Author: hjm33
 */ 


#ifndef UART_H_
#define UART_H_

#include <avr/io.h>
#include <avr/interrupt.h>

void Uart_Init();
unsigned char Uart_Receive();
void Uart_Receive_string(char *str);
void Uart_trans(unsigned char data);
void Uart_trans_string(char *data);ta[i]);




#endif /* UART_H_ */