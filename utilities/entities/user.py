from utilities.db.db_manager import dbManager
from flask import session

class User:
    __email_address = None
    __first_name = None
    __last_name = None
    __user_name = None
    __password = None
    __birth_date = None
    __Registration_DT = None

    def __init__(self,email_address,first_name,last_name,user_name,password,birth_date,Registration_DT):
        self.__email_address = email_address
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__password = password
        self.__birth_date = birth_date
        self.__Registration_DT = Registration_DT

    def getEmail(self):
        return self.__email_address

    def getPassword(self):
        return self.__password

    def getFirstName(self):
        return self.__first_name

    def getLastName(self):
        return self.__last_name

    def getUserName(self):
        return self.__user_name

    def getBirthDate(self):
        return self.__birth_date

    def getRegistrationDate(self):
        return self.__Registration_DT

    def getUserId(self):
        query = f"select user_id from Users where email_address='{self.__email_address}';"
        userID = dbManager.fetch(query)
        userID = userID[0]
        return userID

    def registerUser(self):
        query="insert into Users(email_address,first_name,last_name,user_name,password,birth_date,Registration_DT) values (%s,%s,%s,%s,%s,%s,%s);"
        # query="insert into Users(email_address,first_name,last_name,user_name,password,birth_date,Registration_DT) values ('david@yossi.com','david','yossi','davidyossi','123123','2021-11-02','2022-01-19 16:21:24.785227');"
        args = (self.__email_address,self.__first_name,self.__last_name,self.__user_name,self.__password,self.__birth_date,self.__Registration_DT)
        affected_rows = dbManager.commit(query,args)
        return affected_rows ==1
