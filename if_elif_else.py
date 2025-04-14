
#  if elif else ladder in python


a=int(int(input("enter your age: ")))


if(a<18 and a>0):
    print("you are below 18")

elif(a==18):
    print("you are 18")
    
elif(a>18):
    print("you are above 18")

elif(a<0):
    print("pleae type a correct age")



# marks1=int(input("type your marks"))
# marks2=int(input("type your marks"))
# marks3=int(input("type your marks"))
# marks4=int(input("type your marks"))


# totalpercentage=100*(marks1+marks2+marks3+marks4)/400

# if(totalpercentage>40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
#    print(f"you are passed and your percentage is {totalpercentage}")

# else:
#     print(f"you are failed with grade of {totalpercentage}")



s1="click here"
s2="go to shopping"
s3="visit now"
s4="subscribe here"



user1=input("type anything")

if(user1 in s1 or user1 in s2 or user1 in s3 or user1 in s4):
    print("this is a spam")
  
else:
    print("this is not a spam")





var1="hello my name is muneeb"

user2=input("type anything")

if(user2.lower() in var1):
    print(user2)



























































