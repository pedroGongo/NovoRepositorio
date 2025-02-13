#Importações das Biblioteca
import streamlit as st
from firebase_admin import firestore
import time
import datetime
from streamlit_autorefresh import st_autorefresh


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
       
