import os

costumers = {} 
costumersList = {}

userInput = ''


while userInput.lower() != '3':
    
    
    print('Profile Menu\n\n')
    userInput = input('1. Add\n2. See\n3. Exit\n')
    
    if userInput.lower() == '1':
       
        os.system('cls')
        
        nome = input("Insert a name\n")
        cpf = input("Insert a CPF\n")
        nickname = input("Insert a nickname\n")

        costumers.update({"name" : nome, "CPF" : cpf}) 
        costumersList[nickname] = costumers

        os.system('cls')

        print("Profile Created!\n")
    
    elif userInput.lower() == '2':
        os.system('cls')
        print(costumersList)
        print("\n")

os.system('cls')