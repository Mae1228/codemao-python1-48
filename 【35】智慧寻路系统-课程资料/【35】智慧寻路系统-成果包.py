ite = input('请输入学校坐标（例：9 9）：').split()
# print(ite)
n, m = map(int, ite)
a = []
for i in range(n+1):
    a.append([])
    for j in range(m+1):
        a[i].append(0)
print(a)

k = int(input('请输入施工路口数（例：1）：'))
for i in range(k):
    x, y = map(int, input('请输入施工路口坐标，注意0<x<n且0<y<m（例：4 4）：').split())
    a[x][y] = -1
    a[x-1][y] = -1
    a[x][y-1] = -1
    a[x+1][y] = -1
    a[x][y+1] = -1




for i in range(n+1):
    for j in range(m+1):         
        if i==0 and j==0:
            a[i][j] = 1

        elif i==0 and j!=0:        
            if a[i][j]==-1:
                a[i][j] = 0
            else:
                a[i][j]=0+a[i][j-1] #纵坐标上的点

        elif j==0 and i!=0:
            if a[i][j] == -1:
                a[i][j] = 0
            else:
                a[i][j] = a[i-1][j]+0#横坐标上的点

        else:
            if a[i][j] == -1:
                a[i][j] = 0
            else:
                a[i][j] = a[i-1][j]+a[i][j-1]
print(a[n][m])
    
