#list*********************************************************************
shoplist = ['apple','banana','flower','carrot']
shop = ['ha']
print shop
print shoplist
print len(shoplist)
shoplist.append('berry')
print shoplist
print 'the items are'
for i in shoplist:
    print i
a = shoplist[0]
del shoplist[0]
print shoplist
print a
#tuple***********************************************************************
zoo = ('lion','tiger','cat','dog','rat')
print zoo
print len(zoo)
new_zoo = ('spider','horse', zoo)
print new_zoo
print (len(new_zoo)-1 + len(new_zoo[2]))
zoo1 = ('janish',)
print zoo1
#Dictionary*******************************************************************
ab = {'1':'janish','2':'john','3':'rahul'}
print ab
print ab['2']
ab['4'] = 'jessica'
print ab
del ab['1']
print ab
print ('there are {} contacts in dict'.format(len(ab)))

for a,b in ab.items():
    print a,b
    print ('contact {} at {}'.format(a,b))
if '1' in ab:
    print 'found'
else:
    print 'not found'
#Sequence*************************************************************************
#slicing

a = 'janish'
print a[1:5]
print a[::2]
print a[-3:-1]
b = ['jan','feb','march']
print b[1:2]

#Sets************************************************************
s = set(['a','b','c'])
print s
print 'a' in s
new_s = s.copy()
print new_s
new_s.add('d')
print new_s
print s & new_s
print new_s.issuperset(s)
print s.issubset(new_s)

#References***************************************************************
li = ['j','h','k','l']
a = li
print a
print li
del a[1]
print a
print li

b = li[:]
print b
del b [2]
print b
print li


