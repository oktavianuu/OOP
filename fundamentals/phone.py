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


