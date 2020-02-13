import serial

# ser = serial.Serial(port='COM1', baudrate=15200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)


class Serial:

    def __init__(self):
        ser = serial.Serial('COM1', 115200)

    @staticmethod
    def write(ser, arr):
        for i in range(len(arr)):
            ser.write(arr[i])
