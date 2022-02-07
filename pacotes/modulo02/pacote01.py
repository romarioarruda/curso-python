def lowercase_decorator(function):
    def decorator(*args, **kwargs):
        return function(*args, **kwargs).lower()
    
    return decorator