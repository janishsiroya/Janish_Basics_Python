dict={}
dict['a'] = ['janish1']
dict['c']=['anubhuti']
dict['b']=['binni']
dict['d']=['rahil']
print dict #{'a','janish','b','anubhuti','c','binni','d','rahil'}

for key in dict:
    print key
for key in dict.keys():
    print key
print dict.keys()

print dict.values()

print dict.items()

for key in sorted(dict.keys()):
    print ' the key are', key, dict[key]

for k,v in dict.items():
    print k, '>', v

dict['d']=['rahil123']
print dict['d']

print 'a' in dict

if 'z' in dict:
    print 'True'
else:
    print 'False'

if 'p' in dict:
    print dict ['p']

print dict.get('z')



hash = {}
hash['x'] = 'garfield'
hash['y'] = 100
s = 'MY name is %(x)s age is %(y)d' % hash
print s
  # 'I want 42 copies of garfield'

var = 6

print var

list = {'b':1,'a':2, 'c':4, 'd':3}
print list
print list
print sorted(list)
print list.values()
del list['a']
print list



for list in sorted(list.values()):
    print list


f = open ('C:/Users/janish/PycharmProjects/untitled/src/google-python-exercises/logpuzzle/solution/janish.txt', 'w+')
for line in f:
    print line,
f.write('hello sandeep')
f.close()