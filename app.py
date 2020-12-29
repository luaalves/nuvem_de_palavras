import streamlit as st
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

def gerar_nuvem(texto):
    # Ajustando os Stopwords
    stop = set(stopwords.words('portuguese'))
    stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '@', '#', '|', '/', '://', '_'])
    stop.update([
        'neste', 'nesta', 'nisto'
    ])

    # Definindo a nuvem
    nuvem = WordCloud(
        mode='RGBA',
        background_color=None,
        stopwords=stop,
        max_words=100,
        scale=3
        ).generate(texto)

    st.image(nuvem.to_image(), use_column_width=True)

if __name__ == '__main__':

    # Baixar Stopwords
    nltk.download('stopwords')

    # Configurações da página
    st.set_page_config(
        page_title="Nuvem de Palavras",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    # Título da Página
    st.markdown("<h1 style='text-align: center; color: dark;'>Nuvem de Palavras</h1>", unsafe_allow_html=True)

    # Definir modo de importação
    modo_importacao = st.selectbox("Selecionar modo de inserção de dados", options=["Carregar arquivo de texto", "Colar texto"])

    if modo_importacao == "Colar texto":
        texto = st.text_area("", height=210)
        if len(texto) > 0:
            gerar_nuvem(texto)
    else:
        arq = st.file_uploader("Carregar arquivo", type="txt")
        if arq is not None:
            texto = str(arq.read(), "latin-1")
            gerar_nuvem(texto)
