
def calcSaveReports(intputFile:str) -> int:
    file = open(intputFile,"r")

    totalSafe = 0
    for line in file.readlines():
        if analyseReportLine(line):
            totalSafe +=1

    return totalSafe

    
def analyseReportLine(line:str) ->bool:
    reps = line.strip("\n").split(" ")

    accending:bool = True
    first:bool = True
    FaultsTolerated = 0

    for i in range(len(reps)-1):

        if(first):
            if(int(reps[i]) > int(reps[i+1])):
                accending = False
            first = False
        else:
            if (int(reps[i]) > int(reps[i+1])) and accending:
                if(FaultsTolerated >= 1):
                    return False
                else:
                    FaultsTolerated +=1
                    continue
            elif (int(reps[i]) < int(reps[i+1])) and not accending:
                if(FaultsTolerated >= 1):
                    return False
                else:
                    FaultsTolerated +=1
                    continue

        if abs(int(reps[i]) - int(reps[i+1])) > 3 or abs(int(reps[i]) - int(reps[i+1])) == 0:
            if(FaultsTolerated >= 1):
                return False
            else:
                FaultsTolerated +=1
                continue
    
    return True
           


if __name__ == "__main__":
    print(calcSaveReports("AdventOfCode2024/AdventOfCode2024/Day2/input.txt"))