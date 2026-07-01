"""
app.py - Portfólio Raphael Pires - Arquivo Único e Completo
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
# DADOS DO CURRÍCULO
# ============================================================================
DADOS_PESSOAIS = {
    "nome": "Raphael Fernando S. Pires",
    "titulo": "Analista de Dados & Business Intelligence",
    "localizacao": "Volta Redonda — RJ",
    "modalidades": ["Remoto", "Disponível para viagens"],
    "telefone1": "(24) 3018-1303",
    "telefone2": "(24) 99278-9637",
    "email": "raphael_caxias@hotmail.com",
    "linkedin": "linkedin.com/in/raphael-pires-caxias",
    "github": "github.com/raphaelcaxias"
}

PERFIL_PROFISSIONAL = """
Não cheguei aos dados por acaso. Cheguei porque vivi o negócio por anos — estoque, vendas, margem, fluxo de caixa, operação. Quando aprendi Power BI, Python e SQL, não foi para seguir tendência. Foi porque finalmente tinha as ferramentas para resolver os problemas que eu já conhecia de perto.

Sou Analista de Dados e BI com formação em Sistemas de Informação, mas minha verdadeira escola foi o chão de loja, o balcão do banco, a gestão de empresas próprias. Hoje transformo essa experiência em dashboards, automações e indicadores que fazem diferença real.
"""

CITACAO_PESSOAL = "Não estou entrando em tecnologia. Estou mostrando que, durante anos, já resolvi problemas com dados — mesmo quando meu cargo não tinha 'Analista' no nome."

KPIS = [
    {"valor": "70%", "label": "Redução no tempo operacional", "contexto": "Banco do Brasil", "icone": "⚡"},
    {"valor": "2h→15min", "label": "Ciclo de análise", "contexto": "Relatórios comerciais", "icone": "⏱️"},
    {"valor": "213 mil+", "label": "Registros analisados", "contexto": "Projeto CNPq", "icone": "📊"},
    {"valor": "16 anos", "label": "De experiência real", "contexto": "Vivendo o negócio", "icone": "🏆"}
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
        "cursos": ["Cloud Computing", "Cloud 101", "AWS Console", "Storage", "ML Foundations", "Sustainability"],
        "status": "Em andamento (40%)",
        "icone": "☁️",
        "modulos_concluidos": 8
    }
]

FORMACAO = [
    {"curso": "Sistemas de Informação", "instituicao": "UniFOA", "ano": "2010"},
    {"curso": "Técnico em Informática", "instituicao": "CIBA", "ano": "2005"}
]

IDIOMAS = [
    {"idioma": "Português", "nivel": "Nativo"},
    {"idioma": "Inglês", "nivel": "Leitura técnica"}
]

PROJETOS = [
    {
        "nome": "Desenrola Brasil",
        "subtitulo": "Painel Analítico Executivo",
        "tecnologias": ["Python", "Pandas", "Plotly", "Streamlit"],
        "url": "https://desenrolabrasil.streamlit.app",
        "descricao": ["Dados oficiais do Banco Central com KPIs e análise de concentração de mercado.", "Segmentação de perfis via clusterização."],
        "icone": "🇧",
        "contexto": "Entender o impacto real do programa no Brasil"
    },
    {
        "nome": "CNPq Analytics",
        "subtitulo": "Investimentos em Pesquisa",
        "tecnologias": ["Python", "Pandas", "Plotly", "PostgreSQL"],
        "url": "https://cnpq-analytics.streamlit.app",
        "descricao": ["213 mil bolsas e R$ 1,2 bi analisados.", "Dashboard que evidencia desigualdades regionais."],
        "icone": "🔬",
        "contexto": "Mostrar para onde vai o dinheiro da pesquisa"
    },
    {
        "nome": "Dashboard ANP",
        "subtitulo": "Preços de Combustíveis",
        "tecnologias": ["Python", "Pandas", "Plotly"],
        "url": None,
        "descricao": ["Dados da ANP com filtros temporais e regionais.", "Transparência em dados públicos."],
        "icone": "⛽",
        "contexto": "Todo cidadão merece entender o que paga"
    }
]

EXPERIENCIAS = [
    {
        "cargo": "Fundador & Analista de Dados",
        "empresa": "Jardim do Éden — Varejo de Moda",
        "tipo": "Empresa Própria",
        "periodo": "2009 — Atual",
        "status": "Consultiva",
        "historia": "Muita gente vê 'dono de loja'. Mas estruturei a base de dados do zero, criei dashboards, automatizei processos. Reduzi análises de 2h para 15min. Foi aqui que desenvolvi meu BI de verdade.",
        "tags": ["SQL", "Python", "Power BI", "Looker Studio", "IA Generativa"]
    },
    {
        "cargo": "Fundador & Analista de KPIs",
        "empresa": "J Sintonía — Varejo Especializado",
        "tipo": "Empresa Própria",
        "periodo": "2014 — maio 2026",
        "status": "Encerrado",
        "historia": "Trabalhei com KPIs, viabilidade econômica, planejamento. O encerramento foi baseado em análise de dados, não em impulso. Maturidade de quem decide com evidência.",
        "tags": ["KPIs", "Dashboards", "Análise Econômica"]
    },
    {
        "cargo": "Estagiário de Automação e Dados",
        "empresa": "Banco do Brasil S.A.",
        "tipo": "Estágio",
        "periodo": "2008 — 2010",
        "status": None,
        "historia": "Desenvolvi macros VBA que chegaram a 20 agências, reduzindo 70% do tempo operacional. Aqui aprendi automação de verdade em ambiente corporativo.",
        "tags": ["VBA", "Automação", "SQL"]
    },
    {
        "cargo": "Auxiliar de Dados & Operações",
        "empresa": "NSM Comércio",
        "tipo": "CLT",
        "periodo": "2002 — 2009",
        "status": None,
        "historia": "Centralizei registros de estoque de 7 unidades, eliminando inconsistências. Aqui desenvolvi minha visão operacional.",
        "tags": ["Operações", "Estoque", "Dados"]
    },
    {
        "cargo": "Instrutor de Informática",
        "empresa": "UniFOA — Projeto de Extensão",
        "tipo": "Projeto",
        "periodo": "Jan 2006 — Dez 2007",
        "status": None,
        "historia": "Capacitei jovens em Excel avançado e lógica de programação. Descobri que tenho facilidade para transmitir conhecimento.",
        "tags": ["Excel", "Ensino", "Comunicação"]
    }
]

LINKS_SOCIAIS = {
    "linkedin": "https://www.linkedin.com/in/raphael-pires-caxias",
    "github": "https://github.com/raphaelcaxias",
    "email": "mailto:raphael_caxias@hotmail.com",
    "whatsapp": "https://wa.me/5524992789637"
}

SOBRE_MIM = {
    "titulo": "Minha História",
    "texto": "Sou de Volta Redonda, RJ. Casado com Daiane, pai da Melina.\n\nMinha trajetória não é linear — e isso é minha força. Comecei na operação, passei pelo banco, empreendi, ensinei, e agora reorganizo tudo sob a ótica de Dados e BI.\n\nNão sou quem fez curso e saiu procurando emprego. Sou alguém que viveu o negócio e agora tem as ferramentas para transformar experiência em valor.\n\nSou curioso. Quando aprendo algo, quero entender tudo. Gosto de construir, publicar, melhorar. Busco excelência, às vezes até demais.",
    "valores": [
        {"icone": "🎯", "titulo": "Resolução de Problemas", "desc": "Como isso resolve um problema real?"},
        {"icone": "🔍", "titulo": "Curiosidade", "desc": "Quero entender tudo. Não aceito a primeira versão."},
        {"icone": "🛠️", "titulo": "Construção", "desc": "Construo, publico, melhoro."},
        {"icone": "📊", "titulo": "Decisão por Dados", "desc": "Decido com evidência, não com impulso."}
    ]
}

MODOS_VISUALIZACAO = {
    "Dados & BI": {"descricao": "Foco em análise de dados, BI e dashboards", "destaques": ["POWER BI", "SQL", "PYTHON"], "ordem": [0, 1, 2, 3, 4], "cor": "#3B82F6"},
    "Desenvolvimento": {"descricao": "Foco em programação e automação", "destaques": ["PYTHON", "SQL", "ETL"], "ordem": [0, 1, 2, 3, 4], "cor": "#8B5CF6"},
    "Indústria & Gestão": {"descricao": "Foco em operações e processos", "destaques": ["POWER BI", "SQL", "ETL"], "ordem": [3, 2, 0, 1, 4], "cor": "#10B981"},
    "Empreendedorismo": {"descricao": "Foco em gestão de negócios", "destaques": ["POWER BI", "SQL", "PYTHON"], "ordem": [0, 1, 2, 3, 4], "cor": "#F59E0B"}
}

# ============================================================================
# CORES E CSS
# ============================================================================
TEMA_DARK = {
    "primary": "#3B82F6", "secondary": "#0EA5E9", "accent": "#8B5CF6",
    "success": "#22C55E", "warning": "#F59E0B",
    "bg": "#0B0F1A", "text": "#F1F5F9", "text_muted": "#94A3B8", "text_subtle": "#64748B",
    "card_bg": "rgba(255,255,255,0.04)", "border": "rgba(255,255,255,0.08)",
    "tag_bg": "rgba(59,130,246,0.12)", "tag_border": "rgba(59,130,246,0.25)",
    "primary_light": "rgba(59,130,246,0.15)",
    "navbar_bg": "rgba(11,15,26,0.85)", "navbar_border": "rgba(255,255,255,0.06)",
    "nav_hover": "rgba(255,255,255,0.06)",
    "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.1) 0%, transparent 70%)",
    "section_bg": "rgba(11,15,26,0.6)", "section_alt_bg": "rgba(255,255,255,0.02)",
    "shadow": "0 8px 32px rgba(0,0,0,0.4)", "shadow_hover": "0 16px 48px rgba(59,130,246,0.25)",
    "plotly_template": "plotly_dark",
    "chart_colors": ["#3B82F6", "#0EA5E9", "#8B5CF6", "#22C55E", "#F59E0B"],
    "gradient_primary": "linear-gradient(135deg, #3B82F6 0%, #0EA5E9 100%)",
    "gradient_text": "linear-gradient(135deg, #3B82F6 0%, #0EA5E9 50%, #8B5CF6 100%)"
}

TEMA_LIGHT = {
    "primary": "#1D4ED8", "secondary": "#0EA5E9", "accent": "#7C3AED",
    "success": "#16A34A", "warning": "#D97706",
    "bg": "#F8FAFC", "text": "#0F172A", "text_muted": "#475569", "text_subtle": "#94A3B8",
    "card_bg": "rgba(255,255,255,0.8)", "border": "rgba(0,0,0,0.06)",
    "tag_bg": "#DBEAFE", "tag_border": "#93C5FD",
    "primary_light": "#DBEAFE",
    "navbar_bg": "rgba(248,250,252,0.9)", "navbar_border": "rgba(0,0,0,0.06)",
    "nav_hover": "rgba(0,0,0,0.04)",
    "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.06) 0%, transparent 70%)",
    "section_bg": "rgba(255,255,255,0.6)", "section_alt_bg": "rgba(0,0,0,0.01)",
    "shadow": "0 8px 32px rgba(0,0,0,0.08)", "shadow_hover": "0 16px 48px rgba(29,78,216,0.12)",
    "plotly_template": "plotly_white",
    "chart_colors": ["#1D4ED8", "#0EA5E9", "#7C3AED", "#16A34A", "#D97706"],
    "gradient_primary": "linear-gradient(135deg, #1D4ED8 0%, #0EA5E9 100%)",
    "gradient_text": "linear-gradient(135deg, #1D4ED8 0%, #0EA5E9 50%, #7C3AED 100%)"
}

def get_colors():
    return TEMA_DARK if st.session_state.get("theme", "dark") == "dark" else TEMA_LIGHT

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def get_css(colors):
    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        :root {{
            --primary: {colors['primary']}; --secondary: {colors['secondary']}; --accent: {colors['accent']};
            --success: {colors['success']}; --warning: {colors['warning']};
            --bg: {colors['bg']}; --text: {colors['text']}; --text-muted: {colors['text_muted']};
            --text-subtle: {colors['text_subtle']}; --card-bg: {colors['card_bg']};
            --border: {colors['border']}; --tag-bg: {colors['tag_bg']}; --tag-border: {colors['tag_border']};
            --primary-light: {colors['primary_light']}; --navbar-bg: {colors['navbar_bg']};
            --navbar-border: {colors['navbar_border']}; --nav-hover: {colors['nav_hover']};
            --hero-bg: {colors['hero_bg']}; --section-bg: {colors['section_bg']};
            --section-alt-bg: {colors['section_alt_bg']}; --shadow: {colors['shadow']};
            --shadow-hover: {colors['shadow_hover']};
            --gradient-primary: {colors['gradient_primary']}; --gradient-text: {colors['gradient_text']};
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); }}
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: var(--bg); }}
        .block-container {{ padding: 0 !important; max-width: 100%; }}
        
        .navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
            background: var(--navbar-bg); backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--navbar-border);
            padding: 0.875rem 2.5rem; display: flex; align-items: center; justify-content: space-between;
        }}
        .navbar-brand {{
            font-weight: 800; font-size: 1.3rem; color: var(--text);
            text-decoration: none; display: flex; align-items: center; gap: 0.5rem;
        }}
        .navbar-brand .brand-dot {{
            width: 10px; height: 10px; border-radius: 50%;
            background: var(--gradient-primary);
            box-shadow: 0 0 12px var(--primary);
            animation: pulse-dot 2s infinite;
        }}
        @keyframes pulse-dot {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.2); }} }}
        .navbar-brand span {{
            background: var(--gradient-text);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .navbar-links {{ display: flex; gap: 0.5rem; align-items: center; }}
        .nav-link {{
            padding: 0.5rem 1.1rem; border-radius: 999px; font-size: 0.875rem;
            font-weight: 500; text-decoration: none; transition: all 0.25s ease;
            color: var(--text-muted); background: transparent; cursor: pointer;
        }}
        .nav-link:hover {{ background: var(--nav-hover); color: var(--text); }}
        .nav-link.active {{
            background: var(--gradient-primary); color: white !important;
        }}
        .theme-toggle {{
            width: 44px; height: 44px; border-radius: 50%;
            background: var(--card-bg); border: 1px solid var(--border);
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: all 0.4s ease; font-size: 1.2rem; margin-left: 0.5rem;
        }}
        .theme-toggle:hover {{ transform: rotate(360deg) scale(1.1); }}
        
        .hero-full {{
            min-height: 85vh; display: flex; align-items: center; justify-content: center;
            padding: 7rem 2rem 3rem; background: var(--hero-bg);
            position: relative; overflow: hidden;
        }}
        .hero-content {{
            max-width: 1200px; width: 100%;
            display: grid; grid-template-columns: auto 1fr; gap: 4rem;
            align-items: center; position: relative; z-index: 2;
        }}
        @media (max-width: 900px) {{ .hero-content {{ grid-template-columns: 1fr; text-align: center; }} }}
        .hero-photo-wrapper {{ position: relative; width: 260px; height: 260px; }}
        .hero-photo-ring {{
            position: absolute; inset: -12px; border-radius: 50%;
            background: conic-gradient(var(--primary), var(--secondary), var(--accent));
            animation: rotate 8s linear infinite; opacity: 0.6;
        }}
        .hero-photo-ring::after {{
            content: ''; position: absolute; inset: 4px; border-radius: 50%; background: var(--bg);
        }}
        @keyframes rotate {{ to {{ transform: rotate(360deg); }} }}
        .hero-photo {{
            position: relative; z-index: 2; width: 260px; height: 260px; border-radius: 50%;
            object-fit: cover; border: 4px solid var(--bg);
            box-shadow: 0 25px 80px rgba(59,130,246,0.3);
        }}
        .hero-text h1 {{ font-size: 3.5rem; font-weight: 900; margin-bottom: 0.5rem; }}
        .hero-text h1 .gradient-name {{
            background: var(--gradient-text);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .hero-text .role-tag {{
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: var(--primary-light); border: 1px solid var(--tag-border);
            padding: 0.35rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 600; color: var(--primary);
            margin-bottom: 1rem;
        }}
        .hero-text .subtitle {{
            font-size: 1.1rem; color: var(--text-muted);
            margin: 0.5rem 0 1.5rem; line-height: 1.7; max-width: 600px;
            white-space: pre-line;
        }}
        .hero-quote {{
            font-style: italic; color: var(--text-subtle);
            font-size: 0.95rem; margin: 1.5rem 0;
            padding-left: 1.5rem; border-left: 3px solid var(--primary);
        }}
        .badge-group {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; }}
        .badge {{
            background: var(--card-bg); border: 1px solid var(--border);
            padding: 0.4rem 0.9rem; border-radius: 10px;
            font-size: 0.78rem; font-weight: 500; transition: all 0.2s;
        }}
        .badge:hover {{ border-color: var(--primary); transform: translateY(-2px); }}
        .cta-group {{ display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 2rem; }}
        .btn-primary {{
            background: var(--gradient-primary); color: white !important;
            padding: 0.75rem 1.75rem; border-radius: 12px;
            font-weight: 600; text-decoration: none;
            display: inline-flex; align-items: center; gap: 0.5rem;
            box-shadow: 0 4px 16px rgba(59,130,246,0.3);
            transition: all 0.25s; border: none; cursor: pointer;
        }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 28px rgba(59,130,246,0.45); }}
        .btn-secondary {{
            background: var(--card-bg); border: 1px solid var(--border);
            padding: 0.75rem 1.75rem; border-radius: 12px;
            font-weight: 600; color: var(--text) !important;
            text-decoration: none; display: inline-flex;
            align-items: center; gap: 0.5rem;
            transition: all 0.25s;
        }}
        .btn-secondary:hover {{ border-color: var(--primary); transform: translateY(-2px); }}
        
        .section-glass {{
            padding: 5rem 2rem; background: var(--section-bg);
            backdrop-filter: blur(8px); border-top: 1px solid var(--border);
        }}
        .section-glass.alt {{ background: var(--section-alt-bg); }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .section-header {{ text-align: center; margin-bottom: 3.5rem; }}
        .section-header .label {{
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: var(--primary-light); border: 1px solid var(--tag-border);
            padding: 0.35rem 1.1rem; border-radius: 999px;
            font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.1em; color: var(--primary); margin-bottom: 1rem;
        }}
        .section-header h2 {{ font-size: 2.5rem; font-weight: 800; margin-top: 0.5rem; }}
        .section-header p {{ color: var(--text-muted); max-width: 600px; margin: 1rem auto 0; }}
        
        .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; }}
        @media (max-width: 1024px) {{ .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        .kpi-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 20px;
            padding: 1.75rem 1.5rem; text-align: center;
            transition: all 0.3s; position: relative; overflow: hidden;
        }}
        .kpi-card:hover {{ transform: translateY(-6px); border-color: var(--primary); }}
        .kpi-icon {{
            width: 48px; height: 48px; border-radius: 14px;
            background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 1rem; font-size: 1.4rem;
        }}
        .kpi-value {{
            font-size: 2rem; font-weight: 800;
            background: var(--gradient-text);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 0.35rem;
        }}
        .kpi-label {{ font-size: 0.82rem; color: var(--text-muted); font-weight: 500; }}
        .kpi-context {{ font-size: 0.75rem; color: var(--text-subtle); margin-top: 0.25rem; }}
        
        .tech-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }}
        .tech-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 20px;
            padding: 1.75rem; transition: all 0.3s;
        }}
        .tech-card:hover {{ transform: translateY(-4px); border-color: var(--primary); }}
        .tech-card-header {{ display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; }}
        .tech-icon {{
            width: 56px; height: 56px; border-radius: 16px;
            background: var(--primary-light);
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem;
        }}
        .tech-name {{ font-size: 1.1rem; font-weight: 700; }}
        .tech-level {{
            font-size: 0.72rem; font-weight: 600;
            padding: 0.2rem 0.6rem; border-radius: 999px;
            display: inline-block; margin-top: 0.25rem;
        }}
        .tech-level.expert {{ background: rgba(34,197,94,0.15); color: var(--success); }}
        .tech-level.avancado {{ background: rgba(59,130,246,0.15); color: var(--primary); }}
        .tech-level.intermediario {{ background: rgba(245,158,11,0.15); color: var(--warning); }}
        .tech-items {{ display: flex; flex-wrap: wrap; gap: 0.4rem; }}
        .tech-item {{
            font-size: 0.78rem; background: var(--tag-bg);
            border: 1px solid var(--tag-border);
            padding: 0.25rem 0.7rem; border-radius: 8px;
            color: var(--primary); font-weight: 500;
        }}
        
        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
            width: 2px; background: linear-gradient(to bottom, var(--primary), var(--secondary), transparent);
        }}
        .timeline-item {{
            position: relative; padding-left: 80px; margin-bottom: 2.5rem;
        }}
        .timeline-dot {{
            position: absolute; left: 20px; top: 8px; width: 18px; height: 18px;
            border-radius: 50%; background: var(--gradient-primary);
            border: 3px solid var(--bg);
            box-shadow: 0 0 0 4px var(--primary);
            z-index: 2;
        }}
        .timeline-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 20px;
            padding: 1.75rem; transition: all 0.3s;
        }}
        .timeline-card:hover {{ border-color: var(--primary); transform: translateX(8px); }}
        .timeline-date {{
            display: inline-block; font-size: 0.72rem; font-weight: 700;
            background: var(--primary-light); color: var(--primary);
            padding: 0.25rem 0.9rem; border-radius: 999px;
        }}
        .timeline-badge {{
            background: var(--gradient-primary); color: white;
            font-size: 0.62rem; font-weight: 800; padding: 0.2rem 0.7rem;
            border-radius: 999px; margin-left: 0.5rem;
        }}
        .timeline-role {{ font-size: 1.2rem; font-weight: 700; margin: 0.5rem 0 0.2rem; }}
        .timeline-company {{ color: var(--secondary); font-weight: 600; font-size: 0.95rem; margin-bottom: 0.75rem; }}
        .timeline-historia {{ color: var(--text-muted); line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.75rem; }}
        .timeline-tag {{
            font-size: 0.72rem; background: var(--tag-bg);
            border: 1px solid var(--tag-border);
            padding: 0.25rem 0.7rem; border-radius: 8px;
            display: inline-block; margin: 0.2rem;
            color: var(--primary); font-weight: 600;
        }}
        
        .project-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; }}
        .project-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 24px;
            padding: 2rem; transition: all 0.3s; position: relative; overflow: hidden;
        }}
        .project-card::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0;
            height: 3px; background: var(--gradient-primary);
            transform: scaleX(0); transform-origin: left; transition: transform 0.4s;
        }}
        .project-card:hover {{ transform: translateY(-8px); border-color: var(--primary); }}
        .project-card:hover::before {{ transform: scaleX(1); }}
        .project-icon {{
            width: 64px; height: 64px; border-radius: 18px;
            background: var(--gradient-primary);
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem; margin-bottom: 1.25rem;
        }}
        .project-card h3 {{ font-size: 1.25rem; font-weight: 700; margin-bottom: 0.25rem; }}
        .project-card .project-subtitle {{ font-size: 0.9rem; color: var(--text-subtle); margin-bottom: 0.75rem; font-style: italic; }}
        .project-card p {{ color: var(--text-muted); line-height: 1.65; font-size: 0.92rem; margin-bottom: 0.5rem; }}
        .project-card .project-context {{
            font-size: 0.85rem; color: var(--primary);
            font-style: italic; margin-bottom: 1rem;
            padding-left: 1rem; border-left: 2px solid var(--primary);
        }}
        .project-tech {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.25rem; }}
        .project-tag {{
            font-size: 0.7rem; background: var(--tag-bg);
            border: 1px solid var(--tag-border);
            padding: 0.2rem 0.6rem; border-radius: 6px;
            color: var(--primary); font-weight: 600;
        }}
        
        .glass-card {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 24px;
            padding: 2rem; transition: all 0.3s;
        }}
        .glass-card:hover {{ transform: translateY(-6px); border-color: var(--primary); }}
        
        .progress-bar {{
            width: 100%; height: 8px;
            background: var(--border); border-radius: 999px;
            overflow: hidden; margin-top: 0.75rem;
        }}
        .progress-fill {{
            height: 100%; background: var(--gradient-primary);
            border-radius: 999px; box-shadow: 0 0 12px var(--primary);
        }}
        
        .sobre-section {{
            background: var(--card-bg); backdrop-filter: blur(12px);
            border: 1px solid var(--border); border-radius: 24px;
            padding: 2.5rem; margin: 2rem 0;
        }}
        .sobre-text {{
            font-size: 1.05rem; line-height: 1.8; color: var(--text-muted);
            white-space: pre-line; margin-bottom: 2rem;
        }}
        .valores-grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem; margin-top: 2rem;
        }}
        .valor-card {{
            background: var(--bg); border: 1px solid var(--border);
            border-radius: 16px; padding: 1.5rem; text-align: center;
            transition: all 0.3s;
        }}
        .valor-card:hover {{ transform: translateY(-4px); border-color: var(--primary); }}
        .valor-icon {{ font-size: 2.5rem; margin-bottom: 0.75rem; }}
        .valor-title {{ font-size: 1rem; font-weight: 700; color: var(--text); margin-bottom: 0.5rem; }}
        .valor-desc {{ font-size: 0.85rem; color: var(--text-muted); line-height: 1.5; }}
        
        .footer {{
            padding: 4rem 2rem 2.5rem; text-align: center;
            border-top: 1px solid var(--border);
            background: var(--card-bg); backdrop-filter: blur(12px);
        }}
        .footer h3 {{
            font-size: 2rem; font-weight: 800;
            background: var(--gradient-text);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}
        .footer-links {{
            display: flex; justify-content: center; flex-wrap: wrap;
            gap: 0.6rem; margin: 2rem 0 1.5rem;
        }}
        .footer-link {{
            background: var(--card-bg); border: 1px solid var(--border);
            padding: 0.6rem 1.25rem; border-radius: 12px;
            color: var(--text) !important; text-decoration: none;
            font-size: 0.88rem; font-weight: 500;
            display: inline-flex; align-items: center; gap: 0.4rem;
            transition: all 0.25s;
        }}
        .footer-link:hover {{
            background: var(--gradient-primary); color: white !important;
            border-color: transparent; transform: translateY(-2px);
        }}
        .footer-copy {{ color: var(--text-subtle); font-size: 0.8rem; margin-top: 1.5rem; }}
        
        .page-header {{
            padding: 7rem 2rem 2rem; text-align: center;
            background: var(--hero-bg); position: relative; overflow: hidden;
        }}
        .page-header h1 {{ font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem; }}
        .page-header p {{ color: var(--text-muted); font-size: 1.05rem; }}
        
        .scroll-top {{
            position: fixed; bottom: 2rem; right: 2rem;
            width: 48px; height: 48px; border-radius: 50%;
            background: var(--gradient-primary); color: white;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.2rem; cursor: pointer;
            box-shadow: 0 8px 24px rgba(59,130,246,0.35);
            transition: all 0.25s; z-index: 999; text-decoration: none;
        }}
        .scroll-top:hover {{ transform: translateY(-4px); }}
        
        @media (max-width: 768px) {{
            .navbar {{ padding: 0.75rem 1rem; }}
            .hero-full {{ padding: 6rem 1rem 2rem; min-height: auto; }}
            .hero-text h1 {{ font-size: 2.2rem; }}
            .hero-photo-wrapper {{ width: 200px; height: 200px; }}
            .hero-photo {{ width: 200px; height: 200px; }}
            .section-glass {{ padding: 3rem 1rem; }}
            .section-header h2 {{ font-size: 1.8rem; }}
        }}
    </style>
    """

