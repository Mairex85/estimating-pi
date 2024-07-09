import random
import math
import timeit
#import numpy as np
#passos de 100 mil em 100 mil

#INTERVAL = int(input("Quantas simulações deseja fazer? "))  # número de simulações

start = 10**6
step = 10**8
end = 10**9

for i in range(start, end + 1, step):
    circle_points = 0
    square_points = 0
    start = timeit.default_timer()
    # Total Random numbers generated= possible x
    # values* possible y values
    for j in range(i):
        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is -1 to 1
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        # Distance between (x, y) from the origin
        origin_dist = rand_x**2 + rand_y**2

        # Checking if (x, y) lies inside the circle
        if origin_dist <= 1:
        	circle_points += 1

        square_points = i   

    pi = 4 * circle_points / square_points
    stop = timeit.default_timer()
    print(f"{i} {pi} {abs(math.pi - pi)} {stop - start}")
