import os
from os import system
import datetime
from cars import *
from user import *
from function import *

system('cls')

print('Welcome to Prissy Wheels!')
#Prissy: Adjective. Fussily and excessively respectable. "Her prissy mother"

"""
COHORT 3 HACKATHONUsing Methods, Classes, Objects, Getters(Accessors) and Setters (Mutators)

Create a Dealership application where you prompt the user to input the make, model, year, and color of   the   cars   they   want.   
Prices   will   vary   based   on  color,   year,   model,   make.   Present   the   user   withdifferent   options   where   they   can   see   the   price.
Pass   all   prices   for   colors   and   makes   to   another method   which   calculates   the   total   prices   (withtaxes   included).   

If   car   is   black,   the   user   gets   a discount of 25% the price of the car;   
if the car is white,   the   customer   receives   a   bonus   of   $400 towards   the   down   payment.   
If   the   customer   is   awar veteran or disabled, they receive 25% off thecost of the car plus $500 bonus. 

This returns total price   and   bonuses   to   the   main   file.   
Pass   the   fourvalues   (make,   model,   year,   and   color)   to   another method   where   you   use   the   values   to   create objects. 

Return the objects to the main file whereyou will display all of them. 
Requirements:-Organize     your     program     by     separating functionalities in files
-You need to buy 5 cars.
-Make data persist in a database that containsthree tables: customers, orders, and products
-Remember to use primary and foreign keys.
"""

#Ask user to input all preferred search info and customer info
#allInputs()
#cust1 = cust(inputStatus1, inputStatus2)

#Hardcoded car test (HCCT)
HCCT1 = car(0, 'randomMake', 'randomModel', 1984, 'black', 9001)
HCCT2 = car(1, 'randomerMake', 'randomerModel', 1985, 'white', 68419)
HCCT3 = car(2, 'randomestMake', 'randomestModel', 1986, 'randomestColor', 1000001)

#Cart as a list attempt. It starts off blank
cartList = []

#Add to cart
cartList.append(HCCT1)
cartList.append(HCCT2)
cartList.append(HCCT3)
#print('hardcode test HCCTs added to cartList')

#Hardcode customer test
#cust1 = cust('David', 'Sarif', '1337 Elite Street', '0451', 'david@sarifindustries.com', '1984' 'n', 'n')
#cust1 starts off as a blank account
cust1 = cust('', '', '', '', '', '', '', '')

#print('test calling cart')
viewCart(cartList, cust1)
#print('successfully viewed cart')
sglcChoose()



#Cart total function, able to buy 5 cars, calculate taxes

print('')