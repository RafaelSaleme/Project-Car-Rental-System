import os
import Car_Management
import Car_Customer_List

Requests = {}
Request = ''

while Request.lower() != '3' :

    print("Car Request Menu\n\n")

    Request = input("1. Make a new Request\n2. Cancel Request\n3. Exit\n")
    
    # New Request
    if Request.lower() == '1' : 
    
        os.system('cls')
        print(Car_Management.Cars)
    
        
        Car_Request_ID = input("Insert the ID of the car you want to request\n")
    
    
    
        if Car_Management.Cars[Car_Request_ID]['Available'].lower() == 'yes' :

            os.system('cls')

            user_input = input("Insert your ID\n")

            Requests[Car_Request_ID] = user_input
            os.system('cls')
            print("Car successfully requested!\n")
        
            Car_Management.Cars[Car_Request_ID]['Available'] = 'No'

        elif Car_Management.Cars[Car_Request_ID]['Available'].lower() == 'no' :
            os.system('cls')
            print("The car is already requested!\n")

    # Request Cancel
    elif Request.lower() == '2' :

        os.system('cls')
        print(Car_Management.Cars)
    

        Car_Request_ID = input("Insert the ID of the car you want to cancel the request\n")

        if Car_Management.Cars[Car_Request_ID]['Available'].lower() == 'no' :
            os.system('cls')
            print("Car request successfully canceled!\n")
        
            Car_Management.Cars[Car_Request_ID]['Available'] = 'Yes'

        elif Car_Management.Cars[Car_Request_ID]['Available'].lower() == 'yes' :
            os.system('cls')
            print("There is no request for thi car!\n")



os.system('cls')
