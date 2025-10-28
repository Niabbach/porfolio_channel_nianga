import streamlit as st
from PIL import Image
import requests
import json
from streamlit_lottie import st_lottie
import datetime

# --- Configuration générale ---
st.set_page_config(
    page_title="Channel NIANGA - Data Scientist & AI Engineer | Master IA | Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': """Portfolio de Channel NIANGA - Expert en Intelligence Artificielle, 
        Machine Learning, Deep Learning et Computer Vision. 
        En recherche de stage de fin d'études à partir de Février 2026."""
    }
)

# --- Fonctions SEO et Accessibilité ---
def add_seo_meta():
    st.markdown("""
    <!-- Primary Meta Tags -->
    <title>Channel NIANGA - Data Scientist & AI Engineer | Master IA</title>
    <meta name="title" content="Channel NIANGA - Data Scientist & AI Engineer | Master IA">
    <meta name="description" content="Étudiant en Master 2 IA spécialisé en Machine Learning, Deep Learning et Computer Vision. Portfolio avec projets concrets en Python, TensorFlow, PyTorch.">
    <meta name="keywords" content="data scientist, intelligence artificielle, machine learning, deep learning, python, tensorflow, pytorch, computer vision, nlp, portfolio, stage IA">
    <meta name="author" content="Channel NIANGA">
    <meta name="robots" content="index, follow">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Google Search Console Verification -->
    <meta name="google-site-verification" content="JcDPwV9OUPc0dK5stCs_APshLfHxknw4JLH0rBDyTfU" />
    
    <!-- Sitemap -->
    <link rel="sitemap" type="application/xml" title="Sitemap" href="/sitemap.xml">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://channelnianga-portfolio.streamlit.app/">
    <meta property="og:title" content="Channel NIANGA - Data Scientist & AI Engineer">
    <meta property="og:description" content="Portfolio d'un expert en IA - Projets en ML, Deep Learning et Computer Vision">
    <meta property="og:image" content="https://channelnianga-portfolio.streamlit.app/images/Photo.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://channelnianga-portfolio.streamlit.app/">
    <meta property="twitter:title" content="Channel NIANGA - Data Scientist & AI Engineer">
    <meta property="twitter:description" content="Portfolio d'un expert en IA - Projets en ML, Deep Learning et Computer Vision">
    <meta property="twitter:image" content="https://channelnianga-portfolio.streamlit.app/images/Photo.png">
    
    <!-- Structured Data for SEO -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org/",
        "@type": "Person",
        "name": "Channel NIANGA",
        "url": "https://channelnianga-portfolio.streamlit.app",
        "image": "https://channelnianga-portfolio.streamlit.app/images/Photo.png",
        "description": "Data Scientist and AI Engineer specializing in Machine Learning and Deep Learning",
        "jobTitle": "Data Scientist & AI Engineer",
        "alumniOf": {
            "@type": "CollegeOrUniversity",
            "name": "University of Caen"
        },
        "knowsAbout": ["Python", "Machine Learning", "Deep Learning", "Computer Vision", "Natural Language Processing", "Data Science"],
        "seeks": "Internship in Artificial Intelligence",
        "availableFrom": "2026-03-03"
    }
    </script>

    <!-- International SEO -->
    <link rel="alternate" hreflang="fr" href="https://channelnianga-portfolio.streamlit.app/?lang=fr" />
    <link rel="alternate" hreflang="en" href="https://channelnianga-portfolio.streamlit.app/?lang=en" />
    <link rel="alternate" hreflang="x-default" href="https://channelnianga-portfolio.streamlit.app/" />
    """, unsafe_allow_html=True)

def add_skip_links():
    st.markdown("""
    <a href="#main-content" class="sr-only skip-link">Passer au contenu principal</a>
    <a href="#navigation" class="sr-only skip-link">Aller à la navigation</a>
    """, unsafe_allow_html=True)

def load_accessible_image(path, alt_text):
    """Charge une image avec texte alternatif approprié"""
    try:
        img = Image.open(path)
        st.image(img, 
                caption=alt_text, 
                use_container_width=True, 
                output_format="auto")
        st.markdown(f'<span class="sr-only">Image: {alt_text}</span>', 
                   unsafe_allow_html=True)
        return True
    except Exception as e:
        st.error(f"Image non chargée: {alt_text}")
        return False

