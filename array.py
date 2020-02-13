#list:
students=["Leroy","Julius","Collins","Demmy","Gabriel"]
print(students) #outputs all students names
print(students[1]) #outputs the second name 
print(students[0]) #outputs the first name
print(students[2: ]) #outputs students names from second name to the last
students[3]="Phoebe" #replaces the third specified students name with another specified students name.
students[0]="Ivy" #replaces the first specified students name with another specified students name.
print(students)
#loop through the list
for student in students:
    print(student)
#check if an item exist
if "Gabriel" in students:
    print("Gabriel is there")
#methods
print(len(students)) #count number of items
students.append("Brian") #adds another item after the last item on the list
print(students)
students.insert(3,"Zamzam") #adds another item after the third item on the list
print(students)
x=students.pop(1) #method removes the element at the specified position
print(students)
students.remove("Brian") #method removes the first occurrence of the element with the specified value
print(students)
students.reverse() #method reverse the order of the students list
print(students)
students.sort() #method sorts the list ascending by default
print(students)