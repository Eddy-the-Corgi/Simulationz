'''
Suppose that we have N cars parked in a line occupying spaces 1 to N... spaces N+1 to 2N are empty.... every minute a car is considered eligible to move forward one square if a) the space in front of them is empty and b) their square number is less than 2N... suppose that every minute, if a car is eligible to move it has a 1/2 chance of moving forward by one square... what is the expected amount of minutes before the cars occupy squares N+1 to 2N.
'''
### do a simultaneous update rather than a sequential update
### improve debugging logs
### use optimal functions such as random.random() instead of random.randint(1,2), avoiding squareroots, numpy vectorisation, etc.

import random
import matplotlib.pyplot as plt
import numpy as np
N = 40
max_time = 10*N
no_tests = 100000
expected_value = 0
d = {}
for i in range(1, max_time+1):
    d[i] = 0

def simulate(N, max_time, no_tests, expected_value, d):
    for _ in range(no_tests):
        t = 0
        carpark = [1] * N + [0] * N
        while sum(carpark[:N]) != 0:
            t += 1
            index_cars_to_move = []
            for i in range(2*N-1):
                if carpark[i] == 1 and carpark[i+1] == 0:
                    index_cars_to_move.append(i)
            for i in index_cars_to_move:
                if random.random() < 0.5:
                    carpark[i] = 0
                    carpark[i+1] = 1
        if t > max_time:
            t = max_time
        d[t] += 1
    for key, val in d.items():
        d[key] = val / no_tests
        expected_value += key * d[key]
    return (expected_value)

'''
x = np.array([i for i in range(1,N+1)])
y = []
for i in range(1, N+1):
    y.append(simulate(i, max_time, no_tests, expected_value, d))
    print(i)
y = np.array(y)
'''

x = np.array([i for i in range(1,N+1)])
y = np.array(
    [
        2.00595,
        6.6733200595,
        12.068836733200595,
        17.81183068836733,
        23.761938118306883,
        29.81513761938118,
        35.99567815137619,
        42.18890995678152,
        48.48203188909957,
        54.7912348203189,
        61.1554379123482,
        67.52870155437913,
        73.96102528701554,
        80.36788961025285,
        86.7501236788961,
        93.28373750123683,
        99.74684283737501,
        106.24242746842832,
        112.7469524242747,
        119.29276746952425,
        125.8260529276747,
        132.34714826052934,
        138.86749347148253,
        145.3901686749347,
        151.99524390168676,
        158.54767995243895,
        165.1723054767996,
        171.77337172305485,
        178.3457477337173,
        184.91381345747732,
        191.56438913813466,
        198.16122564389138,
        204.74434161225642,
        211.42690744341598,
        218.00758426907456,
        224.6006300758427,
        231.2775960063007,
        237.87182277596006,
        244.47961871822773,
        251.18478479618724
    ]
)

regression_adjustment = 3*N//4

x_slice = x[:regression_adjustment]
y_slice = y[:regression_adjustment]
coefficients = np.polyfit(x_slice, y_slice, 1)
slope = coefficients[0]
intercept = coefficients[1]
regression_line = slope * x + intercept
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, regression_line, color='red', label='Linear Regression')

x_nlogn_transform = x * np.log(x)
x_nlogn_transform_slice = x_nlogn_transform[:regression_adjustment]
coefficients_nlogn = np.polyfit(x_nlogn_transform_slice, y_slice, 1)
slope_nlogn = coefficients_nlogn[0]
intercept_nlogn = coefficients_nlogn[1]
regression_line_nlogn = slope_nlogn * x_nlogn_transform + intercept_nlogn
plt.plot(x, regression_line_nlogn, color='blue', label='n log n Regression')

x_nloglogn_transform = x * np.log(np.log(x))
x_nloglogn_transform_slice = x_nloglogn_transform[:regression_adjustment]
coefficients_nloglogn = np.polyfit(x_nloglogn_transform_slice[1:], y_slice[1:], 1)
slope_nloglogn = coefficients_nloglogn[0]
intercept_nloglogn = coefficients_nloglogn[1]
regression_line_nloglogn = slope_nloglogn * x_nloglogn_transform + intercept_nloglogn
plt.plot(x, regression_line_nloglogn, color='green', label='n log log n Regression')

plt.show()
'''
01: 2.0001999999999995
02: 6.668450001999999
03: 12.073026684500022
04: 17.81767073026684
05: 23.775928176707303
06: 29.830467759281763
07: 35.98798830467759
08: 42.200849879883044
09: 48.455392008498805
10: 54.79578455392009
11: 61.13013795784554
12: 67.48893130137958
13: 73.92723488931298
14: 80.39519927234892
15: 86.7903439519927
16: 93.26746790343951
17: 99.77317267467906
18: 106.23070773172671
19: 112.78782230707729
20: 119.2735178782231
21: 125.73344273517877
22: 132.29754733442735
23: 138.85841297547336
24: 145.46037858412978
25: 152.0405546037858
26: 158.60052040554606
27: 165.2106560052041
28: 171.7562421065601
'''