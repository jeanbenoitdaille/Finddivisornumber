nombre = 50
liste_nombres = list(range(1, nombre+1))
diviseurs = []
     
for i in liste_nombres:
        if nombre % i == 0:
            diviseurs.append(i)
     
print(diviseurs)