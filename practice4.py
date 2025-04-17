
import random

"""
score=0
hiscore=0
"""




def game():
    print("you are playing game")
    score=random.randint(1,100)
    with open("text2.txt") as f:
        hiscore=f.read()

    if(hiscore==""):
        hiscore=0
    else:
        hiscore=int(hiscore)

    if(score>hiscore):
       print(score)
       f=open("text2.txt","w")
       hiscore=f.write(str(score))
       f.close()



game()
















