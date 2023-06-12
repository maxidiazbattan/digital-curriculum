from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Resume | Maximiliano Diaz Battan"
PAGE_ICON = ":wave:"
NAME = "Maximiliano Diaz Battan"
DESCRIPTION =   """
                BBA | Data Analyst
                """
EMAIL = "maxidiazbattan@gmail.com"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- OPTION MENU ---

selected = option_menu(
    menu_title=None,
    options=['Home', 'Proyects', 'Contact'],
    icons=['house', 'book', 'envelope'],
    default_index=0,
    orientation='horizontal',
    styles= {
        "container": {"padding": "0!important", "background-color": "#141414"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
        "nav-link-selected": {"background-color": "darkgray"},
            }

)


if selected == 'Home':

    # --- ME SECTION ---
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.title(NAME)
        st.write(DESCRIPTION)
    
    with col2:
        st.write('')
        
    with col3:
        st.image(profile_pic, width=230)

    # --- ABOUT ME ---
    st.write('\n')
    st.header("About me")
    st.write("---")
    st.write(
    """
    I have been working as a business administrator for 10 years and have always been fascinated by the field of data. A few years ago, I discovered Python and its vast capabilities. 
    That's why I decided to focus on studying data analysis with Python and am now pursuing data science. 
    My goal is to obtain a master's degree in the field of data in the next few years and transition fully into this exciting field.
    """
    )


    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.header("Experience & Qualifications")
    st.write("---")
    st.write(
        """
    - ✔️ 10 Years of accounting experience and more than a year of freelancing experience extracting insights of data and machine learning.
    - ✔️ Deep understanding of Python, SQL and Excel.
    - ✔️ A strong grasp of statistical principles and their practical applications.
    - ✔️ Great team player.
        """
    )


    # --- SKILLS ---
    st.write('\n')
    st.header("Hard Skills")
    st.write("---")
    st.write(
        """
    - 💻 Languages: Python, SQL, Excel.
    - 📊 Data analysis: Pandas, Modin, Rapids (cuDF & cuPY), DuckDB, Sqlite3, Numpy, Matplotlib, Seaborn, Plotly, Dash, and more.
    - 📚 Machine Learning: Sklearn, Rapids (cuML), XGBoost, LightGBM, Catboost, Interpret, Tabnet, Optuna, Feature Engine, SHAP, Streamlit, and more.
    - 📚 Deep Learning: Pytorch, Pytorch lightning, Timm, SMP, Albumentations, Audiomentations, Transformers, and more.
    - 🗄️ Others skills: Docker, Git & Github, Office, Linux.
        """
    )


    # --- WORK HISTORY ---
    st.write('\n')
    st.header("Recent Work History")
    st.write("---")

    # --- JOB 1
    st.write("👷", "**Self employed - Freelancer** | From 02/2018 to Present")
    st.write(
        """
    - ► Frelancing data analysis and machine learning jobs.
    - ► Accounting administrative tasks.
    - ► Business plans, Economic analysis, Feasibility studies, etc.
        """
    )

    # --- JOB 2
    st.write('\n')
    st.write("👷", "**Banking and Accounting manager - Ferretería Zárate (sME)** | From 02/2016 to 06/2017")
    st.write(
        """
    - ► Various banking operations (sale of securities, deposits, loans, leases, banking agreements, etc.).
    - ► Accounting.
    - ► Treasury.
    - ► Suppliers payment.
    - ► In charge of a work team of 5 people.
        """
    )

    # --- JOB 3
    st.write('\n')
    st.write("👷", "**Accounting assistant - Ferretería Zárate (sME)** | From 02/2014 to 06/2016")
    st.write(
        """
    - ► Bank reconciliations.
    - ► Bank debt statements.
    - ► Accounting.
    - ► Bank checks and payments.
        """
    )


if selected == 'Proyects':

    # --- Projects ---
    st.write('\n')
    st.header("Projects")
    st.write("---")
    
    st.write('\n')
    st.subheader("Exploratory data analysis")
    st.write("---")
    st.write(
        """
        Exploratory Data Analysis (EDA) is an approach to analyzing datasets that summarizes their main characteristics using statistical graphics and other data visualization methods. 
        While various statistical models can be used, EDA is primarily used to see what the data can tell us beyond the formal modeling or hypothesis testing task. 
        EDA is one of the crucial steps in Data Science that allows us to gain insights and statistical measures of the data we are dealing with. For this task, I utilized several Python libraries such as Pandas, Numpy, Plotly, and more.
        """
    )

    EDA =   {
    "📊 Kaggle survey EDA | Extracting insights about Kagglers users": "https://www.kaggle.com/code/maxdiazbattan/kaggle-survey-2021-eda-initial-insights",
    "📊 Covid Latin america EDA | Covid pandemic analysis over Latin america": "https://www.kaggle.com/code/maxdiazbattan/covid-eda-on-latin-america-dash-dashboard",
    "📊 Covid impact on learning EDA | Covid pandemic impact on american students": "https://www.kaggle.com/code/maxdiazbattan/covid-impact-digital-learning-data-cleaning-eda",
            }


    for project, link in EDA.items():
        st.write(f"[{project}]({link})")


    st.write('\n')
    st.subheader("Dashboards")
    st.write("---")
    st.write(
    """
    A dashboard is a user interface that organizes and presents information in an easy-to-read format. Through dashboards, stakeholders can quickly identify current and historical performance and can also utilize the data to define metrics and set goals. 
    To create dashboards, I used Dash, a Python library that allows you to create dashboards in pure Python. I also used Pandas for data cleansing. 
    The dashboards are deployed on Render website, a cloud service platform that allows you to deploy web apps among other things. It may take a few seconds to load because the apps are hosted on Render servers.
    """
    )

    DASBOARDS =   {
    "📈 Covid dashboard | Covid pandemic Dashboard": " https://covid-dashboard-colj.onrender.com/",
    "📈 Crypto dashboard | Cryptocurrencies Dashboard": "https://crypto-dashboard-33bn.onrender.com/",
    "📈 House prices Dashboard | New York house prices Dashboard": "https://ny-house-prices-dashboard.onrender.com/",
            }


    for project, link in DASBOARDS.items():
        st.write(f"[{project}]({link})")
    

    st.write('\n')
    st.subheader("Machine learning")
    st.write("---")
    st.write(
    """
    Machine learning (ML) is a process that uses a variety of algorithms that iteratively learn from data to improve, describe data, and predict outcomes. 
    As the algorithms ingest training data, it is then possible to produce more precise models based on that data. A machine learning model is the output generated when you train your machine learning algorithm with data. 
    I have worked on several ML projects and competitions where I have used different libraries such as Pandas, Matplotlib, Seaborn, Plotly, Sklearn, Xgboots, LightGBM, Catboost, Shap, etc. 
    Below are some examples of my work:
    """
    )

    ML =   {
    "💻 Wallmart forecasting | Predict sales of Wallmat stores": " https://www.kaggle.com/code/maxdiazbattan/wallmart-sales-top-3-eda-feature-engineering",
    "💻 House prices | Predict house prices": "https://www.kaggle.com/code/maxdiazbattan/house-prices-top-4",
    "💻 Categorizer app (freelance project) | E-commerce categorizer": "https://github.com/maxidiazbattan/streamlit-categorizador-RepuestosYa",
            }


    for project, link in ML.items():
        st.write(f"[{project}]({link})")


    st.write('\n')
    st.subheader("Deep learning")
    st.write("---")
    st.write(
    """
    Deep learning (DL) is a computer technique that uses multiple layers of neural networks to extract and transform data. Each of these layers takes its inputs from previous layers and progressively refines them. 
    The layers are trained by algorithms that minimize their errors and improve their accuracy. In this way, the network learns to perform a specified task, like human speech recognition to animal image classification. 
    Below are some examples of my DL projects from two different Kaggle competitions:    
    """
    )

    DL =   {
    "💻 Cassava competition | Identify the type of disease present on a cassava leaf image": " https://www.kaggle.com/code/maxdiazbattan/cassava-pipeline-top-5-pytorch-lightning-w-b",
    "💻 Tabular Playground | Predict the forest cover type (the predominant kind of tree cover) ": "https://www.kaggle.com/code/maxdiazbattan/tps-2021-pytorch-lightning",
            }


    for project, link in DL.items():
        st.write(f"[{project}]({link})")


if selected == 'Contact':
    
    st.write('\n')
    st.subheader("Contact information")
    st.write("---")
    st.write("Maximiliano Diaz Battan")
    st.write("📫", EMAIL)

    # --- Download CV ---
    st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
    
    SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/maxidiazbattan/?locale=en_US",
    "Kaggle": "https://www.kaggle.com/maxdiazbattan",
    "GitHub": "https://github.com/maxidiazbattan",
                    }

    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA), gap="large")
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
