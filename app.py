import streamlit as st
from PIL import Image
import requests
import json
from streamlit_lottie import st_lottie

# --- Configuration générale ---
st.set_page_config(page_title="Channel NIANGA – Portfolio", page_icon="🧠", layout="wide")

# --- Animation Lottie ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_pprxh53t.json")
lottie_contact = load_lottie_url("https://assets6.lottiefiles.com/private_files/lf30_e3pteeho.json")

# --- Informations personnelles ---
NOM = "Channel NIANGA"
DESCRIPTION = "🎓 Étudiant Master 2 Informatique parcours Intélligence Artificielle | En recherche d'un stage de fin d'étude | Disponible à partir de Février 2026"
EMAIL = "channeliba@yahoo.com"
VILLE = "Caen, France"
GITHUB = "https://github.com/Niabbach"
LINKEDIN = "https://www.linkedin.com/in/channel-nianga-44095615b"
PHOTO = "Photo.JPG"

# --- Sidebar ---
with st.sidebar:
    st.image(PHOTO, width=150)
    st.markdown(f"### {NOM}")
    st.caption(DESCRIPTION)
    st.markdown(f"📍 **Localisation** : {VILLE}")
    st.markdown(f"📧 [Email](mailto:{EMAIL})")
    st.markdown(f"💼 [GitHub]({GITHUB})")
    st.markdown(f"🔗 [LinkedIn]({LINKEDIN})")
    st.markdown("---")
    page = st.radio("🧭 Navigation", ["🏠 Accueil", "📄 CV", "🚀 Projets", "📬 Contact"])

# --- Accueil ---
if page == "🏠 Accueil":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.title("🌱 Bienvenue sur mon portfolio !")
        st.markdown("""
        Je m'appelle **Channel NIANGA**, étudiant passionné en **Master Informatique**, parcours **Intelligence Artificielle**, actuellement en recherche de stage de fin d'étude.

        Mon objectif ? **Contribuer à des projets innovants en IA**, que ce soit en *machine learning*, *deep learning*, *traitement du langage naturel (NLP)* ou *computer vision*.
        """)
        st.markdown("#### 🔍 Qui suis-je ?")
        st.markdown("""
        - 🎓 Étudiant en IA avec une solide base en algorithmique, statistiques et modélisation.  
        - 💻 Développeur Python expérimenté (TensorFlow, PyTorch, Scikit-learn).  
        - 🚀 Curieux et rigoureux, j'aime explorer de nouvelles méthodes pour résoudre des problèmes complexes.
        """)
        st.markdown("#### 🛠 Ce que vous trouverez ici")
        st.markdown("""
        - Mes projets académiques et personnels en IA *(classification, prédiction, génération de données, etc.)*.  
        - Mes compétences techniques *(Python, SQL, optimisation de modèles...)*.  
        - Mon parcours, mes expériences, et mes ambitions pour un **stage en Master 2**.
        """)
        st.markdown("#### 📫 Envie d'échanger ?")
        st.markdown("""
        🔗 Contactez-moi sur [LinkedIn](https://www.linkedin.com/in/channel-nianga-44095615b)  
        📧 Ou envoyez-moi un mail : [channeliba@yahoo.com](mailto:channeliba@yahoo.com)  
        👉 Ou encore, rendez-vous dans la section **Contact** pour m’envoyer un message.
        """)
        st.markdown("> *\"L'IA est un outil puissant pour façonner demain — j'ai hâte d'y contribuer.\"*")
    with col2:
        st_lottie(lottie_ai, height=350, key="ai")

