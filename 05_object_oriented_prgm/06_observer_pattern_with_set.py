class Subscriber(object):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print("{0}, {1}".format(self.name, message))
    

class Publisher(object):
    def __init__(self):
        self.subscribers = set()
    
    def register(self, who):
        self.subscribers.add(who)
    
    def unregister(self, who):
        self.subscribers.discard(who)
    
    def dispatch(self, message):
        for Subscriber in self.subscribers:
            Subscriber.update(message)

if __name__ == "__main__":
    pub = Publisher()

    astin = Subscriber("astin")
    james = Subscriber("james")
    jeff = Subscriber("jeff")

    pub.register(astin)
    pub.register(james)
    pub.register(jeff)

    pub.dispatch("lunch time")
    pub.unregister("jeff")
    pub.dispatch("dinner time")