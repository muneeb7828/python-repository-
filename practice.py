totalmarks=[]

p1=int(input("enter marks"))
p2=int(input("enter marks"))
p3=int(input("enter marks"))
p4=int(input("enter marks"))
p5=int(input("enter marks"))
p6=int(input("enter marks"))
p7=int(input("enter marks"))

totalmarks.append(p1)
totalmarks.append(p2)
totalmarks.append(p3)
totalmarks.append(p4)
totalmarks.append(p5)
totalmarks.append(p6)
totalmarks.append(p7)
totalmarks.sort()

sum=sum(totalmarks)

print(totalmarks.count(12))
