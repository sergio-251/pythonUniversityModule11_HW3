# Интроспекция
import inspect
from pprint import pprint


class MyObject:
    def __init__(self):
        self.name = 'MyObject'
        self.value = 100

    def my_func(self):
        print('This is MyObject.my_func')


def introspection_info(obj):
    try:
        result = {
        'type': obj.__class__.__name__,
        'attributes': [m for m in vars(obj).keys()],
        'methods': [m for m in dir(obj) if 'method' in str(getattr(obj, m))],
        'module': __name__,
        'is_callable': callable(obj)
    }
    except:
        result = {
            'type': obj.__class__.__name__,
            'attributes': [],
            'methods': [m for m in dir(obj) if 'method' in str(getattr(obj, m))],
            'module': __name__,
            'is_callable': callable(obj)
        }
    return result


number_info_1 = introspection_info(MyObject())
number_info_2 = introspection_info(100)
number_info_3 = introspection_info(MyObject().my_func)
pprint(number_info_1)
pprint(number_info_2)
pprint(number_info_3)
