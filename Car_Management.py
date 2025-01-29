Cars = []
# Base Model
Base_model ={'Brand' : 'BMW', 'Model' : 'M4', 'Color' : 'Silver', 'HP' : '510 Cv', 'Price' : '800 $/day',
            'Available' : 'Yes', 'ID' : '01'}
print("Please Register a new Car\n")

while True
    add_car = input("Do you want to add a car? (Yes or No)")
    if add_car == 'Yes'
        New_Car = Base_model
        New_Car[Brand] = input("Insert the car Brand\n")
        New_Car[Model] = input("Insert the car Model\n")
        New_Car[Color] = input("Insert the car Color\n")
        New_Car[HP] = input("Insert the car HP(Horse Power)\n")
        New_Car[Price] = input("Insert the Rental Price\n")
        New_Car[Available] = input("Insert if the car is Available or not (Yes or No)\n")

    Cars.append(New_Car)

    print("The car was added to the car List")

    see_car_list = input("Do you want to see the car list?(Yes or No)")
    if see_car_list == 'Yes'
        print(Cars)

    add_car = input("Do you want to add another car? (Yes or No)")
    if add_car == 'No' : break