
def readfile(inputfile):
    f = open(inputfile,"r")

    list1 = []
    list2 = []

    totalDif = 0

    for line in f.readlines():
        sp = line.strip("\n").split("   ")
        list1.append(sp[0])
        list2.append(sp[1])

    # first part
    # list1.sort()
    # list2.sort()

    # for i in range(len(list1)):
    #     difernce = abs(int(list1[i]) - int(list2[i]))
    #     totalDif += difernce

    # second part
    for i in list1:
        times = 0
        for j in list2:
            if int(j) == int(i):
                times += 1
        
        totalDif += int(i) * int(times)

    return totalDif


if __name__ == "__main__":
    print(readfile("Day1/input.txt"))