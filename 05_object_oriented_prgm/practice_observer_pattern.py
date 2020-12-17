class C(object):
    def __init__(self, name):
        self._name = name
    
    # @propertu는 getter 역활
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = "{0} >> {1}".format(self._name, new_name)


if __name__ == "__main__":
    c = C("jin")
    print(c._name)
    print(c.name)
    c.name = "austin"
    print(c.name)