def project_card_accessible(title, description, github_url, technologies=None):
    """Carte de projet accessible"""
    tech_str = ""
    if technologies:
        tech_str = f"<p><strong>Technologies :</strong> {', '.join(technologies)}</p>"
    
    return f"""
    <article class="project-card" role="article" aria-labelledby="{title.replace(' ', '-').lower()}">
        <h3 id="{title.replace(' ', '-').lower()}" style="margin-top: 0;">{title}</h3>
        <p>{description}</p>
        {tech_str}
        <a href="{github_url}" 
           target="_blank" 
           aria-label="Voir le projet {title} sur GitHub"
           style="text-decoration: none;">
           🔗 <span style="color:#4CAF50;">Code GitHub</span>
        </a>
    </article>
    """

def accessible_button(text, key, url=None):
    """Bouton accessible avec ARIA labels"""
    if url:
        return st.markdown(f"""
        <a href="{url}" target="_blank" 
           aria-label="{text} - Ouvrir dans un nouvel onglet"
           class="accessible-button"
           style="text-decoration: none;">
            <button style="width: 100%;">
                {text}
            </button>
        </a>
        """, unsafe_allow_html=True)
    else:
        return st.button(text, key=key, use_container_width=True)

# --- Application des optimisations SEO et Accessibilité ---
add_seo_meta()
add_skip_links()

# --- Cache pour les ressources ---
@st.cache_data
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

@st.cache_data
def load_pdf():
    with open("CV Channel NIANGA.pdf", "rb") as f:
        return f.read()

lottie_ai = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_pprxh53t.json")
lottie_contact = load_lottie_url("https://assets6.lottiefiles.com/private_files/lf30_e3pteeho.json")

# --- Style CSS personnalisé ---
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --- Données personnelles ---
NOM = "Channel NIANGA"
DESCRIPTION_FR = "🎓 Étudiant en Master 2 Informatique parcours Intélligence Artificielle | En recherche d'un stage de fin d'étude | Disponible à partir de Mars 2026"
DESCRIPTION_EN = "🎓 Master's student in Computer Science specializing in Artificial Intelligence | Seeking final year internship | Available from March 2026"
EMAIL = "channeliba@yahoo.com"
VILLE = "Caen, France"
GITHUB = "https://github.com/Niabbach"
LINKEDIN = "https://www.linkedin.com/in/channel-nianga-44095615b"
PHOTO = "images/Photo.png"

