from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {"bill": "wide orange", "tail": "long"}
duck2 = Duck(**parts)
print(duck2)