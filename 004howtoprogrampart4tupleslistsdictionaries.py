#immutable integer
intEx = 1
print(intEx)
print(id(intEx))
intEx = 2
print(intEx)
print(id(intEx)) #id for intEx changed

#mutable list
listEx = ["Derek"]
print(listEx)
print(id(listEx))
listEx.append("Cat")
print(listEx)
print(id(listEx)) #id for listEx unchanged

#tuple
#for loop by default creates a new line when cycling through.  Here, let's override a new line by creating a space after each item in tuple tupleEx
tupleEx = ("Derek",35,"Pittsburgh","PA")
for i in tupleEx:
	print(i, end=" ")

print("\nFirst element in tuple is " +tupleEx[0])

#list
listEx = ["Derek",35,"Pittsburgh","PA"]
for i in listEx:
	print(i)
listEx.append("Joy")
print(listEx)
print(listEx[4])
listEx.remove("Joy")
print(listEx)
listEx.insert(2, "USA")
print(listEx)

listEx2 = ["f","e","c","d"]
print(listEx2)
# print(listEx2.sort()) can't do
listEx2.sort()
print(listEx2)
# print(listEx2.reverse()) can't do
listEx2.reverse()
print(listEx2)

listEx3 = [["a","b","c"],["d","e","f"],["g","h","i"]]
print(listEx3)
print(listEx3[2][1]) #prints h

#dictionaries.  They're immutable
dictEx = {"Age":35, "Height":"6'3\"", "Weight":169}
print(dictEx)
print(dictEx.get("Height")) #prints 6'3"
print(dictEx.items()) #prints dict_items([('Height', '6\'3"'), ('Weight', 169), ('Age', 35)])
print(dictEx.values()) #prints dict_values(['6\'3"', 35, 169])
dictEx.pop("Height")
print(dictEx) #prints {'Age': 35, 'Weight': 169}

#while loop
a, b = 1, 11
while a < b:
	if a % 2 == 0:
		print(a)
		a += 1
		continue
	a += 1

string3 = """\nThis is a
multiline string"""
print(string3)