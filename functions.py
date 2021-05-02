import mysql.connector
# from connection import getConnection
import sqlOp as sql 
import cars as car 
from user import User
import re

userInfoList = ["First Name","Last Name","Phone Name","Address","eMail Id","Password","Role"]
carInfoList=["Car Make","Car Model","Year of Manufacturing","Car Color","Car Price"]

def getUserInfo():
    userInput = []
    while True:
        
        fname = input('What is your first name? >> ').title().lstrip().rstrip()
        userInput.append(fname)
        lname = input('What is your last name?  >> ').title().lstrip().rstrip()
        userInput.append(lname)
        phone = input('What is your phone? Include area code [5555555555] >> ').lstrip().rstrip()
        userInput.append(phone)
        address = input('What is your address? >> ').title().lstrip().rstrip()
        userInput.append(address)
        email = input('What is your email? >> ').lstrip().rstrip()
        userInput.append(email)
        password = input('What is your password? Max 4 characters >> ').lstrip().rstrip()
        userInput.append(password)
        role = int(input('What is your role [ 0 for employee, 1 for customer ]? >> ').lstrip().rstrip())
        userInput.append(role)
        
        if ((re.match("^\w{1,10}$", fname)):
            # userInput.append(fname)
            print("")
             
        elif ((re.match("^\w{1,15}$", lname)):
            # userInput.append(lname)
            print("")

        elif (re.match("^\d{10}$", phone)):
            # userInput.append(phone)
            print("")
        
        elif (re.match("^.{18,35}$", address)):
            # userInput.append(address)
            print("")

        elif (re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", email)):
            print("")
                
        elif (re.match("^[a-zA-Z0-9]{4}$", password)):
            # userInput.append(password)
            print("")
        
        elif (role == 0 or role == 1):
            # userInput.append(role)
            print("")

            break    

        else:
            print("Please enter valid data!")

    print(userInput)

    return(userInput)
            
getUserInfo( ) 

def saveUserInfo(newUser):
    if (checkUserExist(newUser.getEmail())):
       print(f'The user {newUser.getEmail} already exist in our system:')
    else:
        status = sql.insertUsersInfo(newUser.getFirstName(),\
        newUser.getLastName(),\
        newUser.getAddress(),\
        newUser.getPhone(),\
        newUser.getEmail(),\
        newUser.getPassword(),\
        newUser.getRole())
        if(status):
            print("Your information has been successfully saved in our system!!")
        else:
            print("Insert failed")

def updateUserInfo():
    userToUpdate=User.getInstance()
    if(userToUpdate.getEmail() != None):
        userId = getUserId(userToUpdate.getEmail()) 
        if(user_id == 0):
            print("") #User does not exist to update
        else:
            counter=1
            choice=0
            flag = false
            while not flag:
                for entry in userInfoList:
                    print(f"{counter}: {entry}")
                    counter += 1
                choice = input(f"What information you wish to update: ")
                if(choice > counter or choice < 1):
                    print(f"Invalid Choice , Please select between [1-{counter}] : ")
                else:
                    flag = True
                    feild=userDataSet[choice-1]
                    value = input(f'Please enter the new {userInfoList[choice-1]} : ')
                    #Check input sanitization
                    sql.updateUsers(user_id, feild, value) 

    
    

# Display Car Inventory 
def showAvailableCars():
    print("We have the following cars in our inventory as of now")
    carlist=sql.readCarsInfo()
    for car in carlist:
        print(f''' Car Id :{car[0]}
                {carInfoList[0]}:{car[1]}
                
                
                
                
                ''')


def addOrRemoveCarToInventory():
    print("We have the following cars in our inventory :")
    showAvailableCars()
    flag=false
    while not flag:
        choice = input('''Do you wish to add/remove a similar car[0] or a new car[1].
                Please select [0-1] : ''')
        if(choice == 1):
            flag=True
            isInserted = sql.insertCarsInfo(car.make, car.model, car.year, car.color, car.price)
            if(isInserted):
                print("New car Information inserted successfully.")
        elif(choice == 0):   
            flag=True     
            updateCarquantity()
        else:
            print("Invalid choice ...")
    
def updateCarquantity(): #This function is for the seller to add/remove cars from inventory
    flag = false
    while not flag:
        car_id= input("Please enter the id of the car whose quatity needs to be updated: ")
        quantity = input("Enter the quantity: ")
        ret = sql.updateCarInfo(car_id,"car_quantity",quantity)
        if(ret):
            choice= input('''Car Quantity Updated Successfully!!
                     Do you wish to update quantity for another Car [Y/N] :''')
            if(choice == 'N' or choice == 'n'):
                flag=True


def updateCarInfo():
    sql.readCarsInfo()
    choice = input("Please enter the id of the car will be updated >>> ")
    sql.updateCarInfo()
    while True:
        choice = input("What information you wish to update: \n[1] for Make\n[2] for Model Name,\n[3] for Model Year\n[4] for Color\n[5] for Price")
        if (choice == 1):
            newmake = input('What will be the new make? >> ')
            sql.updateUsers(user_id, car_make, newmake)   
        elif (choice == 2):
            newmodelname = input('What will be the new model name? >> ')
            sql.updateUsers(user_id, car_model_name, newmodelname) 
        elif (choice == 3):
            newmodelyear = input('What will be the new model year? >> ')
            sql.updateUsers(user_id, car_model_year, newmodelyear) 
        elif (choice == 4):
            newcolor = input('What will be the new color? >> ')
            sql.updateUsers(user_id, car_color, newcolor) 
        else (choice == 5):
            newprice = input('What will be the new price? >> ')
            sql.updateUsers(user_id, car_price, newprice) 
    
  
def countCarsListed():
    count=sql.getCarCount()
    return count        
 
def purchaseCar():
    showAvailableCars()
    totalCars=countCarsListed()
    flag = False
    while not flag:
        choice=input("Select the car Id you wish to purchase : ")
        if(choice < 1 or choice > totalCars):
            print(f"Please select a valid car Id between [1-{totalCars}] ")
        else:
            carPurchased = sql.getCarInfo(choice)
            carInstance = new Car(carPurchased)
            carList.append(carInstance)
            removeCarFromInventory()
            choice=input("Do you want to purchase another Car [Y/N] :")
            if(choice == 'N' or choice == 'n'):
                insertOrdersInfo()
                flag = true

def askUserPref():
     print('Are there any specific details you\'re looking for to help narrow your search?')
    inputMake = input('What is the preferred make of the car? ')
    inputModel = input('What is the preferred model of the car? ')
    inputYear = int(input('What is the preferred year of the car? '))
    now = datetime.datetime.now()
    while (inputYear < 1886 or inputYear > int(now.year)):
        if (inputYear < 1886):
            print(f'Cars weren\'t invented yet. Please enter a number between 1886 and {int(now.year)}')
        elif (inputYear > int(now.year)):
            print(f'We don\'t have any cars from the future in stock. Please enter a number between 1886 and {int(now.year)}')
        inputYear = int(input('What is the preferred year of the car? '))
    inputColor = input('What is the preferred color of the car? ')   
   

def calculatePrice():
   
    total = float(0.0)
    bonus = float(0.0)
    print('')
    print('Getting a few more details from you to give you the best deals')
    print('')
    isVeteran_disabled = input("Are you a war veteran or have any disability (Y/N)")

    for carInstance in carList:
        print(f'''{carInfoList[0]}: {carInstance.getMake()}
                  {carInfoList[1]}: {carInstance.getModel()}
                  {carInfoList[2]}: {carInstance.getYear()}
                  {carInfoList[3]}: {carInstance.getColor()}
                  {carInfoList[4]}: ${carInstance.getPrice()}''')               
    

        #Discount user = receive 25% off the cost of the car plus $500 bonus
        if (isVeteran_disabled == 'y' or isVeteran_disabled == 'Y'):
            total = carInstance.getPrice()
            total = float(total*75/100)
            bonus += 500.00
            print(f'Price with veteran/disabled discount: ${total}. Bonus from car: ${bonus}')
            print('')

        #Discount white car = receives a bonus of $400 towards the down payment
        elif (carInstance.getColor() == 'white'):
            total = carInstance.getPrice()
            bonus += 400.00
            print(f'Bonus from car: ${bonus}')
            print('')

        #Discount black car = discount of 25% the price of the car
        elif (carInstance.getColor() == 'black'):
            total = carInstance.getPrice()
            total = float(total*75/100)
            print(f'Black car discount price: ${carInstance.getPrice()}')
            print('')

       
    print('')
    print(f'Total before tax: ${total}')
    total += round((total*1065/1000), 2)
    print(f'Final total with 6.5% tax: ${total}')
    print(f'Bonuses: ${bonus}')
    print(f'Final total after bonus: ${total-bonus}')
    print('')


       