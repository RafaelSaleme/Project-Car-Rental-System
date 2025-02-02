import os
Cars = {}
New_Car = {}
Brand = ''
Model = ''
Color = ''
HP = ''
Price = ''
Available = ''
user_input = ''


while user_input.lower() != 'exit' :
    
    
    print("Car Management Menu\n\n")
    user_input = input("Add, See or exit\n")
    

    if user_input.lower() == 'add':
        New_Car['Brand'] = input("Insert the car Brand\n")
        New_Car['Model'] = input("Insert the car Model\n")
        New_Car['Color'] = input("Insert the car Color\n")
        New_Car['HP'] = input("Insert the car HP(Horse Power)\n")
        New_Car['Price/day'] = input("Insert the Rental Price\n")
        New_Car['Available'] = input("Insert if the car is Available or not (Yes or No)\n")
        
        Cars['aux'] = New_Car
        
        Car_ID = input("Set an ID for the car\n")
        Cars[Car_ID] = Cars['aux']
        del Cars['aux']


        os.system('cls')

        print("The car was added to the car List\n")



    elif user_input.lower() == 'see':
        os.system('cls')
        print("Car list\n")
        print(Cars)
        print("\n")

os.system('cls')