# --- CV ---
elif page == "📄 CV":
    st.title("📄 Mon CV")
    with open("CV Channel NIANGA.pdf", "rb") as f:
        st.download_button("📥 Télécharger le CV (PDF)", f.read(), "CV_Channel_NIANGA.pdf", mime="application/pdf")

    st.markdown("<hr style='border: 1px solid #bbb;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎓 Formations")
        st.markdown("""
        - Master Informatique parcours IA – Université de Caen *(2026)*  
        - Licence Informatique – CNAM Paris *(2023)*  
        - Licence Sciences de l’Ingénieur – Université de Lorraine Nancy *(2020)*
        """)
        st.markdown("<hr style='border: 1px solid #bbb;'>", unsafe_allow_html=True)

        st.subheader("🧠 Compétences")
        st.markdown(""" 
        - Programmation Python  
        - R et MATLAB  
        - Systèmes de contrôle de version (Git, etc.)  
        - Apprentissage profond (Deep Learning)  
        - Algorithmes d'apprentissage automatique  
        - Vision par ordinateur  
        - Traitement du langage naturel (NLP)  
        - Exploration de données & Big Data  
        - IA éthique  
        - Résolution de problèmes  
        - Bonne communication
        """)
    with col2:
        st.subheader("💼 Expériences")
        st.markdown(""" 
        - **SNCF Réseau** – Développeur Full Stack *(Sept. 2020– Nov. 2023)*  
            - Développement d'une application web et d'API pour les employés ferroviaires.  
            - Réalisation d'analyses de données et automatisation des rapports.  
            - Communication des résultats analytiques aux parties prenantes.  
            - Mise en place de contrôles automatisés pour l'optimisation des processus.  
            **Tech Stack** : Angular (HTML, CSS, TypeScript), Git, Python, Pandas, SQL.

        <hr style='border: 1px solid #bbb;'>

        - **Institut Jean Lamour (IJL)** – Chercheur stagiaire *(janv. 2019 – avr. 2019)*  
            - Stage de recherche en **génie biomédical** sur les capteurs biomédicaux.  
            - Étude et expérimentation de systèmes électroniques pour l’analyse biomédicale.  
            - Contribution à la documentation scientifique du laboratoire.  
            **Compétences** : Génie biomédical, Électronique.

        <hr style='border: 1px solid #bbb;'>

        - **Real Time Sportscast** – Commentateur sportif *(août 2019 – oct. 2021)*  
            - Freelance – Mission exclusivement en anglais  
            - Présence sur le terrain les jours de match pour fournir des commentaires en temps réel.  
            - Réalisation d’interviews avec partenaires et supporteurs.  
            - Rédaction d’articles et de résumés pour le site de l’événement.  
            **Compétences** : Sens de l’organisation, Anglais.
        """, unsafe_allow_html=True)

# --- Projets ---
elif page == "🚀 Projets":
    st.title("🚀 Projets GitHub")
    projets = [
        ("📊 Telecom churn prediction", "Analyse du taux de désabonnement (churn) des clients télécom via EDA et modélisation (Régression logistique, SVM, AdaBoost, XGBoost).", "https://github.com/Niabbach/Telecom-churn-prediction"),
        ("🖼️ Segmentation image", "Ce projet propose une solution simple et efficace pour la segmentation d'image en utilisant deux algorithmes populaires : GrabCut et Graph Cuts.", "https://github.com/Niabbach/Segmentation-Image"),
        ("📈 Sales prediction", "Ce projet met en œuvre un réseau de neurones afin de prédire des ventes sur la base de données historiques", "https://github.com/Niabbach/Sales-prediction"),
        ("🏭 Atelier 4.0", "Ce projet de simulation d'atelier utilise la plateforme JADE (Java Agent DEvelopment Framework) pour créer une simulation interactive d'un environnement de production.", "https://github.com/Niabbach/atelier4.0"),
        ("⚔️ Role Playing Game", "Jeu en C++ (héros, monstres)", "https://github.com/Niabbach/Role-Playing-Game"),
        ("🎿 Ski race management", "Gestion de courses en C", "https://github.com/Niabbach/Ski-race-Management"),
        ("🩺 Pneumonia Detection Model", "Ce projet propose une solution complète pour détecter la pneumonie à partir de radiographies thoraciques en utilisant un réseau de neurones convolutionnel (CNN).", "https://github.com/Niabbach/Pneumonia-detection-model")
    ]
    for nom, desc, lien in projets:
        with st.container():
            left, right = st.columns([0.85, 0.15])
            with left:
                st.subheader(nom)
                st.write(desc)
            with right:
                st.markdown(f"[🔗 GitHub]({lien})")
            st.markdown("---")

# --- Contact ---
elif page == "📬 Contact":
    st.title("📬 Contact")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 💬 Laissez-moi un message")

        st.markdown("""
        <form action="https://formsubmit.co/channeliba@yahoo.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Votre nom" required style="width:100%; padding:0.5em; margin-bottom:0.5em;"><br>
            <input type="email" name="email" placeholder="Votre email" required style="width:100%; padding:0.5em; margin-bottom:0.5em;"><br>
            <textarea name="message" placeholder="Votre message ici..." required style="width:100%; height:150px; padding:0.5em;"></textarea><br>
            <button type="submit" style="margin-top:10px; background:#4CAF50; color:white; padding:0.5em 1em; border:none; border-radius:4px;">Envoyer</button>
        </form>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("")
        st_lottie(lottie_contact, height=300, key="contact")
