
l=[1,"muneeb",False,"this",20]  # List
t=(1,"muneeb",False,"this",24)  # tuple
string="muneeb ur rehman"       # string
s={1,2,3,4,5,67}                # set
dic={"name":"muneeb","isgraduate":True,"age":24} # dict


# ye for in loop hota he ye list tuple set aur string ki value ke liye hota he aur ye javascript me for of loop ki tarah hota he
# aur isme i ko phele declare nahi karte 

for i in l:
    print(i)


for i in t:
    print(i)

for i in string:
    print(i)

for i in s:
    print(i)


for i in dic:
    print(i,dic[i])



# while loop in python
# isse me variable ko define kana padta he phele


k=0

while(k<len(l)):
     print(l[k])
     k+=1



# for in range() loop 
# ye for loop hota he aur range() kya karta he ye 3 argument leta he start stop step_size 
# phele hota he kaha se start karna he aur dusra hota he kaha stop karna he aur teesra hota he step ko jump karne ke liye
# aur agar khali ek argument denge to vo khali stop ke liye hoga



for i in range(0,len(l)):
    print(l[i])


# for loop with else

for i in l:
    print(i)

else:
    print("done")  




for i in range(0,100):
    if(i !=35):
        print(i)
        


del dic # isse pura dict delete ho jata he


lis=["name","gmail","contact","address"]
lis2=["muneeb","muneeb@gmail.com",82695277774,"idgah hills bhopal"]

lis3=zip(lis,lis2)  # ye zip method hota he ye obj return karta he jo ke readable nahi hota to isko convert karna padta dict ya list me
print(dict(lis3))   # ye dict me convert karta he
print(list(lis3))   # ye list me convert karta he
 











