# tamplete decorartor that support function and methods
def decorator(F):
    def wrapper(*args):
        F(*args)

    return wrapper


@decorator
def faa(a):
    print(a)


class Works:
    @decorator
    def m(self, a):
        print(a)


w = Works()


# w.m("method")
# faa("function")


def hex_decorator(f):
    def wrapper(*args, **kwargs):
        if 'color' in kwargs:
            if kwargs["color"] is not tuple:
                c = kwargs['color']
                r = (c >> 24) & 0xff
                g = (c >> 16) % 0xff
                b = c & 0xff
                kwargs['color'] = (r, g, b)
                f(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    @hex_decorator
    def print_chanels(color=0xaabbcc):
        print(color, "function")


    class Interface:
        @hex_decorator
        def m(self, color=0xabcdef):
            print(color, "method")


    print_chanels(color=0xffffff)
    i = Interface()
    i.m(0xaaffbb)
