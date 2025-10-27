class MobilePhone:
    def __init__(self, number):
        self.number = number
    
    def turn_on(self):
        return f'mobile phone {self.number} is turned on'
    
    def turn_off(self):
        return 'mobile phone is turned off'

    def call(self, number):
        return f'calling {number}'

okta = MobilePhone(number='081346803227')
anjo = MobilePhone(number='085821012820')

phones = [okta, anjo]
for phone in phones:
    print(phone.turn_on())

print(phones[0].call(number='911'))

for phone in phones:
    print(phone.turn_off())
