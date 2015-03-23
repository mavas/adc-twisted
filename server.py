import re

from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor


class Client:
    def __init__(s, c):
        s.state = 'p'
        s.connection = c

class ADCHub(LineReceiver):
    def connectionMade(s):
        print('connection')
        s.factory.clients.append(Client(s))
    def lineReceived(s, l):
        print(l)
        if l == 'TSUP':
            s.sendLine('FSUP 1')

class ADCHubFactory(Factory):
    protocol = ADCHub
    def __init__(s):
        s.clients = []
    def buildProtocol(s, a):
        return ADCHub()


reactor.listenTCP(8007, ADCHubFactory())
reactor.run()
