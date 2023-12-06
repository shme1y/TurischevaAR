m = [[9, 9, 9, 9, 9],
     [8, 8, 8, 8, 8],
     [7, 7, 7, 7, 7],
     [6, 6, 6, 6, 6],
     [2, 2, 2, 2, 2], ]
 
for i in range(len(m) - 1):
    for j in range(len(m[0])):
        m[i][j] -= m[-1][j]
 
for i in m:
 print(*i)