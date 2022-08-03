import requests
import time

url = 'https://www.google.com.tw/'

start_time = time.time()


def send_req(url):
    print("Send a request at", time.time() - start_time, "seconds.")
    
    requests.get(url)
    
    print("Receive a response at", time.time() - start_time, "seconds.")


for i in range(10):
    send_req(url)
