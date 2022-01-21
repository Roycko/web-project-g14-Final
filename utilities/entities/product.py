from utilities.db.db_manager import dbManager

class Product:
    __name = None
    __num_of_pcs = None
    __price = None
    __image_src = None
    __is_vegan = None
    __is_gluten_free = None
    __is_birthday_cake = None
    __is_top_seller = None

    def __init__(self,name,num_of_pcs,price,image_src,is_vegan,is_gluten_free,is_birthday_cake,is_top_seller):
        self.__name = name
        self.__num_of_pcs = num_of_pcs
        self.__price = price
        self.__image_src = image_src
        self.__is_vegan = is_vegan
        self.__is_gluten_free = is_gluten_free
        self.__is_birthday_cake = is_birthday_cake
        self.__is_top_seller = is_top_seller

    def getName(self):
        return self.__name

    def getNumOfPieces(self):
        return self.__num_of_pcs

    def getPrice(self):
        return self.__price

    def getImage(self):
        return self.__image_src

    def getVegan(self):
        return self.__is_vegan

    def getGlutenFree(self):
        return self.__is_gluten_free

    def getBirthDayCake(self):
        return self.__is_birthday_cake

    def getTopSeller(self):
        return self.__is_top_seller

