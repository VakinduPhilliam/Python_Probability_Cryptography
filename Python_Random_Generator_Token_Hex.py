# Python Random Generator
# secrets — Generate secure random numbers for managing secrets
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication,
# security tokens, and related secrets.
# In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling
# and simulation, not security or cryptography.
# Random numbers. 
# The secrets module provides access to the most secure source of randomness that your operating system provides.
#
# Generating tokens: 
# The secrets module provides functions for generating secure tokens, suitable for applications such as password resets, hard-to-guess URLs, and similar.
#
# secrets.token_hex([nbytes=None]). 
# Return a random text string, in hexadecimal. The string has nbytes random bytes, each byte converted to two hex digits.
# If nbytes is None or not supplied, a reasonable default is used.
# 

token_hex(16)  

# OUTPUT: 'f9bf78b9a18ce6d46a0cd2b0b86df9da'
