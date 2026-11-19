import streamlit as st
from agente import responder_cidadao, ATALHOS_MENU

st.set_page_config(
    page_title="Citizen Assist AI — Central do Cidadão de Aurora",
    page_icon="🏛️",
    layout="centered",
)

# CSS de Acessibilidade: alto contraste, tipografia legível e indicador de foco para teclado
st.markdown(
    """
    <style>
        .stApp {
            background-color: #0B0F19;
            color: #FFFFFF;
        }
        html, body, [class*="css"], p, li, label, input, button {
            font-size: 18px !important;
            line-height: 1.6 !important;
            color: #FFFFFF !important;
        }
        h1 {
            font-size: 28px !important;
            color: #FFFFFF !important;
            border-bottom: 2px solid #3B82F6;
            padding-bottom: 8px;
        }
        h2, h3 {
            font-size: 22px !important;
            color: #93C5FD !important;
        }
        /* Destaque nítido de foco para navegação via teclado (Tab) */
        button:focus-visible, input:focus-visible, [tabindex]:focus-visible {
            outline: 3px solid #FFD700 !important;
            outline-offset: 2px !important;
        }
        .stButton > button {
            width: 100%;
            text-align: left;
            background-color: #1E293B;
            color: #FFFFFF !important;
            border: 2px solid #60A5FA;
            border-radius: 8px;
            padding: 10px 14px;
            font-weight: 600;
        }
        .stButton > button:hover {
            background-color: #2563EB;
            border-color: #FFFFFF;
        }
        .stTextInput input {
            background-color: #1E293B !important;
            color: #FFFFFF !important;
            border: 2px solid #93C5FD !important;
            border-radius: 8px;
            padding: 12px !important;
        }
        .caixa-resposta {
            background-color: #111827;
            border-left: 5px solid #3B82F6;
            border: 1px solid #374151;
            border-radius: 8px;
            padding: 20px;
            margin-top: 16px;
        }
        .alerta-privacidade {
            background-color: #1E1B4B;
            border: 2px solid #818CF8;
            border-radius: 8px;
            padding: 12px 16px;
            margin-bottom: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if "ultima_resposta" not in st.session_state:
    st.session_state.ultima_resposta = ""
if "ultima_consulta_rotulo" not in st.session_state:
    st.session_state.ultima_consulta_rotulo = ""


def executar_consulta(pergunta: str, rotulo: str):
    with st.spinner("Consultando as fichas da Central do Cidadão de Aurora..."):
        resposta = responder_cidadao(pergunta)
    st.session_state.ultima_consulta_rotulo = rotulo
    st.session_state.ultima_resposta = resposta


# Cabeçalho
st.title("🏛️ Citizen Assist AI — Central do Cidadão de Aurora")
st.write("Assistente digital de orientação sobre documentos pessoais. Navegue usando **Tab** e **Enter**.")

# Aviso fixo de privacidade
st.markdown(
    """
    <div class="alerta-privacidade" role="region" aria-label="Aviso de Privacidade">
        🔒 <strong>Privacidade:</strong> Não informe dados pessoais (CPF, RG, endereço, telefone ou nome completo). 
        Nenhuma conversa é salva neste sistema.
    </div>
    """,
    unsafe_allow_html=True,
)

# 1. Navegação por Categorias (Menu acessível por teclado)
st.subheader("1. Escolha uma categoria")

categorias = [
    ("1", "1. Carteira de Identidade (RG)"),
    ("2", "2. CPF"),
    ("3", "3. Título de Eleitor"),
    ("4", "4. Carteira de Trabalho"),
    ("5", "5. Certidões (Nascimento, Casamento, Óbito)"),
    ("6", "6. Renovação de CNH"),
    ("7", "7. Regras Gerais, Horários e Acessibilidade"),
]

col1, col2 = st.columns(2)
for idx, (chave, titulo) in enumerate(categorias):
    coluna_atual = col1 if idx % 2 == 0 else col2
    with coluna_atual:
        if st.button(titulo, key=f"cat_{chave}"):
            executar_consulta(ATALHOS_MENU[chave], titulo)

# 2. Entrada Livre (Pressionar Enter envia e limpa o campo automaticamente)
st.subheader("2. Ou digite sua pergunta")
with st.form(key="form_pergunta", clear_on_submit=True):
    pergunta_usuario = st.text_input(
        label="Sua dúvida sobre documentos (pressione Enter para enviar):",
        placeholder="Ex: Quanto custa a segunda via do RG?",
        max_chars=500,
    )
    enviar = st.form_submit_button("Enviar pergunta")

if enviar:
    executar_consulta(pergunta_usuario, "Pergunta digitada")

# 3. Exibição da Resposta Atual (sem manter histórico de usuários anteriores)
if st.session_state.ultima_resposta:
    st.subheader(f"Orientação ({st.session_state.ultima_consulta_rotulo})")
    st.markdown('<div class="caixa-resposta">', unsafe_allow_html=True)
    st.markdown(st.session_state.ultima_resposta)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    if st.button("Limpar tela para próxima consulta", key="btn_limpar"):
        st.session_state.ultima_resposta = ""
        st.session_state.ultima_consulta_rotulo = ""
        st.rerun()
