n = int(input())

valores = map(int, input().split())
par=[]
impar=[]
for i in valores:
  if i%2==0:
    par.append(i)
  else:
    impar.append(i)
print(*par)
print(*impar)