"""
app.py - Portfólio Raphael Pires - Streamlit
Arquivo único e completo - Sem erros
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import base64
from datetime import datetime, timedelta

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
# FUNÇÕES AUXILIARES - IMAGEM E PDF
# ============================================================================
def get_foto_path():
    """Busca o caminho da foto em vários locais possíveis"""
    candidatos = [
        "assets/rapha.jpeg", "assets/rapha.jpg",
        "rapha.jpeg", "rapha.jpg",
        "foto.jpeg", "foto.jpg",
        "perfil.jpeg", "perfil.jpg",
        "assets/foto.jpeg", "assets/foto.jpg"
    ]
    for caminho in candidatos:
        if os.path.exists(caminho):
            return caminho
    return None

def get_foto_base64(foto_path):
    """Converte imagem para base64"""
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
    """Busca o caminho do PDF"""
    candidatos = [
        "Curriculo_Raphael_v2.pdf",
        "Curriculo_Raphael.pdf",
        "cv.pdf",
        "assets/Curriculo_Raphael_v2.pdf",
        "assets/Curriculo_Raphael.pdf",
    ]
    for caminho in candidatos:
        if os.path.exists(caminho):
            return caminho
    return None

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

KPIS = [
    {"valor": "70%", "label": "Redução tempo operacional", "contexto": "Banco do Brasil", "icone": "⚡"},
    {"valor": "2h→15min", "label": "Ciclo de análise", "contexto": "Relatórios comerciais", "icone": "⏱️"},
    {"valor": "213 mil+", "label": "Registros analisados", "contexto": "Projeto CNPq", "icone": "📊"},
    {"valor": "16 anos", "label": "Experiência profissional", "contexto": "Acumulada", "icone": "🏆"}
]

TECH_STACK = {
    "POWER BI": {"itens": ["Dashboards", "KPIs", "DAX", "Power Query"], "icone": "📊", "nivel": "Expert"},
    "SQL": {"itens": ["PostgreSQL", "Consultas", "Modelagem"], "icone": "🗄️", "nivel": "Expert"},
    "PYTHON": {"itens": ["Pandas", "NumPy", "Scikit-learn", "Statsmodels"], "icone": "🐍", "nivel": "Avançado"},
    "VISUALIZAÇÃO": {"itens": ["Plotly", "Streamlit", "Looker Studio"], "icone": "📈", "nivel": "Avançado"},
    "ETL": {"itens": ["Coleta", "Limpeza", "Transformação", "Carga"], "icone": "🔄", "nivel": "Expert"},
    "CLOUD": {"itens": ["AWS Educate", "Fundamentos Cloud"], "icone": "☁️", "nivel": "Intermediário"},
    "FERRAMENTAS": {"itens": ["Excel/VBA", "Git", "IA Generativa"], "icone": "🛠️", "nivel": "Expert"}
}

CERTIFICACOES = [
    {
        "instituicao": "Hashtag Treinamentos",
        "cursos": ["SQL Avançado", "Power BI", "Python para Análise de Dados", "Algoritmos e IA Aplicada"],
        "status": "Concluído",
        "icone": "📘"
    },
    {
        "instituicao": "AWS Educate",
        "cursos": ["Cloud Computing", "Cloud 101", "AWS Console", "Storage", "ML Foundations", "Sustainability", "Cloud Support"],
        "status": "Em andamento (40%)",
        "icone": "☁️",
        "modulos": 8
    }
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
        "nome": "Desenrola Brasil — Painel Analítico",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "url": "https://desenrolabrasil.streamlit.app",
        "descricao": "Processamento de dados oficiais do Banco Central com KPIs, séries temporais e análise de concentração de mercado (HHI).",
        "icone": "🇧🇷"
    },
    {
        "nome": "CNPq Analytics — Investimentos",
        "tech": ["Python", "Pandas", "Plotly", "PostgreSQL"],
        "url": "https://cnpq-analytics.streamlit.app",
        "descricao": "ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos.",
        "icone": "🔬"
    },
    {
        "nome": "Dashboard ANP — Combustíveis",
        "tech": ["Python", "Pandas", "Plotly"],
        "url": None,
        "descricao": "Dashboard interativo com filtros temporais e regionais utilizando dados oficiais da ANP.",
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
# CSS - ESTILOS
# ============================================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #0B0F1A;
    color: #F1F5F9;
}

#MainMenu, header, footer, .stDeployButton { display: none !important; }
.stApp { background: #0B0F1A; }
.block-container { padding: 0 !important; max-width: 100%; }

/* NAVBAR */
.navbar {
    position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
    background: rgba(11,15,26,0.9);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255,255,255,0.06);
    padding: 1rem 2.5rem;
    display: flex; align-items: center; justify-content: space-between;
}
.navbar-brand {
    font-weight: 800; font-size: 1.3rem; color: #F1F5F9;
    text-decoration: none; display: flex; align-items: center; gap: 0.5rem;
}
.navbar-brand .dot {
    width: 10px; height: 10px; border-radius: 50%;
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    box-shadow: 0 0 12px #3B82F6;
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.2); } }
.navbar-brand span {
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.navbar-links { display: flex; gap: 0.5rem; align-items: center; }
.nav-link {
    padding: 0.5rem 1.1rem; border-radius: 999px; font-size: 0.875rem;
    font-weight: 500; text-decoration: none; transition: all 0.25s;
    color: #94A3B8; background: transparent; cursor: pointer;
}
.nav-link:hover { background: rgba(255,255,255,0.06); color: #F1F5F9; }
.nav-link.active {
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    color: white !important;
}
.theme-toggle {
    width: 40px; height: 40px; border-radius: 50%;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; transition: all 0.3s; font-size: 1.2rem; margin-left: 0.5rem;
}
.theme-toggle:hover { transform: rotate(360deg); border-color: #3B82F6; }

/* HERO */
.hero {
    min-height: 85vh; display: flex; align-items: center; justify-content: center;
    padding: 7rem 2rem 3rem;
    background: radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.1) 0%, transparent 70%);
    position: relative;
}
.hero-content {
    max-width: 1200px; width: 100%;
    display: grid; grid-template-columns: auto 1fr; gap: 4rem;
    align-items: center;
}
@media (max-width: 900px) { .hero-content { grid-template-columns: 1fr; text-align: center; } }
.foto-wrapper { position: relative; width: 260px; height: 260px; }
.foto-ring {
    position: absolute; inset: -12px; border-radius: 50%;
    background: conic-gradient(#3B82F6, #0EA5E9, #8B5CF6, #3B82F6);
    animation: rotate 8s linear infinite; opacity: 0.6;
}
.foto-ring::after {
    content: ''; position: absolute; inset: 4px; border-radius: 50%; background: #0B0F1A;
}
@keyframes rotate { to { transform: rotate(360deg); } }
.foto {
    position: relative; z-index: 2; width: 260px; height: 260px; border-radius: 50%;
    object-fit: cover; border: 4px solid #0B0F1A;
    box-shadow: 0 25px 80px rgba(59,130,246,0.3);
}
.hero h1 { font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem; }
.hero h1 .gradient {
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero .tag {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: rgba(59,130,246,0.15); border: 1px solid rgba(59,130,246,0.25);
    padding: 0.35rem 1rem; border-radius: 999px;
    font-size: 0.8rem; font-weight: 600; color: #3B82F6;
    margin-bottom: 1rem;
}
.hero .subtitle {
    font-size: 1.1rem; color: #94A3B8; margin: 0.5rem 0 1.5rem; line-height: 1.7;
}
.hero .badges { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; }
.badge {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    padding: 0.4rem 0.9rem; border-radius: 10px;
    font-size: 0.78rem; font-weight: 500; transition: all 0.2s;
}
.badge:hover { border-color: #3B82F6; transform: translateY(-2px); }
.cta { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 2rem; }
.btn-primary {
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    color: white !important; padding: 0.75rem 1.75rem; border-radius: 12px;
    font-weight: 600; text-decoration: none;
    display: inline-flex; align-items: center; gap: 0.5rem;
    box-shadow: 0 4px 16px rgba(59,130,246,0.3); transition: all 0.25s;
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(59,130,246,0.45); }
.btn-secondary {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    padding: 0.75rem 1.75rem; border-radius: 12px;
    font-weight: 600; color: #F1F5F9 !important;
    text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem;
    transition: all 0.25s;
}
.btn-secondary:hover { border-color: #3B82F6; transform: translateY(-2px); }

/* SECTIONS */
.section {
    padding: 5rem 2rem; background: rgba(11,15,26,0.6);
    backdrop-filter: blur(8px); border-top: 1px solid rgba(255,255,255,0.08);
}
.section.alt { background: rgba(255,255,255,0.02); }
.container { max-width: 1200px; margin: 0 auto; }
.section-header { text-align: center; margin-bottom: 3.5rem; }
.section-header .label {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: rgba(59,130,246,0.15); border: 1px solid rgba(59,130,246,0.25);
    padding: 0.35rem 1.1rem; border-radius: 999px;
    font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.1em; color: #3B82F6; margin-bottom: 1rem;
}
.section-header h2 { font-size: 2.5rem; font-weight: 800; margin-top: 0.5rem; }
.section-header p { color: #94A3B8; max-width: 600px; margin: 1rem auto 0; }

/* KPIs */
.kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; }
@media (max-width: 1024px) { .kpi-grid { grid-template-columns: repeat(2, 1fr); } }
.kpi-card {
    background: rgba(255,255,255,0.04); backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08); border-radius: 20px;
    padding: 1.75rem 1.5rem; text-align: center; transition: all 0.3s;
}
.kpi-card:hover { transform: translateY(-6px); border-color: #3B82F6; }
.kpi-icon {
    width: 48px; height: 48px; border-radius: 14px;
    background: rgba(59,130,246,0.15);
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 1rem; font-size: 1.4rem;
}
.kpi-value {
    font-size: 2rem; font-weight: 800;
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0.35rem;
}
.kpi-label { font-size: 0.82rem; color: #94A3B8; font-weight: 500; }
.kpi-context { font-size: 0.75rem; color: #64748B; margin-top: 0.25rem; }

/* TECH */
.tech-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
.tech-card {
    background: rgba(255,255,255,0.04); backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08); border-radius: 20px;
    padding: 1.75rem; transition: all 0.3s;
}
.tech-card:hover { transform: translateY(-4px); border-color: #3B82F6; }
.tech-header { display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }
.tech-icon {
    width: 56px; height: 56px; border-radius: 16px;
    background: rgba(59,130,246,0.15);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.8rem;
}
.tech-name { font-size: 1.1rem; font-weight: 700; }
.tech-level {
    font-size: 0.72rem; font-weight: 600;
    padding: 0.2rem 0.6rem; border-radius: 999px; display: inline-block;
}
.tech-level.expert { background: rgba(34,197,94,0.15); color: #22C55E; }
.tech-level.avancado { background: rgba(59,130,246,0.15); color: #3B82F6; }
.tech-level.intermediario { background: rgba(245,158,11,0.15); color: #F59E0B; }
.tech-items { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.tech-item {
    font-size: 0.78rem; background: rgba(59,130,246,0.12);
    border: 1px solid rgba(59,130,246,0.25);
    padding: 0.25rem 0.7rem; border-radius: 8px;
    color: #3B82F6; font-weight: 500;
}

/* TIMELINE */
.timeline { position: relative; padding: 2rem 0; }
.timeline::before {
    content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
    width: 2px; background: linear-gradient(to bottom, #3B82F6, #0EA5E9, transparent);
}
.timeline-item { position: relative; padding-left: 80px; margin-bottom: 2.5rem; }
.timeline-dot {
    position: absolute; left: 20px; top: 8px; width: 18px; height: 18px;
    border-radius: 50%; background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    border: 3px solid #0B0F1A; box-shadow: 0 0 0 4px #3B82F6; z-index: 2;
}
.timeline-card {
    background: rgba(255,255,255,0.04); backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08); border-radius: 20px;
    padding: 1.75rem; transition: all 0.3s;
}
.timeline-card:hover { border-color: #3B82F6; transform: translateX(8px); }
.timeline-date {
    display: inline-block; font-size: 0.72rem; font-weight: 700;
    background: rgba(59,130,246,0.15); color: #3B82F6;
    padding: 0.25rem 0.9rem; border-radius: 999px;
}
.timeline-badge {
    background: linear-gradient(135deg, #3B82F6, #0EA5E9); color: white;
    font-size: 0.62rem; font-weight: 800; padding: 0.2rem 0.7rem;
    border-radius: 999px; margin-left: 0.5rem;
}
.timeline-role { font-size: 1.2rem; font-weight: 700; margin: 0.5rem 0 0.2rem; }
.timeline-company { color: #0EA5E9; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.75rem; }
.timeline-desc { color: #94A3B8; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.75rem; }
.timeline-tag {
    font-size: 0.72rem; background: rgba(59,130,246,0.12);
    border: 1px solid rgba(59,130,246,0.25);
    padding: 0.25rem 0.7rem; border-radius: 8px;
    display: inline-block; margin: 0.2rem; color: #3B82F6; font-weight: 600;
}

/* PROJECTS */
.project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; }
.project-card {
    background: rgba(255,255,255,0.04); backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08); border-radius: 24px;
    padding: 2rem; transition: all 0.3s; position: relative; overflow: hidden;
}
.project-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0;
    height: 3px; background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    transform: scaleX(0); transform-origin: left; transition: transform 0.4s;
}
.project-card:hover { transform: translateY(-8px); border-color: #3B82F6; }
.project-card:hover::before { transform: scaleX(1); }
.project-icon {
    width: 64px; height: 64px; border-radius: 18px;
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.8rem; margin-bottom: 1.25rem;
}
.project-card h3 { font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem; }
.project-card p { color: #94A3B8; line-height: 1.65; font-size: 0.92rem; margin-bottom: 1rem; }
.project-tech { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.25rem; }
.project-tag {
    font-size: 0.7rem; background: rgba(59,130,246,0.12);
    border: 1px solid rgba(59,130,246,0.25);
    padding: 0.2rem 0.6rem; border-radius: 6px; color: #3B82F6; font-weight: 600;
}

/* FOOTER */
.footer {
    padding: 4rem 2rem 2.5rem; text-align: center;
    border-top: 1px solid rgba(255,255,255,0.08);
    background: rgba(255,255,255,0.04); backdrop-filter: blur(12px);
}
.footer h3 {
    font-size: 2rem; font-weight: 800;
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.footer-links {
    display: flex; justify-content: center; flex-wrap: wrap;
    gap: 0.6rem; margin: 2rem 0 1.5rem;
}
.footer-link {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    padding: 0.6rem 1.25rem; border-radius: 12px;
    color: #F1F5F9 !important; text-decoration: none;
    font-size: 0.88rem; font-weight: 500;
    display: inline-flex; align-items: center; gap: 0.4rem;
    transition: all 0.25s;
}
.footer-link:hover {
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    color: white !important; border-color: transparent;
    transform: translateY(-2px);
}
.footer-copy { color: #64748B; font-size: 0.8rem; margin-top: 1.5rem; }

.scroll-top {
    position: fixed; bottom: 2rem; right: 2rem;
    width: 48px; height: 48px; border-radius: 50%;
    background: linear-gradient(135deg, #3B82F6, #0EA5E9);
    color: white; display: flex; align-items: center; justify-content: center;
    font-size: 1.2rem; cursor: pointer;
    box-shadow: 0 8px 24px rgba(59,130,246,0.35);
    transition: all 0.25s; z-index: 999; text-decoration: none;
}
.scroll-top:hover { transform: translateY(-4px); }

@media (max-width: 768px) {
    .navbar { padding: 0.75rem 1rem; }
    .hero { padding: 6rem 1rem 2rem; min-height: auto; }
    .hero h1 { font-size: 2.2rem; }
    .foto-wrapper { width: 200px; height: 200px; }
    .foto { width: 200px; height: 200px; }
    .section { padding: 3rem 1rem; }
    .section-header h2 { font-size: 1.8rem; }
}
</style>
"""

