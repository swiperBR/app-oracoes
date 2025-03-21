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
        font-size: 2.5rem;
    }
    h2 {
        color: #4A90E2;
        font-family: 'Georgia', serif;
        font-size: 1.8rem;
    }
    .stButton button {
        background-color: #4A90E2;
        color: white;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 18px;
        font-family: 'Georgia', serif;
        width: 100%;
    }
    .stVideo {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
    }
    .stSidebar {
        background-color: #4A90E2;
        color: white;
        padding: 20px;
    }
    .stSidebar .stMarkdown {
        color: white;
    }
    .stDownloadButton button {
        background-color: #FF0000;
        color: white;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 18px;
        font-family: 'Georgia', serif;
        width: 100%;
    }
    .center-image {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem;
        }
        h2 {
            font-size: 1.5rem;
        }
        .stButton button, .stDownloadButton button {
            padding: 12px 24px;
            font-size: 16px;
        }
        .stVideo {
            max-width: 100%;
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

# Lista de vídeos com códigos de embed da Vturb
videos = {
    "1 - Oração de Proteção": """
    <div id="vid_67dd99d49f4fcc238c477086" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd99d49f4fcc238c477086" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd99d49f4fcc238c477086/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd99d49f4fcc238c477086" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd99d49f4fcc238c477086">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd99d49f4fcc238c477086/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "2 - Oração da Espada de São Miguel": """
    <div id="vid_67dd99e56a136f4cd86847ed" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd99e56a136f4cd86847ed" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd99e56a136f4cd86847ed/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd99e56a136f4cd86847ed" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd99e56a136f4cd86847ed">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd99e56a136f4cd86847ed/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "3 - Oração para Força e Coragem": """
    <div id="vid_67dd99f39f4fcc238c4770bd" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd99f39f4fcc238c4770bd" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd99f39f4fcc238c4770bd/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd99f39f4fcc238c4770bd" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd99f39f4fcc238c4770bd">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd99f39f4fcc238c4770bd/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "4 - Oração Contra Inimigos Espirituais": """
    <div id="vid_67dd9a020eb49eca9740090c" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd9a020eb49eca9740090c" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a020eb49eca9740090c/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd9a020eb49eca9740090c" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd9a020eb49eca9740090c">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a020eb49eca9740090c/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "5 - Oração para Abrir Caminhos": """
    <div id="vid_67dd9a2422fea58712cd1b23" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd9a2422fea58712cd1b23" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a2422fea58712cd1b23/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd9a2422fea58712cd1b23" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd9a2422fea58712cd1b23">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a2422fea58712cd1b23/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "6 - Oração de Libertação": """
    <div id="vid_67dd9a416a136f4cd8684845" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd9a416a136f4cd8684845" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a416a136f4cd8684845/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd9a416a136f4cd8684845" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd9a416a136f4cd8684845">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a416a136f4cd8684845/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "7 - Oração para Paz e Harmonia": """
    <div id="vid_67dd9a5a645071bc70b83f9d" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd9a5a645071bc70b83f9d" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a5a645071bc70b83f9d/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd9a5a645071bc70b83f9d" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd9a5a645071bc70b83f9d">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a5a645071bc70b83f9d/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "8 - Oração para a Noite": """
    <div id="vid_67dd9a749f4fcc238c477128" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd9a749f4fcc238c477128" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a749f4fcc238c477128/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd9a749f4fcc238c477128" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd9a749f4fcc238c477128">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a749f4fcc238c477128/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "9 - Oração para Tomada de Decisões": """
    <div id="vid_67dd9a7c2a9e96efc2787324" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd9a7c2a9e96efc2787324" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a7c2a9e96efc2787324/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd9a7c2a9e96efc2787324" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd9a7c2a9e96efc2787324">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a7c2a9e96efc2787324/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    "10 - Oração de Agradecimento": """
    <div id="vid_67dd9a6c9f4fcc238c47711a" style="position: relative; width: 100%; padding: 177.77777777777777% 0 0;">
      <img id="thumb_67dd9a6c9f4fcc238c47711a" src="https://images.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a6c9f4fcc238c47711a/thumbnail.jpg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; display: block;" alt="thumbnail">
      <div id="backdrop_67dd9a6c9f4fcc238c47711a" style="-webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); position: absolute; top: 0; height: 100%; width: 100%;"></div>
    </div>
    <script type="text/javascript" id="scr_67dd9a6c9f4fcc238c47711a">
      var s=document.createElement("script");
      s.src="https://scripts.converteai.net/5c08f4fa-db53-4297-ace5-9c47f4306a40/players/67dd9a6c9f4fcc238c47711a/player.js";
      s.async=!0,document.head.appendChild(s);
    </script>
    """,
    # Adicione os outros 30 vídeos aqui...
}

# Exibir a lista de vídeos
st.write("### Escolha uma oração para assistir:")
for nome, embed_code in videos.items():
    st.write(f"**{nome}**")
    st.markdown(embed_code, unsafe_allow_html=True)
    st.markdown("---")