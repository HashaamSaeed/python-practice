

## x**2 = power of x to 2 
## % remainder 
## order of solving in an equation = Parenthesis ---> Power ---> Multiplication ---> Addition ---> left to right 
## + means addition and  CONCATENATION when 2 strings are involved
## type(x) gives the type of variable like integar etc ...\
## float(x) turns an int into a float
## int() can turn a string '123' into a number and then can be used like numbers

'''
try:
	## anything that could give error will go to except otherwise try will work
except:
	## this will run if try doesnt work and gives error 
## and rest of the code will run on

'''

'''

while True :
	line = input('>')
	if line[0]== 'somehing':
		continue             ## continue ends curent iteration and jumps to top to start a new loop
	if line == 'somehing else' :
	     break

'''	     

# variable = None ## means nothing inside the variable

##  if value is "something"  is , is an operator that is similar to == but is more stronger as 0==0.0 but 0 is 0.0 will be false  
## same for : is not  as above

'''
fruit = bananna 
letter = fruit[2]

'''

'''
s= 'hello world'

print(s[0:3])    >> hell       this is called slicing 
if 0 not entered it assumes begining of string
if 3 not enteredd it assumes end of string
if just : entered then it means everything

'''

'''
fruit = 'banna'
n in fruit  >> True ## can be used in if else statements

fruit.loweer() ## remember strings can have objects that be used so search the documentation for that
fruit.find('na') >> gives 3 since thats the postion of na in banna >> -1 if not found

'''

'''
handle = open('hello.txt') opening files
for line in handle:
	print(line) this prints everything line by line since it recognises the end of the line as a new character

new= handle.read()     will load whole text doc into a string and then you can use slicing to get character by character info like new[0:20]

'''
## for adding new line we use '\n'
## s = hello\nworld  >> print(s) >> hello
##                                  world 
'''


## list comprehension for loop 
"""
## A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
 # The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

list = [<expression> for <item> in <collection> if <expression>] 


customers = [("John", 240000),
             ("Alice", 120000),
             ("Ann", 1100000),
             ("Zach", 44000)]


whales = []
for customer, income in customers:
    if income>1000000:
        whales.append(customer)
print(whales) >>  ['Ann']             

## the above can be written like below 
whales = [x for x,y in customers if y>1000000]

# another example of list comprehension
small_fishes = [x + str(y) for x,y in customers if y<1000000 if x!='John']

"""