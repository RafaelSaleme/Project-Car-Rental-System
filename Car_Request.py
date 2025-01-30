import Car_Management

while True :
    Request = input("Do you want to make a car Request (Yes or No)")
    if Request.lower() != 'Yes' : break 
    
    print(Car_Management.Cars)
    
    Car_Request = input("What car do you want to request?")
    
    if Car_Management.Cars[Car_Request[Car_Management.Available]] == 'Yes' :
        print("Car successfully requested")
        
        Car_Management.Cars[Car_Request[Car_Management.Available]] = 'No'

    elif Car_Management.Cars[Car_Request[Car_Management.Available]] == 'No' :
        print("The car is already requested!")

    Request = input("Do you want to make another request?")
    if Request == 'No' : break
