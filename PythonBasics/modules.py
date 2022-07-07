#Python modules
import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=70))

from datetime import timedelta

print(timedelta(minutes=80))

#Own Module
import fmath
fmath.add(1,3)
fmath.add(5,2)

from fmath import add, substract
substract(2,3)
add(5,3)
