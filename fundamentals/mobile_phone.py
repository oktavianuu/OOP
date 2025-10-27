class MobilePhone:
    def __init__(self, number):
        self.number = number
    
    def turn_on(self):
        return print(f'mobile phone {self.number} is turned on')
    
    def turn_off(self):
        return print('mobile phone is turned off')

    def call(self, number):
        return print(f'calling {number}')

okta = MobilePhone(number='081346803227')
anjo = MobilePhone(number='085821012820')

okta.turn_on()
anjo.turn_on()
okta.call(number='911')
okta.turn_off()
okta.turn_off()