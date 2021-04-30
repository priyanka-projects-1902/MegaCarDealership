from os import system
from user import *

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

    