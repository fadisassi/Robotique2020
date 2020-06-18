# Une variables est une "boite" contenant une valeur qui peut etre changee durant l'execution du programme.
# il existe differents type de variable.

nombre_entier = 5 
nombre_virgule = 2.3
texte = "Bonjour"
boolean = True # False pour faux
liste = ["1er element", "2eme element"]

#on affiche le contenu de certaine variables avec la fonction print()
print (texte)
print (liste) # affiche tout les elements de la liste 
print (liste[1]) # Une lise commence toujours par l'element 0. on demande ici le 2eme

print("....................................")
# pour afficher les types de variables, on utilise la fonction type() puis on l'affiche avec print
print( type(nombre_entier) )
print( type(nombre_virgule) )
print( type(texte) )
print( type(boolean) )
print( type(liste) )


#Test d'erreur de type
var1 = 5
var2 = "3"
# print(var1+var2) # genere une erreur de type
print(str(var1)+var2) #permet de contourner le probleme en forcant le type ,ici , str pour texte