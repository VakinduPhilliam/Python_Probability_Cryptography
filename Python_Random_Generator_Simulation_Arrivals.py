# Python Random Generator
# random — Generate pseudo-random numbers.
# This module implements pseudo-random number generators for various distributions.
# For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate
# a random permutation of a list in-place, and a function for random sampling without replacement.
# On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions.
# For generating distributions of angles, the von Mises distribution is available.
#
# Simulation of arrival times and service deliveries in a single server queue:
# 

from random import expovariate, gauss
from statistics import mean, median, stdev

average_arrival_interval = 5.6
average_service_time = 5.0

stdev_service_time = 0.5

num_waiting = 0
arrivals = []

starts = []
arrival = service_end = 0.0

for i in range(20000):

    if arrival <= service_end:
        num_waiting += 1

        arrival += expovariate(1.0 / average_arrival_interval)
        arrivals.append(arrival)

    else:
        num_waiting -= 1

        service_start = service_end if num_waiting else arrival
        service_time = gauss(average_service_time, stdev_service_time)

        service_end = service_start + service_time
        starts.append(service_start)

waits = [start - arrival for arrival, start in zip(arrivals, starts)]

print(f'Mean wait: {mean(waits):.1f}.  Stdev wait: {stdev(waits):.1f}.')
print(f'Median wait: {median(waits):.1f}.  Max wait: {max(waits):.1f}.')
