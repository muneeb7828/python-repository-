
# Object Oriented Programming


# Class in Object Oriented Programming
# ye javascript me class constructor ki tarah hota he
# iska use karke ek class se baar baar instance bana sakte he
# aur ye ek form ki tarah hota he jese kisi ne form fill kiya to uske naam ka form hojayga aur nahi kiya to kuch nahi hoga
# aur isme abstraction aur incapsulation bhi hota javascript ki tarah






# basic class

class employee:  
    name="sami"      
    language="python"
    salary=1200000
    
    def __init__(self):
        print("i am creating an object")

    def getinfo(s):   # method in class aur iske andar ek parameter dena compalsory hota he kyuki jab isko kisi instance ke sath call karte he to bydefalt ek argument leta he usi instance ke naam ka 
        print(f"the name is {s.name}.The salary is {s.salary}")

    @staticmethod     # ye likhne se parameter me likhna zaruri nahi hota aur staticmethod ye decorator hota he
    def greet():
        print("Good morning")
    


# class ke andar jo property likhte he usko class attrbutes bolte he 
# aur jo instance create karke property set karte he usko instance attribute bolte he
# aur instance attribute zada preference lete he class attrbutes

muneeb=employee()
muneeb.name="muneeb"
print(muneeb.name,muneeb.language,muneeb.salary)
print(muneeb.getinfo())  # employee.getinfo(muneeb) jab call karte he to ye esa hojata he

sami=employee()
sami.getinfo() 
sami.greet()



# _init_() constructor

# _init_() ye method ye tab chalta he object create hota he
# _init_() isko constructor bhi bolte he
# _init_() isko call karna nahi padta ye apne aap chal jata he







class Cars:
    company="maruti"
    color="red"
    price=2000000

    def __init__(self,name,color,price):   
        self.company=name  # aur ye instance attribute ko hi change karte he
        self.color=color
        self.price=price
    
     




audi= Cars("audi","black",4000000)


print(audi.company,audi.price,audi.color)



































