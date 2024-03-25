# 1) Este código está em um pseudo-código, e ele soma os números de 1 até 13 (inclusive), porque o incremento de K ocorre antes da soma. A variável SOMA acumula a soma de todos os valores de K de 1 a 13. 
#A soma dos primeiros 13 números naturais é dada pela fórmula da soma de uma progressão aritmética: S = n/2 * (a1 + an), onde n é o número de termos, a1 é o primeiro termo, e an é o último termo.
#Substituindo os valores: S = 13/2 * (1 + 13) = 91.
#Portanto, ao final do processamento, a variável SOMA será 91.

# 2) Programa para verificar se um número pertence à sequência de Fibonacci:

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")

# 3) 
# a) 9 (padrão de adicionar 2)
# b) 128 (padrão de multiplicar por 2)
# c) 49 (padrão de quadrados dos números naturais: 0^2, 1^2, 2^2, 3^2, ...)
# d) 100 (padrão de quadrados dos números pares: 2^2, 4^2, 6^2, 8^2, ...)
# e) 13 (sequência de Fibonacci)
# f) 20 (sequência parece aumentar arbitrariamente, mas o próximo número lógico seria 20 seguindo o padrão de incremento unitário do final).    
    
# 4)    
# a) Ligue o primeiro interruptor e deixe-o ligado por alguns minutos. Em seguida, desligue-o.
# b) Ligue o segundo interruptor.
# c) Vá até a sala das lâmpadas:
#A lâmpada que está acesa é controlada pelo segundo interruptor. Toque nas lâmpadas que estão apagadas; a lâmpada que estiver quente é controlada pelo primeiro interruptor (porque estava ligada por alguns minutos e depois desligada).
#A lâmpada que está fria e apagada é controlada pelo terceiro interruptor.
    
# 5) Programa para inverter os caracteres de um string:
def inverter_string(s):
    string_invertida = ''
    for caracter in s:
        string_invertida = caracter + string_invertida
    return string_invertida

string_original = input("Digite uma string: ")
print("String invertida:", inverter_string(string_original))
