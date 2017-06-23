s = 'hello'
print s
print s[1]
#lenght of string s
print len(s)
# to concatenate 2 strings
print s + 'janish' + 'siroya' \
                     'ramesh' \

raw = r'this\t\n and that'
print raw
print len(raw)
#trying to print strings in new line
multi = """It is best.
It is best."""
print multi
#trying to use the lower string method
s = "    Hello Janish   a"
print s #printing before applying lower method on string
a = s.lower()
print a # printing after applying the lower method
print s.upper()
print s.strip()

print s.startswith(' ')
print s.endswith('a ')
print s.find('Hello') # returns the index from where this word has started if it exists in the string
print s.find('hello') # retunrns -1 if the string does not matches
print s.split()
print ' '.join(['Hello', 'Janish', 'a']) # join is the opposite of split, you can join the string by the delimiter specified

##STRING SLICES
z = 'California'
print (z[1:3])
print (z[2:])
print (z[:])
print (z[1:100]) # If length entered is more then it will truncate the string length
print (z[-5])
print (z[:3])

# % operator
text = "%s Janish, What do you select 1, %d, %d ?" % ("Hello",2,3)
print text
# add parens to make the long-line work:
text = ("%s Janish, What do you select 1, %d, %d ?" %
        ("Hello",2,3))
print text

#Unicode literal
ustring = u'A unicode \u018e string \xf1'
ustring
u'A unicode \u018e string \xf1'
print ustring


# this didn't match ..??????
s=ustring.encode('utf-8')
s
'A unicode \xc6\x8e string \xc3\xb1'
t = unicode(s, 'utf-8')
t == ustring

# if else
if value >= 80:
    print "Correct"
else:
    print "Wrong"









