n=20 #Размер
#Формирование исходной матрицы
A = [[(1/(1+i+j)) for i in range(n+1)] for j in range(n)]
for i in range(n):
    suma=0
    for j in range(n):
        suma+=A[i][j]
    A[i][n]=suma
#Матрица результатов
X =[0 for i in range(n)]
print("Исходная матрица:")
print(A)
#Метод Гаусса
#Прямой ход
for i in range(n):
    tmp=A[i][i]
    for j in range(n+1):
        A[i][j]/=tmp
    for j in range(i+1,n):
        tmp=A[j][i]
        for k in range(n+1):
           A[j][k]-=tmp*A[i][k]
#Обратный ход
X[n-1]=A[n-1][n]
for i in range(n-2,-1,-1):
    X[i] = A[i][n]
    for j in range(i+1,n):
        X[i]-=A[i][j]*X[j]
print("Результат:")
print(X)
