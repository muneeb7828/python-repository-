
def generate(n):
        with open(f"tables/table{n}.txt","w") as f:
         for i in range(1,11):
          print(f"{n}*{i}={n*i}\n")
          f.write(f"{n}*{i}={n*i}\n")









for i in range(2,11):
    generate(i)












