import project.packages.env
from project.packages.tensorML.TensorObservale import tensorOb
from project.packages.server import server


def handleDistancia(distancia):
    tensorOb.updateObject('distancia', int(distancia))


server.serverInstance.appendFunction('distancia', handleDistancia)

server.serverInstance.createServer()
