#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split()[5] + " " +str.split()[6][0:-1] + " " + str[:6] + " " + str.split()[-4]
print(str)
