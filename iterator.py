#test filter

def is_palindrome(n):
    temp=0
    nn=n
    while nn>0:
        temp=temp*10+nn%10
        nn=nn//10
    if n==temp:
        return True
    else:
        return False
def test():
    output=filter(is_palindrome,range(1,1000))
    print(list(output))

if __name__=='__main__':
    test()
#test iterator
'''
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
    #不满足的才会被删掉
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
#g=primes()
for n in primes():
    if n<20:
        print(n)
    else:
        break

from functools import reduce
def normalize(name):
    return name[0].upper()+name[1:].lower()
print(list(map(normalize,['adam','LISA','barT'])))
def c2n(x):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]
def change(st):
    return reduce(lambda x,y:x*10+y,map(c2n,st))
print(change('123978'))
'''
