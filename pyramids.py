row = int(input("Enter Row :: "))
col = int(input("Enter Col :: "))
print("Row :: ", row)
print("Col ::", col)


# Square
for i in range(row):
    for j in range(0, col):
        print("*", end="")
    print()

# *
# **
# ***
# ****
# *****
for i in range(row):
    for j in range(0, i+1):
        print("*", end="")
    print()
print("==================")
for i in range(row):
    for j in range(0, row-i-1):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print()
