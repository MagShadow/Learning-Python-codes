#test cPickle
import pickle as p
shoplistfile='shoplist.data'
shoplist=['mango','banana','eagle']
f=open(shoplistfile,'wb')
p.dump(shoplist,f)
f.close()

del shoplist
f=open(shoplistfile,'rb')
storedlist=p.load(f)
Print(storedlist)
