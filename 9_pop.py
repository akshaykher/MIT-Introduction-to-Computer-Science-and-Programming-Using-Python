class Queue(object):
    def __init__(self):
        self.val = []
    def insert(self, ins):
        self.val.append(ins)
    def remove(self):
        try:
            a = self.val[0]
            del self.val[0]
            return a
        except:
            raise ValueError()
                

q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
q1.remove()
q2.remove()
