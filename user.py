class User:

    def __init__(self, fname = None, lname = None, phone = None,address = None, email = None,password = None,role = None):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.address = address
        self.email=email
        self.password=password
        self.role=role

    # def getUserInfo:
    #     retrun self

    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname 

    def getPhone(self):
        return self.phone

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getRole(self):
        return self.role

    def setFirstName(self, fname):
            self.fname = fname

    def setLastName(self, lname):
            self.lname = lname

    def setPhone(self, phone):
            self.phone = phone

    def setAddress(self, address):
            self.address = address

    def setEmail(self, email):
            self.email = email

    def setRole(self, role):
            self.role = role

    def setPassword(self, password):
            self.phone = password

# For Testing
# user1=User("HArry","Tank",2132143112,'asftysaf','ydtfwy','ewshrftgewyu',1)
# print(user1.getFirstName())
# print(user1.getPhone())
# print(user1.getRole())