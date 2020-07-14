from locust import task,TaskSet
import re
import logging ,sys
import CSVWriter


class AAA_Add_to_cart(TaskSet):


    @task
    def addToCart(self):


        with self.client.get("/index.php",
                             headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                      "Accept-Encoding": "gzip, deflate",
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                      "Connection": "keep-alive",
                                      "Host": "automationpractice.com",
                                      "Upgrade-Insecure-Requests": "1"},
                             name="A101_Homepage",catch_response=True) as response:

            request_meta = response.locust_request_meta

            #verification
            if len(re.compile("Search").findall(response.text)) == 0:
                response.failure(response.reason)
                response_text= str(response.text)
                #logging.info("A101_Homepage_Fail " + response.text)
            else:
                response_text = "NA"
                #logging.info("A101_Homepage_Pass " + response.text)

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))




        with self.client.get("/index.php?controller=search&orderby=position&orderway=desc&search_query=shirt&submit_search=",
                             headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                      "Accept-Encoding": "gzip, deflate",
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                                      "Referer": "http://automationpractice.com/index.php",
                                      "Upgrade-Insecure-Requests": "1",
                                      "Connection": "keep-alive",
                                      "Host": "automationpractice.com"},
                             name="A102_Search_Product",catch_response=True) as response:

            request_meta = response.locust_request_meta

            #verification
            if len(re.compile("been found").findall(response.text)) == 0:
                response.failure(response.reason)
                response_text = str(response.text)
                #logging.info("A102_Search_Product_Fail " + response_text)
            else:
                response_text = "NA"
                #logging.info("A102_Search_Product_Pass " + response_text)

        CSVWriter.csvWriter(request_meta["name"], str(response.status_code), str(response.reason),
                            str(response.headers), str(response_text))



