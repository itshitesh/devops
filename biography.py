while True:
    name = input("please enter your name: ")
    dob = input("please enter your date of birth (e.g 2 May, 1988): ")
    addr = input("please enter your address: ")
    goal = input("please enter your personal goal: ")
    if not name.isalpha():
        print("Please enter a valid input")
        
        continue
    else:
        break
print("Name: " + name)
print("Date of Birth: " + dob)    
print("Address: " + addr)
print("Personal goals: " + goal)