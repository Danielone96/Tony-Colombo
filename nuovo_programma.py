# il nostro primo programma python 
# """Triple aplice per dare un print con accapo e poterlo mettere su più righe"""
# La & significa AND mentre | significa OR 
# Per commentare più righe insieme evidenza e fai control +k + c

robot_name = "Chappie"
robot_age = 1

print("Ciao! Il mio nome è "+ robot_name + " e ho " +str(robot_age)+  " anni")
      
user_name = input("Tu come ti chiami ? ")
print("Ciao " + user_name + "!")

user_age = int(input("Quanti anni hai ? "))
print("Hai " + str(user_age) + " anni ! ")

#L'introduzione di If_Else

license = True

if user_age >= 18 and license == True :
    print ("Congratulazioni ! Puoi noleggiare una ferrari ")
elif user_age >=18 and license == False :
        print ("Attenzione ! Prima devi fare la patente ")
else:
    print ("Attenzione ! Non hai l'età per noleggiare una ferrari !")

    
#Il ciclo while 

counter = 0

while counter <=10:
    print(counter)
    counter +=1 

#Fermare un ciclo

run = True
Stop = 10
counter = 0

while run == True:
    print(counter)
    counter +=1
    if counter >= Stop:
        print("Sto uscendo dal ciclo ")
        run = False

#Se volessi saltare un numero 

run = True
skip = 3
counter = 0

while counter <10:
    counter +=1
    if counter == skip:
        print ("Sto saltando il numero : " +str(skip))
        continue #perchè dobbiamo far continuare il ciclo
    print(counter)