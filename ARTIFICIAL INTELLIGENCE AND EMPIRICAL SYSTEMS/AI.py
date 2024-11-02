import random
from random import randint

V = 5  # Number of cities
city_name = "ABCDE"  # Names of the cities
lista = [['1-2', 4], ['1-3', 4], ['1-4', 7], ['1-5', 3], ['2-3', 2], ['2-4', 3], ['2-5', 5], ['3-4', 2], ['3-5', 3], [
    '4-5', 6]]  # The cost moving between cities
trips = []
s = []
for i in range(100):
    num = 0
    raw = []
    while num != 5:
        if num == 0:
            raw.append(1)
            num = 1
        if num == 1:
            raw.append(randint(2, 5))
            num = 2;
        else:
            x = randint(2, 5)
            end = 0
            while end == 0:
                if x in raw:
                    x = randint(2, 5)
                else:
                    end = 1
            raw.append(x)
            num += 1
        if num == 5:
            raw.append(1)
    trips.append(raw)
    arth = 0
    for i in range(5):
        convert1 = str(raw[i])
        convert2 = str(raw[i + 1])
        trip = convert1 + '-' + convert2
        trip2 = convert2 + '-' + convert1
        for j in range(10):
            if trip.__eq__(lista[j][0]) or trip2.__eq__(lista[j][0]):
                arth += lista[j][1]
    arth = 1 / arth
    s.append(arth)
print("paths")
print(trips)
print("percents:")
print(s)
goneas = []
for j in range(50):
    random_num = random.choice(s)
    for i in range(100):
        if random_num == s[i]:
            goneas.append(trips[i])
            break
print("parents:")
print(goneas)
kids = []
skids = []
z = ""
k = ""
for i in range(100):
    random_g = random.choice(goneas)
    random_g2 = random.choice(goneas)
    comp1 = []
    comp2 = []
    for i in range(4):
        comp1.append(random_g[i + 1])
        comp2.append(random_g2[i + 1])
    x = 0
    end = 0
    merg = []
    while x != 5 and end != 1:
        num = randint(0, 1)
        if x == 0:
            merg.append(1)
            x = 1
        elif num == 0:
            for i in range(x):
                if merg[i] == random_g[x]:
                    end = 1
            if end == 0:
                merg.append(random_g[x])
                x += 1
        elif num == 1:
            for i in range(x):
                if merg[i] == random_g2[x]:
                    end = 1

            if end == 0:
                nem = int(random_g2[x])
                merg.append(random_g[x])
                x += 1

        if x == 5:
            merg.append(1)
            kids.append(merg)
            arth = 0
            for i in range(5):
                convert1 = str(merg[i])
                convert2 = str(merg[i + 1])
                trip = convert1 + '-' + convert2
                trip2 = convert2 + '-' + convert1
                for j in range(10):
                    if trip.__eq__(lista[j][0]) or trip2.__eq__(lista[j][0]):
                        arth += lista[j][1]
            arth = 1 / arth
            skids.append(arth)
print('kids:')
print(kids)
print("percents of kids:")
print(skids)