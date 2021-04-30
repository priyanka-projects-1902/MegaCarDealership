import mysql.connector
# from connection import getConnection
import sqlOp as sql 
import cars as car 
from user import User



def getUserInfo():
    user = User()
    fname = input('What is your first name? >> ')
    user.setFirstName(fname)
    lname = input('What is your last name? >> ')
    user.setLastName(lname)
    phone = input('What is your phone? >> ')
    user.setPhone(phone)
    address = input('What is your address? >> ')
    user.setAddress(address)
    email = input('What is your email? >> ')
    user.setEmail(email)
    password = input('What is your password? >> ')
    user.setPassword(password)
    role = input('What is your role [0 for employee, 1 for customer]? >> ')
    user.role(role)
    

# Display Car Inventory 
def carInventory():
    sql.readIventory()


def saveUserInfo():
    if (checkUserEsxist(user.getEmail)):
       print('Existing User:', user.getEmail)
    elif string_1:
        print('String is empty.')
    else:
        # print(string_1) 
        sql.insertUsersInfo(user.getFirstName, user.getLastName, user.getAddress, user.getPhone, user.getEmail, user.getPassword, user.getRole)

def addCarToInventory():
    sql.insertCarsInfo(car.make, car.model, car.year, car.color, car.price)
    
def updateUserInfo():
    user_id = getUserId(user.getEmail) 
    if(user_id == 0):
        print("") #User does not exist to update
    else:
        while True:
            choice = input("What information you wish to update: \n[1] for first name\n[2] for last name,\n[3] for phone\n[4]address\n[5] for email\n[6] for password\n[7]for role")
            if (choice == 1):
                newfirstname = input('What will be the new name? >> ')
                sql.updateUsers(user_id, user_fname, newfirstname)    
            elif (choice == 2):
                newlastname = input('What will be the new last name? >> ')
                sql.updateUsers(user_id, user_lname, newlastname) 
            elif (choice == 3):
                newphone = input('What will be the new phone? >> ')
                sql.updateUsers(user_id, user_phone, newphone) 
            elif (choice == 4):
                newaddress = input('What will be the new address? >> ')
                sql.updateUsers(user_id, user_address, newaddress) 
            elif (choice == 5):
                newemail = input('What will be the new email? >> ')
                sql.updateUsers(user_id, user_email, newemail) 
             elif (choice == 6):
                newpassword = input('What will be the new password? >> ')
                sql.updateUsers(user_id, user_password, newpassword)   
             else (choice == 7):
                newrole = input('What will be the new role? >> ')
                sql.updateUsers(user_id, user_role, newrole)                   

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
    
def removeCarfromInventory(car_id):
    sql.readCarsInfo()
    input("Please enter the id of the car deleted >>> ")
        sql.updateUsers(car_id)   
        
 
# -------------- Roger ----------------- 
def allInputs():
    system('cls')
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
    #inputStatus1 = input('Are you a veteran (y/n)? ')
    #inputStatus2 = input('Are you disabled (y/n)? ')

    #Uncomment when hardcode testing ends
    #cust1 = cust(status1, status2)

def guestCustDetails():
    system('cls')
    custG = cust('', '', '', '', '', '', '', '')
    print('Guest account creation')
    custG.fname = input('First name: ')
    custG.lname = input('Last name: ')
    custG.address = input('Address: ')
    custG.phone = input('Phone number: ')
    custG.email = input('Email: ')
    custG.password = input('Password: ')
    custG.status1 = input('Are you a war veteran (y/n)? ')[0:1]
    custG.status2 = input('Do you have any disabilities (y/n)? ')[0:1]
    return custG

def viewCart(cartList1, cust2):
    system('cls')
    total = float(0.0)
    bonus = float(0.0)
    print('')
    print('Your cart')
    print('')
    for i in cartList1:
        print(f'Car make: {i.make}\nmodel: {i.model}\nyear: {i.year}\ncolor: {i.color}\nprice: ${i.price}')

        #Discount user = receive 25% off the cost of the car plus $500 bonus
        if (cust2.status1 == 'y' or cust2.status2 == 'y'):
            i.price = float(i.price*75/100)
            bonus += 500.00
            print(f'Price with veteran/disabled discount: ${i.price}. Bonus from car: ${bonus}')
            print('')

        #Discount white car = receives a bonus of $400 towards the down payment
        elif (i.color == 'white' or i.color == 'white'):
            bonus += 400.00
            print(f'Bonus from car: ${bonus}')
            print('')

        #Discount black car = discount of 25% the price of the car
        elif (i.color == 'black' or i.color == 'black'):
            i.price = float(i.price*75/100)
            print(f'Black car discount price: ${i.price}')
            print('')

        total += i.price
    print('')
    print(f'Total before tax: ${total}')
    total = round((total*1065/1000), 2)
    print(f'Final total with 6.5% tax: ${total}')
    print(f'Bonuses: ${bonus}')
    print('')


# -------------- Roger -----------------        