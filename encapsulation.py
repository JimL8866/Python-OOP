class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, "r")

    def read_fist(self):
        self.file.read()


obj = FileHandler("file_path")
obj.file.close()


def func_3(arg):
    print(arg.k1)
    print(arg.k2)
    print(arg.k3)


class Foo:
    def __init__(self, k1, k2, k3):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3


obj = Foo(123, 11, 333)
func_3(obj)