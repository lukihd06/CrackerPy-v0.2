CrackPass


calc capacité de calcul du pc : 
p = possibilités
k = nombre de caractère du mdp
i = nombre d'itérations par secondes

i = p**k / la durée en seconde du test (avec la valeur maximal rentrée)

Donc p**k/ le nombre d'itérations donne le temps maximal

p = 91
k = 5
p**k = 6240321451


Etapes du projet :

Core :

 - Fonction de hash en sha256
    - paramètres : le mdp à Hash
    - retourne : le hash
 
 - Fonction bruteforce
    - paramètres : le hash du mdp, nombre de caractères, liste des possibilités
    - créé le produit cartésien, compare avec le hash du mot de passe
    - retourne le mot de passe

Compteur et estimation du temps nécessaire :

 - Fonction pour savoir à quelles vitesse fonctionnera le programme
    - utilisation des tests précedement mis en place (voir haut de page)
    - succession de tests pour déterminer quelle est la capacité d'itérations par secondes de la machine
    - retournera le résultat d'itérations par secondes dans l'interface
 
 - Fonction qui va afficher le temps théorique maximal pour trouver le résultat
    - paramètres : le nombres des possibilités, le nombre de caractères
    - affiche le temps théorique maximal en année jour heures minutes secondes

Affichage / interface :

 - complexité : contient les caractères à utiliser pour casser le mot de passe ainsi que le total des possibilités (chiffres, minuscules, majuscules, spéciaux, accents ...) (checkbox)
 - Charactères : contient le nombre de caractères du mot de passe (input)
 - Mdp : on y entrera notre mot de passe (input)
 
 - Vitesse : contient la vitesse de calcul de la machine (text view)
 - calcul vitesse : exécutera la fonction de test pour connaitre la vitesse de traitement de la machine (bouton)
 
 - commencer : exécute le brute force (bouton) 
 - temps estimé : affiche le temps estimé maximal pour casser le mot de passe 

 TERMINE

 - Stopper le test en cours et faire le calcul avec le chiffre récupérer à l'arret
 - Afficher une courbe par x nbcaractère, y temps en secondes. Elle s'actualise a chaque ajout de possibilité
 - 

 - Enregistrement du nombre d'itération dans un fichier et le tester à chaque ouverture
 - Progress bar
 - Intégrer les collections de Toulon  
   - Affichage d'une entrée vers un fichier (box pour choisir un fichier dans le gestionnaire)
   - possiblement csv
 
Etapes


Scénario :
   on trouve le mail d'une personne sur facebook
   on recherche sur pastebin le mail de la personne
   on tente de peter le hash qui correspond
