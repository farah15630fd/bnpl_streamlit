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

# Navigation personnalisée
pages = {
    "Accueil": "accueil",
    "Simulation Paiement": "simulation",
    "Boutique": "boutique",
    "Commande et gestion des cartes": "commande",
    "Historique Paiement": "historique",
    "Profil": "profil"
}

choix = st.sidebar.selectbox("Navigation", list(pages.keys()))
st.experimental_set_query_params(page=pages[choix])

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
            st.experimental_set_query_params(page="commande")
            st.rerun()

# ... (toutes les autres fenêtres restent inchangées : Simulation, Boutique, Commande, Historique, Profil)

# COMMANDER ET GESTION DES CARTES (à compléter comme dans la version précédente)
if choix == "Commande et gestion des cartes":
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

# PROFIL
elif choix == "Profil":
    st.title("👤 Mon Profil")
    st.text_input("Nom complet", "Ahmed Ali")
    st.text_input("Email", "Ahmed@email.com")
    st.text_input("CIN", "12345678")
    st.success("Profil à jour.")