# ============================================================================
# FUNÇÕES DE RENDERIZAÇÃO
# ============================================================================
def render_navbar(page):
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    nome = DADOS_PESSOAIS['nome'].split()
    html = f"""
    <nav class="navbar">
        <a href="/?page=home" class="navbar-brand">
            <span class="brand-dot"></span>
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
    foto_url = "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=3B82F6&color=fff"
    modo = st.session_state.get("modo", "Dados & BI")
    cor = MODOS_VISUALIZACAO[modo]["cor"]
    
    html = f"""
    <section class="hero-full">
        <div class="hero-content">
            <div class="hero-photo-wrapper">
                <div class="hero-photo-ring"></div>
                <img src="{foto_url}" alt="Raphael Pires" class="hero-photo">
            </div>
            <div class="hero-text">
                <div class="role-tag">
                    <span style="width:6px;height:6px;border-radius:50%;background:{cor};"></span>
                    {DADOS_PESSOAIS['titulo']}
                </div>
                <h1>Raphael <span class="gradient-name">Pires</span></h1>
                <p class="subtitle">{PERFIL_PROFISSIONAL.strip()}</p>
                <div class="hero-quote">{CITACAO_PESSOAL}</div>
                <div class="badge-group">
                    <span class="badge">📍 {DADOS_PESSOAIS['localizacao']}</span>
                    <span class="badge">🏠 {DADOS_PESSOAIS['modalidades'][0]}</span>
                    <span class="badge">✈️ {DADOS_PESSOAIS['modalidades'][1]}</span>
                </div>
                <div class="cta-group">
                    <a href="#experiencia" class="btn-primary">💼 Conhecer trajetória</a>
                    <a href="{LINKS_SOCIAIS['linkedin']}" target="_blank" class="btn-secondary">💼 LinkedIn</a>
                </div>
            </div>
        </div>
    </section>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_sobre():
    valores_html = ""
    for v in SOBRE_MIM['valores']:
        valores_html += f"""
        <div class="valor-card">
            <div class="valor-icon">{v['icone']}</div>
            <div class="valor-title">{v['titulo']}</div>
            <div class="valor-desc">{v['desc']}</div>
        </div>
        """
    
    html = f"""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">👤 Quem sou eu</span>
                <h2>{SOBRE_MIM['titulo']}</h2>
            </div>
            <div class="sobre-section">
                <p class="sobre-text">{SOBRE_MIM['texto']}</p>
                <div class="valores-grid">{valores_html}</div>
            </div>
        </div>
    </div>
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
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">📈 Impacto</span>
                <h2>Números que contam histórias</h2>
            </div>
            <div class="kpi-grid">{kpis_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_tech():
    modo = st.session_state.get("modo", "Dados & BI")
    destaques = MODOS_VISUALIZACAO[modo]["destaques"]
    
    techs_html = ""
    for tech, dados in TECH_STACK.items():
        nivel_class = dados['nivel'].lower().replace('í', 'i').replace('á', 'a')
        badge = "⭐ " if tech in destaques else ""
        itens = "".join([f'<span class="tech-item">{i}</span>' for i in dados['itens']])
        
        techs_html += f"""
        <div class="tech-card">
            <div class="tech-card-header">
                <div class="tech-icon">{dados['icone']}</div>
                <div>
                    <div class="tech-name">{badge}{tech}</div>
                    <span class="tech-level {nivel_class}">{dados['nivel']}</span>
                </div>
            </div>
            <div class="tech-items">{itens}</div>
        </div>
        """
    
    html = f"""
    <div class="section-glass alt">
        <div class="container">
            <div class="section-header">
                <span class="label">⚡ Tech Stack</span>
                <h2>Ferramentas que uso</h2>
            </div>
            <div class="tech-grid">{techs_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_experiencias():
    modo = st.session_state.get("modo", "Dados & BI")
    ordem = MODOS_VISUALIZACAO[modo]["ordem"]
    
    timeline_html = ""
    for idx in ordem:
        exp = EXPERIENCIAS[idx]
        badge = f'<span class="timeline-badge">{exp["status"]}</span>' if exp.get("status") else ""
        tags = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        
        timeline_html += f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp['periodo']}</span> {badge}
                <div class="timeline-role">{exp['cargo']}</div>
                <div class="timeline-company">{exp['empresa']} · {exp['tipo']}</div>
                <div class="timeline-historia">{exp['historia']}</div>
                <div>{tags}</div>
            </div>
        </div>
        """
    
    html = f"""
    <div class="section-glass" id="experiencia">
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
        desc = "<br>".join([f"• {d}" for d in p["descricao"]])
        techs = "".join([f'<span class="project-tag">{t}</span>' for t in p["tecnologias"]])
        link = f'<a href="{p["url"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">🔗 Ver</a>' if p.get("url") else f'<a href="{LINKS_SOCIAIS["github"]}" target="_blank" class="btn-primary" style="padding:0.5rem 1.2rem;font-size:0.85rem;">💻 GitHub</a>'
        
        projetos_html += f"""
        <div class="project-card">
            <div class="project-icon">{p['icone']}</div>
            <h3>{p['nome']}</h3>
            <div class="project-subtitle">{p['subtitulo']}</div>
            <p>{desc}</p>
            <div class="project-context">💡 {p['contexto']}</div>
            <div class="project-tech">{techs}</div>
            {link}
        </div>
        """
    
    html = f"""
    <div class="section-glass alt">
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

def render_certificacoes():
    colors = get_colors()
    certs_html = ""
    
    for cert in CERTIFICACOES:
        cursos = " · ".join(cert["cursos"])
        if "Em andamento" in cert["status"]:
            status = f'<div style="display:inline-block;background:{colors["warning"]};color:white;padding:0.25rem 0.9rem;border-radius:999px;font-size:0.75rem;font-weight:700;">🔄 {cert["status"]}</div>'
            status += f'<div class="progress-bar"><div class="progress-fill" style="width:40%;"></div></div>'
        else:
            status = f'<div style="display:inline-block;background:{colors["success"]};color:white;padding:0.25rem 0.9rem;border-radius:999px;font-size:0.75rem;font-weight:700;">✓ {cert["status"]}</div>'
        
        certs_html += f"""
        <div class="glass-card" style="text-align:center;">
            <div style="font-size:3rem;margin-bottom:1rem;">{cert['icone']}</div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:0.75rem;">{cert['instituicao']}</h3>
            <p style="color:var(--text-muted);font-size:0.9rem;line-height:1.6;margin-bottom:1rem;">{cursos}</p>
            {status}
        </div>
        """
    
    html = f"""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">🎓 Certificações</span>
                <h2>Aprendizado contínuo</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">{certs_html}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_footer():
    tel = DADOS_PESSOAIS['telefone1'].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    
    html = f"""
    <div class="footer" id="contato">
        <div style="display:inline-flex;align-items:center;gap:0.6rem;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.25);padding:0.4rem 1.2rem;border-radius:999px;font-size:0.82rem;font-weight:600;color:var(--success);margin-bottom:1.5rem;">
            <span style="width:8px;height:8px;border-radius:50%;background:var(--success);animation:pulse 2s infinite;"></span>
            Disponível para oportunidades
        </div>
        <h3>Vamos conversar?</h3>
        <p style="color:var(--text-muted);font-size:1.05rem;margin-bottom:2rem;">Se busca alguém que entende de negócio E de dados, vamos tomar um café.</p>
        
        <div style="display:flex;justify-content:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:2rem;">
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.4rem 1rem;border-radius:999px;font-size:0.82rem;">📍 {DADOS_PESSOAIS['localizacao']}</span>
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.4rem 1rem;border-radius:999px;font-size:0.82rem;">🏠 {DADOS_PESSOAIS['modalidades'][0]}</span>
        </div>
        
        <div class="footer-links">
            <a href="{LINKS_SOCIAIS['linkedin']}" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="{LINKS_SOCIAIS['github']}" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="{LINKS_SOCIAIS['email']}" class="footer-link">✉️ E-mail</a>
            <a href="{LINKS_SOCIAIS['whatsapp']}" target="_blank" class="footer-link">📱 WhatsApp</a>
            <a href="tel:{tel}" class="footer-link">📞 {DADOS_PESSOAIS['telefone1']}</a>
        </div>
        
        <p class="footer-copy">© 2026 {DADOS_PESSOAIS['nome']} · Feito com ❤️ e ☕</p>
    </div>
    <a href="#topo" class="scroll-top">↑</a>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_analytics_page():
    colors = get_colors()
    st.markdown(f"""
    <div class="page-header">
        <h1>📊 Analytics Interativo</h1>
        <p>Dashboards em Streamlit + Plotly</p>
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
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=.6,
                         template=colors["plotly_template"])
            fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380,
                              font=dict(color=colors["text"]))
            fig2 = px.histogram(filtro, x="Status", color="Status",
                               template=colors["plotly_template"])
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380,
                              font=dict(color=colors["text"]), showlegend=False)
            a.plotly_chart(fig1, use_container_width=True)
            b.plotly_chart(fig2, use_container_width=True)
    
    with tabs[1]:
        estados = ["SP", "RJ", "MG", "PR"]
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
        dados = []
        np.random.seed(1)
        for e in estados:
            preco = 5.4
            for m in meses:
                preco += np.random.normal(0, .10)
                dados.append([e, m, preco])
        df = pd.DataFrame(dados, columns=["Estado", "Mês", "Preço"])
        estado = st.selectbox("Estado", estados)
        f = df[df["Estado"] == estado]
        
        st.metric("Preço Médio", f"R$ {f['Preço'].mean():.2f}")
        fig = px.line(f, x="Mês", y="Preço", markers=True,
                     template=colors["plotly_template"])
        fig.update_layout(height=400, paper_bgcolor="rgba(0,0,0,0)",
                         font=dict(color=colors["text"]))
        st.plotly_chart(fig, use_container_width=True)
    
    with tabs[2]:
        antes = [120, 125, 118, 130, 122, 128, 126, 124, 129, 127, 125, 130]
        depois = [95, 70, 55, 45, 38, 35, 33, 32, 30, 29, 28, 27]
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        df = pd.DataFrame({
            "Mês": meses * 2,
            "Horas": antes + depois,
            "Período": ["Antes"] * 12 + ["Depois"] * 12
        })
        fig = px.area(df, x="Mês", y="Horas", color="Período",
                     template=colors["plotly_template"])
        fig.update_layout(height=400, paper_bgcolor="rgba(0,0,0,0)",
                         font=dict(color=colors["text"]))
        st.plotly_chart(fig, use_container_width=True)
        
        k1, k2, k3 = st.columns(3)
        k1.metric("Horas Economizadas", "1.108 h", "+93%")
        k2.metric("Custo Evitado", "R$ 185 mil")
        k3.metric("Projetos", "24", "+60%")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# MAIN
# ============================================================================
def main():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    if "modo" not in st.session_state:
        st.session_state.modo = "Dados & BI"
    
    colors = get_colors()
    st.markdown(get_css(colors), unsafe_allow_html=True)
    
    page = st.query_params.get("page", "home")
    
    if "theme_toggle" in st.query_params:
        toggle_theme()
        params = dict(st.query_params)
        params.pop("theme_toggle", None)
        st.query_params.clear()
        st.query_params.update(params)
        st.rerun()
    
    render_navbar(page)
    
    if page == "home":
        render_hero()
        render_sobre()
        render_kpis()
        render_tech()
        render_experiencias()
        render_projetos()
        render_certificacoes()
    elif page == "curriculo":
        render_sobre()
        render_kpis()
        render_tech()
        render_experiencias()
        render_certificacoes()
    elif page == "projetos":
        render_projetos()
    elif page == "analytics":
        render_analytics_page()
    
    render_footer()

if __name__ == "__main__":
    main()
