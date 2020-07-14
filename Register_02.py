from locust import TaskSet,task
import re
import logging,sys
import GlobalVariables
import CSVWriter


class BBB_Register(TaskSet):


    fname= "Not Found"
    lname= "Not Found"
    email= "Not Found"
    mobileno= "Not Found"
    password= "Not Found"



    @task
    def register(self):


        #homepage

        with self.client.get("/index.php",
                             headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "en-US,en;q=0.9",
                                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                 "Connection": "keep-alive",
                                 "Host": "automationpractice.com",
                                 "Upgrade-Insecure-Requests": "1"},
                             name="B101_Homepage", catch_response=True) as response:

            request_meta = response.locust_request_meta

            if len(re.compile("Search").findall(response.text)) == 0:
                response.failure(response.reason)
                response_text= str(response.text)
                #logging.info("B101_Homepage_Fail " + response_text)
            else:
                response_text = "NA"
                #logging.info("B101_Homepage_Pass " + response_text)

        CSVWriter.csvWriter(request_meta["name"],str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))




        #ClickonSign

        with self.client.get("/index.php?controller=my-account",
                             headers={
                                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                 "Accept-Encoding": "gzip, deflate",
                                 "Accept-Language": "en-US,en;q=0.9",
                                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                 "Referer": "http://automationpractice.com/index.php",
                                 "Connection": "keep-alive",
                                 "Host": "automationpractice.com"},
                             name="B102_Click_on_Signin_01", catch_response=True) as response:
            request_meta = response.locust_request_meta
            #logging.info("B102_Click_on_Signin_01 "+str(response.text))

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response.text))

        with self.client.get("/index.php?controller=authentication&back=my-account",
                             headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                      "Accept-Encoding": "gzip, deflate",
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                      "Referer": "http://automationpractice.com/index.php",
                                      "Connection": "keep-alive",
                                      "Host": "automationpractice.com"},
                             name="B102_Click_on_Signin_02",catch_response=True) as response:

            request_meta = response.locust_request_meta

            if len(re.compile("Create an account").findall(response.text)) == 0:
                response.failure(response.reason)
                response_text= str(response.text)
                #logging.info("B102_Click_on_Signin_02_Fail " + response_text)

            else:
                response_text= "NA"
                #logging.info("B102_Click_on_Signin_02_Pass " + response_text)

            pattern = re.compile("var token = '(.*)'")
            result = pattern.findall(response.text)
            token = result[0]
            logging.info("Token " +token )

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))





        #click on create an account

        if len(GlobalVariables.Register_deatils) > 0:
            self.email,self.fname,self.lname,self.password,self.mobileno= GlobalVariables.Register_deatils.pop()

            with self.client.post("/index.php",
                                  headers={"Accept": "application/json, text/javascript, */*; q=0.01",
                                           "Accept-Encoding": "gzip, deflate",
                                           "Accept-Language": "en-US,en;q=0.9",
                                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                           "X-Requested-With": "XMLHttpRequest",
                                           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                           "Content-Length": "140",
                                           "Referer": "http://automationpractice.com/index.php?controller=authentication&back=my-account",
                                           "Origin": "http://automationpractice.com",
                                           "Connection": "keep-alive",
                                           "Host": "automationpractice.com"},
                                  data={"controller": "authentication",
                                        "SubmitCreate": "1",
                                        "ajax": "true",
                                        "email_create": self.email,
                                        "back": "my-account",
                                        "token": result[0]},
                                  name="B103_Enter_Email_Click_on_Create_Account", catch_response=True) as response:

                request_meta= response.locust_request_meta

                if len(re.compile("false").findall(response.text)) == 0:
                    response.failure(response.reason)
                    response_text = str(response.text)
                    #logging.info("B103_Enter_Email_Click_on_Create_Account_Fail " + response_text)

                else:
                    response_text = "NA"
                    #logging.info("B103_Enter_Email_Click_on_Create_Account_Pass " + response_text)



        else:

            logging.info("No more data to register")

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))

        #click on register


        with self.client.post("/index.php?controller=authentication",
                              headers={"Accept": "application/json, text/javascript, */*; q=0.01",
                                       "Accept-Encoding": "gzip, deflate",
                                       "Accept-Language": "en-US,en;q=0.9",
                                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                       "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                       "Content-Length": "375",
                                       "Referer": "http://automationpractice.com/index.php?controller=authentication&back=my-account",
                                       "Origin": "http://automationpractice.com",
                                       "Upgrade-Insecure-Requests": "1",
                                       "Connection": "keep-alive",
                                       "Host": "automationpractice.com"},
                              data={"id_gender": "1",
                                    "customer_firstname": self.fname,
                                    "customer_lastname": self.lname,
                                    "email": self.email,
                                    "passwd": self.password,
                                    "days": "",
                                    "months": "",
                                    "years": "",
                                    "firstname": self.fname,
                                    "lastname": self.lname,
                                    "company": "QK",
                                    "address1": "Worli",
                                    "address2": "",
                                    "city": "Mumbai",
                                    "id_state": "1",
                                    "postcode": "12345",
                                    "id_country": "21",
                                    "other": "",
                                    "phone": "",
                                    "phone_mobile": self.mobileno,
                                    "alias": "My address",
                                    "dni": "",
                                    "email_create": "1",
                                    "is_new_customer": "1",
                                    "back": "my-accounut",
                                    "submitAccount": ""},
                              name="B104_Click_on_resiter",catch_response=True) as response:

            request_meta = response.locust_request_meta

            if len(re.compile("My account").findall(response.text)) == 0:
                response.failure(response.reason)
                response_text= str(response.text)
                #logging.info("B104_Click_on_resiter_Fail " + response_text)

            else:
                response_text= "NA"
                #logging.info("B104_Click_on_resiter_Pass " + response_text)

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))

        with self.client.get("/index.php?controller=my-account",
                             headers={"Accept": "application/json, text/javascript, */*; q=0.01",
                                      "Accept-Encoding": "gzip, deflate",
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                      "Referer": "http://automationpractice.com/index.php?controller=authentication&back=my-account",
                                      "Upgrade-Insecure-Requests": "1",
                                      "Connection": "keep-alive",
                                      "Host": "automationpractice.com"},
                             name="B105_register_01", catch_response=True) as response:

            request_meta = response.locust_request_meta

            if len(re.compile("Sign out").findall(response.text)) == 0:
                response.failure(response.reason)
                response_text = str(response.text)
                #logging.info("B105_register_01_Fail " + response_text)

            else:
                response_text = "NA"
                #logging.info("B105_register_01_Pass " + response_text)

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))

        #logout


        with self.client.get("/index.php?mylogout=",
                            headers={"Accept": "application/json, text/javascript, */*; q=0.01",
                                      "Accept-Encoding": "gzip, deflate",
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                      "Referer": "http://automationpractice.com/index.php?controller=my-account",
                                      "Upgrade-Insecure-Requests": "1",
                                      "Connection": "keep-alive",
                                      "Host": "automationpractice.com"},
                            name="B106_signout_1",catch_response=True) as response:

            request_meta = response.locust_request_meta

            logging.info("B106_signout_1" +str(response.text))

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response.text))


        with self.client.get("/index.php?controller=my-account",
                            headers={"Accept": "application/json, text/javascript, */*; q=0.01",
                                      "Accept-Encoding": "gzip, deflate",
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                      "Referer": "http://automationpractice.com/index.php?controller=my-account",
                                      "Upgrade-Insecure-Requests": "1",
                                      "Connection": "keep-alive",
                                      "Host": "automationpractice.com"},
                            name="B106_signout_2",catch_response=True) as response:

            request_meta = response.locust_request_meta

            logging.info("B106_signout_2" +str(response.text))

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response.text))


        with self.client.get("/index.php?controller=authentication&back=my-account",
                            headers={"Accept": "application/json, text/javascript, */*; q=0.01",
                                      "Accept-Encoding": "gzip, deflate",
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                      "Referer": "http://automationpractice.com/index.php?controller=my-account",
                                      "Upgrade-Insecure-Requests": "1",
                                      "Connection": "keep-alive",
                                      "Host": "automationpractice.com"},
                            name="B106_signout_3",catch_response=True) as response:

            request_meta = response.locust_request_meta

            if len(re.compile("Login - My Store").findall(response.text)) ==0 :
                response.failure(response.reason)
                response_text = str(response.text)
                #logging.info("B106_signout_3_Fail " + response_text)

            else:
                response_text = "NA"


        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))




