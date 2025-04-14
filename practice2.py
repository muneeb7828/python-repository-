
def greatestnumber(user1,user2,user3):
    if(user1>user2 and user1>user3):
        print(f"user1 is bigger number {user1}")
    elif(user2>user1 and user2>user3):
         print(f"user2 is bigger number {user2}")      
    elif(user3>user1 and user3>user2):
         print(f"user3 is bigger number {user3}")


user1=int(input("enter number"))
user2=int(input("enter number"))
user3=int(input("enter number"))

greatestnumber(user1,user2,user3)


#  we can prevent of print() new line by this
print("muneeb",end="")


def sum(n):
     if(n==1):
        return 1
     return n + sum(n-1)



user4=int(input("enter number"))

print(sum(user4))



















