#Importações das Biblioteca
import streamlit as st
from firebase_admin import firestore
import firebase_admin
import time
import datetime
from streamlit_autorefresh import st_autorefresh
#Importações das Biblioteca
import firebase_admin._auth_client
import firebase_admin.auth
import streamlit as st
import firebase_admin
from firebase_admin import credentials
import requests
import jwt  
from jwt import DecodeError

# Configuração do Firebase 
firebaseConfig = {
    "apiKey": "AIzaSyBFIMnD7uOvASP08_a9Zp6px_ub4DWl2aI",
    "authDomain": "anotherproject-5e811.firebaseapp.com",
    "projectId": "anotherproject-5e811",
    "storageBucket":"anotherproject-5e811.firebasestorage.app",
    "messagingSenderId": "1069155836636",
    "appId": "1:1069155836636:web:8aa2ce0c80a4320d584a19",
    "databaseURL": ""
}


# Criação do Firebase Com as Credencias
if not firebase_admin._apps:
    cred = credentials.Certificate("another/anotherproject-5e811-firebase-adminsdk-fbsvc-407565d917.json")
    default_app=firebase_admin.initialize_app(cred)


#Configurações da Pagina
st.set_page_config(
    page_title="Projecto",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



#------------------ Funções ---------------------

#Função Para Criar um Div
def criar_div(titulo, texto,tempo):
        st.markdown(
            f"""
            <div style="
                background-color: #262730;
                padding: 10px 10px 4px;
                border-radius: 10px;
                margin: 10px 0;
            ">
                <h2 style="color: white;">{titulo}</h2>
                <p style="color: white;">{texto}</p>
                <p style="color: #717275;text-align:right">{tempo}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


#Verificação se existe um user ou não

def inicio():

        tab1 = st.tabs(["Enviar"])
        db = firestore.client()

        with tab1:
            with st.form("formulario"):
                st.header("Compartilhar")
                option = st.selectbox("",("Ideia", "Reclamação"),label_visibility="hidden",key="Reclamação")
                txt = st.text_area("Digite algo :")
                enviar = st.form_submit_button("Enviar")
                if enviar:
                    status = st.empty()
                    if txt:
                        dados = {
                            "tipo": option,
                            "texto":txt ,
                            "tempo":f"{datetime.date.today()} {datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}:{datetime.datetime.now().time().second}:{datetime.datetime.now().time().microsecond}"
                            
                        }
                        db.collection("arquivos").add(dados)
                        
                        status.success("Enviado com sucesso!")
                        time.sleep(2)
                        st.rerun()
                    else:
                        status.error("Escreve alguma coisa")
                        time.sleep(1)
                        status.empty()
       
                
        
  
  
inicio()
