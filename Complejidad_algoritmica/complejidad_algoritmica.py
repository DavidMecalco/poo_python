import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

def facotorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

if __name__ == "__main__":
    n = 100000
    
    comienzo = time.time()
    facotorial_r(n)
    final = time.time()
    print(final - comienzo)