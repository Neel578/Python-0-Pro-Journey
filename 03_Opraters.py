# ============================================
# PYTHON OPERATORS – FULL EXPLANATION PROGRAM
# ============================================

print("PYTHON OPERATORS EXPLAINED\n")

# --------------------------------------------
# 1. ARITHMETIC OPERATORS
# --------------------------------------------
print("1. ARITHMETIC OPERATORS")
a = 10
b = 3

print("a =", a, "b =", b)
print("Addition (+):", a + b)        # 10 + 3 = 13
print("Subtraction (-):", a - b)     # 10 - 3 = 7
print("Multiplication (*):", a * b)  # 10 * 3 = 30
print("Division (/):", a / b)        # 10 / 3 = 3.33
print("Floor Division (//):", a // b)# 10 // 3 = 3
print("Modulus (%):", a % b)         # Remainder = 1
print("Power (**):", a ** b)         # 10³ = 1000

print("\n----------------------------------\n")

# --------------------------------------------
# 2. COMPARISON (RELATIONAL) OPERATORS
# --------------------------------------------
print("2. COMPARISON OPERATORS")

print("a == b:", a == b)   # Equal to
print("a != b:", a != b)   # Not equal to
print("a > b :", a > b)    # Greater than
print("a < b :", a < b)    # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to

print("\n----------------------------------\n")

# --------------------------------------------
# 3. LOGICAL OPERATORS
# --------------------------------------------
print("3. LOGICAL OPERATORS")

x = True
y = False

print("x =", x, "y =", y)
print("AND (x and y):", x and y)  # True if both True
print("OR  (x or y):", x or y)    # True if any one True
print("NOT (not x):", not x)      # Reverse the result

print("\n----------------------------------\n")

# --------------------------------------------
# 4. ASSIGNMENT OPERATORS
# --------------------------------------------
print("4. ASSIGNMENT OPERATORS")

c = 5
print("Initial c =", c)

c += 3   # c = c + 3
print("c += 3 :", c)

c -= 2   # c = c - 2
print("c -= 2 :", c)

c *= 2   # c = c * 2
print("c *= 2 :", c)

c /= 2   # c = c / 2
print("c /= 2 :", c)

c %= 2   # c = c % 2
print("c %= 2 :", c)

print("\n----------------------------------\n")

# --------------------------------------------
# 5. BITWISE OPERATORS
# --------------------------------------------
print("5. BITWISE OPERATORS")

m = 5   # Binary: 0101
n = 3   # Binary: 0011

print("m =", m, "n =", n)
print("Bitwise AND (&):", m & n)
print("Bitwise OR (|):", m | n)
print("Bitwise XOR (^):", m ^ n)
print("Bitwise NOT (~m):", ~m)
print("Left Shift (m << 1):", m << 1)
print("Right Shift (m >> 1):", m >> 1)

print("\n----------------------------------\n")

# --------------------------------------------
# 6. MEMBERSHIP OPERATORS
# --------------------------------------------
print("6. MEMBERSHIP OPERATORS")

list1 = [10, 20, 30, 40]

print("List:", list1)
print("20 in list1:", 20 in list1)
print("50 not in list1:", 50 not in list1)

print("\n----------------------------------\n")

# --------------------------------------------
# 7. IDENTITY OPERATORS
# --------------------------------------------
print("7. IDENTITY OPERATORS")

p = 10
q = 10
r = 20

print("p =", p, "q =", q, "r =", r)
print("p is q:", p is q)       # Same memory location
print("p is r:", p is r)
print("p is not r:", p is not r)

print("\n----------------------------------\n")

print("✅ ALL PYTHON OPERATORS EXPLAINED SUCCESSFULLY")
