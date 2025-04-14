# totalmarks=[]

# p1=int(input("enter marks"))
# p2=int(input("enter marks"))
# p3=int(input("enter marks"))
# p4=int(input("enter marks"))
# p5=int(input("enter marks"))
# p6=int(input("enter marks"))
# p7=int(input("enter marks"))

# totalmarks.append(p1)
# totalmarks.append(p2)
# totalmarks.append(p3)
# totalmarks.append(p4)
# totalmarks.append(p5)
# totalmarks.append(p6)
# totalmarks.append(p7)
# totalmarks.sort()

# sum=sum(totalmarks)

# print(totalmarks.count(12)) # ye batata he ki 12 kinti baar he iske andar



for i in range(1,11):
    print(i*2)



# l=[]

# person1=input("enter your name")
# person2=input("enter your name")
# person3=input("enter your name")
# person4=input("enter your name")
# person5=input("enter your name")

# l.append(person1)
# l.append(person2)
# l.append(person3)
# l.append(person4)
# l.append(person5)


# for i in l:
#     if(i.lower().startswith("s")):
#      print(f"hello {i}")

# i=0

# while (i<len(l)):
#    if(l[i].lower().startswith("s")):
#        print(f"hello {l[i]}")
#    i+=1



star=""

for i in range(6):
    star+="*"
    print(star)



num=int(input("enter number"))


for i in range(2,num):
    if(num%i==0):
       print(f"this is not prime number {i}")         

else:
    print("this is prime number")





number=int(input("enter number"))


for i in range(1,number+1):
    print(" "*(number-i),end="")
    print("*"*((2*i)-1),end="")
    print("")
    

number2=int(input("enter number"))

for i in range(1,number2+1):
    print("*"*i)


number3=10

for i in range(1,number3+1):
    if(i<number3):
        if(i==1):
             print("*"*number3)
        elif(i>1):    
          print("*"+" "*(number3-2)+"*")


else:
     print("*"*number3)


number4=10
user=int(input("enter any number"))

while(number4>0):
    print(number4*user)

    number4-=1
  



