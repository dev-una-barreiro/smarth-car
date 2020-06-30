from project.packages.env import currentEnv
import socket
import json
# import threading


class Server:

    HOST = currentEnv['serverHostNtk']
    PORT = currentEnv['serverPort']
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    functions = []

    # def handle_client(self, client, addr):
    #     with client:
    #         print('Connected by', addr)
    #         if len(self.functions) > 0:
    #             for functionObject in self.functions:
    #                 data = client.recv(1024).decode('utf-8')

    #                 listData = data.split(';')
    #                 for itemData in listData:
    #                     if len(itemData) > 1:
    #                         dataJson: str = json.loads(itemData)
    #                         if dataJson['type'] == functionObject['mensageType']:
    #                             resultFunction = functionObject['function']
    #                             resultFunction(dataJson['mensage'])
    #         client.send(1)
    #         client.close()

    def createServer(self):
        self.socketServer.bind((self.HOST, self.PORT))
        while True:
            print('waiting for a connection')
            data, client = self.socketServer.recvfrom(1024)
            with client:
                print('Connected by', client)
                if len(self.functions) > 0:
                    listData = data.decode('utf-8').split(';')
                    print(listData)
                    for functionObject in self.functions:
                        for itemData in listData:
                            if len(itemData) > 1:
                                dataJson: str = json.loads(itemData)
                                if dataJson['type'] == functionObject['mensageType']:
                                    resultFunction = functionObject['function']
                                    resultFunction(dataJson['mensage'])
                client.send('1'.encode())
            # thread = threading.Thread(
            #     target=self.handle_client, args=(client, addr))
            # thread.start()

    def sendMessage(self, typeMessage, message, address, port, json=True):
        try:
            connection = socket.create_connection((address, port))
            with connection:
                data = message
                if(json):
                    data = json.dumps(
                        {"message": typeMessage, 'data': message})

                connection.send(bytes(data, 'utf-8'))
        except:
            print(f'{typeMessage} refuse')

    def appendFunction(self, mensageType, func):
        def executeFunction(dataMensage):
            return func(dataMensage)

        functionDic = {
            'mensageType': mensageType,
            'function': executeFunction
        }

        self.functions.append(functionDic)


serverInstance = Server()
