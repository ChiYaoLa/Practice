# 魔术方法
# https://www.cnblogs.com/dachenzi/p/8185792.html
# https://blog.csdn.net/weixin_42223833/article/details/86512801#2.__call__
# # 实验的不好
class MagicMethod:

    def __init__(self,name):
        self._name = name


    # repr() 或 str() 调用
    def __repr__(self):
        return "MagicMethod:{}".format(self._name)
    def __str__(self):
        return "__str__"


    # 析构或显式del()
    def __del__(self):
        print("__del__")

    """
     hash()触发
    """
    def __hash__(self):
        return hash(self._name)

    """
    F = MagicMethod("xuliang") 对象变函数柄
    F(1) 
    """
    def __call__(self, num):
        print("__call__"+str(num))




A = MagicMethod("XULIANG")

print(hash(A))
print(str(A))

MagicMethod("xuliang")(1)


