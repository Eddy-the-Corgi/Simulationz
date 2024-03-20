import random
import math
inside_circle = 0
n = 10000000
for _ in range(n):
    x = random.random()
    y = random.random()
    if math.sqrt((x-0.5)**2 + (y-0.5)**2) < 0.5:
        inside_circle += 1
print (inside_circle / (n/4))