from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol


class ADCClient(LineReceiver):
    def connectionMade(s):
        s.sendLine('TSUP')
    def lineReceived(s, l):
        print('hello: ' + l)

def gotProtocol(p):
    print(p)


point = TCP4ClientEndpoint(reactor, "localhost", 8007)
d = connectProtocol(point, ADCClient())
d.addCallback(gotProtocol)
reactor.run()
