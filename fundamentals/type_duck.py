# Class
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')
    
duckling = Duck(height=10, weight=3.4, sex='Male')
drake = Duck(height=25, weight=3.7, sex='Male')
hen = Duck(height=20, weight=3.4, sex='Female')

print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)