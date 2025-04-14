

# ye syntax hota he python me funtion ka

def func():
    print(f"hellow muneeb")



func()

# types of functions in python

# isme me 2 type ke functions hote he build in function and user defined function

# exp of build in len() print() range() 

# exp of user defined function user defined function vo hote he jo user banata he



# default parameters
# isme ham function ke andar default parameter bhi de sakte he 
# jese agar argument nahi di to vo use hoga



def gooday(name,ending="thank you"):
    print(f"""good day {name} \n {ending} """)


gooday("muneeb")


# recurrsions in python
# ye factorial ya sum nikal ne ke liye hote he


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)



user1=int(input("enter number"))

print(factorial(user1))












































