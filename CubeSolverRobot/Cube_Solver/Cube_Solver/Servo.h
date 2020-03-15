/*
 * Servo.h
 *
 * Created: 2020-03-14 오후 4:37:02
 *  Author: hjm33
 */ 


#ifndef SERVO_H_
#define SERVO_H_

#include <avr/io.h>
#include <avr/interrupt.h>

void Timer_init();
void servo(int servo_num, int OCR);

#endif /* SERVO_H_ */