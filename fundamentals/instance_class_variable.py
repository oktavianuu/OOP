class MobilePhone:
    # defining class variable
    is_mobile = True
    phone_count = 0

    def __init__(self, number):
        self.number = number #instance variable
        MobilePhone.phone_count += 1 #update the shared class variable

# usage
phone_a = MobilePhone('111')
phone_b = MobilePhone('222')

# accessing shared variable through instance
print(phone_a.is_mobile)

# the value of class variable shared in all instances
print(phone_a.phone_count)
print(phone_b.phone_count)

# when we change the value of class variable affects all instances
MobilePhone.is_mobile = False

print(phone_a.is_mobile)
print(phone_b.is_mobile)
