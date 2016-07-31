#try and exception
class TooShortException(Exception): #这是个继承
    '''User-Defined'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    s=input("Enter you comment-->")
    if len(s)<3:
        raise TooShortException(len(s),3)
except EOFError:
    print("\nEOF!")
except TooShortException as x:
    print ("Length too short {0}->{1}".format(x.length,x.atleast))
else:
    print("Yes!")
finally:
    print("End!")
