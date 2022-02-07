def uppercase_decorator(function):
    def decorator(*args, **kwargs):
        return function(*args, **kwargs).upper()
    
    return decorator

