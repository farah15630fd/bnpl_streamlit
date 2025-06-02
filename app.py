import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(page_title="Application BNPL", layout="wide")

# Définir le chemin des images
image_path = "images_cartes"

def charger_image(nom_fichier):
    chemin = os.path.join(image_path, nom_fichier)
    if os.path.exists(chemin):
        return Image.open(chemin)
    return None

# État initial
if "carte_achetee" not in st.session_state:
    st.session_state.carte_achetee = "aucune"

# Menu
menu = ["Accueil", "Simulation Paiement", "Boutique", "Commande et gestion des cartes", "Historique Paiement", "Profil"]
choix = st.sidebar.selectbox("Navigation", menu)

# ACCUEIL
if choix == "Accueil":
    st.title("Bienvenue dans votre espace BNPL")
    carte_virtuelle = charger_image("carte_virtuelle.png")
    carte_physique = charger_image("carte_physique.png")

    st.markdown("#### Carte achetée :")
    if st.session_state.carte_achetee == "virtuelle" and carte_virtuelle:
        st.image(carte_virtuelle, caption="Carte virtuelle", use_container_width=True)
    elif st.session_state.carte_achetee == "physique" and carte_physique:
        st.image(carte_physique, caption="Carte physique", use_container_width=True)
    else:
        st.info("Aucune carte achetée pour le moment.")

    if st.session_state.carte_achetee != "aucune":
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
        st.warning("Aucun paiement enregistré. Veuillez commander une carte pour activer votre espace de paiement.")

# SIMULATION PAIEMENT
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

# BOUTIQUE
elif choix == "Boutique":
    st.title("Boutique BNPL")
    produits = [
        {"nom": "Smartphone Samsung A14", "prix": 950, "desc": "Ecran 6.6\" / 128 Go"},
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

# COMMANDE ET GESTION DES CARTES
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
        st.write(f"**Numéro de carte :** 1234 5678 9012 3456")
        st.write(f"**Type :** Carte {st.session_state.carte_achetee.capitalize()}")
        st.write("**Date d'expiration :** 12/2026")
        st.write("**Code de sécurité :** ***")

# HISTORIQUE PAIEMENT
elif choix == "Historique Paiement":
    st.title("📜 Historique des Paiements")
    if st.session_state.carte_achetee != "aucune":
        st.subheader("Paiements par carte physique")
        paiements_physique = [
            ("25/05/2025", "Chaussures Adidas", "220 DT", "FootZone"),
            ("20/05/2025", "Aspirateur Rowenta", "310 DT", "Electro Tounes"),
            ("15/05/2025", "Table basse en bois", "180 DT", "Maison Déco")
        ]
        for date, article, montant, magasin in paiements_physique:
            st.write(f"- {date} — {article} — {montant} — {magasin}")

        st.subheader("Paiements en ligne")
        paiements_en_ligne = [
            ("28/05/2025", "Abonnement Netflix", "29 DT", "Netflix.com"),
            ("22/05/2025", "Recharge téléphonique", "20 DT", "Ooredoo"),
            ("10/05/2025", "Cours Udemy : Python", "45 DT", "Udemy")
        ]
        for date, article, montant, site in paiements_en_ligne:
            st.write(f"- {date} — {article} — {montant} — {site}")
    else:
        st.warning("Aucun historique disponible : aucune carte n’a été achetée.")

# PROFIL
elif choix == "Profil":
    st.title("👤 Mon Profil")
    st.text_input("Nom complet", "Ahmed Ali")
    st.text_input("Email", "Ahmed@email.com")
    st.text_input("CIN", "12345678")
    st.success("Profil à jour.")
