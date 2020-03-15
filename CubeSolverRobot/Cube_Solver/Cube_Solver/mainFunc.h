/*
 * mainFunc.h
 *
 * Created: 2020-03-14 오후 5:12:47
 *  Author: hjm33
 */ 


#ifndef MAINFUNC_H_
#define MAINFUNC_H_

#include <avr/io.h>
#include <avr/interrupt.h>
#include "constant.h"
#include "Servo.h"
#include "Stepper.h"
#include "Serial.h"

void init();
void motor_init();
void cameraFunc();
void readData();


#endif /* MAINFUNC_H_ */