# students = ["Needi","Ayesha","Maheen", "Ahmad", "Ali", "Sana", "Musa"]
students = ("Needi","Ayesha","Maheen", "Ahmad", "Ali", "Sana", "Musa")
for index, student in enumerate(students, start=15):
    print(f"Roll No: {index}, Student Name: {student}")
    
names = ["Naveed","Sara","Fatima", "Maheen"]
scores = [90, 85, 88, 99, 45]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

zipped = [("Naveed", 90), ("Sara", 85), ("Fatima", 88)]
names, scores = zip(*zipped)

print(names)
print(scores)
