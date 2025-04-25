
# incapculation
# incapculation matlab jo sirf class me hi accesible ho 

# abstraction
# abstraction iska use karke class ko abstract kar sakte he matlab ki agar abstraction decorator laga diya kisi method pe
# to jab bhi vo class inherit karenge kisi dusri class me to dusri class me bhi vo method dena padega
# iskeliye phele abc library se ABD class ko import karna padta he fir usme abstractmethod naam ka function bana hota he
# jo ki @abstractmethod is decorator se call hojata he
from abc import ABC,abstractmethod

# inheritance
# inheritance ye pura javascript ki tarah hota he iska use karke dusri class ke methods ko bhi use kar sakte he

# __name ye lagane se method ya proper hide ho jati bas class ka name use karke hi dekh sakte he isntance me nahi dekh sakte
# agar aap chate ho ki jo hide kiya he vo access kar sake to class me method galana hoga aur usme vo return karna hoga
# aur jab instance me access karna ho to bhi usi method se hi karna hoga

# polymorphism
# polymorphism matlab ek cheez lekin kaam bohot saare for exp same methods but different work


class employee:
    a=10
    def __init__(self):
        print("this is a constructor of employee")

    def run(self):
        print("run fast")     



class coder(employee):   # inheritance single
    b=20

class programmer(coder,employee):   # inheritance multiple
    c=30
    def __init__(self):         
      super().run() # super() is method se parent ke methods ko call kar sakte he child me lekin bas ye __init__ constructor me chalta he

class manager(programmer):          # inheritance multilevel matlab iska parent prgrammer aur programmer ka parent coder aur coder ka parent employee to ye sab ki properties use kar sakta he
    d=40
    @classmethod   # agar ham chate he class attribute change na ho to iska use karte he
    def __init__(cls):
        print(f"this is a constructor of manager and the property of this class is {cls.d}")

    



person1=employee()
print(person1.a)

person2=coder()
print(person2.b,person2.a)

person3=programmer()
print(person3.c,person3.a,person3.b)

person4=manager()
person4.d=20
person4.__init__()











