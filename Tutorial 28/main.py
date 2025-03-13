students = ["Ali","Naveed","Sara","Zoya","Ali","Sara"]
marks = (85, 90, 78, 88, 85, 78)

# Finding Unique Students
unique_students = list(dict.fromkeys(students))
print(f"Unique Students: {unique_students}")

# Combining Students and Marks
full_data = dict(zip(students, marks))
print(f"Full Data: {full_data}")
print(full_data.keys())
print(full_data.values())