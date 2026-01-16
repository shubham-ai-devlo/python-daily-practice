# ---------------------
#Data Types 
# --------------------- 
name ="shubham"  
age = 21
height = 5.11
learning_python = True 

print("Name:",name)
print("Age:",age)
print("Height:",height)
print("Learning python:",learning_python )

print(type(name))
print(type(age))
print(type(height))
print(type(learning_python))

#--------------------------
#Type conversion
#--------------------------

user_age = input("Enter your age: ")
print("Before conversion:", user_age,type
(user_age))

user_age =int(user_age)
print("After conversion:",user_age,type(user_age))

#-------------------------
#Operators in Python
#-------------------------

x= 50
y = 5

# Arithmetic Operators
print("Addition:", x + y)
print("Subtractoin:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Moduls:", x % y)

# Comperison Operators
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)

# Logical Operators
print("x > 5 and y < 5:", x > 5 and y < 5)
print("x > 5 or y > 5:", x > 5 or y > 5)
print("not(x > 5):", not x > 5)