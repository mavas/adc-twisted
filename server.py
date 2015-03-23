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
    """
    An Advanced Direct Connect (ADC) hub protocol talker.

    It's a 'LineReceiver' b/c the protocol spec says it operates on plain text
    lines.
    """
    def __init__(s, c):
        c.append(s)
    def connectionMade(s):
        print('connection')
        print(dir(s))
    def lineReceived(s, l):
        print(l)
        if l == 'TSUP':
            s.sendLine('FSUP 1')

class ADCHubFactory(Factory):
    """
    Launches a ADCHub protocol instance each time a client connects to the hub.
    """
    protocol = ADCHub
    def __init__(s):
        s.clients = []
    def buildProtocol(s, a):
        return ADCHub(s.clients)


reactor.listenTCP(8007, ADCHubFactory())
reactor.run()
