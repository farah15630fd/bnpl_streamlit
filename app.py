import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="BNPL App", layout="wide")

# Chargement des images
image_path = "images_cartes"
carte_virtuelle = Image.open(os.path.join(image_path, "carte_virtuelle.png"))
carte_physique = Image.open(os.path.join(image_path, "carte_physique.png"))

# Menu latéral
menu = st.sidebar.selectbox("Menu", ["Accueil", "Simulation", "Commande de carte", "Suivi Paiement", "Profil", "Acheter"])

# Page Accueil
if menu == "Accueil":
    st.title("BNPL - Tableau de bord")
    st.metric(label="Paiements sur 30j", value="650 DT")
    st.write("Aperçu des paiements récents...")
    
# Simulation
elif menu == "Simulation":
    st.title("Simulateur BNPL")
    montant = st.number_input("Montant Total (DT)", value=1200)
    tmm = 0.09
    duree = st.slider("Durée (mois)", 1, 24, 12)
    interet = round(montant * tmm, 2)
    mensualite = round((montant + interet) / duree, 2)
    st.write(f"Intérêts: {interet} DT")
    st.write(f"Mensualité: {mensualite} DT/mois")

# Commande de carte
elif menu == "Commande de carte":
    st.title("Commande Carte BNPL")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Carte Virtuelle")
        st.image(carte_virtuelle, width=200)
    with col2:
        st.subheader("Carte Physique")
        st.image(carte_physique, width=200)

# Suivi des paiements
elif menu == "Suivi Paiement":
    st.title("Suivi Paiement")
    st.subheader("Montre Connectée")
    st.radio("Mode de paiement", ["Paiement immédiat", "Paiement BNPL"])
    st.info("Prochain paiement : 25 Avril 2024 - 60 DT")

# Profil
elif menu == "Profil":
    st.title("Profil Utilisateur")
    st.text("Nom : Ahmed Ben Ali")
    st.text("Nationalité : Tunisienne")
    st.text("Nom d'utilisateur : alfredred")

# Achat
elif menu == "Acheter":
    st.title("Acheter via l'application")
    st.write("Plafond disponible : 1700 DT")
    st.success("Produit sélectionné : Laptop - 1200 DT")

