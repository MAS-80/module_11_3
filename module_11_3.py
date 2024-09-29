import inspect


class MyClass:
    pass
def introspection_info(obj):
    type_ = type(obj).__name__
    attribute = getattr(obj, '__dict__', None)
    methods = dir(obj)
    module = obj.__class__.__module__
    func = inspect.isfunction(obj)
    info = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module, 'function': func}
    return info
obj = MyClass()
number_info = introspection_info(42)
print(number_info)
