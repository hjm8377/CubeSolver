import serial
from time import sleep

sol = 'XoYoXoYoYoUtFtRtBtLtLoUtLpFpUpFoLoUoLpBoUtBpUpBoUoBpUpLoUoLpUoRoUpRpUpFpUoFtUpFpUpLpUoLoUtRpUoRoUoBoUpBpUoLpUoLoUoFoUpFpFoRoUoRpUpFpUtFoRoUoRpUpRoUoRpUpFpFoRpFpLoFoRoFpLpUoRoUtRpUpRoUtLpUoRpUpLoYp'


try:
    print(len(sol))
    ser = serial.Serial(port='COM3', baudrate=9600)
    sleep(2)

    ser.write(sol.encode('utf-8'))
    sleep(1)
except:
    exit(1)
