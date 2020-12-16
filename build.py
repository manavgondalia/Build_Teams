import random
l1 = list(range(1,83))
p = int(input("Total number of players: "))
n = int(input("Number of team members: "))
l2 = []
l3 = []

for i in range(p//n):
    l3 = []
    x = 0
    y = 0
    z = 0
    a = 0
    x = random.choice(l1)
    l1.remove(x)
    y = random.choice(l1)
    l1.remove(y)
    z = random.choice(l1)
    l1.remove(z)
    a = random.choice(l1)
    l1.remove(a)

    
    l3.append(x)
    l3.append(y)
    l3.append(z)
    l3.append(a)
    l2.append(l3)

    
print("The teams: ",l2)
print("Players remaining: ",l1)
