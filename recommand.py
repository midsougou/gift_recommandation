import streamlit as st
import pandas as pd
from csv import writer


def recommander():
    cadeau = pd.read_csv("db_test.csv", index_col=0)
    cadeau_si = cadeau.drop(['item'], axis=1)  # retirer la dernière colonne contenant les cadeaux

    with st.form(key="pl"):

        # retirer l'utilisateur de la matrice
        def similarity(L, n):  # la liste L des features de user et le nombre n de users similaires qu'on cherche à afficher
            new_user_index = cadeau_si.index[-1] + 1  # par ex si la dernnière ligne est user 5 alors new_user_index devient 6
            cadeau_si.loc[new_user_index] = L  # on rajoute la liste des features àla dataframe en index new_user_index
            # calculer la matrice de similarity en utilisant le coefficient de corrélation
            new_m = cadeau_si.T.corr()
            # retirer l'utilisateur destinataire de la matrice "la ligne"
            new_m.drop(index=new_user_index, inplace=True)
            similaires_users = new_m[new_user_index]  # on sélectionne que la dernière colonne de la matrice
            similaires_users = similaires_users.sort_values(ascending=False)  # ordre croissant
            similaires_users = similaires_users.head(n)  # on sélectionne que les n users les plus similaires à lui
            return similaires_users

        st.title( "Application de recommandation de cadeaux ")
        st.markdown("##### Cette application recommande un cadeau à offrir à une personne")
        destinataire = {
            "Ami": 1,
            "Famille": 2,
            "Compagnon": 3,
            "Moi-même": 4,
            "Collègue": 5,
        }
        sexe = {
            "Homme": 0,
            "Femme": 6
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
        n = st.slider("Le nombre de recommandations", 1, 5, 1)

        ok = st.form_submit_button(label='Enregistrer')

        ag = 0
        if ok:
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

            df = similarity([destinataire[des], sexe[sx], ag, occasion[occ], lieu[li], passion[pa], couleur[cl], boisson[boi], animal[ani], mot[mo]], n)
            st.subheader("Le cadeau recommandé est : ")

            for a in df.index:  # trouver le cadeau correspondant pour chaque user
                st.write(cadeau.iloc[a - 1]['item'])


            entrer = st.text_input(label='Dites nous votre choix')
            if len(entrer) !=0:
                new = cadeau.index[-1] + 1
                with open('db_test.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow([new, destinataire[des], sexe[sx], ag, occasion[occ], lieu[li], passion[pa], couleur[cl],boisson[boi], animal[ani], mot[mo], entrer])
                    f_object.close()
