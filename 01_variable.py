# ============================================
# PYTHON VARIABLES – FULL EXPLANATION PROGRAM
# ============================================

print("PYTHON VARIABLES EXPLAINED\n")

# --------------------------------------------
# 1. WHAT IS A VARIABLE?
# --------------------------------------------
# A variable is a container that stores data/value in memory

age = 19
name = "Neel"
height = 5.8
is_student = True

print("Age:", age)
print("Name:", name)
print("Height:", height)
print("Is Student:", is_student)

print("\n----------------------------------\n")

# --------------------------------------------
# 2. VARIABLE NAMING RULES
# --------------------------------------------
# ✔ Can contain letters, numbers, underscore
# ✔ Must start with letter or underscore
# ✖ Cannot start with number
# ✖ Cannot use keywords

valid_variable = 10
_valid = 20
name1 = "Python"

print("Valid variable examples:")
print(valid_variable, _valid, name1)

print("\n----------------------------------\n")

# --------------------------------------------
# 3. MULTIPLE VARIABLE ASSIGNMENT
# --------------------------------------------
print("3. MULTIPLE VARIABLE ASSIGNMENT")

a = b = c = 50
print("a =", a, "b =", b, "c =", c)

x, y, z = 10, 20, 30
print("x =", x, "y =", y, "z =", z)

print("\n----------------------------------\n")

# --------------------------------------------
# 4. DYNAMIC TYPING (Python Feature)
# --------------------------------------------
print("4. DYNAMIC TYPING")

var = 10
print("var =", var, "Type:", type(var))

var = "Hello Python"
print("var =", var, "Type:", type(var))

var = 3.14
print("var =", var, "Type:", type(var))

print("\n----------------------------------\n")

# --------------------------------------------
# 5. VARIABLE TYPE CHECKING
# --------------------------------------------
print("5. VARIABLE TYPE CHECKING")

num = 100
text = "Python"
price = 99.99

print("Type of num:", type(num))
print("Type of text:", type(text))
print("Type of price:", type(price))

print("\n----------------------------------\n")

# --------------------------------------------
# 6. VARIABLE INPUT FROM USER
# --------------------------------------------
print("6. USER INPUT VARIABLES")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)
print("Your age is", user_age)

print("\n----------------------------------\n")

# --------------------------------------------
# 7. CONSTANT STYLE VARIABLES
# --------------------------------------------
# Python does not have real constants
# We use CAPITAL letters to indicate constants

PI = 3.14159
GRAVITY = 9.8

print("PI:", PI)
print("GRAVITY:", GRAVITY)

print("\n----------------------------------\n")

# --------------------------------------------
# 8. DELETE VARIABLE
# --------------------------------------------
print("8. DELETE VARIABLE")

temp = 123
print("Before delete:", temp)

del temp
# print(temp)  # This will give error if uncommented

print("Variable deleted successfully")

print("\n----------------------------------\n")

print("✅ ALL PYTHON VARIABLE CONCEPTS EXPLAINED")
