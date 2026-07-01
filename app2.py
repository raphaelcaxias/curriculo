"""
app.py - Portfólio Raphael Pires - Streamlit Premium
Versão com Estilos Inline para Garantir Funcionamento
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
# CSS COM VARIÁVEIS CSS PERSONALIZADAS
# ============================================================================
def get_css():
    theme = st.session_state.theme
    if theme == "dark":
        bg = "#0B0F1A"
        text = "#F1F5F9"
        text_muted = "#94A3B8"
        text_muted_light = "#64748B"
        card_bg = "rgba(255,255,255,0.04)"
        border = "rgba(255,255,255,0.08)"
        shadow = "rgba(59,130,246,0.3)"
        hover_bg = "rgba(255,255,255,0.06)"
    else:
        bg = "#F8FAFC"
        text = "#0F172A"
        text_muted = "#475569"
        text_muted_light = "#64748B"
        card_bg = "rgba(255,255,255,0.8)"
        border = "rgba(0,0,0,0.06)"
        shadow = "rgba(59,130,246,0.2)"
        hover_bg = "rgba(0,0,0,0.04)"
    
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    :root {{
        --bg: {bg};
        --text: {text};
        --text-muted: {text_muted};
        --text-muted-light: {text_muted_light};
        --card-bg: {card_bg};
        --border: {border};
        --shadow: {shadow};
        --hover-bg: {hover_bg};
        --primary: #3B82F6;
        --secondary: #0EA5E9;
    }}
    
    * {{
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    
    #MainMenu, header, footer, .stDeployButton {{
        display: none !important;
    }}
    
    .stApp {{
        background: var(--bg);
        color: var(--text);
    }}
    
    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
    }}
    
    /* ===== NAVBAR ===== */
    .navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        background: {'rgba(11,15,26,0.92)' if theme == 'dark' else 'rgba(248,250,252,0.92)'};
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid var(--border);
        padding: 0.75rem 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.5rem;
    }}
    
    .navbar-brand {{
        font-weight: 800;
        font-size: 1.2rem;
        color: var(--text);
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    
    .navbar-brand .dot {{
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        box-shadow: 0 0 12px var(--primary);
        animation: pulse 2s infinite;
        flex-shrink: 0;
    }}
    
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.2); }}
    }}
    
    .navbar-brand .gradient-text {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    .nav-links {{
        display: flex;
        gap: 0.25rem;
        align-items: center;
        flex-wrap: wrap;
    }}
    
    .nav-btn {{
        padding: 0.4rem 0.9rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        border: none;
        background: transparent;
        color: var(--text-muted);
        cursor: pointer;
        transition: all 0.25s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        font-family: 'Inter', sans-serif;
    }}
    
    .nav-btn:hover {{
        background: var(--hover-bg);
        color: var(--text);
        transform: translateY(-1px);
    }}
    
    .nav-btn.active {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white !important;
        box-shadow: 0 2px 12px rgba(59,130,246,0.3);
    }}
    
    .theme-btn {{
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: var(--card-bg);
        border: 1px solid var(--border);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 1.1rem;
        flex-shrink: 0;
        color: var(--text);
    }}
    
    .theme-btn:hover {{
        transform: rotate(360deg);
        border-color: var(--primary);
        box-shadow: 0 0 20px rgba(59,130,246,0.15);
    }}
    
    /* ===== HERO ===== */
    .hero {{
        min-height: 85vh;
        display: flex;
        align-items: center;
        padding: 6rem 2rem 3rem;
        background: radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.08) 0%, transparent 70%);
        position: relative;
    }}
    
    .hero-content {{
        max-width: 1200px;
        width: 100%;
        margin: 0 auto;
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 4rem;
        align-items: center;
    }}
    
    @media (max-width: 900px) {{
        .hero-content {{
            grid-template-columns: 1fr;
            text-align: center;
            gap: 2rem;
        }}
        .hero-quote {{
            margin-left: auto !important;
            margin-right: auto !important;
            padding-left: 1rem !important;
            border-left: 3px solid var(--primary) !important;
            text-align: left !important;
            max-width: 400px !important;
        }}
        .hero-badges {{
            justify-content: center !important;
        }}
        .hero-actions {{
            justify-content: center !important;
        }}
    }}
    
    .foto-wrapper {{
        position: relative;
        width: 260px;
        height: 260px;
        flex-shrink: 0;
        margin: 0 auto;
    }}
    
    @media (max-width: 480px) {{
        .foto-wrapper {{
            width: 200px;
            height: 200px;
        }}
    }}
    
    .foto-ring {{
        position: absolute;
        inset: -12px;
        border-radius: 50%;
        background: conic-gradient(var(--primary), var(--secondary), #8B5CF6, var(--primary));
        animation: rotate 8s linear infinite;
        opacity: 0.5;
    }}
    
    .foto-ring::after {{
        content: '';
        position: absolute;
        inset: 4px;
        border-radius: 50%;
        background: var(--bg);
    }}
    
    @keyframes rotate {{
        to {{ transform: rotate(360deg); }}
    }}
    
    .foto {{
        position: relative;
        z-index: 2;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid var(--bg);
        box-shadow: 0 25px 80px var(--shadow);
    }}
    
    .hero-title {{
        font-size: 3.5rem;
        font-weight: 900;
        color: var(--text);
        margin-bottom: 0.5rem;
        line-height: 1.1;
    }}
    
    @media (max-width: 768px) {{
        .hero-title {{
            font-size: 2.2rem;
        }}
    }}
    
    .hero-title .gradient {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    .hero-subtitle {{
        font-size: 1.05rem;
        color: var(--text-muted);
        line-height: 1.7;
        margin: 0.5rem 0 1rem;
        max-width: 600px;
    }}
    
    .hero-quote {{
        font-style: italic;
        color: var(--text-muted-light);
        font-size: 0.95rem;
        margin: 1.2rem 0 1.5rem;
        padding-left: 1.5rem;
        border-left: 3px solid var(--primary);
        max-width: 500px;
        line-height: 1.6;
    }}
    
    .hero-badges {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1rem 0;
    }}
    
    .badge {{
        background: var(--card-bg);
        border: 1px solid var(--border);
        padding: 0.35rem 0.9rem;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 500;
        color: var(--text-muted);
        display: inline-block;
        transition: all 0.2s ease;
        white-space: nowrap;
    }}
    
    .badge:hover {{
        border-color: var(--primary);
        transform: translateY(-2px);
    }}
    
    .hero-actions {{
        display: flex;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
    }}
    
    /* ===== BOTÕES ===== */
    .btn-primary {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
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
        border: none;
        cursor: pointer;
        font-family: 'Inter', sans-serif;
    }}
    
    .btn-primary:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 28px rgba(59,130,246,0.45);
    }}
    
    .btn-secondary {{
        background: var(--card-bg);
        border: 1px solid var(--border);
        padding: 0.65rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.9rem;
        color: var(--text) !important;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.25s ease;
        font-family: 'Inter', sans-serif;
    }}
    
    .btn-secondary:hover {{
        border-color: var(--primary);
        transform: translateY(-2px);
    }}
    
    /* ===== SEÇÕES ===== */
    .section {{
        padding: 4rem 2rem;
        background: var(--bg);
        border-top: 1px solid var(--border);
    }}
    
    .section-alt {{
        background: var(--card-bg);
    }}
    
    .container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    
    .section-header {{
        text-align: center;
        margin-bottom: 3rem;
    }}
    
    .section-label {{
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
        color: var(--primary);
        margin-bottom: 0.75rem;
    }}
    
    .section-title {{
        font-size: 2.5rem;
        font-weight: 800;
        color: var(--text);
        margin-top: 0.25rem;
    }}
    
    .section-subtitle {{
        color: var(--text-muted);
        max-width: 600px;
        margin: 0.75rem auto 0;
        font-size: 1rem;
        line-height: 1.6;
    }}
    
    @media (max-width: 768px) {{
        .section {{
            padding: 3rem 1rem;
        }}
        .section-title {{
            font-size: 1.8rem;
        }}
    }}
    
    /* ===== SOBRE MIM ===== */
    .sobre-section {{
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 2.5rem;
        margin: 1.5rem 0;
    }}
    
    .sobre-text {{
        font-size: 1.05rem;
        line-height: 1.8;
        color: var(--text-muted);
        white-space: pre-line;
        margin-bottom: 0;
    }}
    
    /* ===== KPIs ===== */
    .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.25rem;
    }}
    
    @media (max-width: 1024px) {{
        .kpi-grid {{
            grid-template-columns: repeat(2, 1fr);
        }}
    }}
    
    @media (max-width: 480px) {{
        .kpi-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    
    .kpi-card {{
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        height: 100%;
    }}
    
    .kpi-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    
    .kpi-card:hover {{
        transform: translateY(-6px);
        border-color: var(--primary);
        box-shadow: 0 12px 40px var(--shadow);
    }}
    
    .kpi-card:hover::before {{
        opacity: 1;
    }}
    
    .kpi-icon {{
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }}
    
    .kpi-value {{
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.25rem;
    }}
    
    .kpi-label {{
        font-size: 0.85rem;
        color: var(--text-muted);
        font-weight: 500;
    }}
    
    .kpi-context {{
        font-size: 0.72rem;
        color: var(--text-muted-light);
        margin-top: 0.15rem;
        opacity: 0.7;
    }}
    
    /* ===== TECH STACK ===== */
    .tech-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1.25rem;
    }}
    
    .tech-card {{
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .tech-card:hover {{
        transform: translateY(-4px);
        border-color: var(--primary);
        box-shadow: 0 8px 24px var(--shadow);
    }}
    
    .tech-header {{
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 0.75rem;
    }}
    
    .tech-icon {{
        font-size: 1.8rem;
        flex-shrink: 0;
    }}
    
    .tech-name {{
        font-size: 1rem;
        font-weight: 700;
        color: var(--text);
    }}
    
    .tech-level {{
        font-size: 0.65rem;
        font-weight: 600;
        padding: 0.15rem 0.6rem;
        border-radius: 999px;
        display: inline-block;
    }}
    
    .tech-level.expert {{
        background: rgba(34,197,94,0.15);
        color: #22C55E;
    }}
    
    .tech-level.avancado {{
        background: rgba(59,130,246,0.15);
        color: var(--primary);
    }}
    
    .tech-level.intermediario {{
        background: rgba(245,158,11,0.15);
        color: #F59E0B;
    }}
    
    .tech-items {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
    }}
    
    .tech-item {{
        font-size: 0.7rem;
        background: rgba(59,130,246,0.1);
        border: 1px solid rgba(59,130,246,0.2);
        padding: 0.15rem 0.6rem;
        border-radius: 8px;
        color: var(--primary);
        font-weight: 500;
    }}
    
    /* ===== TIMELINE ===== */
    .timeline {{
        position: relative;
        padding: 0.5rem 0;
    }}
    
    .timeline-item {{
        position: relative;
        padding-left: 2rem;
        margin-bottom: 1.5rem;
        border-left: 2px solid var(--primary);
        animation: slideIn 0.5s ease backwards;
    }}
    
    .timeline-item:nth-child(1) {{ animation-delay: 0.05s; }}
    .timeline-item:nth-child(2) {{ animation-delay: 0.1s; }}
    .timeline-item:nth-child(3) {{ animation-delay: 0.15s; }}
    .timeline-item:nth-child(4) {{ animation-delay: 0.2s; }}
    .timeline-item:nth-child(5) {{ animation-delay: 0.25s; }}
    
    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(-16px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    
    .timeline-dot {{
        position: absolute;
        left: -8px;
        top: 4px;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border: 3px solid var(--bg);
        box-shadow: 0 0 0 3px var(--primary);
    }}
    
    .timeline-card {{
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.25rem;
        transition: all 0.3s ease;
    }}
    
    .timeline-card:hover {{
        border-color: var(--primary);
        transform: translateX(6px);
        box-shadow: 0 8px 24px var(--shadow);
    }}
    
    .timeline-date {{
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 700;
        background: rgba(59,130,246,0.12);
        color: var(--primary);
        padding: 0.15rem 0.8rem;
        border-radius: 999px;
    }}
    
    .timeline-badge {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        font-size: 0.6rem;
        font-weight: 700;
        padding: 0.15rem 0.6rem;
        border-radius: 999px;
        margin-left: 0.4rem;
    }}
    
    .timeline-role {{
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text);
        margin: 0.4rem 0 0.1rem;
    }}
    
    .timeline-company {{
        color: var(--secondary);
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }}
    
    .timeline-desc {{
        color: var(--text-muted);
        line-height: 1.6;
        font-size: 0.92rem;
        margin-bottom: 0.5rem;
    }}
    
    .timeline-tag {{
        font-size: 0.65rem;
        background: rgba(59,130,246,0.1);
        border: 1px solid rgba(59,130,246,0.2);
        padding: 0.15rem 0.6rem;
        border-radius: 8px;
        display: inline-block;
        margin: 0.15rem;
        color: var(--primary);
        font-weight: 500;
    }}
    
    /* ===== PROJECTS ===== */
    .project-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
    }}
    
    .project-card {{
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 1.75rem;
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }}
    
    .project-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s ease;
    }}
    
    .project-card:hover {{
        transform: translateY(-8px);
        border-color: var(--primary);
        box-shadow: 0 12px 40px var(--shadow);
    }}
    
    .project-card:hover::before {{
        transform: scaleX(1);
    }}
    
    .project-icon {{
        font-size: 2.2rem;
        margin-bottom: 0.75rem;
    }}
    
    .project-card h3 {{
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 0.15rem;
    }}
    
    .project-subtitle {{
        font-size: 0.85rem;
        color: var(--text-muted);
        margin-bottom: 0.5rem;
        font-style: italic;
    }}
    
    .project-card p {{
        color: var(--text-muted);
        line-height: 1.6;
        font-size: 0.88rem;
        margin-bottom: 0.5rem;
    }}
    
    .project-context {{
        font-size: 0.8rem;
        color: var(--primary);
        font-style: italic;
        margin-bottom: 0.75rem;
        padding-left: 0.75rem;
        border-left: 2px solid var(--primary);
    }}
    
    .project-tag {{
        font-size: 0.65rem;
        background: rgba(59,130,246,0.1);
        border: 1px solid rgba(59,130,246,0.2);
        padding: 0.15rem 0.5rem;
        border-radius: 6px;
        color: var(--primary);
        font-weight: 500;
        display: inline-block;
        margin: 0.15rem;
    }}
    
    /* ===== CERTIFICAÇÕES ===== */
    .cert-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1.25rem;
    }}
    
    .cert-card {{
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .cert-card:hover {{
        border-color: var(--primary);
        transform: translateY(-4px);
        box-shadow: 0 8px 24px var(--shadow);
    }}
    
    .cert-header {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.5rem;
    }}
    
    .cert-icon {{
        font-size: 1.8rem;
        flex-shrink: 0;
    }}
    
    .cert-inst {{
        font-weight: 700;
        font-size: 1rem;
        color: var(--text);
    }}
    
    .cert-status {{
        font-size: 0.75rem;
        color: var(--text-muted);
        margin-bottom: 0.5rem;
    }}
    
    .cert-cursos {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.3rem;
    }}
    
    .cert-curso {{
        font-size: 0.7rem;
        background: rgba(59,130,246,0.1);
        border: 1px solid rgba(59,130,246,0.2);
        padding: 0.15rem 0.6rem;
        border-radius: 8px;
        color: var(--primary);
        font-weight: 500;
        display: inline-block;
    }}
    
    .progress-bar {{
        width: 100%;
        height: 6px;
        background: var(--border);
        border-radius: 999px;
        overflow: hidden;
        margin-top: 0.75rem;
    }}
    
    .progress-fill {{
        height: 100%;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border-radius: 999px;
        transition: width 0.8s ease;
        box-shadow: 0 0 12px rgba(59,130,246,0.3);
    }}
    
    /* ===== FOOTER ===== */
    .footer {{
        padding: 3rem 2rem 2rem;
        text-align: center;
        border-top: 1px solid var(--border);
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
    }}
    
    .footer h3 {{
        font-size: 1.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }}
    
    .footer-links {{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1.5rem 0 1rem;
    }}
    
    .footer-link {{
        background: var(--card-bg);
        border: 1px solid var(--border);
        padding: 0.5rem 1.1rem;
        border-radius: 12px;
        color: var(--text) !important;
        text-decoration: none;
        font-size: 0.82rem;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        transition: all 0.25s ease;
    }}
    
    .footer-link:hover {{
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white !important;
        border-color: transparent;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(59,130,246,0.3);
    }}
    
    .footer-copy {{
        color: var(--text-muted-light);
        font-size: 0.75rem;
        margin-top: 1rem;
    }}
    
    .scroll-top {{
        position: fixed;
        bottom: 1.5rem;
        right: 1.5rem;
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
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
    }}
    
    .scroll-top:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(59,130,246,0.5);
    }}
    
    @media (max-width: 768px) {{
        .navbar {{
            padding: 0.5rem 1rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}
        .navbar-brand {{
            font-size: 1rem;
        }}
        .nav-links {{
            width: 100%;
            justify-content: center;
            gap: 0.15rem;
        }}
        .nav-btn {{
            font-size: 0.7rem;
            padding: 0.3rem 0.6rem;
        }}
        .hero {{
            padding: 5rem 1rem 2rem;
            min-height: auto;
        }}
        .hero-title {{
            font-size: 2rem;
        }}
        .hero-subtitle {{
            font-size: 0.95rem;
        }}
        .hero-quote {{
            font-size: 0.85rem;
            padding-left: 1rem;
        }}
        .section {{
            padding: 2rem 1rem;
        }}
        .section-title {{
            font-size: 1.6rem;
        }}
        .sobre-section {{
            padding: 1.5rem;
        }}
        .sobre-text {{
            font-size: 0.95rem;
        }}
        .footer {{
            padding: 2rem 1rem 1.5rem;
        }}
        .footer h3 {{
            font-size: 1.4rem;
        }}
        .footer-links {{
            gap: 0.35rem;
        }}
        .footer-link {{
            font-size: 0.75rem;
            padding: 0.4rem 0.8rem;
        }}
        .scroll-top {{
            width: 38px;
            height: 38px;
            font-size: 0.9rem;
            bottom: 1rem;
            right: 1rem;
        }}
    }}
    
    @media (max-width: 480px) {{
        .hero-title {{
            font-size: 1.6rem;
        }}
        .kpi-value {{
            font-size: 1.5rem;
        }}
        .nav-btn {{
            font-size: 0.6rem;
            padding: 0.2rem 0.5rem;
        }}
        .nav-links {{
            gap: 0.1rem;
        }}
        .btn-primary, .btn-secondary {{
            font-size: 0.8rem;
            padding: 0.5rem 1rem;
        }}
        .project-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    </style>
    """

