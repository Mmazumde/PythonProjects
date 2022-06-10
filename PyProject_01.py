# This is a sample Python script.
# Python program to generate random password.
# The random module in Python.
import random

# Asked for user input for the length of the password.
passlen = int(input("enter the length of password"))

# Declare a string of different characters.
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# a random sample of the string of a length given by the user.
p = "".join(random.sample(s,passlen ))

print(p)


