import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(page_title="BNPL App", layout="wide")

# Définition du chemin des images
image_path = "images_cartes"

# Chargement des images de cartes
def charger_image(nom_fichier):
    chemin = os.path.join(image_path, nom_fichier)
    if os.path.exists(chemin):
        return Image.open(chemin)
    else:
        return None

# Menu latéral
menu = st.sidebar.selectbox(
    "📋 Menu",
    ["Accueil", "Simulateur", "Suivi Paiements", "Profil", "Boutique", "Support"]
)

# ACCUEIL
if menu == "Accueil":
    st.title("💳 Bienvenue dans votre espace BNPL")
    st.subheader("Vos cartes actives")

    col1, col2 = st.columns(2)

    with col1:
        img_v = charger_image("carte_virtuelle.png")
        if img_v:
            st.image(img_v, caption="Carte Virtuelle", use_column_width=True)
        else:
            st.warning("Carte virtuelle non trouvée.")

    with col2:
        img_p = charger_image("carte_physique.png")
        if img_p:
            st.image(img_p, caption="Carte Physique", use_column_width=True)
        else:
            st.warning("Carte physique non trouvée.")

# SIMULATEUR
elif menu == "Simulateur":
    st.title("🧮 Simulateur BNPL")

    montant = st.number_input("Montant de l'achat (DT)", min_value=50, step=10)
    duree = st.slider("Durée de remboursement (mois)", 3, 24, 12)
    taux = 0.015  # 1.5% par mois

    if montant:
        mensualite = round((montant * (1 + taux * duree)) / duree, 2)
        st.success(f"💰 Mensualité estimée : {mensualite} DT/mois pendant {duree} mois.")

# SUIVI PAIEMENTS
elif menu == "Suivi Paiements":
    st.title("📊 Suivi des Paiements")
    st.info("Historique et statut de vos paiements BNPL")

    st.table({
        "Date": ["2025-04-01", "2025-05-01", "2025-06-01"],
        "Montant (DT)": [80, 80, 80],
        "Statut": ["Payé", "Payé", "À venir"]
    })

# PROFIL UTILISATEUR
elif menu == "Profil":
    st.title("👤 Mon Profil")
    st.text_input("Nom complet", "Mimi Test")
    st.text_input("Email", "mimi@email.com")
    st.text_input("Numéro client", "C123456789")

    st.success("Profil à jour.")

# BOUTIQUE
elif menu == "Boutique":
    st.title("🛍️ Boutiques Partenaires")
    st.info("Découvrez où utiliser votre carte BNPL.")

    boutiques = [
        {"Nom": "ElectroShop", "Catégorie": "Électronique"},
        {"Nom": "HomePlus", "Catégorie": "Maison"},
        {"Nom": "Style&Mode", "Catégorie": "Vêtements"}
    ]

    for b in boutiques:
        st.write(f"**{b['Nom']}** — *{b['Catégorie']}*")

# SUPPORT
elif menu == "Support":
    st.title("📞 Support Client")
    st.write("Vous avez une question ? Nous sommes là pour vous aider.")

    nom = st.text_input("Votre nom")
    message = st.text_area("Votre message")

    if st.button("Envoyer"):
        st.success("Message envoyé ! Un conseiller vous contactera rapidement.")

# Pied de page
st.markdown("---")
st.markdown("© 2025 - Application Buy Now Pay Later (BNPL) - by Mimi Dev")
