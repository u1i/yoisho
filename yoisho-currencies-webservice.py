import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, ComplexModel
from spyne import Iterable
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication

from random import randint
from datetime import datetime

class CurrencyReturn(ComplexModel):
    buy = Unicode
    sell = Unicode
    timestamp = Unicode

class YoishoCurrencies(ServiceBase):
    @rpc(Unicode, _returns=CurrencyReturn)
    def get_currency(ctx, currency):

	clist_buy={'USD':'389', 'SGD':'281'}
	clist_sell={'USD':'489', 'SGD':'381'}

	rcur=CurrencyReturn()
	rcur.buy=-1
	rcur.sell=-1

	rand1 = randint(100,200)
	rand2 = randint(100,200)

	try:
		rcur.buy = str(clist_buy[currency]) + "." + str(rand1)
	except:
		rcur.buy=-1

	try:
		rcur.sell = str(clist_sell[currency]) + "." + str(rand2)
	except:
		rcur.sell=-1

	rcur.timestamp=str(datetime.now())

	return rcur
	
application = Application([YoishoCurrencies],
    tns='yoisho.currencies.webservices',
    in_protocol=HttpRpc(validator='soft'),
    out_protocol=JsonDocument()
)
if __name__ == '__main__':

    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8189, wsgi_app)
    server.serve_forever()
