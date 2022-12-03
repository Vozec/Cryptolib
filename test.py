from glob import glob

from Cryptolib.logger import logger

def load(path="examples"):
	modules = {}
	for module_name in sorted(glob('%s/*.py'%path)):
		name = module_name.replace('/','.')[:-3]
		modules[name.split('.')[-1]]= getattr(__import__(name),name.split('.')[-1])
	return modules

logger('	Module   | Test Succeed','info',0,0,True)
logger('_________________________________\n','info',0,0,True)

for name,obj in load('examples').items():
	res = obj.test()
	color = 'flag' if res else 'error'
	logger('%15s | %5s'%(name,res),color,0,0,True)