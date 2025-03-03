try:
    num = int(input("Enter a number:")) # User se number lena
    print(f"Result: {10 / num}") # Division by user input
# except Exception as e:
#     print(f"Error: {e}")   
 
# except:
#     print("Some error occured")    

except ValueError: # Agar user number na de (ValueError)
    print("Please enter a valid number.")
except ZeroDivisionError: # Agar user 0 input kare
    print("You cannot divide by zero!")

num = int(input("Enter a number:")) # User se number lena
print(f"Result: {10 / num}")


def students():
    try:
        student_names = ["Ali", "Ahmed", "Sara", "Needi", "Kamran"]
        index = int(input("Enter the index of the student: "))
        print(student_names[index])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("This is an important line.")
   
    print("This is an important line.")
    
va = students()
print(va)