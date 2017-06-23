print "hello janish"
a = 'janish'
str = a
print a

a = 'siroya'
print a
print a[1:4]
print a[1] #to print the first character in the string

print len(a) #length of string

raw = r'this\t\n and that'
print raw

multi = """                  hello.             ss
janish                         """
print multi
print multi.upper()
print multi.strip()
m = 'hello sir my name is janish'
print m.isalpha(),m.isdigit()
print m.find('janis')
print m
print m.startswith('hello')



x = '-'
print x.join(['a','b','c'])

text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print text

text = ("%d little pigs come out or I'll %s and %s and %s" %
    (3, 'huff', 'puff', 'blow down'))

print text

x = "helloalpha"
print x.isalpha() # to check if string is alpha characters only

y = '4567890'
print y.isdigit() # to check if string is digit only

d = "hello anubhuti"
print d.split()
print '     '.join(['hello', 'Janish', ' hello'])
