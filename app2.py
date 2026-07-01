"""
app.py - Portfólio Raphael Pires - Streamlit Premium
Versão com Estilos Inline para Garantir Funcionamento 100%
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import base64

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires · Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# INICIALIZAÇÃO DE ESTADO
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
if "page" not in st.session_state:
    st.session_state.page = "home"

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================
def get_foto_path():
    candidatos = [
        "assets/rapha.jpeg", "assets/rapha.jpg",
        "rapha.jpeg", "rapha.jpg",
        "foto.jpeg", "foto.jpg",
        "perfil.jpeg", "perfil.jpg"
    ]
    for caminho in candidatos:
        if os.path.exists(caminho):
            return caminho
    return None

def get_foto_base64(foto_path):
    if foto_path and os.path.exists(foto_path):
        try:
            with open(foto_path, "rb") as f:
                data = f.read()
                encoded = base64.b64encode(data).decode()
                ext = foto_path.split('.')[-1].lower()
                mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
                return f"data:{mime};base64,{encoded}"
        except:
            pass
    return None

def get_pdf_path():
    candidatos = [
        "Curriculo_Raphael_v2.pdf",
        "Curriculo_Raphael.pdf",
        "cv.pdf",
        "assets/Curriculo_Raphael_v2.pdf",
    ]
    for caminho in candidatos:
        if os.path.exists(caminho):
            return caminho
    return None

def ler_pdf_base64(caminho):
    if caminho and os.path.exists(caminho):
        with open(caminho, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def get_theme_colors():
    if st.session_state.theme == "dark":
        return {
            "bg": "#0B0F1A",
            "text": "#F1F5F9",
            "text_muted": "#94A3B8",
            "text_subtle": "#64748B",
            "card_bg": "rgba(255,255,255,0.04)",
            "border": "rgba(255,255,255,0.08)",
            "hover_bg": "rgba(255,255,255,0.06)",
            "primary": "#3B82F6",
            "secondary": "#0EA5E9",
            "success": "#22C55E",
            "warning": "#F59E0B"
        }
    else:
        return {
            "bg": "#F8FAFC",
            "text": "#0F172A",
            "text_muted": "#475569",
            "text_subtle": "#64748B",
            "card_bg": "rgba(255,255,255,0.8)",
            "border": "rgba(0,0,0,0.06)",
            "hover_bg": "rgba(0,0,0,0.04)",
            "primary": "#1D4ED8",
            "secondary": "#0EA5E9",
            "success": "#16A34A",
            "warning": "#D97706"
        }

# ============================================================================
# DADOS DO CURRÍCULO
# ============================================================================
DADOS = {
    "nome": "Raphael Fernando S. Pires",
    "titulo": "Analista de Dados & Business Intelligence (BI)",
    "localizacao": "Volta Redonda — RJ",
    "contato": {
        "telefone1": "(24) 3018-1303",
        "telefone2": "(24) 99278-9637",
        "email": "raphael_caxias@hotmail.com",
        "linkedin": "linkedin.com/in/raphael-pires-caxias",
        "github": "github.com/raphaelcaxias"
    },
    "modalidades": ["Remoto", "Disponível para viagens"]
}

PERFIL = """Analista de Dados e Business Intelligence (BI) com formação em Sistemas de Informação e experiência prática na construção de soluções analíticas, modelagem de dados, automação de processos e desenvolvimento de dashboards para apoio à tomada de decisão. Atua com Power BI, SQL, Python e Excel em operações reais de negócio."""

CITACAO = "Não estou entrando em tecnologia. Estou mostrando que, durante anos, já resolvi problemas com dados — mesmo quando meu cargo não tinha 'Analista' no nome."

SOBRE_MIM = {
    "texto": """Sou de Volta Redonda, RJ. Minha trajetória não é linear — e isso é minha maior força. Comecei na operação, passei pelo banco, empreendi, ensinei, e agora reorganizo tudo sob a ótica de Dados e BI.

Não sou quem fez curso e saiu procurando emprego. Sou alguém que viveu o negócio por anos e agora tem as ferramentas para transformar experiência em valor.

