import streamlit as st
import pandas as pd
from csv import writer

def rt_experience():
    cadeau = pd.read_csv("db_test.csv", index_col=0)
    st.write('''# Entrer le cadeau que vous avez reçu et vos préférences''')

    destinataire = {
        "Ami": 1,
        "Famille": 2,
        "Compagnon": 3,
        "Moi-même": 4,
        "Collègue": 5,
    }
    sexe = {
        "Homme": 1,
        "Femme": 5
    }

    occasion = {
        "Mariage": 1,
        "Anniversaire": 2,
        "Noël": 3,
        "Professionel (retraite, départ...)": 4,
        "Occasion particulière": 5
    }

    lieu = {
        "Plage": 1,
        "Forêt": 2,
        "Ferme": 3,
        "Montagne": 4,
        "Les vacances ? c'est quoi les vacances ?": 5
    }
    passion = {
        "Jeux-vidéos": 1,
        "Musique": 2,
        "Films": 3,
        "Sport": 4,
        "Lectures": 5
    }

    couleur = {
        "Bleu": 1,
        "Rouge": 2,
        "Noir": 3,
        "Blanc": 4,
        "Vert": 5
    }

    boisson = {
        "Café": 1,
        "Thé": 2,
        "Boisson gazeuse": 3,
        "Eau": 4,
        "Jus": 5
    }

    animal = {
        "Koala": 1,
        "Tortue": 2,
        "Dauphin": 3,
        "Lion": 4,
        "Mouette": 5
    }

    mot = {
        "Résérvé": 1,
        "Indépendant": 2,
        "Romantique": 3,
        "Détendu": 4,
        "Travailleur": 5
    }
    des = st.selectbox("Pour qui tu cherches un cadeau ?", destinataire)
    sx = st.selectbox("Genre ", sexe)
    age = st.slider("Age", 0, 100, 20)
    occ = st.selectbox("Pour quelle occasion ?", occasion)
    li = st.selectbox("Lieu préféré pour passer les vacances", lieu)
    pa = st.selectbox("Passion", passion)
    cl = st.selectbox("Couleur préférée", couleur)
    boi = st.selectbox("Boisson préférée", boisson)
    ani = st.selectbox("Animal qui représente le destinataire le mieux", animal)
    mo = st.selectbox("Le mot qui représente le destinataire le mieux", mot)
    feedback = st.text_input("Entrer le cadeau qui vous semble le mieux convenable")
    push=st.button("Envoyer")
    ag=0
    if push:
        if age <= 20:
            ag = 1
        elif 20 < age <= 40:
            ag = 2
        elif 40 < age <= 60:
            ag = 3
        elif 60 < age <= 80:
            ag = 4
        elif 80 < age <= 100:
            ag = 5

        # pour modifier notre nouvelle base de données
        new = cadeau.index[-1] + 1
        with open('db_test.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([new,destinataire[des],sexe[sx],ag,occasion[occ],lieu[li],passion[pa],couleur[cl],boisson[boi],animal[ani],mot[mo], feedback])
            f_object.close()
        st.markdown('''### Merci pour votre collaboration, A bientôt''')



