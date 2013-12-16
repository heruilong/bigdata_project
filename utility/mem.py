import pylibmc
import time

class WebMC:
	def __init__(self):
		self.mc = pylibmc.Client(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})

	def fillMC(self,datas):
		for (key,val) in datas:
			if key!=None: self.mc.set(key,val)

	def clearMC(self):
		self.mc.flush_all()

	def run(self):
		print self.cold()
		print self.warm()
		self.clearMC()

if __name__ == "__main__":
	webMC = WebMC()
	webMC.mc.set('1',123)
	print webMC.mc.get('1')
	webMC.clearMC()
