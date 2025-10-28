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

#### The Superclass: `Phone` (The Master Blueprint)
The Phone class is the generic blueprint for anything that can make a call. It establishes the two crucial, shared attributes for all descendants:
|Code Line(s)|Concept|Detailed Explanation|
|---|---|---|
|`counter = 0`|Class Variable `(Global State)`|This is the global tracker. It lives on the class itself, not inside any specific phone. It starts at zero and is designed to count every single phone object created (fixed or mobile).|
|`def __init__(self, number):`|Initializer|This method sets up the initial state for every object. The number parameter is essential because every phone needs a number.|
|`self.number = number`|Instance Variable|This data is unique to each object. One phone's number is independent of every other phone's number.|
|`Phone.counter += 1`|State Modification|This is the key line for the global count. We access the counter via the class name (Phone.counter) to ensure we modify the single, shared value for the entire hierarchy.|
|`def call(self, number):`|Instance Method|This defines a behavior common to all phones. It uses `self.number` (instance data) to display which specific phone is making the call.|

#### The Subclasses: `FixPhone` and `MobilePhone` (Specific Blueprints)
The subclasses inherit the structure and behavior of Phone but add specific details and their own unique counters.
1. `last_SN = 0` (The Unique Counter)
In both `FixPhone` and `MobilePhone`, we define a separate `last_SN = 0`.
   - **Concept: Class Variable (Subclass-Specific State)**.
   - **Why it's unique**: Because `FixPhone` and `MobilePhone` are separate classes, they each get their own independent copy of `last_SN`. Incrementing `FixPhone.last_SN` has absolutely no effect on `MobilePhone.last_SN`. This lets we track serial numbers separately!
2. `super().__init__(number)` (**The Inheritance Link**)
   This is the most critical line for linking the subclasses to the superclass.
   - **Concept: Explicit Superclass Initialization.**
   - What it does: When we create a `FixPhone` object, Python executes this line, which says: "Before doing anything else, go run the Phone's `__init__` method."
   - The Chain Reaction: This execution automatically sets `self.number` (Instance Variable) AND increments `Phone.counter` (Global Class Variable).
3. **The Subclass's Unique Logic**
   After calling `super().__init__`, the subclass adds its own specific logic:
    |Code Line(s)|Concept|Detailed Explanation|
    |---|---|---|
    |`FixPhone.last_SN += 1`|Unique State Modification|This line increments the counter only for the `FixPhone` class. It uses the subclass name    `(FixPhone.last_SN)` to modify its unique serial number tracker.|
    |`self.SN = 'FP-{}'.format(...)`|`Creating New Instance Data`|The subclass creates a new instance variable (`self.SN`) that did not exist in the base `Phone` class. This holds the final, unique serial number for this specific object.|

**Final Execution (Putting the Concepts to Work)**
   |Code Line(s)|Concept|Detailed Explanation|
   |---|---|---|
   |`fphone = FixPhone(...)`|`super()` runs, and `Phone.counter` goes to 1. Then, `FixPhone` increments `FixPhone.last_SN to 1`.|No output yet|
   |`mphone = MobilePhone(...)`|`super()` runs, and `Phone.counter` goes to 2. Then, `MobilePhone` increments `MobilePhone.last_SN` to 1.|No output yet|
   |`print(..., Phone.counter)`|Accesses the shared class variable.|Total number of phone devices created: 2|
   |`print(mphone.call(...))`|Executes an inherited instance method (call) on `mphone`, accessing mphone's unique `self.number`.|Calling 01632-960004 using own number 555-2368|

