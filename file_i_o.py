# 2 tarike ki files hoti he
# text files (.txt,.py etc)
# binary files (.jpg, .dat, etc)


# text files
# iski madad se ham kisi bhi file read ya write kar sakte he

# open("text1.txt") is method kisi bhi file ko connect kar sakte he
# aur ye 2 argument leta he phela files ke liye aur dusra mode yani read write ya jo bhi karna he uske liye 

# read() is method se file ke andar jisna bhi bhi likha he un sab ko get kar sakte he
# readline() is method se ek ek karke line get kar sakte he
# readlines() is method se puri lines ajati he list ke form me
# write() is method se file ke andar write kar sakte he


# r=open for read
# w=open for write
# a=open for appending
# +=open for update

# rb=open for read in binary 

# close() is method se file close kar sakte he


# f=open("text1.txt","r")
# data=f.read()
# print(data)
# f.close()



# f=open("text1.txt")
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data=="")
# f.close()



# f=open("text1.txt")
# data=f.readlines()
# print(data)




# open file with 'with' isse file ko close karne ki zarurat nahi karti he

with open("text1.txt") as f:
    data=f.read()

print(data)


with open("text1.txt","a") as f:
    data=f.write("muneeb\n")




# agar koi file open kare aur vo file nahi bani ho to vo create kar deta he































