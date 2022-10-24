# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

class Log(object):
    def __init__(self,n):
        self.n = n
        self.ringBuffer = []
        self.current = 0
        pass

    def register(self, value):
        if(len(self.ringBuffer) <self.n):
            self.ringBuffer.append(value)
        else:
            self.ringBuffer[self.current] = value
            self.current = (self.current+1)%self.n
    
    def getValueByLast(self, i):
        return self.ringBuffer[self.current-i]
    def printAll(self):
        print(str(self.ringBuffer))
        


def main():
    log = Log(3)
    log.register(1)
    log.register(2)
    log.register(3)
    print(log.getValueByLast(0))
    print(log.getValueByLast(1))
    print(log.getValueByLast(2))
    log.printAll()
    log.register(4)
    log.register(5)
    print(log.getValueByLast(0))
    print(log.getValueByLast(1))
    print(log.getValueByLast(2))
    log.printAll()

    pass

if __name__ == "__main__":
    main()