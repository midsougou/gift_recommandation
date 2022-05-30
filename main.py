import streamlit as st
from recommand import recommander
from retour_exp import rt_experience

#configurer l'onglet
st.set_page_config(page_title="Recommandation de cadeaux",
                   page_icon=":gift:")

st.sidebar.header("Fonctionnement de l'application ")
st.sidebar.write("""Vous pouvez fournir l'ensemble des informations concernant le destinataire de votre cadeau en répondant aux questions suivantes """)
page=st.sidebar.selectbox("Choisir le type de statut", {"Recommander", "Retour expérience"},index=1)

if page=="Recommander":
    recommander()

else:
    rt_experience()

# pour supprmier  streamlit style
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)