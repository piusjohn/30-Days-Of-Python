# # ===== DAY 3: Operators in Python =====
# # This script demonstrates all types of operators: arithmetic, comparison, logical, assignment, and bitwise

# # ===== Section 1: Arithmetic Operators =====
# # Used to perform mathematical operations

# print("===== Arithmetic Operators =====")

# a = 10  # First operand
# b = 3   # Second operand

# # Addition: adds two operands
# print(f"Addition: {a} + {b} = {a + b}")

# # Subtraction: subtracts second operand from first
# print(f"Subtraction: {a} - {b} = {a - b}")

# # Multiplication: multiplies two operands
# print(f"Multiplication: {a} * {b} = {a * b}")

# # Division: divides first operand by second (returns float)
# print(f"Division: {a} / {b} = {a / b}")

# # Floor Division: divides and returns integer result (rounds down)
# print(f"Floor Division: {a} // {b} = {a // b}")

# # Modulus: returns remainder after division
# print(f"Modulus: {a} % {b} = {a % b}")

# # Exponentiation: raises first operand to power of second
# print(f"Exponentiation: {a} ** {b} = {a ** b}")


# # ===== Section 2: Comparison Operators =====
# # Used to compare two values, returns True or False

# print("\n===== Comparison Operators =====")

# x = 5
# y = 8

# # Equal: checks if values are equal
# print(f"Equal: {x} == {y} is {x == y}")

# # Not Equal: checks if values are different
# print(f"Not Equal: {x} != {y} is {x != y}")

# # Greater Than: checks if left is greater than right
# print(f"Greater Than: {x} > {y} is {x > y}")

# # Less Than: checks if left is less than right
# print(f"Less Than: {x} < {y} is {x < y}")

# # Greater Than or Equal: checks if left is >= right
# print(f"Greater Than or Equal: {x} >= {y} is {x >= y}")

# # Less Than or Equal: checks if left is <= right
# print(f"Less Than or Equal: {x} <= {y} is {x <= y}")


# # ===== Section 3: Logical Operators =====
# # Used to combine conditional statements, returns True or False

# print("\n===== Logical Operators =====")

# p = True
# q = False

# # AND: returns True if both conditions are True
# print(f"AND: {p} and {q} = {p and q}")

# # OR: returns True if at least one condition is True
# print(f"OR: {p} or {q} = {p or q}")

# # NOT: reverses the boolean value
# print(f"NOT: not {p} = {not p}")

# # Practical example with conditions
# age = 25
# has_license = True
# can_drive = age >= 18 and has_license  # Both conditions must be True
# print(f"Can drive: {can_drive}")


# # ===== Section 4: Assignment Operators =====
# # Used to assign values to variables

# print("\n===== Assignment Operators =====")

# # Basic assignment
# num = 10
# print(f"Basic assignment: num = {num}")

# # Add and assign: adds right operand to left and stores result
# num += 5  # Equivalent to: num = num + 5
# print(f"Add and assign (+=): num = {num}")

# # Subtract and assign
# num -= 3
# print(f"Subtract and assign (-=): num = {num}")

# # Multiply and assign
# num *= 2
# print(f"Multiply and assign (*=): num = {num}")

# # Divide and assign
# num /= 4
# print(f"Divide and assign (/=): num = {num}")

# # Floor divide and assign
# num //= 2
# print(f"Floor divide and assign (//=): num = {num}")

# # Modulus and assign
# num %= 3
# print(f"Modulus and assign (%=): num = {num}")

# # Exponent and assign
# num **= 2
# print(f"Exponent and assign (**=): num = {num}")


# # ===== Section 5: Bitwise Operators =====
# # Used to perform operations on binary representations of integers

# print("\n===== Bitwise Operators =====")

# m = 5    # Binary: 0101
# n = 3    # Binary: 0011

# # AND: performs bitwise AND (both bits must be 1)
# print(f"Bitwise AND: {m} & {n} = {m & n}")  # Result: 0001 (1)

# # OR: performs bitwise OR (at least one bit must be 1)
# print(f"Bitwise OR: {m} | {n} = {m | n}")   # Result: 0111 (7)

# # XOR: performs bitwise XOR (bits must be different)
# print(f"Bitwise XOR: {m} ^ {n} = {m ^ n}")  # Result: 0110 (6)

# # NOT: performs bitwise NOT (inverts all bits)
# print(f"Bitwise NOT: ~{m} = {~m}")

# # Left Shift: shifts bits left, fills with zeros on right
# print(f"Left Shift: {m} << 1 = {m << 1}")   # 0101 becomes 1010 (5 becomes 10)

# # Right Shift: shifts bits right, fills with zeros on left
# print(f"Right Shift: {m} >> 1 = {m >> 1}")  # 0101 becomes 0010 (5 becomes 2)


# # ===== Section 6: Membership Operators =====
# # Used to test if a sequence contains a specific value

# print("\n===== Membership Operators =====")

# fruits = ['apple', 'banana', 'orange', 'grape']

# # In: returns True if value exists in sequence
# print(f"'apple' in fruits: {'apple' in fruits}")

# # Not in: returns True if value does NOT exist in sequence
# print(f"'mango' not in fruits: {'mango' not in fruits}")


# # ===== Section 7: Identity Operators =====
# # Used to compare objects, checks if they are the same object in memory

# print("\n===== Identity Operators =====")

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = list1

# # is: returns True if both variables reference the same object
# print(f"list1 is list3: {list1 is list3}")  # True (same object in memory)
# print(f"list1 is list2: {list1 is list2}")  # False (different objects, same content)

# # is not: returns True if variables do NOT reference the same object
# print(f"list1 is not list2: {list1 is not list2}")  # True


# # ===== Section 8: Operator Precedence =====
# # Order in which operators are evaluated (PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)

# print("\n===== Operator Precedence =====")

# result1 = 2 + 3 * 4  # Multiplication happens first: 2 + 12 = 14
# result2 = (2 + 3) * 4  # Parentheses first: 5 * 4 = 20

# print(f"Without parentheses: 2 + 3 * 4 = {result1}")
# print(f"With parentheses: (2 + 3) * 4 = {result2}")

age = 21
height = 6.0
cmp = 4j

print("enter base of the triangle")
base = float(input())
print("now enter the height of the triangle")
height = float(input())

area = 0.5*base*height
print(f"The area of the triangle is {area}")

a, b, c = [int(x) for x in input("enter side a, side b, and side c of the triangle seperated by comma and a space to get the perimeter: ").split(", ")]

print(f"the perimeter is: {a*b*c}")


