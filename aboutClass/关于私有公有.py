class ScopeOfAction:
    def __init__(self):
        self.__private = "私有变量"
        self._protect = "保护型变量"

    def __private_func(self):
        print("私有方法")

    def _protect_func(self):
        print("保护方法")

    def public_func(self):
        print("公有方法")

A = ScopeOfAction()
print(A._protect)  #  "保护型变量"
# print(A.__private )  # bug
A.public_func()   #
A._protect_func()
A.__private_func()
