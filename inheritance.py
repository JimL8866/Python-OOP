# class Base:
#     @staticmethod
#     def f1():
#         print("base.f1")
#
#     def f3(self):
#         self.f1()
#         print("base.f3")
#
#
# class Foo(Base):
#     def f2(self):
#         print("foo.f2")  # will print first
#         self.f3()  # next be executed
#
#
# obj = Foo()
# obj.f2()

class Base:
    @staticmethod
    def f1():
        print("base.f1")

    def f3(self):
        self.f1()
        print("base.f3")


class Foo(Base):
    def f1(self):
        print("foo.f1")

    def f2(self):
        print("foo.f2")  # will print first
        self.f3()  # next be executed


obj = Foo()
obj.f2()

obj2 = Base()
obj2.f3()

# self 是哪个个类的对象，就从哪个类开始找（自己没有就找父类）
# 多继承先找左边
