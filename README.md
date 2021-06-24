# Finddivisornumber
Trouver les diviseurs d'un nombre 
Le but de cet exercice était de trouver tous les diviseurs du nombre contenu dans la variable 'nombre'.

La première étape était donc de créer une liste de nombres qui contient tous les nombres de 1 au nombre contenu dans la variable 'nombre' (ici, 50) :

    liste_nombres = list(range(1, nombre+1))

On crée ensuite une liste vide qui va nous permettre de stocker les nombres qui sont des diviseurs de 50.

On commence ensuite une boucle à travers notre liste de nombres. Grâce à l'opérateur modulo, on récupère le reste de la division.
Si le reste est égal à 0, alors le nombre courant, contenu dans la variable i, est un diviseur du nombre 50. Nous l'ajoutons donc à notre liste 'diviseurs' :

    for i in liste_nombres:
        if nombre % i == 0:
            diviseurs.append(i)

Et voilà, un exercice assez simple en somme, mais qui faisait appel à l'opérateur modulo dont beaucoup de gens oublient souvent l'existence.
Je suis sur qu'une petite piqûre de rappel avec cet exercice ne vous a donc pas fait de mal ;)
