"""
关于 属性方面 的魔术方法
"""
class AAAA:
    def __init__(self,name1,name2):
        self._name1 = name1
        self._name2 = name2

    def __getattr__(self, item):
        return item

    def __setattr__(self, key, value):
        print("key:{} value:{}".format(key,value))

# print(AAAA("xuliang","wmy").a)
AAAA("xuliang","wmy").a = 12