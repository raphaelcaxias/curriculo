"""
app.py - Portfólio Raphael Pires - Streamlit
Versão Premium com Design Moderno e Animações
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os
import base64
from datetime import datetime

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
    {"valor": "70%", "label": "Redução tempo operacional", "contexto": "Banco do Brasil", "icone": "⚡", "cor": "#3B82F6"},
    {"valor": "2h→15min", "label": "Ciclo de análise", "contexto": "Relatórios comerciais", "icone": "⏱️", "cor": "#0EA5E9"},
    {"valor": "213 mil+", "label": "Registros analisados", "contexto": "Projeto CNPq", "icone": "📊", "cor": "#8B5CF6"},
    {"valor": "16 anos", "label": "Experiência profissional", "contexto": "Acumulada", "icone": "🏆", "cor": "#F59E0B"}
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
# CSS PREMIUM COM ANIMAÇÕES
# ============================================================================
def get_css():
    theme = st.session_state.theme
    if theme == "dark":
        bg = "#0B0F1A"
        text = "#F1F5F9"
        text_muted = "#94A3B8"
        card_bg = "rgba(255,255,255,0.04)"
        border = "rgba(255,255,255,0.08)"
    else:
        bg = "#F8FAFC"
        text = "#0F172A"
        text_muted = "#475569"
        card_bg = "rgba(255,255,255,0.8)"
        border = "rgba(0,0,0,0.06)"
    
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {{ font-family: 'Inter', sans-serif; }}
    
    #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
    .stApp {{ background: {bg}; }}
    
    /* Navbar Fixa */
    .navbar {{
        position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
        background: {'rgba(11,15,26,0.9)' if theme == 'dark' else 'rgba(248,250,252,0.9)'};
        backdrop-filter: blur(20px);
        border-bottom: 1px solid {border};
        padding: 1rem 2.5rem;
        display: flex; align-items: center; justify-content: space-between;
    }}
    .navbar-brand {{
        font-weight: 800; font-size: 1.3rem; color: {text};
        text-decoration: none; display: flex; align-items: center; gap: 0.5rem;
    }}
    .navbar-brand .dot {{
        width: 10px; height: 10px; border-radius: 50%;
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        box-shadow: 0 0 12px #3B82F6;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.2); }} }}
    .navbar-brand span {{
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .nav-links {{ display: flex; gap: 0.5rem; align-items: center; }}
    .nav-link {{
        padding: 0.5rem 1.1rem; border-radius: 999px; font-size: 0.875rem;
        font-weight: 500; text-decoration: none; transition: all 0.25s;
        color: {text_muted}; background: transparent; cursor: pointer;
        border: none;
    }}
    .nav-link:hover {{ background: {'rgba(255,255,255,0.06)' if theme == 'dark' else 'rgba(0,0,0,0.04)'}; color: {text}; }}
    .nav-link.active {{
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        color: white !important;
    }}
    .theme-toggle {{
        width: 40px; height: 40px; border-radius: 50%;
        background: {card_bg}; border: 1px solid {border};
        display: flex; align-items: center; justify-content: center;
        cursor: pointer; transition: all 0.3s; font-size: 1.2rem; margin-left: 0.5rem;
    }}
    .theme-toggle:hover {{ transform: rotate(360deg); border-color: #3B82F6; }}
    
    /* Hero */
    .hero {{
        min-height: 85vh; display: flex; align-items: center;
        padding: 7rem 2rem 3rem;
        background: radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.1) 0%, transparent 70%);
        position: relative;
    }}
    .hero-content {{
        max-width: 1200px; width: 100%; margin: 0 auto;
        display: grid; grid-template-columns: auto 1fr; gap: 4rem;
        align-items: center;
    }}
    @media (max-width: 900px) {{ .hero-content {{ grid-template-columns: 1fr; text-align: center; }} }}
    .foto-wrapper {{
        position: relative; width: 260px; height: 260px;
    }}
    .foto-ring {{
        position: absolute; inset: -12px; border-radius: 50%;
        background: conic-gradient(#3B82F6, #0EA5E9, #8B5CF6, #3B82F6);
        animation: rotate 8s linear infinite; opacity: 0.6;
    }}
    .foto-ring::after {{
        content: ''; position: absolute; inset: 4px;
        border-radius: 50%; background: {bg};
    }}
    @keyframes rotate {{ to {{ transform: rotate(360deg); }} }}
    .foto {{
        position: relative; z-index: 2; width: 260px; height: 260px;
        border-radius: 50%; object-fit: cover; border: 4px solid {bg};
        box-shadow: 0 25px 80px rgba(59,130,246,0.3);
    }}
    .hero-title {{
        font-size: 3.5rem; font-weight: 900; color: {text};
        margin-bottom: 0.5rem; line-height: 1.1;
    }}
    .hero-title .gradient {{
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hero-subtitle {{
        font-size: 1.1rem; color: {text_muted}; line-height: 1.7;
        margin: 0.5rem 0 1.5rem; max-width: 600px;
    }}
    .hero-quote {{
        font-style: italic; color: {text_muted};
        font-size: 0.95rem; margin: 1.5rem 0;
        padding-left: 1.5rem; border-left: 3px solid #3B82F6;
        max-width: 500px;
    }}
    .badge {{
        background: {card_bg}; border: 1px solid {border};
        padding: 0.4rem 0.9rem; border-radius: 10px;
        font-size: 0.78rem; font-weight: 500; color: {text_muted};
        display: inline-block; transition: all 0.2s; margin: 0.25rem;
    }}
    .badge:hover {{ border-color: #3B82F6; transform: translateY(-2px); }}
    
    /* Botões */
    .btn-primary {{
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        color: white !important; padding: 0.75rem 1.75rem; border-radius: 12px;
        font-weight: 600; text-decoration: none;
        display: inline-flex; align-items: center; gap: 0.5rem;
        box-shadow: 0 4px 16px rgba(59,130,246,0.3); transition: all 0.25s;
        border: none; cursor: pointer;
    }}
    .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 28px rgba(59,130,246,0.45); }}
    .btn-secondary {{
        background: {card_bg}; border: 1px solid {border};
        padding: 0.75rem 1.75rem; border-radius: 12px;
        font-weight: 600; color: {text} !important;
        text-decoration: none; display: inline-flex;
        align-items: center; gap: 0.5rem; transition: all 0.25s;
    }}
    .btn-secondary:hover {{ border-color: #3B82F6; transform: translateY(-2px); }}
    
    /* Seções */
    .section {{
        padding: 5rem 2rem;
        background: {bg};
        border-top: 1px solid {border};
    }}
    .section.alt {{
        background: {'rgba(255,255,255,0.02)' if theme == 'dark' else 'rgba(0,0,0,0.01)'};
    }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .section-header {{ text-align: center; margin-bottom: 3.5rem; }}
    .section-label {{
        display: inline-flex; align-items: center; gap: 0.5rem;
        background: rgba(59,130,246,0.15); border: 1px solid rgba(59,130,246,0.25);
        padding: 0.35rem 1.1rem; border-radius: 999px;
        font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
        letter-spacing: 0.1em; color: #3B82F6; margin-bottom: 1rem;
    }}
    .section-title {{
        font-size: 2.5rem; font-weight: 800; color: {text};
        margin-top: 0.5rem;
    }}
    .section-subtitle {{
        color: {text_muted}; max-width: 600px;
        margin: 1rem auto 0; font-size: 1.05rem;
    }}
    
    /* KPIs */
    .kpi-card {{
        background: {card_bg}; backdrop-filter: blur(12px);
        border: 1px solid {border}; border-radius: 20px;
        padding: 1.75rem 1.5rem; text-align: center;
        transition: all 0.3s; position: relative; overflow: hidden;
        height: 100%;
    }}
    .kpi-card::before {{
        content: ''; position: absolute; top: 0; left: 0; right: 0;
        height: 3px; background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        opacity: 0; transition: opacity 0.3s;
    }}
    .kpi-card:hover {{ transform: translateY(-6px); border-color: #3B82F6; }}
    .kpi-card:hover::before {{ opacity: 1; }}
    .kpi-icon {{ font-size: 2rem; margin-bottom: 0.75rem; }}
    .kpi-value {{
        font-size: 2rem; font-weight: 800;
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.35rem;
    }}
    .kpi-label {{ font-size: 0.85rem; color: {text_muted}; font-weight: 500; }}
    .kpi-context {{ font-size: 0.75rem; color: {text_muted}; margin-top: 0.25rem; opacity: 0.7; }}
    
    /* Sobre Mim */
    .sobre-section {{
        background: {card_bg}; backdrop-filter: blur(12px);
        border: 1px solid {border}; border-radius: 24px;
        padding: 2.5rem; margin: 2rem 0;
    }}
    .sobre-text {{
        font-size: 1.05rem; line-height: 1.8; color: {text_muted};
        white-space: pre-line; margin-bottom: 2rem;
    }}
    .valores-grid {{
        display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem; margin-top: 2rem;
    }}
    .valor-card {{
        background: {bg}; border: 1px solid {border};
        border-radius: 16px; padding: 1.5rem; text-align: center;
        transition: all 0.3s;
    }}
    .valor-card:hover {{ transform: translateY(-4px); border-color: #3B82F6; }}
    .valor-icon {{ font-size: 2.5rem; margin-bottom: 0.75rem; }}
    .valor-title {{ font-size: 1rem; font-weight: 700; color: {text}; margin-bottom: 0.5rem; }}
    .valor-desc {{ font-size: 0.85rem; color: {text_muted}; line-height: 1.5; }}
    
    /* Tech Cards */
    .tech-card {{
        background: {card_bg}; backdrop-filter: blur(12px);
        border: 1px solid {border}; border-radius: 20px;
        padding: 1.75rem; transition: all 0.3s; height: 100%;
    }}
    .tech-card:hover {{ transform: translateY(-4px); border-color: #3B82F6; }}
    .tech-header {{ display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }}
    .tech-icon {{ font-size: 2rem; }}
    .tech-name {{ font-size: 1.1rem; font-weight: 700; color: {text}; }}
    .tech-level {{
        font-size: 0.72rem; font-weight: 600;
        padding: 0.2rem 0.6rem; border-radius: 999px;
        display: inline-block;
    }}
    .tech-level.expert {{ background: rgba(34,197,94,0.15); color: #22C55E; }}
    .tech-level.avancado {{ background: rgba(59,130,246,0.15); color: #3B82F6; }}
    .tech-level.intermediario {{ background: rgba(245,158,11,0.15); color: #F59E0B; }}
    .tech-items {{ display: flex; flex-wrap: wrap; gap: 0.4rem; }}
    .tech-item {{
        font-size: 0.78rem; background: rgba(59,130,246,0.12);
        border: 1px solid rgba(59,130,246,0.25);
        padding: 0.25rem 0.7rem; border-radius: 8px;
        color: #3B82F6; font-weight: 500;
    }}
    
    /* Timeline */
    .timeline-item {{
        position: relative; padding-left: 2rem;
        margin-bottom: 2rem; border-left: 2px solid #3B82F6;
        animation: slideIn 0.6s ease backwards;
    }}
    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(-20px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    .timeline-dot {{
        position: absolute; left: -8px; top: 0;
        width: 14px; height: 14px; border-radius: 50%;
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        border: 3px solid {bg};
        box-shadow: 0 0 0 3px #3B82F6;
    }}
    .timeline-card {{
        background: {card_bg}; backdrop-filter: blur(12px);
        border: 1px solid {border}; border-radius: 16px;
        padding: 1.5rem; transition: all 0.3s;
    }}
    .timeline-card:hover {{ border-color: #3B82F6; transform: translateX(8px); }}
    .timeline-date {{
        display: inline-block; font-size: 0.72rem; font-weight: 700;
        background: rgba(59,130,246,0.15); color: #3B82F6;
        padding: 0.25rem 0.9rem; border-radius: 999px;
    }}
    .timeline-badge {{
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        color: white; font-size: 0.62rem; font-weight: 800;
        padding: 0.2rem 0.7rem; border-radius: 999px; margin-left: 0.5rem;
    }}
    .timeline-role {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin: 0.5rem 0 0.2rem; }}
    .timeline-company {{ color: #0EA5E9; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.75rem; }}
    .timeline-desc {{ color: {text_muted}; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.75rem; }}
    .timeline-tag {{
        font-size: 0.72rem; background: rgba(59,130,246,0.12);
        border: 1px solid rgba(59,130,246,0.25);
        padding: 0.25rem 0.7rem; border-radius: 8px;
        display: inline-block; margin: 0.2rem;
        color: #3B82F6; font-weight: 600;
    }}
    
    /* Projects */
    .project-card {{
        background: {card_bg}; backdrop-filter: blur(12px);
        border: 1px solid {border}; border-radius: 24px;
        padding: 2rem; transition: all 0.3s; height: 100%;
        position: relative; overflow: hidden;
    }}
    .project-card::before {{
        content: ''; position: absolute; top: 0; left: 0; right: 0;
        height: 3px; background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        transform: scaleX(0); transform-origin: left; transition: transform 0.4s;
    }}
    .project-card:hover {{ transform: translateY(-8px); border-color: #3B82F6; }}
    .project-card:hover::before {{ transform: scaleX(1); }}
    .project-icon {{ font-size: 2.5rem; margin-bottom: 1rem; }}
    .project-card h3 {{ font-size: 1.25rem; font-weight: 700; color: {text}; margin-bottom: 0.25rem; }}
    .project-subtitle {{ font-size: 0.9rem; color: {text_muted}; margin-bottom: 0.75rem; font-style: italic; }}
    .project-card p {{ color: {text_muted}; line-height: 1.65; font-size: 0.92rem; margin-bottom: 0.5rem; }}
    .project-context {{
        font-size: 0.85rem; color: #3B82F6; font-style: italic;
        margin-bottom: 1rem; padding-left: 1rem;
        border-left: 2px solid #3B82F6;
    }}
    .project-tag {{
        font-size: 0.7rem; background: rgba(59,130,246,0.12);
        border: 1px solid rgba(59,130,246,0.25);
        padding: 0.2rem 0.6rem; border-radius: 6px;
        color: #3B82F6; font-weight: 600;
        display: inline-block; margin: 0.2rem;
    }}
    
    /* Certifications */
    .cert-card {{
        background: {card_bg}; backdrop-filter: blur(12px);
        border: 1px solid {border}; border-radius: 20px;
        padding: 1.75rem; transition: all 0.3s; height: 100%;
    }}
    .cert-card:hover {{ border-color: #3B82F6; transform: translateY(-4px); }}
    .cert-header {{ display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem; }}
    .cert-icon {{ font-size: 2rem; }}
    .cert-inst {{ font-weight: 700; font-size: 1.1rem; color: {text}; }}
    .cert-status {{ font-size: 0.78rem; color: {text_muted}; margin-bottom: 0.5rem; }}
    .cert-curso {{
        font-size: 0.78rem; background: rgba(59,130,246,0.12);
        border: 1px solid rgba(59,130,246,0.25);
        padding: 0.25rem 0.7rem; border-radius: 8px;
        color: #3B82F6; font-weight: 500;
        display: inline-block; margin: 0.2rem;
    }}
    .progress-bar {{
        width: 100%; height: 8px; background: {border};
        border-radius: 999px; overflow: hidden; margin-top: 0.75rem;
    }}
    .progress-fill {{
        height: 100%; background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        border-radius: 999px; box-shadow: 0 0 12px #3B82F6;
    }}
    
    /* Footer */
    .footer {{
        padding: 4rem 2rem 2.5rem; text-align: center;
        border-top: 1px solid {border};
        background: {card_bg}; backdrop-filter: blur(12px);
    }}
    .footer h3 {{
        font-size: 2rem; font-weight: 800;
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }}
    .footer-link {{
        background: {card_bg}; border: 1px solid {border};
        padding: 0.6rem 1.25rem; border-radius: 12px;
        color: {text} !important; text-decoration: none;
        font-size: 0.88rem; font-weight: 500;
        display: inline-flex; align-items: center; gap: 0.4rem;
        transition: all 0.25s;
    }}
    .footer-link:hover {{
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        color: white !important; border-color: transparent;
        transform: translateY(-2px);
    }}
    .footer-copy {{ color: {text_muted}; font-size: 0.8rem; margin-top: 1.5rem; }}
    
    .scroll-top {{
        position: fixed; bottom: 2rem; right: 2rem;
        width: 48px; height: 48px; border-radius: 50%;
        background: linear-gradient(135deg, #3B82F6, #0EA5E9);
        color: white; display: flex; align-items: center; justify-content: center;
        font-size: 1.2rem; cursor: pointer;
        box-shadow: 0 8px 24px rgba(59,130,246,0.35);
        transition: all 0.25s; z-index: 999; text-decoration: none;
    }}
    .scroll-top:hover {{ transform: translateY(-4px); }}
    
    @media (max-width: 768px) {{
        .navbar {{ padding: 0.75rem 1rem; }}
        .hero {{ padding: 6rem 1rem 2rem; min-height: auto; }}
        .hero-title {{ font-size: 2.2rem; }}
        .foto-wrapper {{ width: 200px; height: 200px; }}
        .foto {{ width: 200px; height: 200px; }}
        .section {{ padding: 3rem 1rem; }}
        .section-title {{ font-size: 1.8rem; }}
    }}
    </style>
    """

