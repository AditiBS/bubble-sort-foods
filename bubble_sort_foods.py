foods = input("Enter your favorite foods separated by commas: ").split(",")
# Remove extra spaces 
foods = [food.strip() for food in foods]

# Bubble Sort by length 
n = len(foods)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(foods[j]) > len(foods[j + 1]):
            foods[j], foods[j + 1] = foods[j + 1], foods[j]

# Print sorted list
print("Foods sorted by length:", foods)
