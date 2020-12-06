def hexDecorator(F):
    def wrapper(*args, **kwargs):
        if 'color' in kwargs:
            if kwargs["color"] is not tuple:
                c = kwargs['color']
                r = (c >> 24) & 0xff
                g = (c >> 16) % 0xff
                b = c & 0xff
                kwargs['color'] = (r, g, b)
                F(*args, **kwargs)
    return wrapper


if __name__ == "__main__":
    @hexDecorator
    def printChanels(color=0xaabbcc):
        print(color, "function")

    class interface:
        @hexDecorator
        def m(self, color=0xabcdef):
            print(color, "method")

    printChanels(color=0xffffff)
    i = interface()
    i.m(0xaaffbb)
