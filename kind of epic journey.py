steps = eval(input("How many steps do you want to take?"))
wizard = input("What is the name of your wizard?")
for i in range(steps):
    print("There once was a wizard named", wizard)
    print(wizard, "takes", i + 1, "steps forward!")
print("The journey of", wizard, "is complete!")
