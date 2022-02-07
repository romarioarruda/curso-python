from facade import uppercase_decorator, lowercase_decorator

@uppercase_decorator
def nome(nome):
    return nome

@lowercase_decorator
def sobrenome(sobrenome):
    return sobrenome


print(nome('romario teste'))
print(sobrenome('romario teste'))