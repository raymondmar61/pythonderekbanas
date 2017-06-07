#Derek Banas Python How to Program Pt 1, Pt2, Pt3, Pt4, Pt5, Pt6

"""Multi line comments use three quotes
Multi line comments use three quotes"""

print("Hello, world")
name = input("Enter your name: ")
print("Hi",name)
print("Hi "+name)
age = int(input("Enter your age: "))
print(type(age)) #print <class 'int'>
if (age == 35):
	print("Your the same age as me.")
else:
	print("Your a different age than me.")

x, y, z = 1, 2, 3
print(x, y, z) #print 1 2 3
print(x) #print 1
print(y) #print 2
print(z) #print 3
def boolEx(a, b):
	print(a and b)
	print(a or b)
	print(type(a))
boolEx(True, False) #return False\nTrue\n<class 'bool'>
d = (1 > 2)
print(d) #print False
e = (1 != 2)
print(e) #print True
f = ((2>1) and (3<=3))
print(f) #print True
x=5
y=2
print("x+y=",x+y) #print x+y= 7
print("{} + {} = ".format(x, y), x+y) #print 5 + 2 = 7
print("{} - {} = ".format(x, y), x-y) #print 5 - 2 = 3
print("{} * {} = ".format(x, y), x*y) #print 5 * 2 = 10
print("{} / {} = ".format(x, y), x/y) #print 5 / 2 = 2.5
print("{} % {} = ".format(x, y), x%y) #print 5 % 2 = 1
print("{} ** {} = ".format(x, y), x**y) #print 5 ** 2 = 25
print(float(x)) #print 5.0
print(pow(x,y)) #print 25
z = 100/3
print(round(z,3)) #print 33.333
import math
print(math.ceil(z)) #print 34
print(math.floor(z)) #print 33
z11 = 1.234567891011
print(z11) #print 1.234567891011
z14 = 1.234567891011121314
print(z14) #print 1.2345678910111213
import decimal
z14 = decimal.Decimal("1.234567891011121314")
print(z14) #print 1.234567891011121314
print(type(z14)) #print <class 'decimal.Decimal'>

stringVar = "This is a sample string"
print(stringVar) #print This is a sample string
numOne = 2
wordOne = "Cats"
print("I have {} {}".format(numOne, wordOne)) #print I have 2 Cats
combineString = "I have " + str(numOne) + " " + wordOne
print(combineString) #print I have 2 Cats
combineString+= " I think?"
print(combineString) #print I have 2 Cats I think?
stringVar2 = "Just another string"
for eachstringVar2 in stringVar2:
	print(eachstringVar2)
print("\nThe first letter in the string is", stringVar2[0]) #The first letter in the string is J
for eachstringVar2 in stringVar2:
	print(eachstringVar2, end="") #print Just another string in one line
print("\n")
string3 = """\nThis is a
multiline string"""
print(string3) #print This is a\n multiline string
print("He said \"I love Python\"") #print He said "I love Python"
string4 = "This is some really long strings here"
print(string4.find("really")) #print 13
print(string4[13:19]) #print really
string4 = string4.replace("e","a")
print(string4) #print This is soma raally long strings hara
string5 = "         There is bunch of white space here         "
print(string5) #print          There is bunch of white space here
string5 = string5.strip()
print(string5) #print There is bunch of white space here
string5 = string5.split()
print(string5) #print ['There', 'is', 'bunch', 'of', 'white', 'space', 'here']
string5 = " ".join(string5)
print(string5) #print There is bunch of white space here
string6 = r"I don't want to \n" #the r tells Python string is raw text
print(string6) #print I don't want to \n

tupleEx = ("Derek", 35, "Pittsburgh", "PA")
for eachtupleEx in tupleEx:
	print(eachtupleEx)
print("First element in tuple is",tupleEx[0]) #First element in tuple is Derek
listEx = ["Derek", 35, "Pittsburgh", "PA"]
for eachlistEx in listEx:
	print(eachlistEx)
