def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(str(a) + str(b))
