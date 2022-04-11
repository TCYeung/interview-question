import random

def main(spaces):
    n = 0.0
    cars = 0
    while n <= spaces:
        rng = random.uniform(1, 2)
        if n + rng > spaces:
            return cars
        n += rng
        cars += 1
    return cars

input = float(input("How many spaces? "))

print("Cars parked in that many spaces:")
print(main(input))

avg = 0
for i in range(10000):
    avg += main(input)
print("Average over 10000 simulations:")
print(avg/10000)