import inspect

def introspection_info(obj):
    type_obj = type(obj).__name__
    list_dir = dir(obj)
    attributes = []
    methods = []
    for i in list_dir:
        if callable(i) is True:
            methods.append(i)
        else:
            attributes.append(i)
    module = obj.__class__.__module__
    func = inspect.isfunction(obj)
    info = {'type': type_obj, 'attributes': attributes, 'methods': methods, 'module': module, 'function': func}
    return info

number_info = introspection_info(42)
print(number_info)
