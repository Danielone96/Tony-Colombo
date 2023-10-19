print("Ciao: come ti chiami ?")
nome=input()
nome = nome.upper()  # rendo il valore inserito in nome TUTTO MAIUSCOLO
print("Ciao: " +nome )
if nome=="TONY COLOMBO":
    print("Attenzione ! ieri sera sei finito in un Bliz !")
else:
    print(nome+ " quanti anni hai ? ")
    eta=int(input())
    if eta >= 18:
        print("Adesso che sei maggiorenne puoi andare direttamente a Poggioreale !")
    else:     print("Finchè sei minorenne la legge ha poco lavore ")
print("ADDIO")



