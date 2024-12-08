import re

def ReadFile(inputFile:str) -> int:
    file = open(inputFile,"r")

    searchString = ""

    for l in file.readlines():
        searchString += l

    return ScanFileForMul(searchString)
    
def ScanFileForMul(searchString:str) -> int:
    
    step:int = 0
    NumerAmount = 0
    mulString = ""
    totalMultiply = 0

    MulEnabled = True
    EnableStep = 0

    for char in searchString:
        #part 2 enable and disable
        match EnableStep:
            case 0:
                if char == "d":
                    EnableStep +=1
                    continue

            case 1:
                if char == "o":
                    EnableStep +=1
                    continue
                else:
                    EnableStep = 0
                    continue

            case 2:
                if char == "(":
                    EnableStep +=1
                    continue
                elif char == "n":
                    EnableStep = 5
                else:
                    EnableStep = 0
                    continue

            case 3:
                if char == ")":
                    MulEnabled = True
                    EnableStep = 0
                    continue
                else:
                    EnableStep = 0
                    continue

            case 5:
                if char == "'":
                    EnableStep +=1
                    continue
                else:
                    EnableStep = 0
                    continue

            case 6:
                if char == "t":
                    EnableStep +=1
                    continue
                else:
                    EnableStep = 0
                    continue

            case 7:
                if char == "(":
                    EnableStep +=1
                    continue
                else:
                    EnableStep = 0
                    continue

            case 8:
                if char == ")":
                    MulEnabled = False
                    EnableStep = 0
                    continue
                else:
                    EnableStep = 0
                    continue

        if  not MulEnabled:
            continue
        # part 1
        match step:
            case 0:
                if char == "m":
                    step += 1
                    continue
            
            case 1:
                if char == "u":
                    step += 1
                    continue
                else:
                    step = 0
                    continue

            case 2:
                if char == "l":
                    step += 1
                    continue
                else:
                    step = 0
                    continue

            case 3:
                if char == "(":
                    step += 1
                    mulString = "mul("
                    continue
                else:
                    mulString = ""
                    step = 0
                    continue

            case 4:
                try:
                    int(char)
                    mulString += char
                    NumerAmount +=1
                    if(NumerAmount > 3):
                        NumerAmount = 0
                        step = 0
                        continue

                except:
                    if(NumerAmount > 0) and char == ",":
                        step +=1
                        mulString += char
                    else:
                        step = 0

                    NumerAmount = 0
                    continue

            case 5:
                try:
                    int(char)
                    NumerAmount +=1
                    mulString += char
                    if(NumerAmount > 3):
                        step = 0
                        NumerAmount = 0
                        continue

                except:
                    if(NumerAmount > 0) and char == ")":
                        step +=1
                        mulString += char

                        totalMultiply += CalcMul(mulString)
                        mulString = ""

                    step = 0
                    NumerAmount = 0
                    continue
                
    return totalMultiply      


def CalcMul(mulString:str)->int:
    temp = mulString.split("(")[1]
    firstNumber = temp.split(",")[0]
    secondNumber = temp.split(",")[1].strip(")")

    return int(firstNumber) * int(secondNumber)

if __name__ == "__main__":
    print(ReadFile("AdventOfCode2024/AdventOfCode2024/Day3/input.txt"))