def all_params(a, b, /, c=42, d=256):
    print(f"{a}, {b}")
    print(f"{c}, {d}")


all_params(1, 2)
all_params(1, 2, 3)
all_params(1, 2, 3, 4)
all_params(1, 2, c=3, d=4)


# / powoduje, ze a i b mogą byc przekazane tylko po pozycji!!
# all_params(a=1, b=2, c=3, d=4) # TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'

def all_params(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a}, {b}")
    print(f"{c}, {d}")
    print(f"{args}, {kwargs}")


all_params(1, 2, 3)
all_params(1, 2, c=3)
all_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# musimy d po nazwie po jest po args
all_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, d=100)
# (4, 5, 6, 7, 8, 9, 0), {}
all_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, d=100, name="radek")
# (4, 5, 6, 7, 8, 9, 0), {'name': 'radek'}
all_params(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, d=100, name="radek", a=7)
