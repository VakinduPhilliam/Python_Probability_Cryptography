# Python Random Generator
# random — Generate pseudo-random numbers.
# This module implements pseudo-random number generators for various distributions.
# For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate
# a random permutation of a list in-place, and a function for random sampling without replacement.
# On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions.
# For generating distributions of angles, the von Mises distribution is available.
#
# Example of statistical bootstrapping using resampling with replacement to estimate a confidence interval for the mean of a sample of size five:
# 

# http://statistics.about.com/od/Applications/a/Example-Of-Bootstrapping.htm

from statistics import mean
from random import choices

data = 1, 2, 4, 4, 10
means = sorted(mean(choices(data, k=5)) for i in range(20))

print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[1]:.1f} to {means[-2]:.1f}')
