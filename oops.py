
# incapculation
# incapculation hota he vo class ke andar jitne bhi method ka ya proterty hoti he un sab ko batata he

# abstraction
# abstraction hota he vo class me jo chupa te he usko bolte he

# inheritance
# inheritance ye pura javascript ki tarah hota he iska use karke dusri class ke methods ko bhi use kar sakte he





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











