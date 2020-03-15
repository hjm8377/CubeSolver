/*
 * Uart.c
 *
 * Created: 2020-03-14 오후 3:58:32
 *  Author: hjm33
 */ 
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