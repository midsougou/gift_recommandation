# Recommandation de cadeaux avec Python et Streamlit

Ce projet est une application web de recommandation de cadeaux. Elle permet à l'utilisateur de fournir des informations sur le destinataire du cadeau et en retour, l'application propose des cadeaux qui pourraient convenir au destinataire en se basant sur des utilisateurs similaires. En plus d’être recommandé, l’utilisateur pourra participer à améliorer les résultats futurs de notre interface. Ainsi, un utilisateur qui n’est pas satisfait peut l’indiquer et aussi indiquer le cadeau finalement choisi.

## Prérequis

- Python 3.7
- Streamlit
- Pandas

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en exécutant la commande suivante :
```
pip install streamlit pandas
```

## Utilisation

Pour lancer l'application, exécutez la commande suivante dans votre terminal :
```
streamlit run main.py
```

Une fois l'application démarrée, vous pouvez interagir avec elle en répondant aux questions concernant le destinataire du cadeau :

1. Choisissez le type de statut : **Recommander** ou **Retour expérience**.
2. Répondez aux questions concernant le destinataire, telles que le genre, l'âge, l'occasion, le lieu préféré, la passion, la couleur préférée, la boisson préférée, l'animal préféré, et le mot qui représente le destinataire.
3. Pour la fonction `Recommander`, l'application proposera alors les 5 meilleurs cadeaux en fonction des utilisateurs similaires.
4. Pour la fonction `Retour expérience` vous pouvez également fournir un cadeau que vous avez reçu et donner vos préférences pour enrichir la base de données.

## Données

Les données utilisées pour la recommandation sont stockées dans un fichier CSV nommé `db_test.csv`. Ce fichier contient les colonnes suivantes :

- user_id : identifiant de l'utilisateur
- destinataire : type de destinataire (Ami, Famille, Compagnon, Moi-même, Collègue)
- sexe : genre du destinataire (Homme, Femme)
- age : âge du destinataire
- occasion : occasion pour offrir le cadeau (Mariage, Anniversaire, Noël, Professionel, Occasion particulière)
- lieu : lieu préféré du destinataire pour passer les vacances
- passion : passion du destinataire (Jeux-vidéos, Musique, Films, Sport, Lectures)
- couleur : couleur préférée du destinataire (Bleu, Rouge, Noir, Blanc, Vert)
- boisson : boisson préférée du destinataire (Café, Thé, Boisson gazeuse, Eau, Jus)
- animal : animal préféré du destinataire (Koala, Tortue, Dauphin, Lion, Mouette)
- mot : mot qui représente le destinataire (Résérvé, Indépendant, Romantique, Détendu, Travailleur)
- item : cadeau recommandé ou reçu par le destinataire

## Contributions

Les contributions à ce projet sont les bienvenues. Si vous trouvez des bugs, des améliorations possibles ou si vous avez des idées pour étendre les fonctionnalités, n'hésitez pas à me le faire savoir.

---

Merci d'avoir utilisé cette application de recommandation de cadeaux. Nous espérons qu'elle vous aidera à trouver le cadeau parfait pour vos proches !

