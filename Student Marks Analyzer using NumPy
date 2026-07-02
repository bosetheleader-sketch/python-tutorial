import numpy as np

# Student Names
students = np.array([
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma"
])

# Marks in 5 subjects
marks = np.array([
    [85, 90, 78, 92, 88],
    [65, 70, 60, 72, 68],
    [95, 94, 96, 98, 99],
    [45, 55, 50, 48, 52],
    [80, 82, 84, 86, 88]
])

# Average marks
average = np.mean(marks, axis=1)

# Highest mark
highest = np.max(marks, axis=1)

# Lowest mark
lowest = np.min(marks, axis=1)

# Standard deviation
std = np.std(marks, axis=1)

print("Student Report\n")

for i in range(len(students)):

    if average[i] >= 90:
        grade = "A+"
    elif average[i] >= 80:
        grade = "A"
    elif average[i] >= 70:
        grade = "B"
    elif average[i] >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Name     : {students[i]}")
    print(f"Average  : {average[i]:.2f}")
    print(f"Highest  : {highest[i]}")
    print(f"Lowest   : {lowest[i]}")
    print(f"Std Dev  : {std[i]:.2f}")
    print(f"Grade    : {grade}")
    print("-" * 30)

# Top Performer
top_index = np.argmax(average)

print("\nTop Performer")
print("-------------")
print("Name :", students[top_index])
print("Average :", round(average[top_index], 2))

# Overall Statistics
print("\nOverall Statistics")
print("------------------")
print("Class Average :", np.mean(marks))
print("Highest Mark  :", np.max(marks))
print("Lowest Mark   :", np.min(marks))
