class MyNumbers:

    def __init__(self):
        self.a_ = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a_ < 10:
            self.a_ += 1
        else:
            raise StopIteration
        return self.a_


m = MyNumbers()


print("next:", next(m))
print("next:", next(m))

myiter = iter(m)
for x in myiter:
    print(x)

