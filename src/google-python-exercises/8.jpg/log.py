
from collections import Counter

data = '''\
ashwin programmer india
amith programmer india'''

c = Counter()
for line in data.splitlines():
    c.update(line.split())
print(c)