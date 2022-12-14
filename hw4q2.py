def Clean(M):
    Black_Col = []
    Black_Row = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 0:
                Black_Col.append(j)
                Black_Row.append(i)
    #print(Black_Col)
    #print(Black_Row)
    for j in Black_Col:
        for i in range(len(M)):
            M[i][j] = 0
    for i in Black_Row:
        for j in range(len(M[i])):
            M[i][j] = 0
    #print(M)


numOfRows = int(input())
M = [[int(item) for item in input().split(' ')] for i in range(numOfRows)]
Clean(M)
print(M)