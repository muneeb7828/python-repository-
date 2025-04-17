
# def greatestnumber(user1,user2,user3):
#     if(user1>user2 and user1>user3):
#         print(f"user1 is bigger number {user1}")
#     elif(user2>user1 and user2>user3):
#          print(f"user2 is bigger number {user2}")      
#     elif(user3>user1 and user3>user2):
#          print(f"user3 is bigger number {user3}")


# user1=int(input("enter number"))
# user2=int(input("enter number"))
# user3=int(input("enter number"))

# greatestnumber(user1,user2,user3)


#  we can prevent of print() new line by this
# print("muneeb",end="")


def sum(n):
     if(n==1):
        return 1
     return n + sum(n-1)



user4=int(input("enter number"))

print(sum(user4))



# def celtiastoferen(c):
    
#     f=(c*9/5)+32
#     return f

# user2=int(input("enter number"))


# print(f"{celtiastoferen(user2)}°F")



# 1 inch= 2.5 cm 


def inchtocm(n):
    
    cm=round(n*2.5)
    return cm


print(f"{inchtocm(2)} cm")


l=["muneeb","ur","rehman","an"]

def removestrip(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n


print(removestrip(l,"an"))



















