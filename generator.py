#test generator
def triange(max=1):
    elist=[1,]
    n=1
    yield elist
    while n<max:
        #print(elist)
        n+=1
        tlist=elist[:]
        #print(tlist)
        elist=elist+[0,]
        #print(elist)
        tlist=[0,]+tlist
        #print(tlist)
        elist=[elist[i]+tlist[i] for i in range(0,len(elist))]
        yield elist

for i in triange(2):
    print(i)
'''
def fib(max):
    n,a,b=1,0,1
    while n<=max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
g=fib(10)
while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break
'''
