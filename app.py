import streamlit as st
from PIL import Image
import os

# Titre principal
st.set_page_config(page_title="BNPL App", layout="centered")
st.title("💳 Interface BNPL")

# Définir le chemin des images (local, relatif)
image_path = "images_cartes"

# Fonctions d'affichage avec gestion d'erreur
def afficher_image(nom_fichier, titre):
    chemin_image = os.path.join(image_path, nom_fichier)
    if os.path.exists(chemin_image):
        image = Image.open(chemin_image)
        st.image(image, caption=titre, use_column_width=True)
    else:
        st.warning(f"❌ L'image '{nom_fichier}' est introuvable dans le dossier '{image_path}'.")

# Affichage des cartes
st.subheader("Carte BNPL Virtuelle")
afficher_image("carte_virtuelle.png", "Carte Virtuelle")

st.subheader("Carte BNPL Physique")
afficher_image("carte_physique.png", "Carte Physique")

# Footer
st.markdown("---")
st.markdown("🛒 Application Buy Now Pay Later (BNPL) - Mockup Streamlit Demo")
