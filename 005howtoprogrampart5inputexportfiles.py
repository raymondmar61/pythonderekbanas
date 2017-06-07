f = open("studentgrades.txt")
for eachstudent in f:
	print(eachstudent, end ="")
print("\n")
f.close()

f = open("studentgrades.txt")
bestGrade = 0
for eachstudent2 in f:
	name, grade = eachstudent2.split()
	if int(grade) > bestGrade:
		bestGrade = int(grade)
		bestStudent = name
print("\nBest Grade ", bestGrade)
print("Best Student ", bestStudent)
f.close()

bestStudent2 = {}
f = open("studentgrades.txt")
for eachstudent3 in f:
	name, grade = eachstudent3.split()
	bestStudent2[grade] = name	
f.close()
print(bestStudent2)
bestStudentStr = ""
for i in sorted(bestStudent2.keys(), reverse=True):
	print(bestStudent2[i] + " scored a " + i)
	bestStudentStr += bestStudent2[i] + " scored a " + i + "\n"
	print(bestStudentStr)
bestStudentStr = "\n The Best Students Ranked\n\n" + bestStudentStr
print(bestStudentStr)
outToFile = open("studentrank.txt", mode="w", encoding="utf-8") #mode="a" is append.  If there is an existing file and mode="w", then existing file is overwritten.
outToFile.write(bestStudentStr)
outToFile.close()
print("Finished update")