listEx.append("Joy")
print(listEx) #print ['Derek', 35, 'Pittsburgh', 'PA', 'Joy']
print(listEx[4]) #print Joy
listEx.remove("Joy")
print(listEx) #print ['Derek', 35, 'Pittsburgh', 'PA']
listEx.remove(listEx[3])
print(listEx) #print ['Derek', 35, 'Pittsburgh']
listEx.insert(2, "PA")
print(listEx) #print ['Derek', 35, 'PA', 'Pittsburgh']
listEx2 = ["f","e","c","d"]
listEx2.sort() #FYI .sort() can't sort a list string and integers
print(listEx2) #print ['c', 'd', 'e', 'f']
listEx3 = [["a","b","c"],["d","e","f"],["g","h","i"]]
print(listEx3)
print(listEx3[2][1]) #prints h
dictEx = {"Age":35, "Height":"6'3", "Weight": 169}
print(dictEx) #print {'Weight': 169, 'Height': "6'3", 'Age': 35}
print(dictEx.get("Height")) #print 6'3
print(dictEx.items()) #print dict_items([('Age', 35), ('Weight', 169), ('Height', "6'3")])
print(dictEx.values()) #print dict_values(["6'3", 35, 169])
dictEx.pop("Height")
print(dictEx) #print {'Weight': 169, 'Age': 35}
a, b = 1, 11
while a < b:
	print(a)
	a += 1
for x in [1, 2 ,3, 4]:
	print(x)
listCycle = [1, 2, 3, 4]
for x in listCycle:
	print(x)
listCycle[:] = range(1,201)
for i in listCycle : print(i)
for i in listCycle:
	if (i % 2) == 0:
		continue
	elif (i == 101):
		break
	else:
		print(i)

#Comment Part 5 to learn Part 6
# f = open("studentgrades.txt")
# for eachline in f:
# 	print(eachline, end = "")
# f.close()
# print("\n")
# bestGrade = 0
# f2 = open("studentgrades.txt")
# for eachline in f2:
# 	name, grade = eachline.split()
# 	print(name, grade)	
# 	if int(grade) > bestGrade:
# 		bestGrade = int(grade)
# 		bestStudent = name
# print("\nBest Grade",bestGrade) #print Best Grade 99
# print("Best Student",bestStudent) #print Best Student John
# f2.close()
# bestStudent = {}
# f3 = open("studentgrades.txt")
# for eachline in f3:
# 	name, grade = eachline.split()
# 	bestStudent[grade] = name
# f3.close()
# print(bestStudent) #print {'67': 'Mark', '89': 'Suzy', '99': 'John', '76': 'Paul', '73': 'Jim', '90': 'Zac', '93': 'Jennifer'}
# bestStudentStr = ""
# for eachline in sorted(bestStudent.keys(), reverse=True):
# 	print(bestStudent[eachline] + "scored a" + eachline)
# 	bestStudentStr += bestStudent[eachline] + " scored a " + eachline + "\n"
# 	print(bestStudentStr)
# bestStudentStr = "\n The Best Students Ranked\n\n" + bestStudentStr
# outToFile = open("studentrank.txt", mode="w", encoding="utf-8") #mode="a" is append.  If there is an existing file and mode="w", then existing file is overwritten.
# outToFile.write(bestStudentStr)
# outToFile.close()
# print("Finished update")

class Animal:
	def __init__(self, name = "default is No Name"):
		self._name = name
	def set_name(self, name = "default is No Name"):
		self._name = name
	def get_name(self):
		return self._name
	def noise(self):
		print("Errrrr")
	def move(self):
		print("Moving Forward")
	def eat(self):
		print("Crunch, Crunch")
dog = Animal("Puppy")
dog.noise()
dog.move()
dog.eat()
print(dog.get_name()) #print puppy
print(dog.set_name("Jake")) #run set_name to change name from Puppy to Jake
print(dog.get_name()) #print Jake
print("\n")

class Animalkeywordarguments:
	def __init__(self, **kwargs):
		self._attributes = kwargs
	def set_attributes(self, key, value):
		self._attributes[key] = value
	def get_attributes(self, key):
		return self._attributes.get(key, None)
	def noise(self):
		print("Errrrr")
	def move(self):
		print("Moving Forward")
	def eat(self):
		print("Crunch, Crunch")
dog = Animalkeywordarguments(name = "Puppy")
dog.noise()
dog.move()
dog.eat()
print(dog.get_attributes("name")) #print puppy
dog.set_attributes("Feet",3)
print(dog.get_attributes("Feet")) #print 3, from set attribute Feet = 3.  Like create a new attribute Feet.  Set attribute Feet equal to 3.
print("\n")

class Doginheritance(Animalkeywordarguments):
	def noise(self):
		print("Woof, Woof")
		super().noise()  #reference def noise function in parent class Animalkeywordarguments
jake = Doginheritance()
print(jake.noise()) #print Woof, Woof\nErrrrr
print(jake.move()) #print Moving Forward
print("\n")

class Catpolymorphism(Animal):
	def noise(self):
		print("Meow")
def talkToMe(Animal):
	Animal.noise()
	Animal.eat()
jake = Doginheritance()
sophie = Catpolymorphism()
talkToMe(sophie) #return Meow\nCrunch, Crunch
