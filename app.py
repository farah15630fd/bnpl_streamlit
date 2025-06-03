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

if "page_commande_demande" not in st.session_state:
    st.session_state.page_commande_demande = False

# Navigation personnalisée
pages = {
    "Accueil": "accueil",
    "Simulation Paiement": "simulation",
    "Boutique": "boutique",
    "Commande et gestion des cartes": "commande",
    "Historique Paiement": "historique",
    "Profil": "profil"
}

# Navigation conditionnelle
if st.session_state.page_commande_demande:
    choix = "Commande et gestion des cartes"
    st.session_state.page_commande_demande = False
else:
    choix = st.sidebar.selectbox("Navigation", list(pages.keys()))

# ACCUEIL
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
        st.markdown("---")
        st.markdown("### 🔍 Qu'est-ce que BNPL ?")
        st.write("""
        Le modèle *Buy Now Pay Later* (Achetez maintenant, payez plus tard) vous permet d'effectuer des achats aujourd'hui 
        et de les rembourser en plusieurs fois sans intérêt ou avec des frais réduits. 
        Pour activer votre espace BNPL, vous devez d'abord commander une carte (virtuelle ou physique).
        """)
        if st.button("🛒 Commander maintenant"):
            st.session_state.page_commande_demande = True
            st.experimental_rerun()

# SIMULATION PAIEMENT (même contenu pour tous)
elif choix == "Simulation Paiement":
    st.title("Simulateur de Paiement BNPL")

    montant = st.number_input("Montant du crédit (DT)", min_value=0.0, step=50.0)
    duree = st.slider("Durée (mois)", 1, 12, 6)

    if montant > 0:
        tmm = 0.075
        marge = 0.03
        interet = (tmm + marge) * (montant/ duree)
        mensualite = interet + (montant / duree)

        st.markdown(f"### Mensualité estimée : **{mensualite:.2f} DT**")
        st.markdown(f"Dont intérêt : {interet:.2f} DT")

# BOUTIQUE (même contenu pour tous)
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
        st.write("**Code de sécurité :** 1234")

# HISTORIQUE PAIEMENT
elif choix == "Historique Paiement":
    st.title("Historique des Paiements")

    if st.session_state.carte_achetee == "aucune":
        st.info("Historique vide")
    else:
        st.markdown("### Paiements par Carte Physique")
        paiements_physique = [
            {"date": "15/05/2025", "montant": "150 DT", "marchand": "Carrefour"},
            {"date": "20/05/2025", "montant": "75 DT", "marchand": "Decathlon"},
        ]
        for p in paiements_physique:
            st.write(f"- {p['date']} : {p['montant']} chez {p['marchand']}")

        st.markdown("### Paiements en Ligne")
        paiements_en_ligne = [
            {"date": "17/05/2025", "montant": "200 DT", "marchand": "Amazon"},
            {"date": "22/05/2025", "montant": "50 DT", "marchand": "Spotify"},
        ]
        for p in paiements_en_ligne:
            st.write(f"- {p['date']} : {p['montant']} chez {p['marchand']}")

# PROFIL
elif choix == "Profil":
    st.title("👤 Mon Profil")
    st.text_input("Nom complet", "Ahmed Ali")
    st.text_input("Email", "Ahmed@email.com")
    st.text_input("CIN", "12345678")
    st.success("Profil à jour.")
