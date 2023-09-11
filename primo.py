#Programa Python para verificar a primalidade de um número



n = int( input("Entre com um número inteiro positivo: ") )

if n==1:
       print("1 não é primo")
    d=2
    while d<n/2:
    if n % d == 0:
        print("é divisível por", d)   
    d += 1
    if d==n:
    print( n, "é primo")
  
