from .builder import CLASS


@CLASS.register_module()
class test(object):
    def __init__(self, n):
        self.n = n

    def printf(self):
        print(self.n)
        
        
        """我们在这里定义了一个类，@CLASS.register_module()的作用是将我们这个类放入CLASS注册表里面，
        只要在@CLASS.register_module()下写入一个类就可以将这个类放入我们创建的注册表里面了。
        """