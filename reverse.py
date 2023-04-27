# Lendo a string a ser invertida
string = input("Digite uma string: ")

# Invertendo a string
string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Imprimindo a string invertida
print("A string invertida é:", string_invertida)