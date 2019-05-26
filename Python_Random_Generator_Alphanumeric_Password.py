# Python Random Generator
# secrets — Generate secure random numbers for managing secrets
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication,
# security tokens, and related secrets.
# In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling
# and simulation, not security or cryptography.
# Random numbers. 
# The secrets module provides access to the most secure source of randomness that your operating system provides.
#
# Generating a ten-character alphanumeric password with at least one lowercase character, at least one uppercase character, and at least three digits:
# 

import string

alphabet = string.ascii_letters + string.digits

while True:
    password = ''.join(choice(alphabet) for i in range(10))

    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)

            and sum(c.isdigit() for c in password) >= 3):

        break

