x = None
while x.lower() != "yes" and x.lower() != "no":
    x = input("Do you like fruits?")
if x.lower() == "yes":
    print("Good.")
    fruit = input("Name a fruit, any fruit")
    if fruit.lower() == "mango" or fruit.lower() == "pineapple":
        print("That's a tropical fruit")
    elif fruit.lower() == "orange" or fruit.lower() == "lemon":
        print("That's a citrus fruit")
    else:
        print("That's neither a tropical fruit nor a citrus fruit")
else:
    print("GET OUT")
