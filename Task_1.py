# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
def slovar(start, stop):
    slov = [dict(zip(['bin', 'dec', 'hex', 'oct'], [bin(n), n, hex(n), oct(n)])) for n in range(start, stop)]
    return slov
pprint(slovar(0, 16))