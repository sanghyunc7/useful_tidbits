# Since Python 3.6, dict.popitem always acts as a LIFO like OrderedDict.popitem(last=True) does.

# But while there is no direct support from dict to make the popitem method pop from the front of the dict, you can simulate the FIFO behavior of OrderedDict.popitem(last=False) such as:

from collections import OrderedDict


d = OrderedDict(a=1, b=2)
k, v = d.popitem(last=False) # k = 'a', v = 1
# by getting the first key of the dict and then popping that key for its value:

# default dict
d = {'a': 1, 'b': 2}
k = next(iter(d)) # k = 'a'
v = d.pop(k) # v = 1
