# Python Random Generator
# secrets — Generate secure random numbers for managing secrets
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication,
# security tokens, and related secrets.
# In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling
# and simulation, not security or cryptography.
# Random numbers. 
# The secrets module provides access to the most secure source of randomness that your operating system provides.
#
# Using secrets to manage a basic level of security.
# 
# Generate an eight-character alphanumeric password:
# 

import string

alphabet = string.ascii_letters + string.digits
password = ''.join(choice(alphabet) for i in range(8))
 
#
# However:
# 
# Applications should not store passwords in a recoverable format, whether plain text or encrypted.
# They should be salted and hashed using a cryptographically-strong one-way (irreversible) hash function.
# 
