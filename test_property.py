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
    def __init__(self):
        self._width=1080
        self._height=720
myscreen=screen()
def test():
    #myscreen=screen()
    pass

if __name__=='__main__':
    test()
