class MySet:

    def __init__(self):
        self.in_iter = False
        self.queued_ops = []
        self.data_ = set()

    def __iter__(self):
        self.in_iter = True
        self.iter_ = iter(self.data_)
        return self

    def __next__(self):
        try:
            n = next(self.iter_)
            return n
        except StopIteration:
            self.in_iter = False
            print("Putting in queued operations if any.")
            while self.queued_ops:
                op, item = self.queued_ops.pop(0)
                if op == 'add':
                    self.data_.add(item)
                elif op == 'remove':
                    if item in self.data_:
                        self.data_.remove(item)
            raise StopIteration

    def add(self, item):
        if not self.in_iter:
            self.data_.add(item)
        else:
            print("Queing add")
            op = ('add', item)
            self.queued_ops.append(op)

    def remove(self, item):
        if not self.in_iter:
            self.data_.remove(item)
        else:
            print("Queuing remove")
            op = ('remove', item)
            self.queued_ops.append(op)


set = MySet()

set.add(1)

set.add(2)

myiter = iter(set)
print("next:", next(myiter))
print("next:", next(myiter))

for i in set:
    set.add(4)
    set.remove(1)
    print(i)

for i in set:
    print(i)
