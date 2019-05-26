# Python Random Generator
# secrets — Generate secure random numbers for managing secrets
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication,
# security tokens, and related secrets.
# In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling
# and simulation, not security or cryptography.
# Random numbers. 
# The secrets module provides access to the most secure source of randomness that your operating system provides.
#
# Generate a hard-to-guess temporary URL containing a security token suitable for password recovery applications:
# 

url = 'https://mydomain.com/reset=' + token_urlsafe()
