opc=0


print("Bem Vindo" )
print("Prima 1 para nome cliente")
print("Prima 2 para Iban")
opc = input("Intrud opçao")

match opc :
    case  1:
        print("Nome")
    case 2:
        print ("Iban")
    case default:
        print ("falhou opc")




num1=0
num2=0
num3=0

# entre 3 numeros saber maior, meio e menor 

if num1>num2:
    if num1>num3:
        print("Numero 1 é o maior")
        if num2>num3:
            print("Numero 2 é o meio ")
else:
    print("")