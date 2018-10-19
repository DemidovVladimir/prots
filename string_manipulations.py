from datetime import datetime
import sys

gen_exp = (x ** 2 for x in range(10) if x % 2 == 0) 
list_done = [x ** 2 for x in range(10) if x % 2 == 0]

print(sys.getsizeof(gen_exp))

print(sys.getsizeof(list_done))

class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

print('{0!s} {0!r}'.format(Data()))

print('{:>10}'.format('test'))

print('{:.5}'.format('xylophone'))

print('{0:10.5}'.format('xylophone'))

print('{:4d}'.format(42))

print('{:07.2f}'.format(3.141592653589793))

print('{:+d}'.format(42))

print('{:=+5d}'.format(23))

data = {'first': 'Hodor', 'last': 'Hodor!'}

print('{first} {last}'.format(**data))

person = {'first': 'Jean-Luc', 'last': 'Picard'}

print('{p[first]} {p[last]}'.format(p=person))

class Plant(object):
    type = 'tree'

print('{p.type}'.format(p=Plant()))

print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))

print('{:{align}{width}}'.format('test', align='^', width='10'))

print('{0:.{prec}} = {1:.{prec}f}'.format('Gibberish', 2.7182, prec=3))

print('{:{dfmt} {tfmt}}'.format(datetime(2001, 2, 3, 4, 5), dfmt='%Y-%m-%d', tfmt='%H:%M'))

class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'

print('{:open-the-pod-bay-doors}'.format(HAL9000()))