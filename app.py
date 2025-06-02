import streamlit as st
from PIL import Image
import os
import random

# Configuration de la page
st.set_page_config(page_title="Application BNPL", layout="wide")

# Chemin vers les images
image_path = "images_cartes"

def charger_image(nom_fichier):
    chemin = os.path.join(image_path, nom_fichier)
    if os.path.exists(chemin):
        return Image.open(chemin)
    else:
        st.warning(f"Image non trouvée : {chemin}")
        return None

# Menu principal
menu = ["Accueil", "Simulation Paiement", "Boutique", "Commande et gestion des cartes", "Profil", "Support"]
choix = st.sidebar.selectbox("Navigation", menu)

# Page d'accueil
if choix == "Accueil":
    st.title("Bienvenue dans votre espace BNPL")

    # Carte achetée aléatoirement (ou aucune)
    carte_virtuelle = charger_image("carte_virtuelle.png")
    carte_physique = charger_image("carte_physique.png")
    carte_choisie = random.choice(["virtuelle", "physique", "aucune"])

    st.markdown("#### Carte achetée :")
    if carte_choisie == "virtuelle" and carte_virtuelle:
        st.image(carte_virtuelle, caption="Carte virtuelle", use_container_width=True)
    elif carte_choisie == "physique" and carte_physique:
        st.image(carte_physique, caption="Carte physique", use_container_width=True)
    else:
        st.info("Aucune carte achetée pour le moment.")

    st.markdown("### Total des paiements effectués (30 jours) : **650 DT**")
    st.markdown("### Montant dû dans 30 jours : **350 DT**")

    st.markdown("### Détails par marque :")
    marques = [
        ("Monoprix", "70 DT", "dans 5 jours"),
        ("Batam", "240 DT", "dans 7 jours"),
        ("Fatal", "50 DT", "dans 15 jours")
    ]
    for marque, montant, delai in marques:
        st.write(f"- **{marque}** : {montant} ({delai})")

# Simulation Paiement
elif choix == "Simulation Paiement":
    st.title("Simulateur de Paiement BNPL")

    montant = st.number_input("Montant du crédit (DT)", min_value=0.0, step=50.0)
    duree = st.slider("Durée (mois)", 1, 12, 6)

    if montant > 0:
        tmm = 0.075
        marge = 0.03
        interet = (tmm + marge) * montant
        mensualite = interet + (montant / duree)

        st.markdown(f"### Mensualité estimée : **{mensualite:.2f} DT**")
        st.markdown(f"Dont intérêt : {interet:.2f} DT")

# Boutique
elif choix == "Boutique":
    st.title("Boutique BNPL")

    produits = [
        {"nom": "Smartphone Samsung A14", "prix": 950, "desc": "Écran 6.6\" / 128 Go"},
        {"nom": "Lave-linge LG", "prix": 1200, "desc": "8kg Inverter"},
        {"nom": "TV Sony 4K 55\"", "prix": 2000, "desc": "HDR, Smart TV"},
        {"nom": "AirPods Pro", "prix": 850, "desc": "Apple Original"},
        {"nom": "Ordinateur ASUS 15\"", "prix": 1800, "desc": "Core i5, 8Go RAM"},
        {"nom": "Climatiseur Samsung 12000 BTU", "prix": 1600, "desc": "Split froid/chaud"},
    ]

    for p in produits:
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"**{p['nom']}** — {p['prix']} DT  \n> *{p['desc']}*")
        with col2:
            st.button("🛒", key=p['nom'])

# Commande et gestion des cartes
elif choix == "Commande et gestion des cartes":
    st.title("Commande et Gestion des Cartes")

    carte_virtuelle = charger_image("carte_virtuelle.png")
    carte_physique = charger_image("carte_physique.png")

    col1, col2 = st.columns(2)
    with col1:
        if carte_physique:
            st.image(carte_physique, caption="Carte Physique", use_container_width=True)
        st.markdown("Prix : **40 DT**")
    with col2:
        if carte_virtuelle:
            st.image(carte_virtuelle, caption="Carte Virtuelle", use_container_width=True)
        st.markdown("Prix : **50 DT**")

    carte_choisie = st.radio("Choisissez la carte à commander :", ("Physique", "Virtuelle"))
    if st.button("Commander la carte"):
        st.success(f"Commande effectuée pour la carte {carte_choisie.lower()} !")

# Profil
elif choix == "Profil":
    st.title("👤 Mon Profil")
    st.text_input("Nom complet", "Mimi Test")
    st.text_input("Email", "mimi@email.com")
    st.text_input("Numéro client", "C123456789")
    st.success("Profil à jour.")

# Support
elif choix == "Support":
    st.title("📞 Support Client")
    st.write("Vous avez une question ? Nous sommes là pour vous aider.")
    nom = st.text_input("Votre nom")
    message = st.text_area("Votre message")
    if st.button("Envoyer"):
        st.success("Message envoyé ! Un conseiller vous contactera bientôt.")
