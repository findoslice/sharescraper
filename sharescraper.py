class Pricescraper:

	from json import dumps
	from time import time, sleep

	try:
		from yahoo_finance import Share, Currency
	except:
		print("You need to have yahoo_finance installed, you silly sausage!")
		exit(1)

	def __init__(self, name):
		self.name = name 
	
	def logPrice(self):
		prices = {}
		try:
			price = Share(name)
			type = "sh"
		except:
			price = Currency(name)
			type = "cu"			
		outfile = open(str(name + '_pricelog.json'), 'a')
		starttime = time()

		if (type == 'sh'):
			price.refresh()
			dumps({name : {int(time() - starttime) : price.get_price()}})
		
		if (type == 'cu'):
			price.refresh()
			dumps({name : {int(time() - starttime) : price.get_price()}})

apple = Pricescraper()
apple.logPrice('AAPL')