Sou curioso por natureza. Quando aprendo algo, quero entender tudo. Gosto de construir, publicar, melhorar. Busco excelência, às vezes até demais.""",
    "valores": [
        {"icone": "🎯", "titulo": "Resolução de Problemas", "desc": "Como isso resolve um problema real?"},
        {"icone": "🔍", "titulo": "Curiosidade", "desc": "Quero entender tudo. Não aceito a primeira versão."},
        {"icone": "🛠️", "titulo": "Construção", "desc": "Construo, publico, melhoro."},
        {"icone": "📊", "titulo": "Decisão por Dados", "desc": "Decido com evidência, não com impulso."}
    ]
}

KPIS = [
    {"valor": "70%", "label": "Redução tempo operacional", "contexto": "Banco do Brasil", "icone": "⚡"},
    {"valor": "2h→15min", "label": "Ciclo de análise", "contexto": "Relatórios comerciais", "icone": "⏱️"},
    {"valor": "213 mil+", "label": "Registros analisados", "contexto": "Projeto CNPq", "icone": "📊"},
    {"valor": "16 anos", "label": "Experiência profissional", "contexto": "Acumulada", "icone": "🏆"}
]

TECH_STACK = {
    "POWER BI": {"itens": ["Dashboards", "KPIs", "DAX", "Power Query"], "icone": "📊", "nivel": "Expert", "score": 95},
    "SQL": {"itens": ["PostgreSQL", "Consultas", "Modelagem"], "icone": "🗄️", "nivel": "Expert", "score": 92},
    "PYTHON": {"itens": ["Pandas", "NumPy", "Scikit-learn", "Statsmodels"], "icone": "🐍", "nivel": "Avançado", "score": 85},
    "VISUALIZAÇÃO": {"itens": ["Plotly", "Streamlit", "Looker Studio"], "icone": "📈", "nivel": "Avançado", "score": 88},
    "ETL": {"itens": ["Coleta", "Limpeza", "Transformação", "Carga"], "icone": "🔄", "nivel": "Expert", "score": 90},
    "CLOUD": {"itens": ["AWS Educate", "Fundamentos Cloud"], "icone": "☁️", "nivel": "Intermediário", "score": 65},
    "FERRAMENTAS": {"itens": ["Excel/VBA", "Git", "IA Generativa"], "icone": "🛠️", "nivel": "Expert", "score": 93}
}

CERTIFICACOES = [
    {
        "instituicao": "Hashtag Treinamentos",
        "cursos": ["SQL Avançado", "Power BI", "Python para Análise de Dados", "Algoritmos e IA Aplicada"],
        "status": "Concluído",
        "icone": "📘",
        "progresso": 100
    },
    {
        "instituicao": "AWS Educate",
        "cursos": ["Cloud Computing", "Cloud 101", "AWS Console", "Storage", "ML Foundations", "Sustainability", "Cloud Support"],
        "status": "Em andamento (40%)",
        "icone": "☁️",
        "progresso": 40
    }
]

FORMACAO = [
    {"curso": "Sistemas de Informação", "instituicao": "UniFOA", "ano": "2010", "icone": "🎓"},
    {"curso": "Técnico em Informática", "instituicao": "CIBA", "ano": "2005", "icone": "💻"}
]

IDIOMAS = [
    {"idioma": "Português", "nivel": "Nativo", "icone": "🇧🇷"},
    {"idioma": "Inglês", "nivel": "Leitura técnica", "icone": "🇺🇸"}
]

EXPERIENCIAS = [
    {
        "cargo": "Fundador & Analista de Dados",
        "empresa": "Jardim do Éden — Varejo de Moda",
        "tipo": "Empresa Própria",
        "periodo": "2009 — Atual",
        "status": "Consultiva",
        "descricao": [
            "Estruturação da base de dados, modelagem, limpeza, integração e desenvolvimento de dashboards gerenciais com SQL, Python, Power BI e Looker Studio — reduzindo ciclo de análise de 2h para 15 min.",
            "Utilização de IA Generativa como apoio na exploração, documentação e automação de processos analíticos."
        ],
        "tags": ["SQL", "Python", "Power BI", "Looker Studio", "IA Generativa"]
    },
    {
        "cargo": "Fundador & Analista de KPIs",
        "empresa": "J Sintonía — Varejo Especializado",
        "tipo": "Empresa Própria",
        "periodo": "2014 — maio 2026",
        "status": "Encerrado",
        "descricao": [
            "Monitoramento de KPIs de vendas, margem e rentabilidade com relatórios automatizados.",
            "Análise de viabilidade econômica que fundamentou encerramento estratégico planejado em maio/2026, evitando prejuízo."
        ],
        "tags": ["KPIs", "Dashboards", "Análise Econômica"]
    },
    {
        "cargo": "Estagiário de Automação e Dados",
        "empresa": "Banco do Brasil S.A.",
        "tipo": "Estágio",
        "periodo": "2008 — 2010",
        "descricao": [
            "Desenvolveu macros VBA em 20 agências, reduzindo 70% do tempo operacional.",
            "Saneou e padronizou bases de dados gerenciais internas."
        ],
        "tags": ["VBA", "Automação", "SQL"]
    },
    {
        "cargo": "Auxiliar de Dados & Operações",
        "empresa": "NSM Comércio",
        "tipo": "CLT",
        "periodo": "2002 — 2009",
        "descricao": ["Centralizou registros de estoque de 7 unidades, eliminando inconsistências de inventário."],
        "tags": ["Operações", "Estoque", "Dados"]
    },
    {
        "cargo": "Instrutor de Informática",
        "empresa": "UniFOA — Projeto de Extensão",
        "tipo": "Projeto",
        "periodo": "Jan 2006 — Dez 2007",
        "descricao": ["Capacitou jovens em Excel avançado (tabelas dinâmicas, PROCV, automações) e lógica de programação."],
        "tags": ["Excel", "Programação", "Ensino"]
    }
]

PROJETOS = [
    {
        "nome": "Desenrola Brasil",
        "subtitulo": "Painel Analítico Executivo",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "url": "https://desenrolabrasil.streamlit.app",
        "descricao": "Processamento de dados oficiais do Banco Central com KPIs, séries temporais e análise de concentração de mercado (HHI).",
        "contexto": "Entender o impacto real do programa no Brasil",
        "icone": "🇧🇷"
    },
    {
        "nome": "CNPq Analytics",
        "subtitulo": "Investimentos em Pesquisa",
        "tech": ["Python", "Pandas", "Plotly", "PostgreSQL"],
        "url": "https://cnpq-analytics.streamlit.app",
        "descricao": "ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos.",
        "contexto": "Mostrar para onde vai o dinheiro da pesquisa",
        "icone": "🔬"
    },
    {
        "nome": "Dashboard ANP",
        "subtitulo": "Preços de Combustíveis",
        "tech": ["Python", "Pandas", "Plotly"],
        "url": None,
        "descricao": "Dashboard interativo com filtros temporais e regionais utilizando dados oficiais da ANP.",
        "contexto": "Transparência em dados públicos",
        "icone": "⛽"
    }
]

LINKS = {
    "linkedin": "https://www.linkedin.com/in/raphael-pires-caxias",
    "github": "https://github.com/raphaelcaxias",
    "email": "mailto:raphael_caxias@hotmail.com",
    "whatsapp": "https://wa.me/5524992789637"
}

# ============================================================================
# CSS MÍNIMO (apenas animações e reset)
# ============================================================================
def get_css():
    colors = get_theme_colors()
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {{
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
    }}
    
    #MainMenu, header, footer, .stDeployButton {{
        display: none !important;
    }}
    
    .stApp {{
        background: {colors['bg']};
    }}
    
    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.2); }}
    }}
    
    @keyframes rotate {{
        to {{ transform: rotate(360deg); }}
    }}
    
    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(-16px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    
    /* Hover effects */
    .hover-card:hover {{
        transform: translateY(-6px) !important;
        box-shadow: 0 12px 40px rgba(59,130,246,0.3) !important;
    }}
    
    .hover-card:hover::before {{
        opacity: 1 !important;
    }}
    </style>
    """

