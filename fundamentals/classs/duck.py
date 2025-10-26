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
    
# class only is the blueprint but has no effect when the code is execute.
# we have to instantiate that class
duckling = Duck(height=10, weight=3.4, sex="Male")
