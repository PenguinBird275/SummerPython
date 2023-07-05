temp = eval(input("How hot is it outside in degrees Fahrenheit?\t"))
if temp < 10:
    print("Stay inside!")
elif temp < 20:
    print("If you're experiencing this in Florida, you might be the luckiest person on Earth!")
elif temp < 30:
    print("...snow?")
elif temp < 40:
    print("Getting really cold...")
elif temp < 50:
    print("Pretty cold")
elif temp < 60:
    print("Nice weather")
elif temp < 70:
    print("Cool breezes should be coming")
elif temp < 80:
    print("Kind of warm...")
elif temp < 90:
    print("Average heat in Florida")
elif temp < 100:
    print("Uncomfortably hot")
else:
    print("Stay inside or go ahead and get heat stroke!")
