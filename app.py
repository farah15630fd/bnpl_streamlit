import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(page_title="Application BNPL", layout="wide")

# Chargement des images
image_path = "images_cartes"

def charger_image(nom_fichier):
    chemin = os.path.join(image_path, nom_fichier)
    if os.path.exists(chemin):
        return Image.open(chemin)
    return None

# Initialisation de l'état global
if "carte_achetee" not in st.session_state:
    st.session_state.carte_achetee = "aucune"

# Navigation
menu = ["Accueil", "Simulation Paiement", "Boutique", "Commande et gestion des cartes", "Historique Paiement", "Profil"]
choix = st.sidebar.selectbox("Navigation", menu)

# Page Accueil
if choix == "Accueil":
    st.title("Bienvenue dans votre espace BNPL")
    carte_virtuelle = charger_image("carte_virtuelle.png")
    carte_physique = charger_image("carte_physique.png")

    if st.session_state.carte_achetee != "aucune":
        st.markdown("#### Carte achetée :")
        if st.session_state.carte_achetee == "virtuelle" and carte_virtuelle:
            st.image(carte_virtuelle, caption="Carte virtuelle", use_container_width=True)
        elif st.session_state.carte_achetee == "physique" and carte_physique:
            st.image(carte_physique, caption="Carte physique", use_container_width=True)

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
    else:
        st.info("Aucune carte achetée pour le moment.\n\nAucune donnée de paiement disponible tant qu'une carte n'est pas activée.")
        st.markdown("### 🔍 Qu'est-ce que BNPL ?")
        st.write("""
        Le modèle *Buy Now Pay Later* vous permet d’acheter maintenant et de payer plus tard en plusieurs fois. 
        Pour activer votre espace BNPL, veuillez commander une carte.
        """)
        if st.button("🛒 Commander maintenant"):
            st.session_state.page = "Commande et gestion des cartes"
            st.experimental_rerun()

# Page Simulation Paiement
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

# Page Boutique
elif choix == "Boutique":
    st.title("Boutique BNPL")
    produits = [
        {"nom": "PC Portable HP 14\"", "prix": 1200, "desc": "Core i3 / 8Go / SSD"},
        {"nom": "TV LG 50''", "prix": 1900, "desc": "4K UHD Smart"},
        {"nom": "Casque JBL", "prix": 300, "desc": "Bluetooth / Bass Boost"},
        {"nom": "Montre connectée Xiaomi", "prix": 450, "desc": "GPS, Cardio"},
        {"nom": "Aspirateur Xiaomi", "prix": 650, "desc": "Sans fil, silencieux"},
    ]
    for p in produits:
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"**{p['nom']}** — {p['prix']} DT  \n> *{p['desc']}*")
        with col2:
            st.button("🛒", key=p['nom'])

# Page Commande Carte
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
        st.session_state.carte_achetee = carte_choisie.lower()
        st.success(f"Commande effectuée pour la carte {carte_choisie.lower()} !")

    if st.session_state.carte_achetee != "aucune":
        st.markdown("### 📇 Informations de la carte")
        st.write("**Numéro de carte :** 1234 5678 9012 3456")
        st.write(f"**Type :** Carte {st.session_state.carte_achetee.capitalize()}")
        st.write("**Date d'expiration :** 12/2026")
        st.write("**Code de sécurité :** ***")

# Historique Paiement
elif choix == "Historique Paiement":
    st.title("📜 Historique des Paiements")
    st.markdown("### Paiements par carte physique")
    st.write("- **11/05/2025** — 240 DT — Boutique Electroménager")
    st.write("- **25/04/2025** — 150 DT — Magasin de sport")
    st.markdown("### Paiements en ligne")
    st.write("- **09/05/2025** — 120 DT — Site Web e-commerce")
    st.write("- **30/04/2025** — 80 DT — Abonnement musique")

# PROFIL
elif choix == "Profil":
    st.title("👤 Mon Profil")
    st.text_input("Nom complet", "Ahmed Ali")
    st.text_input("Email", "Ahmed@email.com")
    st.text_input("CIN", "12345678")
    st.success("Profil à jour.")
