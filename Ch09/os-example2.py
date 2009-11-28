import os

x = os.urandom(25)
y = x
z = os.urandom(25)

print "Does x = y? ", x==y
print "Does x == z? ", x==z
print "x = ", x