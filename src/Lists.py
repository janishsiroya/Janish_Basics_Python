a = ['a','b','c']
print a
print a[2]
print a[-2]

b= a
print b
#MERGE*************** 2 STRINGS
c = ['x','y','z'] + ['m','n','p']
print c

print a + c

# USE OF FOR********************
a = [1,2,3]
sum = 0
for num in a:
    sum += num
    print sum #addition will be printed as in loops. each single addition. BECAUSE OF THE SPACE AND NOT BEING IN THE FOR LOOP LINE
print sum
#USE OF IF************************
b = ['1','2','3']
if 4 in b:
        print 'Yes'
else:
        print 'Fake'

s = ['hi', 'bye']
for ch in s:
    print ch

#USE OF KEYWORD RANGE********
for i in range(50):
    print i

for y in xrange(10):
    print y

#USE OF WHILE LOOP*******************************
p = 'elephant'
i=1
while i<len(p):
    print p[i]
    i=i+2

#LIST METHODS***********************
list = ['a','x','c']
list.append('d')
print list
list.pop(1)
print list
list.extend (['b','y'])
print list
list.reverse()
print list
list.sort()
print list


#LIST BUILD UP*******
list = []
list.append('1')
print list
list. extend(['2','3'])
print list

print list[1:-1]
list[0:1] = '9'
print list