# --- Traductions ---
translations = {
    "fr": {
        "sidebar": {
            "location": "📍 **Localisation** :",
            "email": "📧 [Email](mailto:{})",
            "github": "💼 [GitHub]({})",
            "linkedin": "🔗 [LinkedIn]({})",
            "nav": ["🏠 Accueil", "📄 CV", "🚀 Projets", "📬 Contact"]
        },
        "home": {
            "title": "🌱 Bienvenue sur mon portfolio !",
            "seo_title": "Channel NIANGA - Expert en Intelligence Artificielle",
            "seo_content": """
            <div itemscope itemtype="https://schema.org/Person">
                <meta itemprop="name" content="Channel NIANGA">
                <meta itemprop="jobTitle" content="Data Scientist & AI Engineer">
                <p><strong>Expert en <span itemprop="knowsAbout">Intelligence Artificielle</span>, 
                <span itemprop="knowsAbout">Machine Learning</span> et 
                <span itemprop="knowsAbout">Deep Learning</span></strong>. 
                Étudiant en Master 2 IA à l'Université de Caen, 
                je recherche un <strong>stage de fin d'études à partir de Mars 2026</strong> 
                dans les domaines de l'IA, la data science et l'analyse de données.</p>
            </div>
            """,
            "content": """Je m'appelle **Channel NIANGA**, étudiant passionné en **Master Informatique**, parcours **Intelligence Artificielle**, actuellement en recherche de stage de fin d'étude.
            Mon objectif ? **Contribuer à des projets innovants en IA**, que ce soit en *machine learning*, *deep learning*, *traitement du langage naturel (NLP)* ou *computer vision*.
            """,
            "who": "#### 🔍 Qui suis-je ?",
            "who_content": """
            - 🎓 Étudiant en IA avec une solide base en algorithmique, statistiques et modélisation.  
            - 💻 Développeur Python expérimenté (TensorFlow, PyTorch, Scikit-learn).  
            - 🚀 Curieux et rigoureux, j'aime explorer de nouvelles méthodes pour résoudre des problèmes complexes.
            """,
            "find": "#### 🛠 Ce que vous trouverez ici",
            "find_content": """
            - Mes projets académiques et personnels en IA *(classification, prédiction, génération de données, etc.)*.  
            - Mes compétences techniques *(Python, SQL, optimisation de modèles...)*.  
            - Mon parcours, mes expériences, et mes ambitions pour un **stage en Master 2**.
            """,
            "contact": "#### 📫 Envie d'échanger ?",
            "contact_content": """
            🔗 Contactez-moi sur [LinkedIn](https://www.linkedin.com/in/channel-nianga-44095615b)  
            📧 Ou envoyez-moi un mail : [channeliba@yahoo.com](mailto:channeliba@yahoo.com)  
            👉 Ou encore, rendez-vous dans la section **Contact** pour m'envoyer un message.
            """,
            "quote": "> *\"L'IA est un outil puissant pour façonner demain — j'ai hâte d'y contribuer.\"*"
        },
        "cv": {
            "title": "📄 Mon CV",
            "download": "📥 Télécharger le CV (PDF)",
            "education": "🎓 Formations",
            "education_content": """
            - Master Informatique parcours IA – Université de Caen *(2026)*  
            - Licence Informatique – CNAM Paris *(2023)*  
            - Licence Sciences de l'Ingénieur – Université de Lorraine Nancy *(2020)*
            """,
            "skills": "🧠 Compétences",
            "skills_content": """ 
            - Programmation Python  
            - R et MATLAB  
            - Systèmes de contrôle de version (Git, etc.)  
            - Apprentissage profond 
            - Algorithmes d'apprentissage automatique  
            - Vision par ordinateur  
            - Traitement du langage naturel 
            - Exploration de données & Big Data  
            - IA éthique  
            - Résolution de problèmes  
            - Bonne communication
            """,
            "experience": "💼 Expériences",
            "experience_content": """ 
            - **SNCF Réseau** – Développeur Full Stack *(Sept. 2020– Nov. 2023)*  
                - Développement d'une application web et d'API pour les employés ferroviaires.  
                - Réalisation d'analyses de données et automatisation des rapports.  
                - Communication des résultats analytiques aux parties prenantes.  
                - Mise en place de contrôles automatisés pour l'optimisation des processus.  
                **Tech Stack** : Angular (HTML, CSS, TypeScript), Git, Python, Pandas, SQL.

            <hr style='border: 1px solid #bbb;'> 

            - **Institut Jean Lamour (IJL)** – Chercheur stagiaire *(janv. 2019 – avr. 2019)*  
                - Stage de recherche en **génie biomédical** sur les capteurs biomédicaux.  
                - Étude et expérimentation de systèmes électroniques pour l'analyse biomédicale.  
                - Contribution à la documentation scientifique du laboratoire.  
                **Compétences** : Génie biomédical, Électronique.

            <hr style='border: 1px solid #bbb;'> 

            - **Real Time Sportscast** – Commentateur sportif *(août 2019 – oct. 2021)*  
                - Freelance – Mission exclusivement en anglais  
                - Présence sur le terrain les jours de match pour fournir des commentaires en temps réel.  
                - Réalisation d'interviews avec partenaires et supporteurs.  
                - Rédaction d'articles et de résumés pour le site de l'événement.  
                **Compétences** : Sens de l'organisation, Anglais.
            """
        },
        "projects": {
            "title": "🚀 Projets GitHub",
            "tabs": ["🤖 Intelligence Artificielle", "💻 Développement", "🎓 Académique"],
            "projects_ia": [
                ("📊 Telecom churn prediction", "Analyse du taux de désabonnement (churn) des clients télécom via EDA et modélisation (Régression logistique, SVM, AdaBoost, XGBoost).", "https://github.com/Niabbach/Telecom-churn-prediction", ["Python", "Pandas", "Scikit-learn", "XGBoost"]),
                ("🖼️ Segmentation image", "Ce projet propose une solution simple et efficace pour la segmentation d'image en utilisant deux algorithmes populaires(Grabcut et Graph cut).", "https://github.com/Niabbach/Segmentation-Image", ["Python", "OpenCV", "NumPy"]),
                ("📈 Sales prediction", "Ce projet met en œuvre un réseau de neurones afin de prédire des ventes sur la base de données historiques.", "https://github.com/Niabbach/Sales-prediction", ["Python", "TensorFlow", "Keras"]),
                ("🩺 Pneumonia Detection Model", "Ce projet propose une solution complète pour détecter la pneumonie à partir de radiographies thoraciques en utilisant un réseau de neurones convolutionnel (CNN).", "https://github.com/Niabbach/Pneumonia-detection-model", ["Python", "TensorFlow", "CNN", "Medical Imaging"])
            ],
            "projects_dev": [
                ("⚔️ Role Playing Game", "Jeu en C++ (héros, monstres)", "https://github.com/Niabbach/Role-Playing-Game", ["C++", "OOP"]),
                ("🎿 Ski race management", "Gestion de courses en C", "https://github.com/Niabbach/Ski-race-Management", ["C", "Algorithms"])
            ],
            "projects_aca": [
                ("🏭 Atelier 4.0", "Ce projet de simulation d'atelier utilise la plateforme JADE (Java Agent DEvelopment Framework) pour créer une simulation interactive d'un environnement de production.", "https://github.com/Niabbach/atelier4.0", ["Java", "JADE", "Multi-agent Systems"]),
                ("🌐 Application GraphQL avec base MongoDB et visualisations D3.js", "Ce projet consiste en une application GraphQL qui interagit avec une base de données MongoDB pour fournir des données sur des prestations de service, avec une interface de visualisation basée sur D3.js.", "https://github.com/Niabbach/tp-docker", ["GraphQL", "MongoDB", "D3.js", "Node.js"]),
                ("🟦 ShapeGame", "Jeu graphique Java avec design patterns (MVC, State, Observer, Strategy, Adapter)", "https://github.com/Niabbach/ShapeGame", ["Java", "Design Patterns", "MVC"]),
                ("👥 Mastermind Adversarial","Implémentation avancée du jeu Mastermind où deux IA (Alice et Bob) s'affrontent avec différentes stratégies (Knuth, MinMax, etc.).", "https://github.com/Niabbach/mastermind_adversarial", ["Python", "AI", "Game Theory"])
            ],
            "back_to_top": "↑ Retour en haut"
        },
        "contact": {
            "title": "📬 Contact",
            "form_title": "#### 💬 Laissez-moi un message",
            "form": """
            <form action="https://formsubmit.co/channeliba@yahoo.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Votre nom" required style="width:100%; padding:0.5em; margin-bottom:0.5em;"><br>
                <input type="email" name="email" placeholder="Votre email" required style="width:100%; padding:0.5em; margin-bottom:0.5em;"><br>
                <textarea name="message" placeholder="Votre message ici..." required style="width:100%; height:150px; padding:0.5em;"></textarea><br>
                <button type="submit" style="margin-top:10px; background:#4CAF50; color:white; padding:0.5em 1em; border:none; border-radius:4px;">Envoyer</button>
            </form>
            """
        }
    },
    "en": {
        "sidebar": {
            "location": "📍 **Location**:",
            "email": "📧 [Email](mailto:{})",
            "github": "💼 [GitHub]({})",
            "linkedin": "🔗 [LinkedIn]({})",
            "nav": ["🏠 Home", "📄 Resume", "🚀 Projects", "📬 Contact"]
        },
        "home": {
            "title": "🌱 Welcome to my portfolio!",
            "seo_title": "Channel NIANGA - Artificial Intelligence Scientist",
            "seo_content": """
            <div itemscope itemtype="https://schema.org/Person">
                <meta itemprop="name" content="Channel NIANGA">
                <meta itemprop="jobTitle" content="Data Scientist & AI Engineer">
                <p><strong>Expert in <span itemprop="knowsAbout">Artificial Intelligence</span>, 
                <span itemprop="knowsAbout">Machine Learning</span> and 
                <span itemprop="knowsAbout">Deep Learning</span></strong>. 
                Master's student in AI at the University of Caen, 
                I'm looking for a <strong>final year internship starting March 2026</strong> 
                in the fields of AI, data science and data analysis.</p>
            </div>
            """,
            "content": """I'm **Channel NIANGA**, a passionate student in **Master's in Computer Science**, specializing in **Artificial Intelligence**, currently looking for a final year internship.
            My goal? **Contribute to innovative AI projects**, whether in *machine learning*, *deep learning*, *natural language processing (NLP)* or *computer vision*.""",
            "who": "#### 🔍 Who am I?",
            "who_content": """
            - 🎓 AI student with strong foundation in algorithms, statistics and modeling  
            - 💻 Experienced Python developer (TensorFlow, PyTorch, Scikit-learn)  
            - 🚀 Curious and rigorous, I enjoy exploring new methods to solve complex problems
            """,
            "find": "#### 🛠 What you'll find here",
            "find_content": """
            - My academic and personal projects in AI *(classification, prediction, data generation, etc.)*  
            - My technical skills *(Python, SQL, model optimization...)*  
            - My background, experiences, and ambitions for a **Master's internship**
            """,
            "contact": "#### 📫 Want to connect?",
            "contact_content": """
            🔗 Contact me on [LinkedIn](https://www.linkedin.com/in/channel-nianga-44095615b)  
            📧 Or send me an email: [channeliba@yahoo.com](mailto:channeliba@yahoo.com)  
            👉 Or visit the **Contact** section to send me a message.
            """,
            "quote": "> *\"AI is a powerful tool to shape tomorrow — I'm excited to contribute.\"*"
        },
        "cv": {
            "title": "📄 My Resume",
            "download": "📥 Download Resume (PDF)",
            "education": "🎓 Education",
            "education_content": """
            - Master's in Computer Science,  specializing in AI – University of Caen *(2026)*  
            - Bachelor's in Computer Science – CNAM Paris *(2023)*  
            - Bachelor's in Engineering Sciences – University of Lorraine Nancy *(2020)*
            """,
            "skills": "🧠 Skills",
            "skills_content": """ 
            - Python programming  
            - R and MATLAB  
            - Version control systems (Git, etc.)  
            - Deep Learning  
            - Machine Learning algorithms  
            - Computer Vision  
            - Natural Language Processing (NLP)  
            - Data Exploration & Big Data  
            - Ethical AI  
            - Problem solving  
            - Good communication
            """,
            "experience": "💼 Experience",
            "experience_content": """ 
            - **SNCF Réseau** – Full Stack Developer *(Sept. 2020– Nov. 2023)*  
                - Development of a web application and APIs for railway employees.  
                - Data analysis and report automation.  
                - Communication of analytical results to stakeholders.  
                - Implementation of automated controls for process optimization.  
                **Tech Stack**: Angular (HTML, CSS, TypeScript), Git, Python, Pandas, SQL.

            <hr style='border: 1px solid #bbb;'> 

            - **Jean Lamour Institute (IJL)** – Research Intern *(Jan. 2019 – Apr. 2019)*  
                - Research internship in **biomedical engineering** on biomedical sensors.  
                - Study and experimentation of electronic systems for biomedical analysis.  
                - Contribution to the laboratory's scientific documentation.  
                **Skills**: Biomedical engineering, Electronics.

            <hr style='border: 1px solid #bbb;'> 

            - **Real Time Sportscast** – Sports Commentator *(Aug. 2019 – Oct. 2021)*  
                - Freelance – English-only assignments  
                - On-site presence during matches to provide real-time commentary.  
                - Conducting interviews with partners and supporters.  
                - Writing articles and summaries for the event website.  
                **Skills**: Organizational skills, English.
            """
        },
        "projects": {
            "title": "🚀 GitHub Projects",
            "tabs": ["🤖 Artificial Intelligence", "💻 Development", "🎓 Academic"],
            "projects_ia": [
                ("📊 Telecom churn prediction", "Analysis of telecom customer churn rate through EDA and modeling (Logistic Regression, SVM, AdaBoost, XGBoost).", "https://github.com/Niabbach/Telecom-churn-prediction", ["Python", "Pandas", "Scikit-learn", "XGBoost"]),
                ("🖼️ Image segmentation", "This project offers a simple and effective solution for image segmentation using two popular algorithms (GrabCut and Graph Cut).", "https://github.com/Niabbach/Segmentation-Image", ["Python", "OpenCV", "NumPy"]),
                ("📈 Sales prediction", "This project implements a neural network to predict sales based on historical data.", "https://github.com/Niabbach/Sales-prediction", ["Python", "TensorFlow", "Keras"]),
                ("🩺 Pneumonia Detection Model", "This project provides a complete solution for detecting pneumonia from chest X-rays using a Convolutional Neural Network (CNN).", "https://github.com/Niabbach/Pneumonia-detection-model", ["Python", "TensorFlow", "CNN", "Medical Imaging"])
            ],
            "projects_dev": [
                ("⚔️ Role Playing Game", "Game in C++ (heroes, monsters)", "https://github.com/Niabbach/Role-Playing-Game", ["C++", "OOP"]),
                ("🎿 Ski race management", "Race management in C", "https://github.com/Niabbach/Ski-race-Management", ["C", "Algorithms"])
            ],
            "projects_aca": [
                ("🏭 Workshop 4.0", "This workshop simulation project uses the JADE platform (Java Agent DEvelopment Framework) to create an interactive production environment simulation.", "https://github.com/Niabbach/atelier4.0", ["Java", "JADE", "Multi-agent Systems"]),
                ("🌐 GraphQL/MongoDB Dashboard", "A full-stack project using GraphQL (Node.js/Apollo) and MongoDB, with a frontend dashboard powered by D3.js for data visualization.", "https://github.com/Niabbach/tp-docker", ["GraphQL", "MongoDB", "D3.js", "Node.js"]),
                ("🟦 ShapeGame", "Java graphic game using design patterns (MVC, State, Observer, Strategy, Adapter)", "https://github.com/Niabbach/ShapeGame", ["Java", "Design Patterns", "MVC"]),
                ("👥 Adversarial Mastermind", "Advanced implementation of Mastermind game where two AIs (Alice and Bob) compete with different strategies (Knuth, MinMax, etc.).", "https://github.com/Niabbach/mastermind_adversarial", ["Python", "AI", "Game Theory"])
            ],
            "back_to_top": "↑ Back to top"
        },
        "contact": {
            "title": "📬 Contact",
            "form_title": "#### 💬 Send me a message",
            "form": """
            <form action="https://formsubmit.co/channeliba@yahoo.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required style="width:100%; padding:0.5em; margin-bottom:0.5em;"><br>
                <input type="email" name="email" placeholder="Your email" required style="width:100%; padding:0.5em; margin-bottom:0.5em;"><br>
                <textarea name="message" placeholder="Your message here..." required style="width:100%; height:150px; padding:0.5em;"></textarea><br>
                <button type="submit" style="margin-top:10px; background:#4CAF50; color:white; padding:0.5em 1em; border:none; border-radius:4px;">Send</button>
            </form>
            """
        }
    }
}

