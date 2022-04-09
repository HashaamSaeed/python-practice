
## dir(object) gives the attributes we can use on the type of data structure
'''
list is represented by [] which is basically an array
we cant change a string but we can insert and change a list
if A and B are lists then A+B = a list made from concatenation of A and B
check list documentation online
'''

'''
stuff = list()
stuff.append('book') ## first element
stuff.append('96') ## element added after last element

book in stuff  >> True or False    ## a way to check an item in a list

stuff.sort() ## will sort alphabetically or numerically
sum(list) , len(list) etc etc check documentation for more imp func
'''


## Dictionary
'''
Dictionary is a bag of values that each has their own label, things are indexed by label 
Key:value pairs   
purse = dict()
purse['money'] = 12   ## money is the label for the value
purse['candy'] = 3
print(purse) >> {'money':12,'candy':3}
purse['candy'] = purse['candy'] + 2   ## we can use dicts to keep a count or track of a variable 
print(purse)>>  {'money':12,'candy': 5}
print(purse['candy']) >> 12
hello = {'money':12,'candy':34}  ## another way to make a dict

'cnady' in purse   ## a way to check key if its there or not  >> gives False or True

purse.get(name,0)   ## get is a function that adds a new key and default value when looping in for loops
counts = dict()

## below example can be used to count words in a text
names = ['shit', 'hello', etccccc]
print(list(names)) >>['shit','hello',etccccc]
print(names.keys()) >> same as above
print(names.values()) >> [0,0,etccc]

for name in names:
	counts[name] =counts.get(name,0) + 1
print(counts)

print(names.items()) >> [('shit',0),('hello',0), etc] ## tuple form
for aa,bb in names.items():
	print(aa,bb) >> shit 0     next line  hello 0    next line    etccc 

'''

## Tuples
'''
z= (5,4,3)  ## tuples are encapsulated in () and we cant change its components once theyre injected 
## they cannot be appended , sorted or can do things like lists/arrays
t= tuple()
print(dir(t))
(x,y)=(4,'hello') >> assigns x=4 and y= hello 

(0,1,2) < (0,1,1)  >> False   ## we can use operators with tuples BUT remmember it will only compare the first values in both tuples
                              ## therefore when it cant compare 0<) it goes to 1<1 and so on until it actually can and then returns the response on which the operator works


c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
 tmp.append( (v, k) )      ## we make the value first and key second  ## this is an array of tuples
 print(tmp)
[(10, 'a'), (22, 'c'), (1, 'b')]
tmp = sorted(tmp, reverse=True)
print(tmp)
[(22, 'c'), (10, 'a'), (1, 'b')]

## below is the shorter version of the above program
c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )
[(1, 'b'), (10, 'a'), (22, 'c')]


'''


## Regular expression / regex

'''
## check for the regular expression documentation

import re



$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times (non-greedy)   ## non greedy means that it searches just forward and not both ways
+        Repeats a character one or more times
+?       Repeats a character one or more times (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end


line = line.rstrip()

if re.search('^From:', line) :  ## its equivalent to using line.startswith('from:')


re.search() returns a True/False depending on whether the string matches  the regular expression

If we actually want the matching strings to be extracted, we use re.findall()


x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)                ## [0-9]+  means One or more digits
print(y)
['2', '19', '42']




'''




"""
x, y = 10, 20


## Here we’re setting x to 10 and y to 20.
 # What’s happening at a lower level is that we’re creating a tuple of 10, 20 and then looping over that tuple and taking each of the 
 # two items we get from looping and assigning them to x and y in order.


Parenthesis are optional around tuples in Python and they’re also optional in multiple assignment (which uses a tuple-like syntax). All of these are equivalent:

x, y = 10, 20 
x, y = (10, 20)
(x, y) = 10, 20
(x, y) = (10, 20)




x, y = 'hi'
print(x) >> 'h'
print(y) >> 'i'


point = 10, 20, 30
x, y, z = point
print(x, y, z) >> 10 20 30


"""