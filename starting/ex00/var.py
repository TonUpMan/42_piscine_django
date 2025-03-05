# 42 est de type <class 'int'>
# 42 est de type <class 'str'>
# quarante-deux est de type <class 'str'>
# 42.0 est de type <class 'float'>
# True est de type <class 'bool'>
# [42] est de type <class 'list'>
# {42: 42} est de type <class 'dict'>
# (42,) est de type <class 'tuple'>
# set() est de type <class 'set'>

def my_var():
    a = 42
    A = "42"
    number = "quarante-deux"
    b = 42.0
    B = True
    print(a, "est de type", type(a))
    print(A, "est de type", type(A))
    print(number, "est de type", type(number))
    print(b, "est de type", type(b))
    print(B, "est de type", type(B))


if __name__ == '__main__':
    my_var()