"""
写一个矩形的类，那么这个类默认有长和宽两个参数，
当传入一个叫square的属性时，值就等于边长，由于是正方形那么长和宽就等于边长。
"""
class Rectangle:
    def __init__(self,width,length):
        self._width = width
        self._length = length

    def getArea(self):
        return self._length*self._width

    def __setattr__(self, key, value):
        if key=="square":
            self._width = value
            self._length = value
        else:
            super().__setattr__(key,value)

rec = Rectangle(11,13)
rec.square = 12
print(rec.getArea())


