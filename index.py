var1="muneeb"
print(var1)

# jese java script me datatypes hote he vese hi isme class hote he

print(type(var1))   # class 'str'

print("m" in var1)   # memberhsip operator

num=20
print(type(num))  # class 'int'

num2=12.20
print(type(num2)) # class 'float'

name="muneeb"
array=["hellow","my","name","is",name,24]
print(array)
print(type(array)) # class 'List'

obj={"name":"muneeb"}
print(type(obj))  # class 'dict'

Fname="Muneeb"
Lname="ur rehman"


obj2={Fname,Lname,24}
print(type(obj2))   # class 'set'


variale="muneeb","ur","rehman","age",24
print(type(variale))  # class 'tuple'



# var4=input("enter your name")  # ye prompt ke liye hota he
# print(type(var4))


# var5=int(input("enter your number"))  # isse input number me convert ho jata he
# print(type(var5))


# var6=float(input("enter your number"))  # isse input float me convert ho jata he
# print(type(var6))


# type casting
# matlab uska type badalna

num2=10
change=str(num2)
print(type(change))



str2="python is a langauge of langauge backend"
print(str2.upper())
print(str2.lower())
print(len(str2))   # this is for length
print(str2[0:2])   # this is for slice
print(Fname+" "+Lname) # this is for concat
print(str2.startswith("python"))
print(str2.endswith("backend"))
print(str2.capitalize())
print(str2.replace("backend","frontent"))
print(str2.find("langauge"))
print(str2.removeprefix("py")) # ye shuru se check karta he
print(str2.removesuffix("end")) # ye end se check karta he
count=str2.count("a") # this is for count
print(count)
print(str2.split(" ")) # isse string ko List bana sakte he







var6="""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star."""


print(var6)



# string aur tuple immutible hote jo change nahi hote to agar change karna he to return karna hoga 
# aur List yani array ye mutable hote he jo ke change ho jate he
# aur dict mutable hota he jo ki change ho jata he




string=f"hellow my name is {name}"  # isse variable ko string me daal sakte he
print(string)



# escaped character in python 
# \n \t \r \"

lis=[23,34,1,45,6,34,54]

# List methods
# lis.sort()    ye sequentially arrange kar deta he   
# lis.reverse() ye pure list ko reverse kar deta he
# lis.append()  ye push ki tarah hota he
# lis.insert(3,12) ye slice ki tarah hota he bas ye delete nahi karta add karta he
# lis.pop(2) ye pop kar leta he jo bhi index daalte he usko
# lis.remove() ye remove kar deta he jo bhi value isme likhte he usko




a=(1,2,3,4)  # ese bhi tuple bana sakte he
b=()  # ese empty tuple bana sakte he
print(type(b))


# tuples methods

print(a.count(2)) # ye count batata he
print(a.index(4)) # ye index batata he
print(a[1:3])     # ye slice ke liye hota he



tupl=("muneeb","ur","rehman")
ab,ac,ad = tupl
print(ab)



# dict

marks={
"muneeb":90,
"rehman":40,
"saad":34,
0:"muneeb"    
}


print(marks)


# methods in dict


print(marks.items())  # isse key value pair alag hojate he tuple ke form me  
print(marks.keys())   # isse dict ki keys show hoti he
print(marks.values()) # isse dict ki values show hoti he
print(marks.get("muneeb")) # isse dict ki key ki value ko get kar sakte he agar vo he to nahi to vo none return karega
marks.update({"muneeb":95,"yayah":80})  # isse dict ko update kar sakte he jese kisi key ko update karna he ya nayi key add karni he 
print(marks)
marks_copy=marks.copy() # ye shallow copy bana deta he
print(marks_copy)
marks.clear() # ye pura dict ko clear kar deta he
print(marks)


marks2={
"muneeb":90,
"rehman":40,
"saad":34,
0:"muneeb"      
}

marks3=marks2.pop("muneebs","hoooo") # ye kya karta he ki ye original dict me se us key ko hata deta he aur return kar deta he agar key nahi he to default value bhi deni padti he
print(marks3)


marks4=marks2.popitem() # ye last wale key ko pop karke return kar deta he tuple ke form me
print(marks4)




# some sets informations

# sets kabhi repeat nahi hote
# sets unordered hote he aur unindex hote he



# sets methods

sett={1,23,34,45,56}

sett.add(4)
sett2=sett.copy()
sett2.clear()
print(sett2)


newset=set() # is method se empty set bana sakte he


sett3={"muneeb","ur","rehman",24}
sett3.remove(24) # ye remove kar deta he agar he to nahi to error show hota he
print(sett3)


# sett3.union() # ye combine kar deta he dono sets ko  
# sett3.intersection() # ye jo similar he usko return karta he
# sett3.issubset()  # subset vo hota he jese ham kisi set ko compare kar rahe he agar set me he to vo subset hoga
# sett3.issuperset() # superset vo hota he agar kisi set ka subset he to vo uska superset hoga
# sett3.difference() # ye 2 sets ko compare karta he aur ye vo value return karta he jo value different hoti

print(sett3.union(sett))
print(sett3.intersection(sett))


print("muneeb",end="")  # print ke andar ye likhne se line break nahi hoti 



# sort in simple
# ye sequentially arrange kar deta he list ko yani small to bigger
# lis.sort(reverse=True) ese kare to reverse format me deta he


# sort in advance
# ye key= property ke saath ek function leta he aur iska use karke ham value ko sahi tarike se arrange kar sakte he

fruits=["apple","orange","banana","lichi","mangoass"]

fruits.sort(key=lambda v:len(v))
print(fruits)


# sorted()
# ye bhi sort method ki tarah hota he bas ye 2 argument leta he phela itrator ke liye aur dusra function ke liye 
# aur ye return karta he

fruits2=["apple","orange","banana","lichi","mango"]

list1=sorted(fruits2,key=lambda v:len(v))
print(list1)













