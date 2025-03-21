import streamlit as st
import os
import json

# Configuração da página
st.set_page_config(
    page_title="40 Orações do Arcanjo Miguel com FREI GILSON",  # Título atualizado
    page_icon="✨",
    layout="wide",
)

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f4f4;
        color: #333;
    }
    h1 {
        color: #4A90E2;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.5rem; /* Título maior para mobile */
    }
    h2 {
        color: #4A90E2;
        font-family: 'Georgia', serif;
        font-size: 1.8rem; /* Subtítulo maior para mobile */
    }
    .stButton button {
        background-color: #4A90E2;
        color: white;
        border-radius: 5px;
        padding: 15px 30px; /* Botões maiores para mobile */
        font-size: 18px; /* Texto maior para mobile */
        font-family: 'Georgia', serif;
        width: 100%; /* Botão ocupa toda a largura */
    }
    .stVideo {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 100%; /* Vídeo ocupa toda a largura */
        max-width: 600px; /* Largura máxima para o player de vídeo */
        margin: 0 auto; /* Centraliza o player */
    }
    .stSidebar {
        background-color: #4A90E2;
        color: white;
        padding: 20px;
    }
    .stSidebar .stMarkdown {
        color: white;
    }
    /* Estilo personalizado para o botão de download */
    .stDownloadButton button {
        background-color: #FF0000; /* Vermelho */
        color: white;
        border-radius: 5px;
        padding: 15px 30px; /* Botão maior para mobile */
        font-size: 18px; /* Texto maior para mobile */
        font-family: 'Georgia', serif;
        width: 100%; /* Botão ocupa toda a largura */
    }
    /* Centralizar a imagem */
    .center-image {
        display: flex;
        justify-content: center;
        margin-bottom: 20px; /* Espaçamento abaixo da imagem */
    }
    /* Ajustes para telas pequenas */
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem; /* Título menor em telas pequenas */
        }
        h2 {
            font-size: 1.5rem; /* Subtítulo menor em telas pequenas */
        }
        .stButton button, .stDownloadButton button {
            padding: 12px 24px; /* Botões um pouco menores em telas pequenas */
            font-size: 16px; /* Texto um pouco menor em telas pequenas */
        }
        .stVideo {
            max-width: 100%; /* Player ocupa toda a largura em mobile */
        }
    }
    /* Estilo para a mensagem de carregamento */
    .loading-message {
        font-size: 0.9rem;
        color: #666;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Adicionar a imagem de São Miguel no topo (centralizada)
st.markdown('<div class="center-image">', unsafe_allow_html=True)
st.image("sao_miguel.jpg", width=100)  # Certifique-se de que o arquivo está na mesma pasta que app.py
st.markdown('</div>', unsafe_allow_html=True)

# Título do app
st.title("40 Orações do Arcanjo Miguel com FREI GILSON")  # Título atualizado
st.markdown("---")

# Menu lateral
with st.sidebar:
    st.title("Menu")
    st.write("Bem-vindos ao app das 40 Orações do Arcanjo Miguel com Frei Gilson!")
    if st.button("Sobre"):
        st.write("Este app foi criado para ajudar você a se conectar com as poderosas orações do Arcanjo Miguel.")
    if st.button("Contato"):
        st.write("Para mais informações, entre em contato: contato@arcanjo.com")

# Função para extrair o número do nome do arquivo
def extrair_numero(nome_arquivo):
    try:
        # Extrai o número no início do nome do arquivo
        return int(nome_arquivo.split(".")[0].split(" ")[0])
    except ValueError:
        # Se não houver número, retorna um valor alto para colocar no final da lista
        return float('inf')

# Função para carregar vídeos com cache
@st.cache_data
def load_video(video_path):
    with open(video_path, "rb") as file:
        return file.read()

# Listar os vídeos na pasta atual (mesma pasta do app.py) e ordenar pelo número
videos = sorted(
    [f for f in os.listdir() if f.endswith(".mp4")],
    key=extrair_numero
)

# Carregar descrições das orações (se existir)
descricoes = {}
if os.path.exists("descricoes.json"):
    with open("descricoes.json", "r", encoding="utf-8") as f:
        descricoes = json.load(f)

# Verificar se há vídeos
if not videos:
    st.error("Nenhum vídeo encontrado na pasta atual.")
else:
    # Exibir a lista de vídeos
    st.write("### Escolha uma oração para assistir:")

    # Mensagem de carregamento
    st.markdown('<div class="loading-message">Aguarde alguns segundos para carregar os vídeos...</div>', unsafe_allow_html=True)

    # Exibir vídeos em uma única coluna
    for video in videos:
        st.write(f"**{video}**")
        if video in descricoes:
            st.write(descricoes[video])
        
        # Carregar vídeo com cache
        video_data = load_video(video)
        st.video(video_data, format="video/mp4", start_time=0)

        # Botão de download
        with open(video, "rb") as file:
            btn = st.download_button(
                label=f"Baixar {video}",
                data=file,
                file_name=video,
                mime="video/mp4",
                key=f"download_{video}",
            )
        st.markdown("---")