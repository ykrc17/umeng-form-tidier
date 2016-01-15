import sys

dateList=[]
eventList=[]
matrix = [[]]

def appendLine():
    newLine=[]
    for event in eventList:
        newLine.append(0)
    matrix.append(newLine)

def appendRow():
    for line in matrix:
        line.append(0)

def readFile():
    if len(sys.argv)<3:
        print 'missing argument : file name'
        sys.exit()

    inputFile = open(sys.argv[1])
    try:
        inputFile.readline()
        for line in inputFile:
            lineList= line.split('\t')
            if len(lineList) < 4:
                break
            date = lineList[0]
            event =lineList[2]
            amount= lineList[4]

            if date not in dateList:
                dateList.append(date)
                appendLine()

            if event not in eventList:
                eventList.append(event)
                appendRow()

            matrix[dateList.index(date)][eventList.index(event)] = amount
    finally:
        inputFile.close()

def writeFile():
    outputFile = open(sys.argv[2], 'w')

    seperate=','

    outputFile.write(seperate)
    for row in eventList:
        outputFile.write(row+seperate)
    outputFile.write('\n')

    for i in range(0, len(matrix)-1):
        date = dateList[i]
        line = matrix[i]
        outputFile.write(date + seperate)
        for row in line:
            outputFile.write(str(row)+seperate)
        outputFile.write('\n')

def main():
    readFile()
    writeFile()

if __name__ == '__main__' :
    main()
