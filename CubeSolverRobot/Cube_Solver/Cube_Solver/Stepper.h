/*
 * Stepper.h
 *
 * Created: 2020-02-06 오전 1:07:34
 *  Author: hjm33
 */ 


#ifndef STEPPER_H_
#define STEPPER_H_

#define F_CPU 16000000UL

#include <util/delay.h>
#include <avr/io.h>
#include "constant.h"

void step(int motor_num, float degree);
void step_multi(int motor_num1, int motor_num2, float degree);
void set_dir(int motor_num, int dir);
void set_step(int motor_num, int step);
void my_delay(double ms);

#endif /* STEPPER_H_ */