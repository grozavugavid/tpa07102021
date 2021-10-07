matrix=[]
n=int(input("Dati dimensiunile matricei de la 2 pana la 10:"))
if n>=2 and n<=10:
    for i in range(0,n):
        k=int(input("Dati elemetele:"))
        for j in range(0,n):
            matrix.append(k[i][j])

print(matrix)

diagpr=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])) :
        if i==j :
            diagpr.append(matrix[i][j])
print("Suma elementelor diagonalei principale este:",sum(diagpr))

diagsec=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])) :
        if i+j==n-1:
            diagsec.append(matrix[i][j])
print("Suma elemetelor diagonalei secundare este:",sum(diagsec))

sumaelemmaisusdediagpr=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])) :
        if i-j<0 :
            sumaelemmaisusdediagpr.append(matrix[i][j])
print("Suma elementelor mai sus de diagonala principala este:",sum(sumaelemmaisusdediagpr))

sumaelemmaijosdediagpr=[]
for i in range(len(matrix)):
for j in range(len(matrix[0])) :
        if i-j>0 :
            sumaelemmaijosdediagpr.append(matrix[i][j])
print("Suma elementelor mai jos de diagonala principala este:",sum(sumaelemmaijosdediagpr))

sumaelemmaisusdediagsec=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])) :
        if i+j<n-1 :
            sumaelemmaisusdediagsec.append(matrix[i][j])
print("Suma elementelor mai sus de diagonala secundara este:",sum(sumaelemmaisusdediagsec))

sumaelemmaijosdediagsec=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])) :
        if i+j>n-1 :
            sumaelemmaijosdediagsec.append(matrix[i][j])
print("Suma elementelor mai jos de diagonala secundara este:",sum(sumaelemmaijosdediagsec))
