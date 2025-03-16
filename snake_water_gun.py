inputs=[1,2,3]
import random
computer = random.choice(inputs)

# c I  s  w  g
# p s  0  1 -1
#   w -1  0  1
#   g  1  -1  0

matrix=[["I","snake","water","gun"],["snake",0,1,-1], ["water",-1,0,1],["gun",1,-1,0]]
# dic={"snake":1,"water":2,"gun":3}
score=[]
print("Are you ready?")
ask=input("YES OR NO:")
ask=True if (ask=="yes") else False
if ask:
    for round in range(5):
        print("Round:",round+1)
        player = int(input('Enter the entry from "snake"=1,"water"=2,"gun"=3:'))
        print("Your input:",player)
        print("Computer's input:",computer)
        score.append(matrix[player][computer])
        print("Score is:",matrix[player][computer],"\n")
    print("The score set is:",score)
    from functools import reduce
    scr = reduce(lambda x, y: x + y, score)
    print("The total score is:", scr)
else:
 print("_____EXITED_____")
