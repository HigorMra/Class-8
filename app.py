tenho_sede = True

if tenho_sede:
    print("beber agua")

print("Vida que segue")

esta_frio = False

if esta_frio:
    print("Vestir um casaco")
else:
    print("Vestir camiseta")

tenho_sede = False ###ambos sendo falso, utiliza o else
tenho_fome = False ###se houver um true, utiliza o if

if tenho_sede or tenho_fome:
    print("vou na cozinha")
else: 
    print("ficar vendo na netflix")

tenho_sede = False ###só utiliza o if se ambos forem true
tenho_fome = False

if tenho_sede and tenho_fome:
    print("fazer sanduiche e coca-cola")
else: 
    print("não tenho fome ou não tenho sede")

tenho_sede = True
tenho_fome = False

estou_em_dieta = False #ativa os comparadores em cadeia

if tenho_sede and tenho_fome:
    print("fazer sanduice e coca-cola")
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
        print("vou tomar agua")
    else:
        print("tomar uma coquinha")
elif not(tenho_sede) and tenho_fome:
    print("fazer um sanduiche")
else:
    print("ficar vendo Netflix")

num1 = 5
num2 = 32

if num1 == num2:
    print("num1 é igual num2")  
elif num1 != num2:
    print("num1 é diferente num2")
elif num1 > num2:
    print("num1 é maior que num2")
elif num1 < num2:
    print("num1 é menor que num2")
if num1 <= num2:
    print("num1 é menor  ou igual que num2")


#operadores lógicos
# or = ou
# and = e
# not() = negação


#operadores de comparação
# == igual
# != diferente
# > maior
# < menor
# >= maior ou igual
# <= menor ou igual