# --- Sidebar avec accessibilité ---
with st.sidebar:
    st.markdown('<div id="navigation" role="navigation" aria-label="Navigation principale">', unsafe_allow_html=True)
    
    # Image accessible sans texte
    load_accessible_image(PHOTO, "")
    
    
    # Sélecteur de langue accessible
    lang = st.radio("🌐 Language", ["Français", "English"], key="lang", 
                   label_visibility="visible")
    lang_key = "fr" if lang == "Français" else "en"
    
    st.caption(DESCRIPTION_FR if lang == "Français" else DESCRIPTION_EN)
    st.markdown(f"{translations[lang_key]['sidebar']['location']} {VILLE}")
    st.markdown(translations[lang_key]['sidebar']['email'].format(EMAIL))
    st.markdown(translations[lang_key]['sidebar']['github'].format(GITHUB))
    st.markdown(translations[lang_key]['sidebar']['linkedin'].format(LINKEDIN))
    st.markdown("---")
    
    # Navigation accessible
    page = st.radio("🧭 Navigation", 
                   translations[lang_key]['sidebar']['nav'],
                   label_visibility="visible")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- Contenu principal avec structure sémantique ---
st.markdown('<main id="main-content" role="main">', unsafe_allow_html=True)

# --- Pages ---
if page == translations[lang_key]['sidebar']['nav'][0]:  # Accueil/Home
    col1, col2 = st.columns([1, 1])
    with col1:
        # Titre SEO-friendly avec traduction
        st.markdown(f"# {translations[lang_key]['home']['seo_title']}", unsafe_allow_html=True)
        
        # Contenu structuré avec microdata et traduction
        st.markdown(translations[lang_key]['home']['seo_content'], unsafe_allow_html=True)
        
        st.markdown(translations[lang_key]['home']['content'])
        st.markdown(translations[lang_key]['home']['who'])
        st.markdown(translations[lang_key]['home']['who_content'])
        st.markdown(translations[lang_key]['home']['find'])
        st.markdown(translations[lang_key]['home']['find_content'])
        st.markdown(translations[lang_key]['home']['contact'])
        st.markdown(translations[lang_key]['home']['contact_content'])
        st.markdown(translations[lang_key]['home']['quote'])
        
    with col2:
        st_lottie(lottie_ai, height=350, key="ai")

