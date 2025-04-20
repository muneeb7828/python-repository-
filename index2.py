
# comprehension

# ye code ko aur asaan bana deta he
# ye list or dict ke liye hota he

# comprehension in list

num=[]

for i in range(1,51):
    if(i%5==0):
        num.append(i)
print(num)
# this is without comprehension  

num3=[i for i in range(1,51)if(i%5==0)]
print(num3)
# this is with comprehension


# comprehension in dict

num1=[1,2,3,4,5,6,7,8,9]

dict1={}

for i in num1:
    dict1[i]=i**2

print(dict1)
# this is without comprehension  

dic2={i:i**2 for i in num1}
print(dic2)
# this is with comprehension









































