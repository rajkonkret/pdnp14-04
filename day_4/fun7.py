def connect(**opcje):  # ** keyword argument
    print(opcje)


connect()  # {}
connect(a=6)  # {'a': 6}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args(1, 2, 3)
all_args(a=7, b=0)
all_args(1, 2, 3, b="Radek")
# (1, 2, 3) {}
# () {'a': 7, 'b': 0}
# (1, 2, 3) {'b': 'Radek'}
