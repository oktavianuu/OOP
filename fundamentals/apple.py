import random

class Apple:
    # class variable
    count = 0
    total_weight = 0

    def __init__(self):
        # generate weight for apple
        self.weight = random.uniform(0.2, 0.5)

        # update class level tracking
        Apple.count += 1
        Apple.total_weight += self.weight

MAX_APPLES = 1000
MAX_WEIGHT = 300.0

while True:
    # check if adding another apple would exceed **any** limit
    if Apple.count >= MAX_APPLES:
        break

    # generate a trial apple to see if weight exceeds limit
    next_weight = random.uniform(0.2, 0.5)

    if Apple.total_weight + next_weight > MAX_WEIGHT:
        break

    Apple()

print("Packaging stopped.")
print(f"Total apples processed: {Apple.count}")
print(f"Total weight: {Apple.total_weight:.2f} units.")