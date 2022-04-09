
# Class - a template   - Dog
# Method or Message - A defined capability of a class - bark() 
# Field or attribute- A bit of data in a class - length
# Object or Instance - A particular instance of a class -  max # name of dog

"""

class PartyAnimal:
    x = 0

    def party(self) :
      self.x = self.x + 1
      print("So far",self.x)


an = PartyAnimal()    # Constructing a PartyAnimal object and store it in an
an.party()   >> So far 1        ## PartyAnimal.party(an)  ## basically an is passed in party everytime because we are using self in the party func ## 
                                ## Self is an alias for an meaning self is the object passing itself into the func/method 
an.party()   >> So far 2
an.party()   >> So far 3

"""

"""

y = list()
type(y)  >>    <class 'list'>
dir(y)   >>    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', … '__setitem__',
                '__setslice__', '__str__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


## The dir() command lists capabilities   ## it gives the unc/method and the objects in the classs
## Ignore the ones with underscores - these are used by Python itself
## The rest are real operations that the object can perform
## It is like type() - it tells us something *about* a variable



"""



"""

class PartyAnimal:
   x = 0

   def __init__(self):              #The constructor is typically used to set up variables. basically to initialise ## __init__ is the constructor
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):              ## __del__ is the destructor    although seldom used
     print('I am destructed', self.x)

an = PartyAnimal()      >> I am constructed    ## this line is caused by an = PartyAnimal()
an.party()              >> So far 1
an.party()              >> So far 2
                          I am destructed 2
an = 42
print('an contains',an)   >> an contains 42

"""


"""

class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")  ##  >> Sally constructed
j = PartyAnimal("Jim")    ##  >> Jim constructed  

s.party()                 ##  >> Sally party count 1
j.party()                ##   >> Jim party count 1
s.party()                  ## >> Sally party count 2


## inheritance
class FootballFan(PartyAnimal):   ## FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more.
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()     ## inherited from PartyAnimal
      print(self.name,"points",self.points)


j = FootballFan("Jim")  ## >> Jim constructed  ## over here j now has x,name,points passed to it for it to be used by the constructor in PartyAnimal
j.party()        ## >> Jim party count 1
j.touchdown()  ## >> Jim party count 2
               ##    Jim points 7




"""



