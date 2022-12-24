student = {"Name1":"Wahid" , "Age1":18 , "Gender1":"M" , "Name2":"Ali" , "Age2":20 , "Gender2":"M"}
print(student)
print("number of keys" , student.keys())

print("number of values" , student.values())

print ("student name",student['Name1'])

student["name3"] = "Ahmed"
student["age3"] = 22
student["gender3"] = "M"
print(student)

student.update({'name4': 'maryam', 'age': 23, 'gender': 'F'})

student.pop('name3')
print(student)

del student["Age2"]
print(student)

student.popitem()
print(student)

#print(student.clear())

print(len(student))

print(sorted(student))

print(student.copy())

teachers = {"Name1":"yousaf" , "Age1":37 , "Gender1":"M" , "Name2":"furqan" , "Age2":40 , "Gender2":"M"}
student = {"Name1":"Wahid" , "Age1":18 , "Gender1":"M" , "Name2":"Ali" , "Age2":20 , "Gender2":"M"}
newdict = {}
newdict.update(student)
newdict.update(teachers)
print(newdict)

teachers = {"Name1":"yousaf" , "Age1":37 , "Gender1":"M" , "Name2":"furqan" , "Age2":40 , "Gender2":"M"}
student = {"Name1":"Wahid" , "Age1":18 , "Gender1":"M" , "Name2":"Ali" , "Age2":20 , "Gender2":"M"}
newfile = {}
newfile.copy(teachers)
newfile.update(student)
print("newfile", newfile)
