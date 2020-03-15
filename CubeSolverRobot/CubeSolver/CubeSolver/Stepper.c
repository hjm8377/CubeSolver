﻿/*
 * Stepper.c
 *
 * Created: 2020-02-06 오전 1:07:49
 *  Author: hjm33
 */ 

#include "Stepper.h"

void step(int motor_num, float degree)
{
	int tmp;
	float STEP;
	
	if(degree < 0){
		tmp = degree * (-1);
		set_dir(motor_num, LOW);
	}
	else{
		tmp = degree;
		set_dir(motor_num, HIGH);
	}
	
	STEP = tmp / 1.8;	// 1 : 1.8 = step : degree
	
	for (int i = 0; i < STEP; i++){
		set_step(motor_num, LOW);
		_delay_ms(50);
		set_step(motor_num, HIGH);
		_delay_ms(50);
	}
}

void step_multi(int motor_num1, int motor_num2, float degree)
{
	int step;
	step = degree / 1.8;
}

void set_dir(int motor_num, int dir)	//PORTC 홀수
{
	switch(motor_num){
		case 0:
			PORTC |= (PORTC1 << dir);
			break;
		case 1:
			PORTC |= (PORTC3 << dir);
			break;
		case 2:
			PORTC |= (PORTC5 << dir);
			break;
		case 3:
			PORTC |= (PORTC6 << dir);
			break;
	}	
}

void set_step(int motor_num, int step)	//PORTC 짝수
{
	switch(motor_num){
		case 0:
			PORTC |= (PORTC0 << step);
			break;
		case 1:
			PORTC |= (PORTC2 << step);
			break;
		case 2:
			PORTC |= (PORTC4 << step);
			break;
		case 3:
			PORTC |= (PORTC6 << step);
			break;
	}
}