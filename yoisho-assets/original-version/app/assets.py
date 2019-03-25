import logging
logging.basicConfig(level=logging.DEBUG)

from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode

from spyne import Iterable

from spyne.protocol.soap import Soap11

from spyne.server.wsgi import WsgiApplication

from random import randint

class TotalAssetsService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def bank_assets(ctx):
        for i in range(1):
            yield str(randint(9900000,9999999))


    @rpc(_returns=Iterable(Unicode))
    def bank_debt(ctx):
        for i in range(1):
            yield str(randint(1000000,1999999))

application = Application([TotalAssetsService],
    tns='yoisho.total.assets',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 80, wsgi_app)
    server.serve_forever()

