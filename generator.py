import csv
import random


def generate_values(n, min, max):
    values = []
    for _ in range(n):
        values.append(random.randint(min, max))
    return values


print("Digit the size of the sample")
n = int(input())

print("Min V value")
vMin = int(input())

print("Max V value")
vMax = int(input())

print("Min W value")
wMin = int(input())

print("Max W value")
wMax = int(input())

W = ((wMin + wMax) / 2) * (n * 0.3)

vRange = generate_values(n, vMin, vMax)
wRange = generate_values(n, wMin, wMax)

data = zip(vRange, wRange)

with open("data.csv", "w", newline="") as f:
    write = csv.writer(f)
    write.writerow([W])
    for vi, wi in data:
        write.writerow([vi, wi])
