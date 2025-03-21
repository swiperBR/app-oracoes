import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="40 Orações do Arcanjo Miguel",
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
    </style>
    """,
    unsafe_allow_html=True,
)

# Adicionar a imagem de São Miguel no topo (centralizada)
st.markdown('<div class="center-image">', unsafe_allow_html=True)
st.image("sao_miguel.jpg", width=100)  # Certifique-se de que o arquivo está na mesma pasta que app.py
st.markdown('</div>', unsafe_allow_html=True)

# Título do app
st.title("40 Orações do Arcanjo Miguel")
st.markdown("---")

# Menu lateral
with st.sidebar:
    st.title("Menu")
    st.write("Bem-vinda ao app das 40 Orações do Arcanjo Miguel!")
    if st.button("Sobre"):
        st.write("Este app foi criado para ajudar você a se conectar com as poderosas orações do Arcanjo Miguel.")
    if st.button("Contato"):
        st.write("Para mais informações, entre em contato: contato@arcanjo.com")

# Lista de links dos vídeos no Google Drive
videos = {
    "1 - Oração de Proteção": "https://drive.google.com/uc?export=download&id=1Py7KnZ3E9pl0sa453OOt7845-0ms3qdf",
    "2 - Oração da Espada de São Miguel": "https://drive.google.com/uc?export=download&id=1NF--AuZ4MSSbDV79fF2Iv_U4DE7__8gV",
    "3 - Oração para Força e Coragem": "https://drive.google.com/uc?export=download&id=1624DlHlUZnm_QI03dBxSzH_sKQtCfagm",
    "4 - Oração Contra Inimigos Espirituais": "https://drive.google.com/uc?export=download&id=1FyRHLrbH5OpemXQg8dzHbIQ5LFUQPwOq",
    "5 - Oração para Abrir Caminhos": "https://drive.google.com/uc?export=download&id=1V0ULg2lEptJIp1BTLDWb_S9C4mpxWBmv",
    "6 - Oração de Libertação": "https://drive.google.com/uc?export=download&id=1hxpTPW1aRay_SmbfUPDJ4Wm75nnsMcdw",
    "7 - Oração para Paz e Harmonia": "https://drive.google.com/uc?export=download&id=1G-eJuFb47SFrz6gua60TVqdq_sK4F9gp",
    "8 - Oração para a Noite": "https://drive.google.com/uc?export=download&id=1-3TEomJMFClm_9-Bt7QpBFItO0i1olSF",
    "9 - Oração para Tomada de Decisões": "https://drive.google.com/uc?export=download&id=11jeaAK4IEjXu_GJ9HgZALQa5Snt8bBfI",
    "10 - Oração de Agradecimento": "https://drive.google.com/uc?export=download&id=1a94T3GmsCfKLC5QFivMfR_-5RIwwuoBv",
    "11 - Oração para Cura Física": "https://drive.google.com/uc?export=download&id=1heNyrxjQa0uRaZxIEQ66LdHKfUkJ7pM-",
    "12 - Oração para Cura Emocional": "https://drive.google.com/uc?export=download&id=1r5Wjb30yS94RKB-QxK2j3UKD81PcdJ7A",
    "13 - Oração para Cura Espiritual": "https://drive.google.com/uc?export=download&id=1-H1HfTb4iRnaCnIqfbn0Y2hmcw7NNSHM",
    "14 - Oração para Cura de Traumas e Feridas do passado": "https://drive.google.com/uc?export=download&id=1GOW73loaEilsaBi1JEUTJAPxgDLKFz7S",
    "15 - Oração para Cura da Ansiedade e do Medo": "https://drive.google.com/uc?export=download&id=1h3WCjK-amPbOZSfmJVx61uSvYV7BXV3v",
    "16 - Oração para Cura de Vícios": "https://drive.google.com/uc?export=download&id=1KOMzlfnRp5BzzT_EvHbOYV3zZOlVZylq",
    "17 - Oração para Cura de Doenças Graves": "https://drive.google.com/uc?export=download&id=1pUHxUJs01W3BypFycFq4Qr2CLag8s-h_",
    "18 - Oração para Cura de Energias Negativas": "https://drive.google.com/uc?export=download&id=1JhX0bE2EAqUifOqMgt8vQeBM9Vu4FhPC",
    "19 - Oração para Cura de Relacionamentos": "https://drive.google.com/uc?export=download&id=1MoyPwJJvK0RSaPz6yztg8iuKFuQesHlA",
    "20 - Oração para Cura e Renovação da Fé": "https://drive.google.com/uc?export=download&id=1TvzCk1qkpGcfZEIAjE94AeDixgrSjybA",
    "21 - Oração para Libertação das Dívidas": "https://drive.google.com/uc?export=download&id=1t0znsiNvy01LOYQiPX5g_oI00iiQaRzu",
    "22 - Oração para Abertura de Caminhos Financeiros": "https://drive.google.com/uc?export=download&id=1WqQcBqpA5GBv89OyveaCX8NBaVLKoACT",
    "23 - Oração para Atrair Riqueza e Sucesso": "https://drive.google.com/uc?export=download&id=1y47YcJt155DbCocpZg60Ak2ImIVWhm2d",
    "24 - Oração para Remover Bloqueios Financeiros": "https://drive.google.com/uc?export=download&id=1hSR3wvymny3Hk1n7wnTHAV-KMnRjCJ9-",
    "25 - Oração para Atração de Oportunidades": "https://drive.google.com/uc?export=download&id=1APoeVUlc2Q3h1NvT1MltCRY-ugzLcDgg",
    "26 - Oração para Transformar Dívidas em Riqueza": "https://drive.google.com/uc?export=download&id=1V2G4nDoo2nSMlEbVH-OMcMFIUstEsS3n",
    "27 - Oração para Empreendedores e Trabalhadores": "https://drive.google.com/uc?export=download&id=1JjKoZh5OqjurwNc7Di9IFgbCF8tEOUn_",
    "28 - Oração para Proteção Financeira": "https://drive.google.com/uc?export=download&id=13pqvxOQd48oui1DOars3NtSuqBhdv7ia",
    "29 - Oração para Tomar Decisões Financeiras Sábias": "https://drive.google.com/uc?export=download&id=15s1wcpdCmMJ1pCJNGYRpO_VddcLYlmve",
    "30 - Oração para Gratidão e Multiplicação": "https://drive.google.com/uc?export=download&id=1TRhF7perEqrSa2hJSzugjtrSQkkSA4rM",
    "31 - Oração para Fortalecer a Fé": "https://drive.google.com/uc?export=download&id=1lCGHulejdw_HfLic6-g3UFXvjlcGFQ89",
    "32 - Oração para Renovação do Espírito": "https://drive.google.com/uc?export=download&id=1hnwHi-FjM-s0Fp8iJ8twjohwIBajAjpn",
    "33 - Oração para Paz e União na Família": "https://drive.google.com/uc?export=download&id=1bB5Cn1bkPbG1m9oBLVPgMV-m9pTeiisS",
    "34 - Oração para Proteção da Família": "https://drive.google.com/uc?export=download&id=1tF5hggsKEN8LKxNlHFz5-PTEllmQXUSG",
    "35 - Oração para Superação de Dificuldades": "https://drive.google.com/uc?export=download&id=1tpFa7Z1Pozg22QyY5xIvRvXHA6u-m1vD",
    "36 - Oração para Iluminar o Caminho Espiritual": "https://drive.google.com/uc?export=download&id=1ViVJm4pTQERHFjM4JxXgooHYvB-VRxx_",
    "37 - Oração para Proteção": "https://drive.google.com/uc?export=download&id=1GuwAImNnE3Ivx4uBHP_MbkD2oRN5snIK",
    "38 - Oração para Abençoar o Lar": "https://drive.google.com/uc?export=download&id=1QKw9o74ZK3VNw7wwF16QRPFBc6WdmaAE",
    "39 - Oração para Alívio das Dores do Coração": "https://drive.google.com/uc?export=download&id=1nPRvPHWq1XCy4oIgTMtdoMKjHSsPhvGZ",
    "40 - Oração de Gratidão e Entrega": "https://drive.google.com/uc?export=download&id=1lEeTv3jT2xu2848z5vI3rFAB5pKVyHy5",
}

# Exibir a lista de vídeos
st.write("### Escolha uma oração para assistir:")
for nome, link in videos.items():
    st.write(f"**{nome}**")
    st.video(link)
    st.markdown("---")