# Python Random Generator
# random — Generate pseudo-random numbers.
# This module implements pseudo-random number generators for various distributions.
# For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate
# a random permutation of a list in-place, and a function for random sampling without replacement.
# On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions.
# For generating distributions of angles, the von Mises distribution is available.
#
# Basic examples:
# 

random()                             # Random float:  0.0 <= x < 1.0

# OUTPUT: 0.37444887175646646

uniform(2.5, 10.0)                   # Random float:  2.5 <= x < 10.0

# OUTPUT: 3.1800146073117523

expovariate(1 / 5)                   # Interval between arrivals averaging 5 seconds

# OUTPUT: 5.148957571865031

randrange(10)                        # Integer from 0 to 9 inclusive

# OUTPUT: 7

randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive

# OUTPUT: 26

choice(['win', 'lose', 'draw'])      # Single random element from a sequence

# OUTPUT: 'draw'

deck = 'ace two three four'.split()
shuffle(deck)                        # Shuffle a list

deck

# OUTPUT: ['four', 'two', 'ace', 'three']

sample([10, 20, 30, 40, 50], k=4)    # Four samples without replacement

# OUTPUT: [40, 10, 50, 30]

#
# Simulations:
# 

# Six roulette wheel spins (weighted sampling with replacement)

choices(['red', 'black', 'green'], [18, 18, 2], k=6)

# OUTPUT: ['red', 'green', 'black', 'black', 'red', 'black']

# Deal 20 cards without replacement from a deck of 52 playing cards
# and determine the proportion of cards with a ten-value
# (a ten, jack, queen, or king).

deck = collections.Counter(tens=16, low_cards=36)

seen = sample(list(deck.elements()), k=20)
seen.count('tens') / 20

# OUTPUT: '0.15'

# Estimate the probability of getting 5 or more heads from 7 spins
# of a biased coin that settles on heads 60% of the time.

trial = lambda: choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5
sum(trial() for i in range(10000)) / 10000

# OUTPUT: '0.4169'

# Probability of the median of 5 samples being in middle two quartiles

trial = lambda : 2500 <= sorted(choices(range(10000), k=5))[2]  < 7500
sum(trial() for i in range(10000)) / 10000

# OUTPUT: '0.7958'
