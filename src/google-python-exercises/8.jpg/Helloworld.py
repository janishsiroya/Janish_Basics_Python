class Hello:
    def comparison(self,a,b):
        if a > b:
            print 'a is greater'
        elif a == b:
            print a, 'a and b are equal', b
        else:
            print 'b is greater than a'
p = Hello()
p.comparison(5,6) #directly pass variable literals

#pass variable as arguments
x = 8
y = 8
p.comparison(x,y)
# hello world basic program
def helloworld():
        print 'hello world'
helloworld()
#local variables
x = 5000
def func(x):
    print ('x is', x)
    x = 2
    print ('x is', x)
func(x)
print x
#global variable
def function():
    print 'before defining p as global'
    global p
    p = 10
    print 'after defining p as global',p
function()
print 'p outside the function',p
#default argument values

def default(message,time=1):
    print message*time
default('1 message')
a = 'Hello janish'
b = 2
default(a,b)
#keyword arguments
def keyword(a,b=0,c=100):
    print a,b,c
keyword(3,4,5)
keyword(a=5,b=6)
keyword(9,b=8)

#varargs paramteres
def varargs(a=5,*numbers,**phonebook):
    print 'a =', a
    for single_item in numbers:
        print 'numbers = ', single_item #tuple
    for first,second in phonebook.items():
        print first,second #dictionary
print (varargs(10,1,2,3,john = 2, jack = 3))

#return statement
def return1(a,b):
    if a>b:
        return a
    elif a ==b:
        return ' a = b'
    else:
        return b
print return1(4,4)

#docstrings

def docstringss(x,y):
    '''Converting them into.

    integers.'''
    x = int(x)
    y = int(y)

    if x>y:
        print x, 'is greater'
    else:
        print y, 'is greater'
docstringss(3,4)
print(docstringss.__doc__)








