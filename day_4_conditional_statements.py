marks = int(input("Enter your marks: "))     #---------- CODE --------#
 
if marks >= 50:
    print("You are passed")
else:
    print("You are failed")


if marks >= 95:
    print("Grade: A")
elif marks >= 85:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


marks_list = [65, 85, 92, 7575]
print("\nStudent marks:", marks_list)

new_marks = int(input("Enter new student marks: "))
marks_list.append(new_marks)


print("Updated marks list:", marks_list)
print("Higest marks:", max(marks_list))
print("Lowest maks:", min(marks_list))
marks_list.sort()


#-------- OUTPUT -------#

PS C:\Users\kumar> & C:/Users/kumar/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/kumar/test/conditional statement"
Enter your marks: 99
You are passed
Grade: A

Student marks: [65, 85, 92, 7575]
Enter new student marks: 90
Updated marks list: [65, 85, 92, 7575, 90]
Higest marks: 7575
Lowest maks: 65
sorted marks: [65, 85, 90, 92, 7575]
PS C:\Users\kumar> 
print("sorted marks:", marks_list)