# ============================================================================
# FUNÇÕES DE RENDERIZAÇÃO COM ESTILOS INLINE
# ============================================================================

def render_navbar():
    colors = get_theme_colors()
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    page = st.session_state.page
    
    nav_html = f"""
    <nav style="
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        background: {'rgba(11,15,26,0.92)' if st.session_state.theme == 'dark' else 'rgba(248,250,252,0.92)'};
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid {colors['border']};
        padding: 0.75rem 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.5rem;
    ">
        <a href="#" onclick="window.location.href='?page=home'" style="
            font-weight: 800;
            font-size: 1.2rem;
            color: {colors['text']};
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            cursor: pointer;
        ">
            <span style="
                width: 10px;
                height: 10px;
                border-radius: 50%;
                background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                box-shadow: 0 0 12px {colors['primary']};
                animation: pulse 2s infinite;
                display: inline-block;
            "></span>
            Raphael <span style="
                background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">Pires</span>
        </a>
        <div style="display: flex; gap: 0.25rem; align-items: center; flex-wrap: wrap;">
            <button onclick="window.location.href='?page=home'" style="
                padding: 0.4rem 0.9rem;
                border-radius: 999px;
                font-size: 0.8rem;
                font-weight: 600;
                border: none;
                background: {'linear-gradient(135deg, ' + colors['primary'] + ', ' + colors['secondary'] + ')' if page == 'home' else 'transparent'};
                color: {'white' if page == 'home' else colors['text_muted']};
                cursor: pointer;
                transition: all 0.25s ease;
                font-family: 'Inter', sans-serif;
            ">🏠 Início</button>
            <button onclick="window.location.href='?page=curriculo'" style="
                padding: 0.4rem 0.9rem;
                border-radius: 999px;
                font-size: 0.8rem;
                font-weight: 600;
                border: none;
                background: {'linear-gradient(135deg, ' + colors['primary'] + ', ' + colors['secondary'] + ')' if page == 'curriculo' else 'transparent'};
                color: {'white' if page == 'curriculo' else colors['text_muted']};
                cursor: pointer;
                transition: all 0.25s ease;
                font-family: 'Inter', sans-serif;
            ">📄 Currículo</button>
            <button onclick="window.location.href='?page=projetos'" style="
                padding: 0.4rem 0.9rem;
                border-radius: 999px;
                font-size: 0.8rem;
                font-weight: 600;
                border: none;
                background: {'linear-gradient(135deg, ' + colors['primary'] + ', ' + colors['secondary'] + ')' if page == 'projetos' else 'transparent'};
                color: {'white' if page == 'projetos' else colors['text_muted']};
                cursor: pointer;
                transition: all 0.25s ease;
                font-family: 'Inter', sans-serif;
            ">🚀 Projetos</button>
            <button onclick="window.location.href='?page=analytics'" style="
                padding: 0.4rem 0.9rem;
                border-radius: 999px;
                font-size: 0.8rem;
                font-weight: 600;
                border: none;
                background: {'linear-gradient(135deg, ' + colors['primary'] + ', ' + colors['secondary'] + ')' if page == 'analytics' else 'transparent'};
                color: {'white' if page == 'analytics' else colors['text_muted']};
                cursor: pointer;
                transition: all 0.25s ease;
                font-family: 'Inter', sans-serif;
            ">📊 Analytics</button>
            <button onclick="window.location.href='?theme_toggle=1&page={page}'" style="
                width: 38px;
                height: 38px;
                border-radius: 50%;
                background: {colors['card_bg']};
                border: 1px solid {colors['border']};
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                transition: all 0.3s ease;
                font-size: 1.1rem;
                margin-left: 0.5rem;
                color: {colors['text']};
            ">{theme_icon}</button>
        </div>
    </nav>
    """
    st.markdown(nav_html, unsafe_allow_html=True)
    st.markdown(f'<div style="height: 70px;"></div>', unsafe_allow_html=True)

