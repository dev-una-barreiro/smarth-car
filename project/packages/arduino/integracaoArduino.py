import serial

connection = serial.Serial('/dev/ttyACM0', 9600)


def sendComand(comand):
    if connection.isOpen():
        commandbytes = str(comand)
        connection.write(commandbytes.encode())
    else:
        connection.open()
        commandbytes = str(comand)
        connection.write(commandbytes.encode())

    return comand
