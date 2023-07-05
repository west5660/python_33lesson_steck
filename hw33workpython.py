#
#
stek = []
ochered = []

def add(mas,val):
    mas.append(val)
    return mas
    pass

def next(mas):
    if mas==stek:
        return stek.pop()
    if mas==ochered:
        return ochered.pop(0)

    pass

add(stek,10)
add(stek,20)
a = add(stek,30)
print(a)
print(next(stek))
print(next(stek))
print(next(stek))

# print(stek)
#
add(ochered,40)
add(ochered,50)
print(add(ochered,60))
print(next(ochered))
print(next(ochered))
print(next(ochered))
#
# print(ochered)

class Stek:

    def __init__(self):
        self.steklist=[]
    def add(self,val):
        self.steklist.append(val)
        return self.steklist

    def next(self):
        return self.steklist.pop()

stek1 = Stek()
print(stek1.__dict__)
print(stek1.steklist)

stek1.add('5r')
stek1.add('10r')
print(stek1.add('100r'))

print(stek1.next())
print(stek1.next())
print(stek1.next())

stek2 = Stek()
stek2.add('10c')
stek2.add('20c')
print(stek2.add('30c'))

class Sumstek(Stek):
    def __init__(self):
        super().__init__()
        # Stek.__init__(self)
        self.sum=0
    def checksum(self):
        for m in self.steklist:
            num=int(m[:-1])
            self.sum +=num
        return self.sum

stek3 = Sumstek()
stek3.add('10r')
stek3.add('5r')
print(stek3.add('2r'))
print(stek3.checksum())

class Stringstek(Stek):
    def __init__(self):
        super().__init__()
        self.lenght = 0

    def stringsum(self):
        for i in self.steklist:
            self.lenght += len(i)
        return self.lenght
class Ochered:
    def __init__(self):
        self.ochlist = []
    def add(self,val):
        self.ochlist.append(val)
        return self.ochlist
    def next(self):
        return self.ochlist.pop(0)

stek4 = Ochered()
stek4.add('asd')
stek4.add('ccc')
print(stek4.add('fff'))

print(stek4.next())
print(stek4.next())
print(stek4.next())


