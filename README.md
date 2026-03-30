# Projet de Cryptographie

Ce projet propose l'implémentation en Python de deux algorithmes de chiffrement.

## Algorithme 1 : Chiffrement par Substitution Dynamique
* **Principe** : Substitue chaque lettre d'un texte clair en utilisant deux alphabets désordonnés de 26 lettres (`keyLeft` et `keyRight`).
* **Sécurité** : Possède un espace de clés immense d'environ 1.6 × 10⁵³, ce qui rend la force brute totalement impraticable. Les permutations dynamiques après chaque lettre le rendent résistant à l'analyse de fréquence.
* **Limites** : Ne prend pas en charge les caractères spéciaux ou binaires et est limité à l'alphabet majuscule (A-Z).

## Algorithme 2 : Chiffrement par Transposition en Vagues
* **Principe** : Modifie la position des lettres du texte en les plaçant dans un tableau de hauteur `n` selon un motif en vague, défini par un décalage initial (`offset`).
* **Sécurité** : L'espace de clés est restreint, ce qui rend cet algorithme vulnérable aux attaques par force brute. Puisqu'aucune lettre n'est modifiée, il est également vulnérable à l'analyse de fréquence. Il ne doit pas être utilisé pour des données sensibles.
* **Avantages** : L'algorithme est rapide, facile à implémenter et réversible sans perte de données.

## Utilisation
Les deux algorithmes sont implémentés sous forme de classes (`Algo1` et `Algo2`) dans le script principal. 

Exemple d'utilisation :
1. Instanciez l'objet avec les paramètres requis (les clés pour `Algo1`, `n` et `offset` pour `Algo2`).
2. Utilisez les méthodes `.chiffrer("VOTREMESSAGE")` et `.dechiffrer("VOTREMESSAGE")` pour effectuer les opérations.
