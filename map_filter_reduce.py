
# enumerate()
# ye index bhi deta he jab loop chalate he tuple ke form me aur bagair loop ke ye object return karta he zip() ki tarah

list1=[112,223,323,43,523,62,73,83,93]

for i,value in enumerate(list1):
    print(i,value)




# lambda
# ye aero function ki tarah hota he
# ye ek line ke liye hota he
# aur isme if else lagate he to print phele karna padta he


variable1=lambda name:print(f"hello {name}")
variable1("muneeb")

# map() in python
# ye pura javascript ki tarah hota he
# aur ye 2 argument leta he phela function ke liye aur dusra list ya dict ke liye
# aur ye object return karta he zip() ki tarah to isko convert karna padta he list me ya kisi me bhi
# aur iske callback function 1 hi parameter leta he value ka


list2=[1,2,3,4,5,6,7,8,9]

square=map(lambda v:v*v,list2)
print(list(square))

# filter()
# ye pura map method ki tarah hota he bas isme jo condition true hoti he usko hi return karta he
# aur iske callback function 1 hi parameter leta he value ka


list3=[12,22,33,44,55,67,78,89,90]

even=filter(lambda v:v%2==0,list3)
print(list(even))


# reduce()
# ye pura javascript ki tarah hota he bas isme import karna padta he ese  from functools import reduce
# aur iske callback function 2 parameter leta he phela initaial value ke liye aur dusra puri value ke liye
# aur ye object return nahi karta


from functools import reduce
list3=[12,3,4,5,6,7,8]
sum=reduce(lambda i,v:i+v,list3)
print(sum)




















