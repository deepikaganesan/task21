
from collections import namedtuple
movie = namedtuple('movie', 'name hero heroine')
sa = movie('sarkar', 'vijay', 'keerthy')
sa.name
sa.hero
sa.heroine
sa._asdict()

from collections import deque
d = collections.deque([a,b,c])
d.append(e)
print("after appending: ")
print d
d.appendleft(h)
print d
d.pop()
print d
d.popleft()
print d

from collections import counter
s = ['blue', 'red', 'green']
col_count = counter(s)
print col_count
col = ['blue', 'red', 'pink']
for color in col:
    print(color, col_count[color])

from collection import OrderedDict
odict = ordereddict{}
odict['l'] = 2
odict['k'] = 3
odict['j'] = 4
for key, value in odict.items():
    print(key, value)
odict['j'] = 5
odict.pop('j')
odict['j'] = 4
for key, value in odict.items():
    print(key, value)

defaultdict = collection.defaultdict(lambda: 'key is not found')
defaultdict['d'] = 8
defaultdict['e'] = 9
print("value with d is: ", end = " ")
print(defaultdict['d'])
print(defaultdict['m'])




