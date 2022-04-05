
def fibonacci (x):
    if ( x == 0 ):
        return 0
    elif ( x == 1 ):
        return 1
    else:
        return (fibonacci( x - 2 ) + fibonacci( x - 1 )) 

x = 1
while ( x != 0 ):
    n=int(input("Introduce un valor para la serie Fibonacci: "))

    if n < 0:
        print ("El valor introducido es negativo no se puede hacer una serie Fibonacci")
        x = 1
    else:
        print("La seria Fibonacci es: ")
        for n in range ( 0, n ):
            print(f"{n + 1}: {fibonacci(n)}")
        x = int(input("Para continuar el programa inserte un valor distinto de 0: "))