# ============================================================================
# FUNÇÕES DE RENDERIZAÇÃO
# ============================================================================

def render_navbar():
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    page = st.session_state.page
    
    nav_html = f"""
    <nav class="navbar" role="navigation" aria-label="Navegação principal">
        <a href="#" class="navbar-brand" onclick="window.location.href='?page=home'" style="cursor:pointer;">
            <span class="dot"></span>
            Raphael <span class="gradient-text">Pires</span>
        </a>
        <div class="nav-links">
            <button class="nav-btn {'active' if page == 'home' else ''}" onclick="window.location.href='?page=home'">🏠 Início</button>
            <button class="nav-btn {'active' if page == 'curriculo' else ''}" onclick="window.location.href='?page=curriculo'">📄 Currículo</button>
            <button class="nav-btn {'active' if page == 'projetos' else ''}" onclick="window.location.href='?page=projetos'">🚀 Projetos</button>
            <button class="nav-btn {'active' if page == 'analytics' else ''}" onclick="window.location.href='?page=analytics'">📊 Analytics</button>
            <button class="theme-btn" onclick="window.location.href='?theme_toggle=1&page={page}'" aria-label="Alternar tema">{theme_icon}</button>
        </div>
    </nav>
    """
    st.markdown(nav_html, unsafe_allow_html=True)
    st.markdown('<div style="height: 70px;"></div>', unsafe_allow_html=True)

