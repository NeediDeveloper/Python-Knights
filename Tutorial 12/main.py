# Break Statement
count = 0
while count < 10:
    if count == 6:
        print("Loop stopped at count:", count)
        break
    print(count)
    count += 1

# Continue Statement
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3")
        continue
    print(num)
    
# Pass Statement
num = 5
if num == 5:
    pass


#Short-Hand If Else
age = 25
if age >= 18: print("You are eligible to vote.")


age = 20
status ="Adult" if age >= 18 else"Minor"
print(status)

marks = 45
result ="Excellent" if marks > 80 else"Good" if marks > 50 else"Needs Improvement"
print(result)