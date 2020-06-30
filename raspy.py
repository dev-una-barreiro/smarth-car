import project.packages.env
from project.packages.raspbarryServer import server


for i in range(10):
    server.sendMensage('testes', 'teste')
