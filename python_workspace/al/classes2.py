class Dog:
    kind=''
    name=''
    def __init__(self):
        self.name='3'
        self.kind='4'
        print('Object created')
    def bark(self,times):
        for i in range(times):
            print('wuf')
    
    
b = Dog()
b.bark(4)
#b.name = ('Fluffy')
#b.kind = ('Akita')
print(b.name)
print(b.kind)