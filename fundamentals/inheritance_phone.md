Another example shows that a class variable of a super class can be used to count the number of all objects created from the descendant classes (subclasses). We'll achieve this by calling the superclass `__init__` method.

Another class variable is used to keep track of the serial numbers (which in fact are also counters) of particular subclass instances. In this example, we are also storing instance data (phone numbers) in instance variables.

The class Phone is a class representing a blueprint of generic devices used for calling. This class definition delivers the call method, which displays the object’s variable, which holds the phone number. This class also holds a class variable that is used to count the number of instances created by its subclasses.

Subclasses make use of the superclass `__init__` method, then instances are created. This gives us the possibility to increment the superclass variable. 

```python
class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1 # used to update the class variable
    
    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message

class FixPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixPhone.last_SN)
    
class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)

print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phone devices created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))
```

The Phone class is the generic blueprint for anything that can make a call. It establishes the two crucial, shared attributes for all descendants:
|Code Line(s)|Concept|Detailed Explanation|
|---|---|---|
|`counter = 0`|Class Variable `(Global State)`|This is the global tracker. It lives on the class itself, not inside any specific phone. It starts at zero and is designed to count every single phone object created (fixed or mobile).|
|`def __init__(self, number):`|Initializer|This method sets up the initial state for every object. The number parameter is essential because every phone needs a number.|
|`self.number = number`|Instance Variable|This data is unique to each object. One phone's number is independent of every other phone's number.|
|`Phone.counter += 1`|State Modification|This is the key line for the global count. We access the counter via the class name (Phone.counter) to ensure we modify the single, shared value for the entire hierarchy.|
|`def call(self, number):`|Instance Method|This defines a behavior common to all phones. It uses `self.number` (instance data) to display which specific phone is making the call.|