elif page == translations[lang_key]['sidebar']['nav'][1]:  # CV/Resume
    st.title(translations[lang_key]['cv']['title'])
    
    # Bouton de téléchargement accessible
    if lang_key == "fr":
        with open("CV Channel NIANGA.pdf", "rb") as f:
            st.download_button(
                label=translations[lang_key]['cv']['download'],
                data=f.read(),
                file_name="CV_Channel_NIANGA.pdf",
                mime="application/pdf",
                key="cv_download_fr",
                use_container_width=True
            )
    else:
        with open("Resume Channel NIANGA.pdf", "rb") as f:
            st.download_button(
                label=translations[lang_key]['cv']['download'],
                data=f.read(),
                file_name="Resume_Channel_NIANGA.pdf",
                mime="application/pdf",
                key="cv_download_en",
                use_container_width=True
            )

    st.markdown("<hr style='border: 1px solid #bbb;'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(translations[lang_key]['cv']['education'])
        st.markdown(translations[lang_key]['cv']['education_content'])
        st.markdown("<hr style='border: 1px solid #bbb;'>", unsafe_allow_html=True)
        st.subheader(translations[lang_key]['cv']['skills'])
        st.markdown(translations[lang_key]['cv']['skills_content'])
    
    with col2:
        st.subheader(translations[lang_key]['cv']['experience'])
        st.markdown(translations[lang_key]['cv']['experience_content'], unsafe_allow_html=True)

elif page == translations[lang_key]['sidebar']['nav'][2]:  # Projets/Projects
    st.title(translations[lang_key]['projects']['title'])
    
    tab1, tab2, tab3 = st.tabs(translations[lang_key]['projects']['tabs'])
    
    with tab1:
        for nom, desc, lien, technologies in translations[lang_key]['projects']['projects_ia']:
            st.markdown(project_card_accessible(nom, desc, lien, technologies), unsafe_allow_html=True)
            st.markdown("---")
    
    with tab2:
        for nom, desc, lien, technologies in translations[lang_key]['projects']['projects_dev']:
            st.markdown(project_card_accessible(nom, desc, lien, technologies), unsafe_allow_html=True)
            st.markdown("---")

    with tab3:
        for nom, desc, lien, technologies in translations[lang_key]['projects']['projects_aca']:
            st.markdown(project_card_accessible(nom, desc, lien, technologies), unsafe_allow_html=True)
            st.markdown("---")
    
    # Bouton Retour en haut accessible
    st.markdown(f"""
    <div class="back-to-top">
        <a href="#main-content" 
           aria-label="{translations[lang_key]['projects']['back_to_top']}"
           style="text-decoration:none;">
           {translations[lang_key]['projects']['back_to_top']}
        </a>
    </div>
    """, unsafe_allow_html=True)

elif page == translations[lang_key]['sidebar']['nav'][3]:  # Contact
    st.title(translations[lang_key]['contact']['title'])
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(translations[lang_key]['contact']['form_title'])
        st.markdown(translations[lang_key]['contact']['form'], unsafe_allow_html=True)
    with col2:
        st_lottie(lottie_contact, height=350, key="contact_animation")

# Fermeture de la balise main
st.markdown('</main>', unsafe_allow_html=True)

# --- Sitemap implicite pour l'accessibilité ---
st.markdown("""
<nav aria-label="Plan du site" class="sr-only">
    <h2>Plan du site</h2>
    <ul>
        <li><a href="#main-content">Accueil/Home</a></li>
        <li><a href="#education">Formation/Education</a></li>
        <li><a href="#experience">Expérience/Experience</a></li>
        <li><a href="#projects">Projets/Projects</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)