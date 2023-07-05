diff = 100
sub = eval(input("Pick a number, any number:\t"))
while sub != 0:
    diff -= sub
    sub = eval(input("Pick another number, any number:\t"))
print("Remaining number:", diff)
