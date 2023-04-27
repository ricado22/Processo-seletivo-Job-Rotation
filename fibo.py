def fibonacci(n):
    a, b = 0, 1
    fib = [0, 1]
    while b < n:
        a, b = b, a + b
        fib.append(b)
    if n in fib:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

numero = int(input("Digite um número: "))
fibonacci(numero)