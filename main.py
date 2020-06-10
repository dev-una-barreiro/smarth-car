from project.packages.server import server
from project.packages.tensorML.TensorObservale import tensorOb


def handleDistancia(distancia):
    tensorOb.updateObject('distancia', int(distancia))


server.serverInstance.appendFunction('distancia', handleDistancia)

server.serverInstance.createServer()
