#SRN BP0178079
#Prices for off-peak.
OffFamily = 27.16
OffChildren = 6.79
OffTeen = 7.29
OffStudent = 7.79
OffAdult = 8.79
OffSenior = 7.79

#Prices for peak.
PeakFamily = 39.96
PeakChildren = 10.59
PeakTeen = 10.49
PeakStudent = 10.99
PeakAdult = 13.19
PeakSenior = 10.99

#Variable for the flat that keeps the program running on a loop
keep_going = 'yes'
#While the variable is equal to 'y' loop the following code
while keep_going == 'yes':
    
    #Print to price of tickets
    print("╔════════════════════╦═════════════════════════════════════════╗")
    print("║        Age         ║         Price per ticket (ex. VAT)      ║")
    print("║                    ║    Off-peak price   ║     Peak price    ║")
    print("╠════════════════════╬═════════════════════╬═══════════════════╣")
    print("║  Children (2-12)   ║       £6.79         ║       £10.59      ║")
    print("║     Teen 13-18     ║       £7.29         ║       £10.49      ║")
    print("║       Student      ║       £7.79         ║       £10.99      ║")
    print("║     Adult (19+)    ║       £6.79         ║       £10.59      ║")
    print("║     Senior (60+)   ║       £7.79         ║       £10.99      ║")
    print("║ Family (4 members) ║       £7.79         ║       £10.99      ║")
    print("╚════════════════════╩═════════════════════╩═══════════════════╝")
    
#User inputs for the number of each ticket required.

    
    while True:
        try:
            NoFamily = int(input("How many family tickts would you like to order (4 people)? "))
        except ValueError:
            print("You must enter a valid whole number. Please try again.")
        else:
            break

    while True:
        try:
            NoChildren = int(input("How many children (2-12) tickets would you like to oder? "))
        except ValueError:
            print("You must enter a valid whole number. Please try again.")
        else:
            break

    while True:
        try:
            NoTeen = int(input("How many teen (13-18) tickets would you like to order? "))
        except ValueError:
            print("You must enter a valid whole number. Please try again.")
        else:
            break

    while True:
        try:
            NoStudent = int(input("How many student tickets would you like to order? "))
        except ValueError:
            print("You must enter a valid whole number. Please try again.")
        else:
            break

    while True:
        try:
            NoAdult = int(input("How many adult tickets would you like to order? "))
        except ValueError:
            print("You must enter a valid whole number. Please try again.")
        else:
            break

    while True:
        try:
            NoSenior = int(input("How many senior (60+) tickets would you like to order? "))
        except ValueError:
            print("You must enter a valid whole number. Please try again.")
        else:
            break


#Calculates the total cost of the tickets for both peak and off-peak times.
    TotalPeak = (NoFamily * PeakFamily) + (NoChildren * PeakChildren) + (NoTeen * PeakTeen) + (NoStudent * PeakStudent) + (NoAdult * PeakAdult) + (NoSenior * PeakSenior)
    TotalOff = (NoFamily * OffFamily) + (NoChildren * OffChildren) + (NoTeen * OffTeen) + (NoStudent * OffStudent) + (NoAdult * OffAdult) + (NoSenior * OffSenior)
    TotalPeakVAT = (TotalPeak * 1.2)
    TotalOffVAT = (TotalOff * 1.2)

#Calculates the total number of tickets being ordered. This is then referenced later in the program.
    TotalNoTickets = NoFamily + NoChildren + NoTeen + NoStudent + NoAdult + NoSenior

#This is used to establish if the user needs peak or off-peak tickets.

    Type = input("Do you need peak tickets? (Enter yes or no) ")

    while True:
        if Type.lower() in ('yes', 'no'):
            break
        else:
            print("Not a valid input")
            Type = input("Do you need peak tickets? Enter yes or no) ")

#This section of the code calculates the total cost of the tickets with VAT. It then displays the total amount of VAT paid and the cost excluding VAT. 
#Using an if and else statement it is able to operate for both on peak and off peak tickets.
    if Type == 'yes':
        print()
        print((TotalPeak), "is the price excluding 20% VAT")
        print("The total with VAT is", (format(TotalPeakVAT, '.2f')))
    elif Type == 'no':
        print()
        print((TotalOff), "is the price excluding 20% VAT")
        print("The total with VAT is", (format(TotalOffVAT, '.2f')))


#This section displays the total tickets in the order. It calculates an overall amount and also displays the number of tickets for each age category.
#Once again by using an if and else statement it allows the code to operate for both peak and off-peak tickets.
    if Type == 'yes':
        print("You requested a total of", TotalNoTickets, "peak tickets")
        print()
        print("The breakdown of your purchase is the following")
        print()
        print("You bought", NoFamily, "family ticket(s)")
        print("You bought", NoChildren, "children ticket(s)")
        print("You bought", NoTeen, "teen ticket(s)")
        print("You bought", NoStudent, "student ticket(s)")
        print("You bought", NoAdult, "adult ticket(s)")
        print("You bought", NoSenior, "senior ticket(s)")
    elif Type == 'no':
        print("You requested a total of", TotalNoTickets, "off peak tickets")
        print()
        print("The breakdown of your purchase is the following")
        print()
        print("You bought", NoFamily, "family ticket(s)")
        print("You bought", NoChildren, "children ticket(s)")
        print("You bought", NoTeen, "teen ticket(s)")
        print("You bought", NoStudent, "student ticket(s)")
        print("You bought", NoAdult, "adult ticket(s)")
        print("You bought", NoSenior, "senior ticket(s)")

    
    #If the user puts anything other than 'y' the code will stop looping, otherwise it will continue
    keep_going = input("Do you want to place another order? (enter yes or no): ")

   # while True:
        #try:
            #1keep_going = input("Do you want to place another order? (enter yes or no): ")
    #    if keep_going in ('yes', 'no'):
     #       break
      #  else:
       #     print("Not a valid option, please enter 'yes' or 'no'.")



    while True:
        if keep_going == 'no':
            print()
            print("Thank you for your order!")
            exit()
        elif keep_going == 'yes':
            break
        else:
            print("Error - invalid option selected. Please try again.")
            keep_going = input("Do you want to place another order? (enter yes or no): ")