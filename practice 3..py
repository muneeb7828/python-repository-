
import random

"""
stone=1
paper=0
scisor=-1
"""

computer=random.choice([0,-1,1])

user=input("enter you want")

dic={"stone":1,"paper":0,"scisor":-1}

if(computer==-1):
    print(f"computer scisor \nyou {user}")
elif(computer==1):
    print(f"computer stone \nyou {user}")  
else:
    print(f"computer paper \nyou {user}")



if(user=="scisor" or user=="paper" or user=="stone"):
    you=dic[user]
else:
    you=-2    


if(computer==you):
    print("draw")

else:
    if(computer==-1 and you==1): 
        print("you are winner")

    elif(computer==-1 and you==0): 
        print("computer is winner") 

    elif(computer==1 and you==0): 
        print("you are winner") 

    elif(computer==1 and you==-1): 
        print("computer is winner") 


    elif(computer==0 and you==-1): 
        print("you are winner") 

    elif(computer==0 and you==1): 
        print("computer is winner") 

    else:
        print("you can only type stone paper")    


 

































