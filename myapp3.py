import requests
from json import dumps            



URL ='http://127.0.0.1:8000/studentapi/'    
def updated_data():
  dataa={
  'id':20,  
  'name':'atif',
  'city':'bhopal'
  }

  json_data=dumps(dataa) 
  data=requests.put(url=URL, data=json_data)  
  print(data.json())



updated_data()

def delete_data():
  dataa={
  'rollno':52
  }

  json_data=dumps(dataa) 
  data=requests.delete(url=URL, data=json_data)  
  print(data.json())



# delete_data()







