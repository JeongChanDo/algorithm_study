class Symbol(object):
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    x = Symbol("py")
    y = Symbol("py")

    print(x is y)
    print(x == y)