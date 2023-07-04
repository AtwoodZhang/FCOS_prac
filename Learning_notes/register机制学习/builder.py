from mmcv import Registry
from mmcv.utils.registry import build_from_cfg

CLASS = Registry("class_test")

"""在这里，我们创建了一个名为class_test的注册表，其中Registry的参数如下：
    name(str): 注册表的名字
    build_func(func, optional): 构造类接口的函数，简单来说，就是用来后续处理获取初始化类的函数，
               mmcv提供了一个build_from_cfg的函数，只需要建立一个字典，然后type=需要调用的类名，
               然后正常的参数的键值对输入就可以得到一个用自己配置参数获取的初始化的类了。
"""