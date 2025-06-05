

# operator overloading in python
# python overloading ko support nahi karta matlab same functions but different parameter aur fir jab call karenge to ye nahi chalega


# ye methods tab use karte he jab object me ye plus minus karna ho 
# operator in python can be overloaded using dunder methods for exp  
# p1+p2 = p1._add_(p2) 
# p1-p2 = p1._sub_(p2) 
# p1*p2 = p1._mul_(p2) 
# p1+p2 = p1._truediv_(p2) 

# __str__ ye tab chalta he jab instance object return karta he

# __init__,__add__, jo bhi ese likha hota he use dunder method bolte he
# @property aur jo bhi ese likha hota he use decorator bolte he

# complex()
# complex() ye complex number return karta he isme ek hota he real number ek hota he imaginary number


class employee:
    a=10
    def __init__(self):
        print("this is a constructor of employee")
    @staticmethod           # is method se instance dena nahi padta
    def run():
        print("run fast")      


class coder(employee):
    b=20


class programmer(coder):  
    c=30
    def __init__(self):         
      print("this is contructor of programmer")  

    @property      # iska use karke property ko set kar sakte he lekin iske liye ek setter decorator bhi banana padta he jo isko set karta he nahi to nahi set kar sakte he
    def name(self):
        return self.fname , self.lname
    
    @name.setter    # ye he setter decorator
    def name(self,v):
        self.fname=v.split()[0]    
        self.lname=v.split()[1]


person1=employee()
print(person1.a)

person2=coder()
print(person2.b,person2.a)

person3=programmer()
print(person3.c,person3.a,person3.b)


person3.name="muneeb ur rehman"
print(person3.name)





class calculator:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):    # ye tab call hota he jab 2 instance ke beech me + ka sign laga hota he 
        return self.n+num.n
        
    def __sub__(self,num):    # ye tab call hota he jab 2 instance ke beech me - ka sign laga hota he 
        return self.n-num.n
    
    def __mul__(self,num):    # ye tab call hota he jab 2 instance ke beech me * ka sign laga hota he 
        return self.n*num.n    
    
    def __truediv__(self,num): # ye tab call hota he jab 2 instance ke beech me / ka sign laga hota he 
        return self.n/num.n 
    
    def __len__(self):         # ye tab call hota he jab instance ki length check karte he
        return len(f"{self.n}")
 







ab=calculator(10)
print(ab.n)

bb=calculator(20)
print(bb.n)

cc=calculator(50)
print(cc.n)

print(ab+bb)
print(ab-cc)
print(ab*cc)
print(ab/bb)
print(len(ab))


 
# getter and setter 

class student:


     def __init__(self):
        self.__name="muneeb"


     def get_name(self):
        return self.__name   

     def set_name(self,nam):
        self.__name=nam
        return self.__name

s1=student()
print(s1.get_name())
print(s1.set_name("muneeb ur rehman"))
print(s1.get_name())




# mini project

class MobilePhone:
    def __init__(self):
        self.brand="Samsung"     # public
        self._apps=["Whatsapp","Instagram"]  # protected
        self.__password="1234"   # private


    def unlock_phone(self,entered_password):
        if entered_password == self.__password:
            print("phone unlock")

        else:
            print("wrong password")

    def show_apps(self):
        print(f"Installed Apps: {self._apps}")



phone=MobilePhone()

print(phone.brand)


print(phone._apps)


# print(phone.__password) this will give error 

print(phone._MobilePhone__password)    # is tarike se bhi private property ko dekh sakte he


phone.unlock_phone("1234")