def render_hero():
    colors = get_theme_colors()
    foto_path = get_foto_path()
    foto_b64 = get_foto_base64(foto_path)
    foto_url = foto_b64 if foto_b64 else "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=3B82F6&color=fff&bold=true"
    
    pdf_path = get_pdf_path()
    cv_button = ""
    if pdf_path:
        pdf_b64 = ler_pdf_base64(pdf_path)
        if pdf_b64:
            cv_button = f'<a href="data:application/pdf;base64,{pdf_b64}" download="Curriculo_Raphael_Pires.pdf" style="background: {colors["card_bg"]}; border: 1px solid {colors["border"]}; padding: 0.65rem 1.5rem; border-radius: 12px; font-weight: 600; font-size: 0.9rem; color: {colors["text"]} !important; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.25s ease;">📄 Baixar CV</a>'
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <div style="position: relative; width: 260px; height: 260px;">
                <div style="
                    position: absolute;
                    inset: -12px;
                    border-radius: 50%;
                    background: conic-gradient({colors['primary']}, {colors['secondary']}, #8B5CF6, {colors['primary']});
                    animation: rotate 8s linear infinite;
                    opacity: 0.5;
                "></div>
                <div style="
                    position: absolute;
                    inset: 4px;
                    border-radius: 50%;
                    background: {colors['bg']};
                "></div>
                <img src="{foto_url}" alt="Raphael Pires" style="
                    position: relative;
                    z-index: 2;
                    width: 100%;
                    height: 100%;
                    border-radius: 50%;
                    object-fit: cover;
                    border: 4px solid {colors['bg']};
                    box-shadow: 0 25px 80px rgba(59,130,246,0.3);
                ">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div>
            <div style="
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: rgba(59,130,246,0.12);
                border: 1px solid rgba(59,130,246,0.2);
                padding: 0.3rem 1rem;
                border-radius: 999px;
                font-size: 0.7rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                color: {colors['primary']};
                margin-bottom: 0.75rem;
            ">📊 {DADOS['titulo']}</div>
            
            <h1 style="
                font-size: 3.5rem;
                font-weight: 900;
                color: {colors['text']};
                margin-bottom: 0.5rem;
                line-height: 1.1;
            ">Raphael <span style="
                background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">Pires</span></h1>
            
            <p style="
                font-size: 1.05rem;
                color: {colors['text_muted']};
                line-height: 1.7;
                margin: 0.5rem 0 1rem;
                max-width: 600px;
            ">{PERFIL}</p>
            
            <div style="
                font-style: italic;
                color: {colors['text_subtle']};
                font-size: 0.95rem;
                margin: 1.2rem 0 1.5rem;
                padding-left: 1.5rem;
                border-left: 3px solid {colors['primary']};
                max-width: 500px;
                line-height: 1.6;
            ">"{CITACAO}"</div>
            
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">
                <span style="
                    background: {colors['card_bg']};
                    border: 1px solid {colors['border']};
                    padding: 0.35rem 0.9rem;
                    border-radius: 10px;
                    font-size: 0.75rem;
                    font-weight: 500;
                    color: {colors['text_muted']};
                    display: inline-block;
                ">📍 {DADOS['localizacao']}</span>
                <span style="
                    background: {colors['card_bg']};
                    border: 1px solid {colors['border']};
                    padding: 0.35rem 0.9rem;
                    border-radius: 10px;
                    font-size: 0.75rem;
                    font-weight: 500;
                    color: {colors['text_muted']};
                    display: inline-block;
                ">🏠 {DADOS['modalidades'][0]}</span>
                <span style="
                    background: {colors['card_bg']};
                    border: 1px solid {colors['border']};
                    padding: 0.35rem 0.9rem;
                    border-radius: 10px;
                    font-size: 0.75rem;
                    font-weight: 500;
                    color: {colors['text_muted']};
                    display: inline-block;
                ">✈️ {DADOS['modalidades'][1]}</span>
            </div>
            
            <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem;">
                <a href="#experiencia" style="
                    background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                    color: white !important;
                    padding: 0.65rem 1.5rem;
                    border-radius: 12px;
                    font-weight: 600;
                    font-size: 0.9rem;
                    text-decoration: none;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    box-shadow: 0 4px 16px rgba(59,130,246,0.3);
                    transition: all 0.25s ease;
                ">💼 Ver Experiência</a>
                {cv_button}
                <a href="{LINKS['linkedin']}" target="_blank" style="
                    background: {colors['card_bg']};
                    border: 1px solid {colors['border']};
                    padding: 0.65rem 1.5rem;
                    border-radius: 12px;
                    font-weight: 600;
                    font-size: 0.9rem;
                    color: {colors['text']} !important;
                    text-decoration: none;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    transition: all 0.25s ease;
                ">💼 LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_sobre():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">👤 Quem sou eu</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Minha História</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background: {colors['card_bg']};
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid {colors['border']};
        border-radius: 24px;
        padding: 2.5rem;
        margin: 1.5rem 0;
    ">
        <p style="
            font-size: 1.05rem;
            line-height: 1.8;
            color: {colors['text_muted']};
            white-space: pre-line;
            margin-bottom: 0;
        ">{SOBRE_MIM['texto']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="margin-top: 2rem; text-align: center;">
        <h3 style="color: {colors['text']}; font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem;">💎 Meus Valores</h3>
        <p style="color: {colors['text_muted']}; font-size: 0.95rem; margin-bottom: 1.5rem;">O que me move e como trabalho</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, valor in enumerate(SOBRE_MIM['valores']):
        with cols[i]:
            st.markdown(f"""
            <div class="hover-card" style="
                background: {colors['card_bg']};
                border: 1px solid {colors['border']};
                border-radius: 16px;
                padding: 1.5rem 1rem;
                text-align: center;
                transition: all 0.3s ease;
                height: 100%;
                min-height: 160px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                cursor: default;
            ">
                <div style="font-size: 2.8rem; margin-bottom: 0.75rem;">{valor['icone']}</div>
                <div style="font-weight: 700; font-size: 1.05rem; color: {colors['text']}; margin-bottom: 0.35rem;">{valor['titulo']}</div>
                <div style="font-size: 0.85rem; color: {colors['text_muted']}; line-height: 1.5; max-width: 200px;">{valor['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_kpis():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">📈 Impacto</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Números que contam histórias</h2>
        <p style="
            color: {colors['text_muted']};
            max-width: 600px;
            margin: 0.75rem auto 0;
            font-size: 1rem;
            line-height: 1.6;
        ">Resultados concretos de mais de uma década</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, kpi in enumerate(KPIS):
        with cols[i]:
            st.markdown(f"""
            <div class="hover-card" style="
                background: {colors['card_bg']};
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid {colors['border']};
                border-radius: 20px;
                padding: 1.5rem;
                text-align: center;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
                height: 100%;
            ">
                <div style="
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 3px;
                    background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                    opacity: 0;
                    transition: opacity 0.3s ease;
                "></div>
                <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">{kpi['icone']}</div>
                <div style="
                    font-size: 2rem;
                    font-weight: 800;
                    background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                    margin-bottom: 0.25rem;
                ">{kpi['valor']}</div>
                <div style="font-size: 0.85rem; color: {colors['text_muted']}; font-weight: 500;">{kpi['label']}</div>
                <div style="font-size: 0.72rem; color: {colors['text_subtle']}; margin-top: 0.15rem; opacity: 0.7;">{kpi['contexto']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_tech():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">⚡ Tech Stack</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Ferramentas que domino</h2>
    </div>
    """, unsafe_allow_html=True)
    
    tech_items = list(TECH_STACK.items())
    cols_per_row = 3
    
    for i in range(0, len(tech_items), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(tech_items):
                tech, dados = tech_items[i + j]
                nivel_cor = "#22C55E" if dados['nivel'] == "Expert" else ("#3B82F6" if dados['nivel'] == "Avançado" else "#F59E0B")
                nivel_bg = "rgba(34,197,94,0.15)" if dados['nivel'] == "Expert" else ("rgba(59,130,246,0.15)" if dados['nivel'] == "Avançado" else "rgba(245,158,11,0.15)")
                
                with cols[j]:
                    itens_html = "".join([f'<span style="font-size: 0.7rem; background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.2); padding: 0.15rem 0.6rem; border-radius: 8px; color: {colors["primary"]}; font-weight: 500; display: inline-block; margin: 0.15rem;">{item}</span>' for item in dados['itens']])
                    
                    st.markdown(f"""
                    <div class="hover-card" style="
                        background: {colors['card_bg']};
                        backdrop-filter: blur(12px);
                        -webkit-backdrop-filter: blur(12px);
                        border: 1px solid {colors['border']};
                        border-radius: 20px;
                        padding: 1.5rem;
                        transition: all 0.3s ease;
                        height: 100%;
                    ">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem;">
                            <span style="font-size: 1.8rem; flex-shrink: 0;">{dados['icone']}</span>
                            <div>
                                <div style="font-size: 1rem; font-weight: 700; color: {colors['text']};">{tech}</div>
                                <span style="
                                    font-size: 0.65rem;
                                    font-weight: 600;
                                    padding: 0.15rem 0.6rem;
                                    border-radius: 999px;
                                    display: inline-block;
                                    background: {nivel_bg};
                                    color: {nivel_cor};
                                ">{dados['nivel']}</span>
                            </div>
                        </div>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">{itens_html}</div>
                    </div>
                    """, unsafe_allow_html=True)

def render_skills_chart():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">📊 Visualização</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Nível de domínio</h2>
    </div>
    """, unsafe_allow_html=True)
    
    df = pd.DataFrame({
        "Tecnologia": list(TECH_STACK.keys()),
        "Proficiência": [d['score'] for d in TECH_STACK.values()],
        "Nível": [d['nivel'] for d in TECH_STACK.values()]
    })
    
    fig = px.bar(
        df, x="Proficiência", y="Tecnologia", color="Nível",
        orientation="h",
        color_discrete_map={"Expert": "#22C55E", "Avançado": "#3B82F6", "Intermediário": "#F59E0B"},
        template="plotly_dark" if st.session_state.theme == "dark" else "plotly_white",
        text="Proficiência"
    )
    
    fig.update_layout(
        height=420,
        margin=dict(l=20, r=60, t=20, b=40),
        xaxis=dict(range=[0, 110], showgrid=True, gridcolor="rgba(148,163,184,0.12)"),
        yaxis=dict(showgrid=False, categoryorder='total ascending'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=colors['text'])
    )
    fig.update_traces(textposition="outside")
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_certificacoes():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">🎓 Certificações</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Formação contínua</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, cert in enumerate(CERTIFICACOES):
        with cols[i]:
            cursos_html = "".join([f'<span style="font-size: 0.7rem; background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.2); padding: 0.15rem 0.6rem; border-radius: 8px; color: {colors["primary"]}; font-weight: 500; display: inline-block; margin: 0.15rem;">{c}</span>' for c in cert['cursos']])
            
            st.markdown(f"""
            <div class="hover-card" style="
                background: {colors['card_bg']};
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid {colors['border']};
                border-radius: 20px;
                padding: 1.5rem;
                transition: all 0.3s ease;
                height: 100%;
            ">
                <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.8rem; flex-shrink: 0;">{cert['icone']}</span>
                    <span style="font-weight: 700; font-size: 1rem; color: {colors['text']};">{cert['instituicao']}</span>
                </div>
                <div style="font-size: 0.75rem; color: {colors['text_muted']}; margin-bottom: 0.5rem;">{cert['status']}</div>
                <div style="display: flex; flex-wrap: wrap; gap: 0.3rem;">{cursos_html}</div>
                <div style="
                    width: 100%;
                    height: 6px;
                    background: {colors['border']};
                    border-radius: 999px;
                    overflow: hidden;
                    margin-top: 0.75rem;
                ">
                    <div style="
                        height: 100%;
                        width: {cert['progresso']}%;
                        background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                        border-radius: 999px;
                        transition: width 0.8s ease;
                        box-shadow: 0 0 12px rgba(59,130,246,0.3);
                    "></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_formacao():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">🎓 Formação</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Formação acadêmica</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, form in enumerate(FORMACAO):
        with cols[i]:
            st.markdown(f"""
            <div class="hover-card" style="
                background: {colors['card_bg']};
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid {colors['border']};
                border-radius: 20px;
                padding: 1.5rem;
                transition: all 0.3s ease;
                height: 100%;
            ">
                <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.8rem; flex-shrink: 0;">{form['icone']}</span>
                    <div>
                        <div style="font-weight: 700; font-size: 1rem; color: {colors['text']};">{form['curso']}</div>
                        <div style="font-size: 0.75rem; color: {colors['text_muted']};">{form['instituicao']} · {form['ano']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_idiomas():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">🌐 Idiomas</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Competências linguísticas</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, idioma in enumerate(IDIOMAS):
        with cols[i]:
            st.markdown(f"""
            <div class="hover-card" style="
                background: {colors['card_bg']};
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid {colors['border']};
                border-radius: 20px;
                padding: 1.5rem;
                transition: all 0.3s ease;
                height: 100%;
                text-align: center;
            ">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">{idioma['icone']}</div>
                <div style="font-weight: 700; font-size: 1rem; color: {colors['text']};">{idioma['idioma']}</div>
                <div style="font-size: 0.75rem; color: {colors['text_muted']};">{idioma['nivel']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_experiencias():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;" id="experiencia">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">💼 Trajetória</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Experiência profissional</h2>
    </div>
    """, unsafe_allow_html=True)
    
    for exp in EXPERIENCIAS:
        badge = f'<span style="background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]}); color: white; font-size: 0.6rem; font-weight: 700; padding: 0.15rem 0.6rem; border-radius: 999px; margin-left: 0.4rem; display: inline-block;">{exp["status"]}</span>' if exp.get("status") else ""
        desc = "<br>".join([f"• {d}" for d in exp["descricao"]])
        tags = "".join([f'<span style="font-size: 0.65rem; background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.2); padding: 0.15rem 0.6rem; border-radius: 8px; display: inline-block; margin: 0.15rem; color: {colors["primary"]}; font-weight: 500;">{t}</span>' for t in exp["tags"]])
        
        st.markdown(f"""
        <div style="
            position: relative;
            padding-left: 2rem;
            margin-bottom: 1.5rem;
            border-left: 2px solid {colors['primary']};
            animation: slideIn 0.5s ease backwards;
        ">
            <div style="
                position: absolute;
                left: -8px;
                top: 4px;
                width: 14px;
                height: 14px;
                border-radius: 50%;
                background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                border: 3px solid {colors['bg']};
                box-shadow: 0 0 0 3px {colors['primary']};
            "></div>
            <div class="hover-card" style="
                background: {colors['card_bg']};
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid {colors['border']};
                border-radius: 16px;
                padding: 1.25rem;
                transition: all 0.3s ease;
            ">
                <div>
                    <span style="
                        display: inline-block;
                        font-size: 0.7rem;
                        font-weight: 700;
                        background: rgba(59,130,246,0.12);
                        color: {colors['primary']};
                        padding: 0.15rem 0.8rem;
                        border-radius: 999px;
                    ">{exp['periodo']}</span> {badge}
                </div>
                <div style="font-size: 1.1rem; font-weight: 700; color: {colors['text']}; margin: 0.4rem 0 0.1rem;">{exp['cargo']}</div>
                <div style="color: {colors['secondary']}; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.5rem;">{exp['empresa']} · {exp['tipo']}</div>
                <div style="color: {colors['text_muted']}; line-height: 1.6; font-size: 0.92rem; margin-bottom: 0.5rem;">{desc}</div>
                <div>{tags}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_projetos():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 3rem;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.2);
            padding: 0.3rem 1rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {colors['primary']};
            margin-bottom: 0.75rem;
        ">🚀 Projetos</div>
        <h2 style="
            font-size: 2.5rem;
            font-weight: 800;
            color: {colors['text']};
            margin-top: 0.25rem;
        ">Analytics na prática</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, p in enumerate(PROJETOS):
        with cols[i]:
            techs = "".join([f'<span style="font-size: 0.65rem; background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.2); padding: 0.15rem 0.5rem; border-radius: 6px; color: {colors["primary"]}; font-weight: 500; display: inline-block; margin: 0.15rem;">{t}</span>' for t in p["tech"]])
            link = f'<a href="{p["url"]}" target="_blank" style="background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]}); color: white !important; padding: 0.5rem 1.2rem; border-radius: 12px; font-weight: 600; font-size: 0.85rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 16px rgba(59,130,246,0.3); transition: all 0.25s ease;">🔗 Ver</a>' if p.get("url") else f'<a href="{LINKS["github"]}" target="_blank" style="background: linear-gradient(135deg, {colors["primary"]}, {colors["secondary"]}); color: white !important; padding: 0.5rem 1.2rem; border-radius: 12px; font-weight: 600; font-size: 0.85rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 16px rgba(59,130,246,0.3); transition: all 0.25s ease;">💻 GitHub</a>'
            
            st.markdown(f"""
            <div class="hover-card" style="
                background: {colors['card_bg']};
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid {colors['border']};
                border-radius: 24px;
                padding: 1.75rem;
                transition: all 0.3s ease;
                height: 100%;
                position: relative;
                overflow: hidden;
            ">
                <div style="
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 3px;
                    background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                    transform: scaleX(0);
                    transform-origin: left;
                    transition: transform 0.4s ease;
                "></div>
                <div style="font-size: 2.2rem; margin-bottom: 0.75rem;">{p['icone']}</div>
                <h3 style="font-size: 1.15rem; font-weight: 700; color: {colors['text']}; margin-bottom: 0.15rem;">{p['nome']}</h3>
                <div style="font-size: 0.85rem; color: {colors['text_muted']}; margin-bottom: 0.5rem; font-style: italic;">{p['subtitulo']}</div>
                <p style="color: {colors['text_muted']}; line-height: 1.6; font-size: 0.88rem; margin-bottom: 0.5rem;">{p['descricao']}</p>
                <div style="
                    font-size: 0.8rem;
                    color: {colors['primary']};
                    font-style: italic;
                    margin-bottom: 0.75rem;
                    padding-left: 0.75rem;
                    border-left: 2px solid {colors['primary']};
                ">💡 {p['contexto']}</div>
                <div>{techs}</div>
                <div style="margin-top: 1rem;">{link}</div>
            </div>
            """, unsafe_allow_html=True)

def render_footer():
    colors = get_theme_colors()
    tel = DADOS['contato']['telefone1'].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    
    st.markdown("---")
    
    st.markdown(f"""
    <div style="text-align: center; padding: 1.5rem 0;">
        <div style="
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            background: rgba(34,197,94,0.1);
            border: 1px solid rgba(34,197,94,0.2);
            padding: 0.35rem 1.2rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            color: {colors['success']};
            margin-bottom: 1.5rem;
        ">
            <span style="
                display: inline-block;
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: {colors['success']};
                animation: pulse 2s infinite;
            "></span>
            Disponível para oportunidades
        </div>
        <h2 style="
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        ">Vamos conversar?</h2>
        <p style="color: {colors['text_muted']}; font-size: 1.05rem; margin-bottom: 1.5rem;">Se busca alguém que entende de negócio E de dados, vamos tomar um café.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f'<a href="{LINKS["linkedin"]}" target="_blank" style="background: {colors["card_bg"]}; border: 1px solid {colors["border"]}; padding: 0.5rem 1.1rem; border-radius: 12px; color: {colors["text"]} !important; text-decoration: none; font-size: 0.82rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.25s ease;">💼 LinkedIn</a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<a href="{LINKS["github"]}" target="_blank" style="background: {colors["card_bg"]}; border: 1px solid {colors["border"]}; padding: 0.5rem 1.1rem; border-radius: 12px; color: {colors["text"]} !important; text-decoration: none; font-size: 0.82rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.25s ease;">💻 GitHub</a>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<a href="{LINKS["email"]}" style="background: {colors["card_bg"]}; border: 1px solid {colors["border"]}; padding: 0.5rem 1.1rem; border-radius: 12px; color: {colors["text"]} !important; text-decoration: none; font-size: 0.82rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.25s ease;">✉️ E-mail</a>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<a href="{LINKS["whatsapp"]}" target="_blank" style="background: {colors["card_bg"]}; border: 1px solid {colors["border"]}; padding: 0.5rem 1.1rem; border-radius: 12px; color: {colors["text"]} !important; text-decoration: none; font-size: 0.82rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.25s ease;">📱 WhatsApp</a>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<a href="tel:{tel}" style="background: {colors["card_bg"]}; border: 1px solid {colors["border"]}; padding: 0.5rem 1.1rem; border-radius: 12px; color: {colors["text"]} !important; text-decoration: none; font-size: 0.82rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.25s ease;">📞 {DADOS["contato"]["telefone1"]}</a>', unsafe_allow_html=True)
    
    pdf_path = get_pdf_path()
    if pdf_path:
        pdf_b64 = ler_pdf_base64(pdf_path)
        if pdf_b64:
            st.markdown(f"""
            <div style="text-align: center; margin: 0.5rem 0 1rem;">
                <a href="data:application/pdf;base64,{pdf_b64}" download="Curriculo_Raphael_Pires.pdf" style="background: {colors["card_bg"]}; border: 1px solid {colors["border"]}; padding: 0.5rem 1.1rem; border-radius: 12px; color: {colors["text"]} !important; text-decoration: none; font-size: 0.82rem; font-weight: 500; display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.25s ease;">📄 Baixar Currículo (PDF)</a>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <p style="color: {colors['text_subtle']}; font-size: 0.75rem; margin-top: 1rem; text-align: center;">© 2026 {DADOS['nome']} · Feito com ❤️ e Streamlit</p>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <a href="#topo" style="
        position: fixed;
        bottom: 1.5rem;
        right: 1.5rem;
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        cursor: pointer;
        box-shadow: 0 8px 24px rgba(59,130,246,0.35);
        transition: all 0.25s ease;
        z-index: 999;
        text-decoration: none;
        border: none;
    ">↑</a>
    """, unsafe_allow_html=True)

def render_analytics():
    colors = get_theme_colors()
    
    st.markdown(f"""
    <div style="padding: 1rem 0 2rem; text-align: center;">
        <h1 style="
            font-size: 2.8rem;
            font-weight: 900;
            color: {colors['text']};
            margin-bottom: 0.5rem;
            line-height: 1.1;
        ">📊 Analytics Interativo</h1>
        <p style="
            font-size: 1.05rem;
            color: {colors['text_muted']};
            line-height: 1.7;
            margin: 0 auto;
            max-width: 500px;
        ">Dashboards em Streamlit + Plotly</p>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ ANP", "📈 Impacto"])
    
    with tabs[0]:
        np.random.seed(42)
        regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
        status = ["Renegociado", "Em Negociação", "Inadimplente"]
        df = pd.DataFrame({
            "Região": np.random.choice(regioes, 400, p=[.45, .28, .15, .07, .05]),
            "Valor": np.random.lognormal(8.5, 1.2, 400),
            "Status": np.random.choice(status, 400, p=[.65, .25, .10])
        })
        
        col1, col2 = st.columns(2)
        with col1:
            reg = st.multiselect("Região", regioes, default=regioes)
        with col2:
            stat = st.multiselect("Status", status, default=status)
        
        filtro = df[df["Região"].isin(reg) & df["Status"].isin(stat)]
        
        if not filtro.empty:
            k1, k2, k3 = st.columns(3)
            with k1:
                st.metric("Contratos", f"{len(filtro):,}")
            with k2:
                st.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f} M")
            with k3:
                st.metric("Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
            
            col_a, col_b = st.columns(2)
            with col_a:
                fig1 = px.pie(filtro, names="Região", values="Valor", hole=.6,
                             template="plotly_dark" if st.session_state.theme == "dark" else "plotly_white")
                fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380)
                st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})
            with col_b:
                fig2 = px.histogram(filtro, x="Status", color="Status",
                                   template="plotly_dark" if st.session_state.theme == "dark" else "plotly_white")
                fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380, showlegend=False)
                st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

# ============================================================================
# MAIN
# ============================================================================
def main():
    st.markdown(get_css(), unsafe_allow_html=True)
    
    if "theme_toggle" in st.query_params:
        toggle_theme()
        page = st.query_params.get("page", "home")
        st.query_params.clear()
        st.query_params["page"] = page
        st.rerun()
    
    if "page" in st.query_params:
        st.session_state.page = st.query_params["page"]
    
    render_navbar()
    st.markdown('<div id="topo"></div>', unsafe_allow_html=True)
    
    page = st.session_state.page
    
    if page == "home":
        render_hero()
        st.markdown("---")
        render_sobre()
        st.markdown("---")
        render_kpis()
        st.markdown("---")
        render_tech()
        st.markdown("---")
        render_skills_chart()
        st.markdown("---")
        render_experiencias()
        st.markdown("---")
        render_projetos()
        st.markdown("---")
        render_certificacoes()
        st.markdown("---")
        render_formacao()
        st.markdown("---")
        render_idiomas()
    
    elif page == "curriculo":
        render_sobre()
        st.markdown("---")
        render_kpis()
        st.markdown("---")
        render_tech()
        st.markdown("---")
        render_skills_chart()
        st.markdown("---")
        render_certificacoes()
        st.markdown("---")
        render_formacao()
        st.markdown("---")
        render_idiomas()
        st.markdown("---")
        render_experiencias()
    
    elif page == "projetos":
        render_projetos()
    
    elif page == "analytics":
        render_analytics()
    
    render_footer()

if __name__ == "__main__":
    main()
