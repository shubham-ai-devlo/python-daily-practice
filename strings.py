print("----- Creating Strings -----")
name = "Shubham"
Course = "Python + AI"
print(name)
print(Course)

print("\n----- String Indexing -----")
text = "mangojuice"
print(text[0])   #First character
print(text[1])   #Third character
print(text[-1])  #Last character

print("\n----- String Slicing -----")
word = "Programminglanguage"
print(word[0:6])
print(word[3:8])
print(word[:4])
print(word[4:])

print("\n----- Common Strin Methods -----")
msg = "  python learning  "
print(msg.upper())
print(msg.lower())
print(msg.strip())
print(msg.replace("python", "AI"))
print(len(msg))

print("\n----- String Formatting -----")
age = 21
print(f"My name is {name} and my age is {age}")
language = "Pyhton"
field = "AI"
print("I am learning{} for {}". format(language, field))