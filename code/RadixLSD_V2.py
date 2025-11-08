import random as R
import time
InLen = 100
Data = []
SortedData = []
Bucket = [[],[],[],[],[],[],[],[],[],[]]
DataOut = []

def shufill(List, Len):
    for n in range(Len):
        List.insert(n,n+1)
    R.shuffle(List)

def getDigit(N, D):
    N = "%06d" % N
    return int(str(N)[(len(str(N))-D)-1])

def Radix(array,MaxDigits):
    Bucket = [[],[],[],[],[],[],[],[],[],[]]
    for Digit in range(MaxDigits):
        for element in range(len(array)-1,-1,-1):
            Bucket[getDigit(array[element],Digit)].insert(0,array[element])
        array = []
        for item in range(len(Bucket)-1,-1,-1):
            for i in range(len(Bucket[item])-1,-1,-1):
                array.insert(0,Bucket[item][i])
        Bucket = [[],[],[],[],[],[],[],[],[],[]]
    Bucket = [[],[],[],[],[],[],[],[],[],[]]
    return array

def Sort(DataLength):
    Data = []
    SortedData = []
    Bucket = [[],[],[],[],[],[],[],[],[],[]]
    shufill(Data,DataLength)
    start = time.time()
    DataOut = Radix(Data,len(str(DataLength)))
    end = time.time()
    print(end-start,"Seconds")
    PrintData = int(input("Print Data? Yes(1) No(0)"))
    if PrintData == 1:
        print(DataOut)
    else:
        print("Terminated")




