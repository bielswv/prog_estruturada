#primeiro exercico

a = int(input("Digite o valor do coeficiente a: "))
b = int(input("Digite o valor do coeficiente b: "))
c = int(input("Digite o valor do coeficiente c: "))
delta = b**2 - 4*a*c 
print("o valor de delta é: ", delta)
x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
print("o valor de x1 é: ", x1)
print("o valor de x2 é: ", x2)




#segundo exercicio

ano = int(input('informe ano '))

print( ano%4==0 and ano%100!=0  or  (not ano%400!=0))



      
