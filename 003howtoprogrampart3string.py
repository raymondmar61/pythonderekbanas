stringVar = "This is a sample string"
print(stringVar)

numOne = 2
wordOne = "Cats"
print("I have {} {}".format(numOne, wordOne)) #return I have 2 Cats
combineStr = "I have " + str(numOne) + " " + wordOne
print(combineStr)
combineStr += " I think?" #append string quick way
print(combineStr)

stringVar2 = "Just another string"
for cycleler in stringVar2:
	print(cycleler)
print("\nThe first letter in the string is ", stringVar2[0])
#for loop by default creates a new line when cycling through.  Here, let's override a new line
for cycleler in stringVar2:
	print(cycleler, end="")

string3 = """\nThis is a
multiline string"""
print(string3)

#print("He said "I love Python"") error message
print("He said \"I love Python\"")

string4 = "This is some really long strings here"
print(string4)
print(string4.find("really")) #returns 13, the index position for really
print(string4[13:19])
begin = (string4.find("really"))  #returns really
print(begin) #returns 13
print(string4[begin:begin+len("really")]) #returns really
string4 = string4.replace("e","a")
print(string4)

string5 = "                  There is bunch of white space here                 "
print(string5)
string5 = string5.strip() #removed white spaces
print(string5)
string5 = string5.split() #splits the sentence to individual words in a list format
print(string5)
string5 = " ".join(string5) #combines the individual words in a list to a sentence
print(string5)
print(len(string5))

string6 = r"I don't want to \n in other worlds no \n.  Print \n" #r is the escape character.
print(string6)
