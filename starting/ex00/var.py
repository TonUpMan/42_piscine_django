def my_var():
    a = 42
    A = "42"
    number = "quarante-deux"
    b = 42.0
    B = True
    l = [42]
    d = {42: 42}
    t = 42,
    s = set()

    print(a, "est de type", type(a))
    print(A, "est de type", type(A))
    print(number, "est de type", type(number))
    print(b, "est de type", type(b))
    print(B, "est de type", type(B))
    print(l, "est de type", type(l))
    print(d, "est de type", type(d))
    print(t, "est de type", type(t))
    print(s, "est de type", type(s))



if __name__ == '__main__':
    my_var()