import Car_Management

while True
    Request = input("Do you want to make a car Request (Yes or No)")
    if Request == 'Yes'
    else : break
    
    print(Cars)
    
    Car_Request = input("What car do you want to request?")
    
    if Cars[Car_Request[Available]] == 'Yes'
        print("Car successfully requested")
        Cars[Car_Request[Available]] = 'No'
    elif Cars[Car_Request[Available]] == 'No'
        print("The car is already requested!")

    Request = input("Do you want to make another request?")
    if Request == 'No' : break
