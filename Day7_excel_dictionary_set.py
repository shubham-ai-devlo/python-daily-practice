# Day 7 : Excel Data Analysis using python (Dictionary + set)
# Author: Shubham

print("---- Raw Excel Data (Simulated in Python)----")

data = [
    ("Shubham", 85),
    ("Amit", 78),
    ("Diksha", 90),
    ("Ritika", 88),
    ("Suman", 65),
    ("Amit", 78)  # duplicate row 
    #(Excel duplicate)
]

for row in data:
    print(row)

# Renove duplicates like Excel
print("\n---- Removing Duplicates ----")
unique_data = set(data)
 
# Create dictionary
student_marks = {}
for name, marks in unique_data:
    student_marks[name] = marks

# Final Analysis
print("\n---- Final Analysis Report----")
print("Total Students:",
    len(student_marks)) 

highest = max(student_marks.values())
lowest = min(student_marks.values())
average = sum(student_marks.values()) 
len(student_marks)

topper = max(student_marks,
    key=student_marks.get)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", round(average,2))
print("Topper:", topper)
print("Topper Marks:",
    student_marks[topper])