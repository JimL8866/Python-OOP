def func(arg):
    print(arg[0])

func((1, 2, 3))
func([8, 9, 3])
func("Melbourne")


class Foo1:
    def f1(self):
        pass

class Foo2:
    def f1(self):
        pass

class Foo3:
    def f1(self):
        pass


def func(arg):
    arg.f1()
    

obj = Foo1()
func(obj)