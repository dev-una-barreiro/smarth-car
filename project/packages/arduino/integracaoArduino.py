import serial
from project.packages.env import currentEnv

connection = serial.Serial(currentEnv['usbPath'], currentEnv['usbPort'])


def sendComand(comand):
    if connection.isOpen():
        commandbytes = str(comand)
        connection.write(commandbytes.encode())
    else:
        connection.open()
        commandbytes = str(comand)
        connection.write(commandbytes.encode())

    return comand