def render_hero():
    foto_path = get_foto_path()
    foto_b64 = get_foto_base64(foto_path)
    foto_url = foto_b64 if foto_b64 else "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=3B82F6&color=fff&bold=true"
    
    pdf_path = get_pdf_path()
    cv_button = ""
    if pdf_path:
        pdf_b64 = ler_pdf_base64(pdf_path)
        if pdf_b64:
            cv_button = f'<a href="data:application/pdf;base64,{pdf_b64}" download="Curriculo_Raphael_Pires.pdf" class="btn-secondary">📄 Baixar CV</a>'
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <div class="foto-wrapper">
                <div class="foto-ring"></div>
                <img src="{foto_url}" alt="Raphael Pires - Foto de perfil" class="foto" loading="eager">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div>
            <div class="section-label">📊 {DADOS['titulo']}</div>
            <h1 class="hero-title">Raphael <span class="gradient">Pires</span></h1>
            <p class="hero-subtitle">{PERFIL}</p>
            <div class="hero-quote">"{CITACAO}"</div>
            <div class="hero-badges">
                <span class="badge">📍 {DADOS['localizacao']}</span>
                <span class="badge">🏠 {DADOS['modalidades'][0]}</span>
                <span class="badge">✈️ {DADOS['modalidades'][1]}</span>
            </div>
            <div class="hero-actions">
                <a href="#experiencia" class="btn-primary">💼 Ver Experiência</a>
                {cv_button}
                <a href="{LINKS['linkedin']}" target="_blank" rel="noopener noreferrer" class="btn-secondary">💼 LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_sobre():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">👤 Quem sou eu</span>
        <h2 class="section-title">Minha História</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="sobre-section">
        <p class="sobre-text">{SOBRE_MIM['texto']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 2rem; text-align: center;">
        <h3 style="color: var(--text); font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem;">💎 Meus Valores</h3>
        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">O que me move e como trabalho</p>
    </div>
    """, unsafe_allow_html=True)
    
    # USANDO ESTILOS INLINE - GARANTIDO QUE FUNCIONA!
    cols = st.columns(4)
    
    for i, valor in enumerate(SOBRE_MIM['valores']):
        with cols[i]:
            st.markdown(f"""
            <div style="
                background: var(--card-bg);
                border: 1px solid var(--border);
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
                <div style="font-weight: 700; font-size: 1.05rem; color: var(--text); margin-bottom: 0.35rem;">{valor['titulo']}</div>
                <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5; max-width: 200px;">{valor['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_kpis():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">📈 Impacto</span>
        <h2 class="section-title">Números que contam histórias</h2>
        <p class="section-subtitle">Resultados concretos de mais de uma década</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, kpi in enumerate(KPIS):
        with cols[i]:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon">{kpi['icone']}</div>
                <div class="kpi-value">{kpi['valor']}</div>
                <div class="kpi-label">{kpi['label']}</div>
                <div class="kpi-context">{kpi['contexto']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_tech():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">⚡ Tech Stack</span>
        <h2 class="section-title">Ferramentas que domino</h2>
    </div>
    """, unsafe_allow_html=True)
    
    tech_items = list(TECH_STACK.items())
    cols_per_row = 3
    
    for i in range(0, len(tech_items), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(tech_items):
                tech, dados = tech_items[i + j]
                nivel_class = dados['nivel'].lower().replace('í', 'i').replace('á', 'a')
                with cols[j]:
                    itens_html = "".join([f'<span class="tech-item">{item}</span>' for item in dados['itens']])
                    st.markdown(f"""
                    <div class="tech-card">
                        <div class="tech-header">
                            <span class="tech-icon">{dados['icone']}</span>
                            <div>
                                <div class="tech-name">{tech}</div>
                                <span class="tech-level {nivel_class}">{dados['nivel']}</span>
                            </div>
                        </div>
                        <div class="tech-items">{itens_html}</div>
                    </div>
                    """, unsafe_allow_html=True)

def render_skills_chart():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">📊 Visualização</span>
        <h2 class="section-title">Nível de domínio</h2>
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
    )
    
    font_color = "#F1F5F9" if st.session_state.theme == "dark" else "#0F172A"
    fig.update_layout(font=dict(color=font_color))
    fig.update_traces(textposition="outside")
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_certificacoes():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">🎓 Certificações</span>
        <h2 class="section-title">Formação contínua</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, cert in enumerate(CERTIFICACOES):
        with cols[i]:
            cursos_html = "".join([f'<span class="cert-curso">{c}</span>' for c in cert['cursos']])
            st.markdown(f"""
            <div class="cert-card">
                <div class="cert-header">
                    <span class="cert-icon">{cert['icone']}</span>
                    <span class="cert-inst">{cert['instituicao']}</span>
                </div>
                <div class="cert-status">{cert['status']}</div>
                <div class="cert-cursos">{cursos_html}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {cert['progresso']}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_formacao():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">🎓 Formação</span>
        <h2 class="section-title">Formação acadêmica</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, form in enumerate(FORMACAO):
        with cols[i]:
            st.markdown(f"""
            <div class="cert-card">
                <div class="cert-header">
                    <span class="cert-icon">{form['icone']}</span>
                    <div>
                        <div class="cert-inst">{form['curso']}</div>
                        <div class="cert-status">{form['instituicao']} · {form['ano']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_idiomas():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">🌐 Idiomas</span>
        <h2 class="section-title">Competências linguísticas</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, idioma in enumerate(IDIOMAS):
        with cols[i]:
            st.markdown(f"""
            <div class="cert-card" style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">{idioma['icone']}</div>
                <div class="cert-inst">{idioma['idioma']}</div>
                <div class="cert-status">{idioma['nivel']}</div>
            </div>
            """, unsafe_allow_html=True)

def render_experiencias():
    st.markdown("""
    <div class="section-header" id="experiencia">
        <span class="section-label">💼 Trajetória</span>
        <h2 class="section-title">Experiência profissional</h2>
    </div>
    """, unsafe_allow_html=True)
    
    for exp in EXPERIENCIAS:
        with st.container():
            badge = f'<span class="timeline-badge">{exp["status"]}</span>' if exp.get("status") else ""
            desc = "<br>".join([f"• {d}" for d in exp["descricao"]])
            tags = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
            
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div>
                        <span class="timeline-date">{exp['periodo']}</span> {badge}
                    </div>
                    <div class="timeline-role">{exp['cargo']}</div>
                    <div class="timeline-company">{exp['empresa']} · {exp['tipo']}</div>
                    <div class="timeline-desc">{desc}</div>
                    <div>{tags}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_projetos():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">🚀 Projetos</span>
        <h2 class="section-title">Analytics na prática</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, p in enumerate(PROJETOS):
        with cols[i]:
            techs = "".join([f'<span class="project-tag">{t}</span>' for t in p["tech"]])
            link = f'<a href="{p["url"]}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Ver</a>' if p.get("url") else f'<a href="{LINKS["github"]}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">💻 GitHub</a>'
            
            st.markdown(f"""
            <div class="project-card">
                <div class="project-icon">{p['icone']}</div>
                <h3>{p['nome']}</h3>
                <div class="project-subtitle">{p['subtitulo']}</div>
                <p>{p['descricao']}</p>
                <div class="project-context">💡 {p['contexto']}</div>
                <div>{techs}</div>
                <div style="margin-top: 1rem;">{link}</div>
            </div>
            """, unsafe_allow_html=True)

def render_footer():
    tel = DADOS['contato']['telefone1'].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    
    st.markdown("---")
    
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0;">
        <div style="display:inline-flex;align-items:center;gap:0.6rem;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.2);padding:0.35rem 1.2rem;border-radius:999px;font-size:0.8rem;font-weight:600;color:#22C55E;margin-bottom:1.5rem;">
            <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#22C55E;animation:pulse 2s infinite;"></span>
            Disponível para oportunidades
        </div>
        <h2 style="font-size:2rem;font-weight:800;background:linear-gradient(135deg, #3B82F6, #0EA5E9);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:0.5rem;">Vamos conversar?</h2>
        <p style="color:#94A3B8;font-size:1.05rem;margin-bottom:1.5rem;">Se busca alguém que entende de negócio E de dados, vamos tomar um café.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f'<a href="{LINKS["linkedin"]}" target="_blank" rel="noopener noreferrer" class="footer-link">💼 LinkedIn</a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<a href="{LINKS["github"]}" target="_blank" rel="noopener noreferrer" class="footer-link">💻 GitHub</a>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<a href="{LINKS["email"]}" class="footer-link">✉️ E-mail</a>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<a href="{LINKS["whatsapp"]}" target="_blank" rel="noopener noreferrer" class="footer-link">📱 WhatsApp</a>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<a href="tel:{tel}" class="footer-link">📞 {DADOS["contato"]["telefone1"]}</a>', unsafe_allow_html=True)
    
    pdf_path = get_pdf_path()
    if pdf_path:
        pdf_b64 = ler_pdf_base64(pdf_path)
        if pdf_b64:
            st.markdown(f"""
            <div style="text-align: center; margin: 0.5rem 0 1rem;">
                <a href="data:application/pdf;base64,{pdf_b64}" download="Curriculo_Raphael_Pires.pdf" class="footer-link">📄 Baixar Currículo (PDF)</a>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <p class="footer-copy">© 2026 {DADOS['nome']} · Feito com ❤️ e Streamlit</p>
    """, unsafe_allow_html=True)
    
    st.markdown('<a href="#topo" class="scroll-top" aria-label="Voltar ao topo">↑</a>', unsafe_allow_html=True)

def render_analytics():
    st.markdown("""
    <div style="padding: 1rem 0 2rem; text-align: center;">
        <h1 class="hero-title" style="font-size: 2.8rem;">📊 Analytics Interativo</h1>
        <p class="hero-subtitle" style="margin: 0 auto; max-width: 500px;">Dashboards em Streamlit + Plotly</p>
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
