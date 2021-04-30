import connection as c 
import mysql.connector

userlist=[]
def readUsersInfo(id):
    print("inside read")
    conn = c.returnConnection()
    try:
        # userlist=[]
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users where user_id = {id} ")
        for row in cursor:
            for i in row:
                userlist.append(i)

        print(userlist)
        return userlist
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)


carlist = []
def readCarsInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM cars ")
        for row in cursor:
            for i in row:
                carlist.append(i)
        # for i in carlist:
        #     print(i)
        return carlist
        
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)  

orderlist = []
def readOrdersInfo(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM orders where order_id = {id} ")
        for row in cursor:
            for i in row:
                orderlist.append(i)
        for i in orderlist:
                print(i)        
        return orderlist

        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)         


def insertUsersInfo(fname, lname, address,phone, email, password, role):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (user_fname, user_lname, user_phone, user_address, user_email, user_password, user_role) VALUES \
                                           ('{fname}', '{lname}', '{address}', '{phone}', '{email}', '{password}', '{role}')")
        
        print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)

        
def insertCarsInfo(make, Mname, Myear, color, price, quantity):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO cars (car_make, car_model_name, car_model_year, car_color, car_price, car_quantity) VALUES \
                                        ('{make}', '{Mname}', '{Myear}', '{color}', '{price}', '{quantity}')")
        print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)



def insertOrdersInfo(O_id, U_id, C_id ):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO orders (order_id, user_id, car_id) VALUES \
                                    ('{O_id}', '{U_id}', '{C_id}')")
        print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)


def updateUsers(id,field, value):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET {field}='{value}' WHERE user_id={id}")
        print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)

    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)     
    

def updateCars(id, field, value):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE cars SET {field} = '{value}' WHERE car_id = {id}")
        print("return = {}".format(cursor.rowcount))
        conn.commit()
        # readCarsInfo()
        cursor.close()
        conn.close()
        return(cursor.rowcount)

    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 

def deleteCars(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM cars WHERE car_id = {id}')
        print("return = {}".format(cursor.rowcount))
        conn.commit()
        readCarsInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)   

purchaselist = []
def getOrdersInfo(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        # cursor.execute({sql})
        # cursor = conn.cursor(buffered=True)
        cursor.execute(f'SELECT  order_id, user_fname, user_lname, user_email, car_model_name, car_model_year, car_make FROM orders INNER JOIN users ON orders.user_id = users.user_id INNER JOIN cars  ON  orders.car_id = cars.car_id WHERE order_id = {id}')
        for row in cursor:
            for i in row:
                purchaselist.append(i)
        #print(purchaselist)
        conn.commit()
        cursor.close()
        conn.close()
        return purchaselist
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 



def checkUserExist(emailid):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT count(*) FROM users WHERE user_email = '{emailid}'")
        conn.commit()
        readUsersInfo()
        cursor.close()
        conn.close()
        return row[0]

    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 

def getUserId(email):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT user_id FROM users WHERE user_email = '{email}' ")
        conn.commit()
        readUsersInfo()
        cursor.close()
        conn.close()
        return row[0]
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)    

 

    