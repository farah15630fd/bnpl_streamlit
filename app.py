import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="BNPL App", layout="wide")

image_path = "images_cartes"

def charger_image(nom_fichier):
    chemin = os.path.join(image_path, nom_fichier)
    if os.path.exists(chemin):
        return Image.open(chemin)
    else:
        return None

menu = st.sidebar.selectbox(
    "📋 Menu",
    ["Accueil", "Simulateur", "Suivi Paiements", "Profil", "Boutique", "Commande & Cartes", "Support"]
)

# ACCUEIL
if menu == "Accueil":
    st.title("💳 Bienvenue dans votre espace BNPL")

    carte_choisie = st.radio("Carte achetée :", ["Carte Virtuelle", "Carte Physique"], horizontal=True)

    if carte_choisie == "Carte Virtuelle":
        img = charger_image("carte_virtuelle.png")
    else:
        img = charger_image("carte_physique.png")

    if img:
        st.image(img, use_column_width=True)
    
    st.markdown("### 📈 Informations financières")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total paiements (30 jours)", "650 DT")
    with col2:
        st.metric("Dû dans 30 jours", "350 DT")

    st.markdown("### 🛍️ Détails par marque")
    st.write("- **Monoprix** : 70 DT *(dû dans 5 jours)*")
    st.write("- **Batam** : 240 DT *(dû dans 7 jours)*")
    st.write("- **Fatal** : 50 DT *(dû dans 15 jours)*")

# SIMULATEUR
elif menu == "Simulateur":
    st.title("🧮 Simulateur BNPL")
    montant = st.number_input("Montant de l'achat (DT)", min_value=50, step=10)
    duree = st.slider("Durée de remboursement (mois)", 3, 24, 12)
    taux = 0.015
    if montant:
        mensualite = round((montant * (1 + taux * duree)) / duree, 2)
        st.success(f"💰 Mensualité estimée : {mensualite} DT/mois pendant {duree} mois.")

# SUIVI
elif menu == "Suivi Paiements":
    st.title("📊 Suivi des Paiements")
    st.table({
        "Date": ["2025-04-01", "2025-05-01", "2025-06-01"],
        "Montant (DT)": [80, 80, 80],
        "Statut": ["Payé", "Payé", "À venir"]
    })

# PROFIL
elif menu == "Profil":
    st.title("👤 Mon Profil")
    st.text_input("Nom complet", "Mimi Test")
    st.text_input("Email", "mimi@email.com")
    st.text_input("Numéro client", "C123456789")
    st.success("Profil à jour.")

# BOUTIQUE
elif menu == "Boutique":
    st.title("🛍️ Boutiques Partenaires")
    st.info("Découvrez nos produits partenaires :")
    produits = [
        {"nom": "iPhone 14", "prix": 3999, "desc": "Smartphone dernière génération"},
        {"nom": "TV Samsung 50\"", "prix": 1899, "desc": "Smart TV 4K"},
        {"nom": "Canapé d'angle", "prix": 2200, "desc": "Salon confort 5 places"},
        {"nom": "Machine à laver", "prix": 1100, "desc": "Capacité 8kg, éco-énergie"},
        {"nom": "Chaussures Nike Air", "prix": 320, "desc": "Édition limitée"}
    ]
    for p in produits:
        st.write(f"**{p['nom']}** — {p['prix']} DT\n> *{p['desc']}*")

# COMMANDE & CARTES
elif menu == "Commande & Cartes":
    st.title("📦 Commande et gestion des cartes")

    col1, col2 = st.columns(2)
    with col1:
        img_v = charger_image("carte_virtuelle.png")
        if img_v:
            st.image(img_v, caption="Carte Virtuelle (50 DT)", use_column_width=True)
    with col2:
        img_p = charger_image("carte_physique.png")
        if img_p:
            st.image(img_p, caption="Carte Physique (40 DT)", use_column_width=True)

    st.markdown("### 📝 Sélection de carte à commander")
    choix_carte = st.radio("Choisissez une carte :", ["Carte Virtuelle - 50 DT", "Carte Physique - 40 DT"])

    if st.button("🛒 Commander la carte"):
        st.success(f"Votre commande pour la **{choix_carte}** a été enregistrée.")

# SUPPORT
elif menu == "Support":
    st.title("📞 Support Client")
    st.write("Vous avez une question ? Nous sommes là pour vous aider.")
    nom = st.text_input("Votre nom")
    message = st.text_area("Votre message")
    if st.button("Envoyer"):
        st.success("Message envoyé ! Un conseiller vous contactera bientôt.")

# FOOTER
st.markdown("---")
st.markdown("© 2025 - Application Buy Now Pay Later (BNPL) - by Mimi Dev")
