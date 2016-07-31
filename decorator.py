#test @property
class screen():
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError("Must be a int!")
        elif value<1 or value>1920:
            raise ValueError("Not in the range!")
        else:
            self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError("Must be a int!")
        elif value<1 or value>1080:
            raise ValueError("Not in the range!")
        else:
            self._height=value
    @property
    def resolution(self):
        return self._width*self._height
myscreen=screen()
def test():
    #myscreen=screen()
    pass

if __name__=='__main__':
    test()

#test decorator
'''
import functools,time,random
from datetime import datetime

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            t=datetime.now()
            print(t,"Run function %s" % func.__name__)
            f=func(*args,**kw)
            t=datetime.now()
            print(t,"End function %s" % func.__name__)
            return f
        return wrapper
    return decorator

@log("Logging:")
def test_func():
    time.sleep(random.random())
    print("nothing happened!")
'''