# ============================================================================
# RENDERIZAÇÃO - HTML COM unsafe_allow_html=True
# ============================================================================
def render_navbar(page):
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    nome = DADOS["nome"].split()
    html = f"""
    <nav class="navbar">
        <a href="/?page=home" class="navbar-brand">
            <span class="dot"></span>
            {nome[0]} <span>{nome[-1]}</span>
        </a>
        <div class="navbar-links">
            <a href="/?page=home" class="nav-link {'active' if page == 'home' else ''}">Início</a>
            <a href="/?page=curriculo" class="nav-link {'active' if page == 'curriculo' else ''}">Currículo</a>
            <a href="/?page=projetos" class="nav-link {'active' if page == 'projetos' else ''}">Projetos</a>
            <a href="/?page=analytics" class="nav-link {'active' if page == 'analytics' else ''}">Analytics</a>
            <a href="#contato" class="nav-link">Contato</a>
            <div class="theme-toggle" onclick="window.location.href='?theme_toggle=1&page={page}'">{theme_icon}</div>
        </div>
    </nav>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_hero():
    foto_path = get_foto_path()
    foto_b64 = get_foto_base64(foto_path)
    foto_url = foto_b64 if foto_b64 else "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=3B82F6&color=fff&bold=true"
    
    html = f"""
    <section class="hero">
        <div class="hero-content">
            <div class="foto-wrapper">
                <div class="foto-ring"></div>
                <img src="{foto_url}" alt="Raphael Pires" class="foto">
            </div>
            <div>
                <div class="tag">📊 {DADOS['titulo']}</div>
                <h1>Raphael <span class="gradient">Pires</span></h1>
                <p class="subtitle">{PERFIL}</p>
                <div class="badges">
                    <span class="badge">📍 {DADOS['localizacao']}</span>
                    <span class="badge">🏠 {DADOS['modalidades'][0]}</span>
                    <span class="badge">✈️ {DADOS['modalidades'][1]}</span>
                </div>
                <div class="cta">
                    <a href="#experiencia" class="btn-primary">💼 Ver Experiência</a>
                    <a href="{LINKS['linkedin']}" target="_blank" class="btn-secondary">💼 LinkedIn</a>
                </div>
            </div>
        </div>
    </section>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_kpis():
    kpis_html = ""
    for kpi in KPIS:
        kpis_html += f"""
        <div class="kpi-card">
            <div class="kpi-icon">{kpi['icone']}</div>
            <div class="kpi-value">{kpi['valor']}</div>
            <div class="kpi-label">{kpi['label']}</div>
            <div class="kpi-context">{kpi['contexto']}</div>
        </div>
        """
    
    html = f"""
    <div class="section">
        <div class="container">
            <div class="section-header">
                <span class="label">📈 Impacto</span>
                <h2>Números que contam histórias</h2>
                <p>Resultados concretos de mais de uma década</p>
            </div>
            <div class="kpi-grid">{kpis_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_tech():
    techs_html = ""
    for tech, dados in TECH_STACK.items():
        nivel_class = dados['nivel'].lower().replace('í', 'i').replace('á', 'a')
        itens = "".join([f'<span class="tech-item">{i}</span>' for i in dados['itens']])
        
        techs_html += f"""
        <div class="tech-card">
            <div class="tech-header">
                <div class="tech-icon">{dados['icone']}</div>
                <div>
                    <div class="tech-name">{tech}</div>
                    <span class="tech-level {nivel_class}">{dados['nivel']}</span>
                </div>
            </div>
            <div class="tech-items">{itens}</div>
        </div>
        """
    
    html = f"""
    <div class="section alt">
        <div class="container">
            <div class="section-header">
                <span class="label">⚡ Tech Stack</span>
                <h2>Ferramentas que domino</h2>
            </div>
            <div class="tech-grid">{techs_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_experiencias():
    timeline_html = ""
    for exp in EXPERIENCIAS:
        badge = f'<span class="timeline-badge">{exp["status"]}</span>' if exp.get("status") else ""
        desc = "<br>".join([f"• {d}" for d in exp["descricao"]])
        tags = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        
        timeline_html += f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp['periodo']}</span> {badge}
                <div class="timeline-role">{exp['cargo']}</div>
                <div class="timeline-company">{exp['empresa']} · {exp['tipo']}</div>
                <div class="timeline-desc">{desc}</div>
                <div>{tags}</div>
            </div>
        </div>
        """
    
    html = f"""
    <div class="section" id="experiencia">
        <div class="container">
            <div class="section-header">
                <span class="label">💼 Trajetória</span>
                <h2>Experiência profissional</h2>
            </div>
            <div class="timeline">{timeline_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_projetos():
    projetos_html = ""
    for p in PROJETOS:
        techs = "".join([f'<span class="project-tag">{t}</span>' for t in p["tech"]])
        link = f'<a href="{p["url"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Ver</a>' if p.get("url") else f'<a href="{LINKS["github"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">💻 GitHub</a>'
        
        projetos_html += f"""
        <div class="project-card">
            <div class="project-icon">{p['icone']}</div>
            <h3>{p['nome']}</h3>
            <p>{p['descricao']}</p>
            <div class="project-tech">{techs}</div>
            {link}
        </div>
        """
    
    html = f"""
    <div class="section alt">
        <div class="container">
            <div class="section-header">
                <span class="label">🚀 Projetos</span>
                <h2>Analytics na prática</h2>
            </div>
            <div class="project-grid">{projetos_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_footer():
    tel = DADOS['contato']['telefone1'].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    
    html = f"""
    <div class="footer" id="contato">
        <div style="display:inline-flex;align-items:center;gap:0.6rem;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.25);padding:0.4rem 1.2rem;border-radius:999px;font-size:0.82rem;font-weight:600;color:#22C55E;margin-bottom:1.5rem;">
            <span style="width:8px;height:8px;border-radius:50%;background:#22C55E;animation:pulse 2s infinite;"></span>
            Disponível para oportunidades
        </div>
        <h3>Vamos conversar?</h3>
        <p style="color:#94A3B8;font-size:1.05rem;margin-bottom:2rem;">Se busca alguém que entende de negócio E de dados, vamos tomar um café.</p>
        
        <div style="display:flex;justify-content:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:2rem;">
            <span style="background:rgba(59,130,246,0.12);border:1px solid rgba(59,130,246,0.25);padding:0.4rem 1rem;border-radius:999px;font-size:0.82rem;">📍 {DADOS['localizacao']}</span>
            <span style="background:rgba(59,130,246,0.12);border:1px solid rgba(59,130,246,0.25);padding:0.4rem 1rem;border-radius:999px;font-size:0.82rem;">🏠 {DADOS['modalidades'][0]}</span>
        </div>
        
        <div class="footer-links">
            <a href="{LINKS['linkedin']}" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="{LINKS['github']}" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="{LINKS['email']}" class="footer-link">✉️ E-mail</a>
            <a href="{LINKS['whatsapp']}" target="_blank" class="footer-link">📱 WhatsApp</a>
            <a href="tel:{tel}" class="footer-link">📞 {DADOS['contato']['telefone1']}</a>
        </div>
        
        <p class="footer-copy">© 2026 {DADOS['nome']} · Feito com ❤️ e Streamlit</p>
    </div>
    <a href="#topo" class="scroll-top">↑</a>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_analytics():
    st.markdown("""
    <div style="padding:7rem 2rem 2rem;text-align:center;">
        <h1 style="font-size:2.5rem;font-weight:800;margin-bottom:0.5rem;">📊 Analytics Interativo</h1>
        <p style="color:#94A3B8;font-size:1.05rem;">Dashboards em Streamlit + Plotly</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="padding:2rem;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)
    
    tabs = st.tabs(["🇧 Desenrola Brasil", "⛽ ANP", "📈 Impacto"])
    
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
        reg = col1.multiselect("Região", regioes, default=regioes)
        stat = col2.multiselect("Status", status, default=status)
        filtro = df[df["Região"].isin(reg) & df["Status"].isin(stat)]
        
        if not filtro.empty:
            k1, k2, k3 = st.columns(3)
            k1.metric("Contratos", f"{len(filtro):,}")
            k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f} M")
            k3.metric("Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
            
            a, b = st.columns(2)
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=.6, template="plotly_dark")
            fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380)
            fig2 = px.histogram(filtro, x="Status", color="Status", template="plotly_dark")
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380, showlegend=False)
            a.plotly_chart(fig1, use_container_width=True)
            b.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# MAIN
# ============================================================================
def main():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    
    st.markdown(CSS, unsafe_allow_html=True)
    
    page = st.query_params.get("page", "home")
    
    if "theme_toggle" in st.query_params:
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        params = dict(st.query_params)
        params.pop("theme_toggle", None)
        st.query_params.clear()
        st.query_params.update(params)
        st.rerun()
    
    render_navbar(page)
    
    if page == "home":
        render_hero()
        render_kpis()
        render_tech()
        render_experiencias()
        render_projetos()
    elif page == "curriculo":
        render_kpis()
        render_tech()
        render_experiencias()
    elif page == "projetos":
        render_projetos()
    elif page == "analytics":
        render_analytics()
    
    render_footer()

if __name__ == "__main__":
    main()
