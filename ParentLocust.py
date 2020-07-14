import csv
import re
import GlobalVariables


from AddToCart_01 import AAA_Add_to_cart
from Register_02 import BBB_Register
from bs4 import BeautifulSoup

from locust import HttpUser,TaskSet,task,between

URL= None
PROTOCOL = None
Add_to_cart_weight= None
register_weight= None


class readConfigFile():

    global PROTOCOL,URL,Add_to_cart_weight,register_weight

    with open("config.xml") as f:
        y= BeautifulSoup(f.read(),"html.parser")
        PROTOCOL = y.other.protocol.contents[0]
        URL = y.other.url.contents[0]
        Add_to_cart_weight= y.weight.addtocart.contents[0]
        register_weight = y.weight.register.contents[0]




class addtoCart_scn_01(HttpUser):

    weight= int(Add_to_cart_weight) # 60% of total users
    min_wait=1000
    max_wait=2000
    host= PROTOCOL + URL
    tasks = [AAA_Add_to_cart]



class register_scn_02(HttpUser):

    weight= int(register_weight) # 40% of total users
    min_wait=1000
    max_wait=2000
    host = PROTOCOL + URL
    tasks = [BBB_Register]

    #for reading data file for this scenario and keeping it in list
    def __init__(self,value):

        self.value=10

        super(register_scn_02, self).__init__(value)
        GlobalVariables.Register_deatils = None

        if GlobalVariables.Register_deatils is None:
            with open('02_data_register.csv', 'r') as f1:
                reader1 = csv.reader(f1)
                GlobalVariables.Register_deatils = list(reader1)




