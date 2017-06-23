import collections
import re
Counter = ([1,2,3,5])
print Counter

print collections.Counter([1,2,3,5])

print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print collections.Counter({'a':2, 'b':3, 'c':1})
print collections.Counter(a=2, b=3, c=1)

c = collections.Counter()
c.update('abdcef')
print c
c.update('abcd')
print c
#using dictionary API
for letter in 'as':
    print (letter,c[letter])
#using elements
c['z'] = 0
print c
print list(c.elements())


#use of most_common method

c = collections.Counter()
with open('Text','rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

for letter, count in c.most_common(3):
    print letter, count


c1 = collections.Counter(['a', 'c', 'a', 'b','q'])
c2 = collections.Counter('alphabet')

print 'C1:', c1
print 'C2:', c2

print '\nCombined counts:'
print c1 + c2

print '\nSubtraction:'
print c1 - c2

print '\nIntersection (taking positive minimums):'
print c1 & c2

print '\nUnion (taking maximums):'
print c1 | c2


