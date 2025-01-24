fruits = ["apple","banana","cherry", "Watemelon", "Mango", "You"]
for fruit in fruits:
    print(f"I love {fruit}!")


for i in range(1, 1001):
    print(f"Number: {i}")


count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1 # Increment the count


# This is a Timer
import time
timer = 10
while timer > 0:
    print(f"Time remaining: {timer} seconds")
    timer -= 1
    time.sleep(1)
print("Time's up!")
