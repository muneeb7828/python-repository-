from json import dumps   
import requests


URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=dumps(data)
    response= requests.get(url =URL, data =json_data)
    data=response.json()
    print(data)
        
get_data()















