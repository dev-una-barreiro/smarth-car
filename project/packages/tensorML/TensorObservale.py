from project.packages.tensorML.tensorkeras import model
from project.packages.arduino.integracaoArduino import sendComand
import numpy


class TensorObservale:
    _oberservableRegister = []
    _object = {'pessoa': 0, 'placa': 0, 'objeto': 0, 'distancia': 0}

    def subscribeFunction(self, func):
        self._oberservableRegister.append(func)

    def unsubscribeFunction(self, func):
        for index, value in enumerate(self._oberservableRegister):
            if isinstance(value, func):
                self._oberservableRegister.remove(func)

    def sendComandNotify(self):
        predict_comand = model.predictValue(
            numpy.array([[*self._object.values()]]))
        sendComand(int(predict_comand))

    def updateObject(self, name, data):
        if self._object[name] != data:
            self._object[name] = data
            print(self._object)
            self.sendComandNotify()


tensorOb = TensorObservale()
