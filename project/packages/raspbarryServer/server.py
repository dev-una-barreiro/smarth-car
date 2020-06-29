# pylint: disable-all
import project.packages.env as env
import socket
import json
import time

HOST = env.currentEnv['serverHostRaspy']
HOSTNTB = env.currentEnv['serverHostNtk']
PORT = env.currentEnv['serverPort']

socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketInstance.connect((self.HOSTNTB, self.PORT))


def sendMensage(self, mensage: str, type):
    print(self.HOSTNTB, self.PORT)
    jsonData = json.dumps({"mensage": mensage, "type": type})
    mensageJson = '{jsonData};'.format(jsonData=jsonData)
    socketInstance.send(str.encode(
        mensageJson))
