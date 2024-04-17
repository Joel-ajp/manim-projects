import os

bsd = open("freeBSD.txt", "r")
pop = open("pop_OS!.txt", "r")

bsdList = bsd.readlines()
popList = pop.readlines()

bsdAverage = 0
popAverage = 0

for i in range(len(bsdList)):
    bsdAverage += int(bsdList[i])
    popAverage += int(popList[i])

bsdAverage /= 50
popAverage /= 50

print("bsd: ", bsdAverage)
print("pop: ", popAverage)