# ============================================================================
# FUNÇÕES DE RENDERIZAÇÃO
# ============================================================================

def render_navbar():
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    page = st.session_state.page
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 1, 1, 1, 1, 1, 1])
    
    with col1:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 0.5rem; padding-top: 0.5rem;">
            <div style="width: 10px; height: 10px; border-radius: 50%; background: linear-gradient(135deg, #3B82F6, #0EA5E9); box-shadow: 0 0 12px #3B82F6; animation: pulse 2s infinite;"></div>
            <span style="font-weight: 800; font-size: 1.3rem; color: var(--text);">Raphael <span style="background: linear-gradient(135deg, #3B82F6, #0EA5E9); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Pires</span></span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("🏠 Início", key="nav_home", use_container_width=True, type="primary" if page == "home" else "secondary"):
            st.session_state.page = "home"
            st.rerun()
    
    with col3:
        if st.button("📄 Currículo", key="nav_cv", use_container_width=True, type="primary" if page == "curriculo" else "secondary"):
            st.session_state.page = "curriculo"
            st.rerun()
    
    with col4:
        if st.button("🚀 Projetos", key="nav_proj", use_container_width=True, type="primary" if page == "projetos" else "secondary"):
            st.session_state.page = "projetos"
            st.rerun()
    
    with col5:
        if st.button("📊 Analytics", key="nav_anal", use_container_width=True, type="primary" if page == "analytics" else "secondary"):
            st.session_state.page = "analytics"
            st.rerun()
    
    with col6:
        st.markdown("")
    
    with col7:
        if st.button(theme_icon, key="theme_btn", use_container_width=True):
            toggle_theme()
            st.rerun()

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
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <div class="foto-wrapper">
                <div class="foto-ring"></div>
                <img src="{foto_url}" alt="Raphael Pires" class="foto">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="section-label">📊 {DADOS['titulo']}</div>
        <h1 class="hero-title">Raphael <span class="gradient">Pires</span></h1>
        <p class="hero-subtitle">{PERFIL}</p>
        <div class="hero-quote">{CITACAO}</div>
        <div>
            <span class="badge">📍 {DADOS['localizacao']}</span>
            <span class="badge">🏠 {DADOS['modalidades'][0]}</span>
            <span class="badge">✈️ {DADOS['modalidades'][1]}</span>
        </div>
        <div style="margin-top: 2rem; display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <a href="#experiencia" class="btn-primary">💼 Ver Experiência</a>
            {cv_button}
            <a href="{LINKS['linkedin']}" target="_blank" class="btn-secondary">💼 LinkedIn</a>
        </div>
        """, unsafe_allow_html=True)

def render_sobre():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">👤 Quem sou eu</span>
        <h2 class="section-title">Minha História</h2>
    </div>
    """, unsafe_allow_html=True)
    
    valores_html = ""
    for v in SOBRE_MIM['valores']:
        valores_html += f"""
        <div class="valor-card">
            <div class="valor-icon">{v['icone']}</div>
            <div class="valor-title">{v['titulo']}</div>
            <div class="valor-desc">{v['desc']}</div>
        </div>
        """
    
    st.markdown(f"""
    <div class="sobre-section">
        <p class="sobre-text">{SOBRE_MIM['texto']}</p>
        <div class="valores-grid">{valores_html}</div>
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
                            <div class="tech-icon">{dados['icone']}</div>
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
        font=dict(color=st.session_state.theme == "dark" and "#F1F5F9" or "#0F172A")
    )
    fig.update_traces(textposition="outside")
    
    st.plotly_chart(fig, use_container_width=True)

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
                <div>{cursos_html}</div>
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
            link = f'<a href="{p["url"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Ver</a>' if p.get("url") else f'<a href="{LINKS["github"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">💻 GitHub</a>'
            
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
    <div style="text-align: center; padding: 2rem 0;">
        <div style="display:inline-flex;align-items:center;gap:0.6rem;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.25);padding:0.4rem 1.2rem;border-radius:999px;font-size:0.82rem;font-weight:600;color:#22C55E;margin-bottom:1.5rem;">
            <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#22C55E;"></span>
            Disponível para oportunidades
        </div>
        <h2 style="font-size:2rem;font-weight:800;background:linear-gradient(135deg, #3B82F6, #0EA5E9);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:0.5rem;">Vamos conversar?</h2>
        <p style="color:#94A3B8;font-size:1.05rem;margin-bottom:2rem;">Se busca alguém que entende de negócio E de dados, vamos tomar um café.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f'<a href="{LINKS["linkedin"]}" target="_blank" class="footer-link">💼 LinkedIn</a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<a href="{LINKS["github"]}" target="_blank" class="footer-link">💻 GitHub</a>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<a href="{LINKS["email"]}" class="footer-link">✉️ E-mail</a>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<a href="{LINKS["whatsapp"]}" target="_blank" class="footer-link">📱 WhatsApp</a>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<a href="tel:{tel}" class="footer-link">📞 {DADOS["contato"]["telefone1"]}</a>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <p class="footer-copy">© 2026 {DADOS['nome']} · Feito com ❤️ e Streamlit</p>
    """, unsafe_allow_html=True)
    
    st.markdown('<a href="#topo" class="scroll-top">↑</a>', unsafe_allow_html=True)

def render_analytics():
    st.markdown("""
    <div style="padding:2rem 0;text-align:center;">
        <h1 class="hero-title">📊 Analytics Interativo</h1>
        <p class="hero-subtitle" style="margin: 0 auto;">Dashboards em Streamlit + Plotly</p>
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
                st.plotly_chart(fig1, use_container_width=True)
            with col_b:
                fig2 = px.histogram(filtro, x="Status", color="Status",
                                   template="plotly_dark" if st.session_state.theme == "dark" else "plotly_white")
                fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380, showlegend=False)
                st.plotly_chart(fig2, use_container_width=True)

# ============================================================================
# MAIN
# ============================================================================
def main():
    st.markdown(get_css(), unsafe_allow_html=True)
    
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
