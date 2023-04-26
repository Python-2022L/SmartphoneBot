from tinydb import TinyDB, Query
import requests

class DB:
    def __init__(self):
        self.base_url = "http://127.0.0.1:5000"

    def get_tables(self):
        """
        To get the list of all the tables in the database
        """
        response = requests.get(self.base_url + "/smartphone")
        return response.json()['brands']
        
    def getPhone(self,brand,idx):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """
        response = requests.get(self.base_url + "/smartphone/" + brand + "/" + str(idx))
        return response.json()

    def get_phone_list(self,brand):
        """
        Return phone list
        """
        response = requests.get(self.base_url + "/smartphone/" + brand)
        print(response.json())
        return response.json()['phones']
