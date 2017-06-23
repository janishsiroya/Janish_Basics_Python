import re
i = [1,2,3,4]
for a in i:
    print i[1]
d = [12,2,3,4,]
v = [a*a*a*a for a in d]
print v


string = "hello:kl% janish"
match= re.search('hello:\w\w\W', string)
if match:
    print 'found', match.group()
else:
    print 'not found'

match = re.search(r'ia', 'piaiaiaiaiaiaiaiaiag')
if match:
    print 'found', match.group()
else:
    print 'not found'

#HOW TO FIND EMAIL ADDRESS IN STRING
str = ' hello janish your email id is janish@yahoo.com'
match = re.search('\w+@\w+', str)
if match:
    print 'found',match.group()
match1 = re.search(r'([\w.]+)@([\w.]+)', str)
if match1:
    print 'found', match1.group()
    print 'found', match1.group(1)








