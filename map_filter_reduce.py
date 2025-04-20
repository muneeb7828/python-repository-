
# enumerate()
# ye index bhi deta he jab loop chalate he tuple ke form me aur bagair loop ke ye object return karta he zip() ki tarah

list1=[112,223,323,43,523,62,73,83,93]

for i,value in enumerate(list1):
    print(i,value)

# comprehensions
# ye code aur asaan bana deta he
# ye list aur dict ke liye hota he 

# list comprehension

num=[i for i in range(1,51) if(i%5==0)]
print(num)

# dict comprehension

dic={i:i*i for i in range(1,10)}
print(dic)

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


# try and except and else
# ye error ko hatane ke liye hota he

num1=int(input("enter number"))
num2=int(input("enter number"))

try:
    num3=num1/num2
    print(num3)
except Exception as e:
    print("you cannot write 0 in division")

except ValueError as v:   # ye tab chalega jab value error hoga
    print(v)

except ZeroDivisionError as z:  # ye tab chalega jab ZeroDivisionError hoga
    print(z)    

else:                            # ye is liye hota he try wala chale tabhi ye chale 
    print("you entered correct")



# raise ZeroDivisionError("you entered wrong")
# ye error lane ke liye hota he



# match case
# ye swich case ki tarah hota he

def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"        
        case 500:
            return "Internet Server Error"
        case _:
            return "unknown status"

print(http_status(100))








