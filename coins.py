#variable created to take in user response
response = input ("Do you have coins? Enter Yes or No: ")
# if statement made with response variable to get input whether user has change
#if user says Yes the program will continue to talk to the user
#if user says No the program will end

if response == 'Yes':
    print ("\nPlace amount of each coin. \n")
    #Variables made to define coins and ask the user to input their coin amount
    pennies_amount = int(input("Pennies: "))
    nickels_amount = int(input("Nickels: "))
    dimes_amount = int(input("Dimes: "))
    quarters_amount = int(input("Quarters: "))
    # printing and displaying a line for organization
    print("\n___________________________________________________________\n")
    #Created variables from coin names making them equal to the amount
    pennies = 0.01
    nickels = 0.05
    dimes = 0.1
    quarters = 0.25
    #calculating the total of pennies
    total_pennies = pennies * pennies_amount
    #the code ["{:.2f}".format ] makes (total_pennies) to only have 2 decimal places
    res = "{:.2f}".format(total_pennies)
    #res is the variable you make for the decimal places
    #then we call res when printing the coin amount
    #We do this for all of the coins that need 2 decimal placements
    print("Pennies: $",res)
    #Nickels
    total_nickels = nickels * nickels_amount
    res = "{:.2f}".format(total_nickels)
    print("Nickels: $",res)
    #Dimes
    total_dimes = dimes * dimes_amount
    res = "{:.2f}".format(total_dimes)
    print("Dimes: $",res)
    #Quarters
    total_quarters = quarters * quarters_amount
    res = "{:.2f}".format(total_quarters)
    print("Quarters: $",res)
    # printing and displaying a line for organization
    print("\n___________________________________________________________\n")
    #Total Amount
    total_amount= total_pennies + total_nickels + total_dimes + total_quarters
    res = "{:.2f}".format(total_amount)
    print("Total Amount: $",res)
    #This is the else statement if the user says no or doesn't type Yes
else:
    print("Try again next time")
