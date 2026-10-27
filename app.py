import base64
import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires · Analista Administrativo | Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================================
# DADOS DO CURRÍCULO — fonte única de verdade
# Atualize aqui e o site inteiro acompanha.
# ============================================================================
CV = {
    "nome": "Raphael Fernando S. Pires",
    "nome_curto": "Raphael Pires",
    "cargo": "Analista Administrativo · Dados & BI",
    "cidade": "Volta Redonda – RJ",
    "perfil": (
        "Analista com formação em Sistemas de Informação e 17 anos conduzindo a gestão "
        "administrativa de negócios próprios no varejo. Organizo processos, controles e "
        "indicadores e transformo dados em relatórios e dashboards que apoiam decisões, "
        "usando Excel, Power BI, SQL e Python."
    ),
    "contato": {
        "email": "raphael_caxias@hotmail.com",
        "celular": "(24) 99278-9637",
        "whatsapp": "5524992789637",
        "fixo": "(24) 3018-1303",
        "linkedin": "https://www.linkedin.com/in/raphael-pires-caxias",
        "github": "https://github.com/raphaelcaxias",
    },
    "modalidades": ["📍 Presencial", "🏢 Híbrido", "🏠 Remoto", "✈️ Disponível para viagens"],
    "kpis": [
        ("⚡", "87,5%", "menos tempo operacional com automação VBA no Banco do Brasil"),
        ("🏦", "20", "agências usando as macros desenvolvidas"),
        ("📊", "213 mil+", "registros tratados no projeto CNPq Analytics"),
        ("💰", "R$ 1,2 bi", "em investimentos públicos analisados"),
        ("🗂️", "17 anos", "de gestão administrativa de negócios próprios"),
    ],
    "experiencias": [
        {
            "periodo": "out/2026",
            "cargo": "Analista Administrativo",
            "empresa": "Santa Casa de Misericórdia de Barra Mansa",
            "itens": [
                "Atuação na área administrativa com foco em processos, controles, "
                "indicadores e suporte às atividades de gestão.",
            ],
            "tags": ["Processos", "Controles", "Indicadores", "Gestão"],
        },
        {
            "periodo": "2014 – mai/2026",
            "cargo": "Sócio-administrador · Indicadores e KPIs",
            "empresa": "J Sintonía — Varejo especializado",
            "itens": [
                "Acompanhamento de vendas, margem e rentabilidade com relatórios estruturados, "
                "trocando decisões intuitivas por dados.",
                "Análise de viabilidade econômica (projeções, cenários e tendências) que embasou "
                "o encerramento planejado da operação em maio/2026, evitando prejuízo.",
            ],
            "tags": ["KPIs", "Rentabilidade", "Viabilidade econômica", "Relatórios"],
        },
        {
            "periodo": "2009 – 2026",
            "cargo": "Sócio-administrador · Dados e BI",
            "empresa": "Jardim do Éden — Varejo de moda",
            "itens": [
                "Estruturação, limpeza e integração da base de dados do negócio; dashboards "
                "gerenciais em Power BI e Looker Studio com SQL e Python.",
                "Automação de relatórios operacionais com Python e uso de IA Generativa na "
                "exploração de dados e documentação de processos.",
            ],
            "tags": ["Power BI", "Looker Studio", "SQL", "Python", "IA Generativa"],
        },
        {
            "periodo": "2008 – 2010",
            "cargo": "Estagiário de Automação e Dados",
            "empresa": "Banco do Brasil S.A.",
            "itens": [
                "Macros VBA usadas em 20 agências, reduzindo o tempo operacional em 87,5% "
                "(de 2h para 15 min).",
                "Saneamento e padronização de bases de dados gerenciais internas.",
            ],
            "tags": ["VBA", "Excel", "Automação", "Qualidade de dados"],
        },
    ],
    "projetos": [
        {
            "icone": "🔬",
            "nome": "CNPq Analytics",
            "desc": "ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos "
                    "em pesquisa, com painel interativo de distribuição regional.",
            "tags": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
            "link": "https://cnpq-analytics.streamlit.app",
            "cta": "Abrir app",
        },
        {
            "icone": "🇧🇷",
            "nome": "Desenrola Brasil",
            "desc": "Painel executivo com dados do Banco Central: KPIs, séries temporais, "
                    "concentração de mercado (HHI) e segmentação de perfis por clusterização.",
            "tags": ["Python", "Scikit-learn", "Statsmodels", "Plotly", "Streamlit"],
            "link": "https://desenrolabrasil.streamlit.app",
            "cta": "Abrir app",
        },
        {
            "icone": "🍯",
            "nome": "MelShape",
            "desc": "Plataforma de análise de negócios com módulos de vendas, estoque e "
                    "rentabilidade, autenticação, banco em nuvem e insights gerados por APIs de LLM.",
            "tags": ["Python", "Streamlit", "Supabase", "PostgreSQL", "IA Generativa"],
            "link": "https://github.com/raphaelcaxias",
            "cta": "Ver no GitHub",
        },
        {
            "icone": "⛽",
            "nome": "Análise de Combustíveis (ANP)",
            "desc": "Dashboard com filtros temporais e regionais sobre preços de combustíveis "
                    "a partir de dados abertos da ANP.",
            "tags": ["Python", "Plotly", "Séries temporais"],
            "link": "https://github.com/raphaelcaxias",
            "cta": "Ver no GitHub",
        },
    ],
    "competencias": [
        ("🗂️", "Gestão administrativa", ["Processos", "Controles", "Indicadores", "Relatórios gerenciais", "Viabilidade econômica"]),
        ("📊", "Power BI", ["Dashboards", "KPIs", "DAX", "Power Query"]),
        ("📗", "Planilhas", ["Excel avançado", "VBA", "Google Planilhas"]),
        ("🗄️", "SQL", ["PostgreSQL", "Supabase", "Consultas", "Modelagem"]),
        ("🐍", "Python", ["Pandas", "NumPy", "Scikit-learn", "Statsmodels"]),
        ("📈", "Visualização & ETL", ["Plotly", "Streamlit", "Looker Studio", "Limpeza e carga"]),
        ("🤖", "IA aplicada", ["IA Generativa", "Engenharia de prompt", "APIs de LLM"]),
    ],
    "formacao": [
        ("🎓", "Bacharelado em Sistemas de Informação", "UniFOA · 2010"),
        ("💻", "Técnico em Informática", "CIBA · 2005"),
    ],
    "cursos": [
        ("Analista Administrativo", "Adequa Cursos · 60h", "Concluído"),
        ("SQL Avançado · Power BI · Python para Análise de Dados · Git e GitHub", "Hashtag Treinamentos", "Concluído"),
        ("IA Generativa (Claude) · Algoritmos e IA Aplicada", "Hashtag Treinamentos", "Concluído"),
        ("AWS Educate — 8 módulos (Cloud 101, Console, Storage, ML Foundations, Cloud Support, Sustainability)", "AWS", "Concluído"),
        ("AWS Cloud Practitioner", "Hashtag Treinamentos", "40%"),
    ],
    "idiomas": [("Português", "Nativo"), ("Inglês", "Leitura técnica")],
}

# ============================================================================
# TEMA — guardado na URL (?theme=dark|light) para sobreviver à navegação
# ============================================================================
PALETTES = {
    "dark": {
        "bg": "#0A1517", "bg2": "#0F1F22", "text": "#EAF2F0", "muted": "#9DB3AF", "subtle": "#6E8682",
        "primary": "#2BB3A3", "primary_strong": "#1F9488", "accent": "#F2B544",
        "card": "rgba(255,255,255,0.035)", "card_hover": "rgba(255,255,255,0.06)",
        "border": "rgba(255,255,255,0.08)", "border_hover": "rgba(43,179,163,0.45)",
        "tint": "rgba(43,179,163,0.14)", "tint_border": "rgba(43,179,163,0.30)",
        "nav": "rgba(10,21,23,0.82)", "shadow": "0 10px 34px rgba(0,0,0,0.35)",
        "glow": "rgba(43,179,163,0.16)",
        "plotly": "plotly_dark",
        "chart": ["#2BB3A3", "#F2B544", "#7CC6E8", "#E07A5F", "#A3B18A"],
    },
    "light": {
        "bg": "#F5F8F7", "bg2": "#FFFFFF", "text": "#13282B", "muted": "#4D6366", "subtle": "#7A8E8C",
        "primary": "#0F766E", "primary_strong": "#0F3D3E", "accent": "#B7791F",
        "card": "#FFFFFF", "card_hover": "#FFFFFF",
        "border": "rgba(15,61,62,0.10)", "border_hover": "rgba(15,118,110,0.40)",
        "tint": "#E3F1EE", "tint_border": "#B9DCD6",
        "nav": "rgba(245,248,247,0.88)", "shadow": "0 10px 30px rgba(15,61,62,0.08)",
        "glow": "rgba(15,118,110,0.10)",
        "plotly": "plotly_white",
        "chart": ["#0F766E", "#D69E2E", "#2B6CB0", "#C05621", "#6B8E23"],
    },
}

theme = st.query_params.get("theme", "dark")
if theme not in PALETTES:
    theme = "dark"
page = st.query_params.get("page", "home")
if page not in ("home", "analytics", "dashboard"):
    page = "home"
C = PALETTES[theme]


def url(page_name=None, theme_name=None):
    return f"?page={page_name or page}&theme={theme_name or theme}"


# ============================================================================
# ARQUIVOS (FOTO E PDF)
# ============================================================================
def first_existing(paths):
    for p in paths:
        if os.path.exists(p):
            return p
    return None


@st.cache_data
def file_to_data_uri(path, mime):
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


foto_path = first_existing([
    "assets/rapha.jpeg", "assets/rapha.jpg", "assets/rapha.png",
    "rapha.jpeg", "rapha.jpg", "foto.jpeg", "foto.jpg", "perfil.jpeg", "perfil.jpg",
])
pdf_path = first_existing([
    "assets/Curriculo_Raphael_Pires.pdf", "Curriculo_Raphael_Pires.pdf",
    "assets/Curriculo_Raphael_v7.pdf", "Curriculo_Raphael_v7.pdf", "cv.pdf",
])


# ============================================================================
# CSS
# ============================================================================
def load_css():
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root {{
  --bg:{C['bg']}; --bg2:{C['bg2']}; --text:{C['text']}; --muted:{C['muted']}; --subtle:{C['subtle']};
  --primary:{C['primary']}; --primary-strong:{C['primary_strong']}; --accent:{C['accent']};
  --card:{C['card']}; --card-hover:{C['card_hover']}; --border:{C['border']}; --border-hover:{C['border_hover']};
  --tint:{C['tint']}; --tint-border:{C['tint_border']}; --nav:{C['nav']}; --shadow:{C['shadow']}; --glow:{C['glow']};
}}
html, body, [class*="css"], .stApp {{ font-family:'Inter',-apple-system,sans-serif; background:var(--bg); color:var(--text); }}
.stApp {{ background:var(--bg); }}
#MainMenu, footer:not(.footer), header[data-testid="stHeader"], .stDeployButton, [data-testid="stToolbar"] {{ display:none !important; }}
.block-container {{ padding:0 0 2rem !important; max-width:100% !important; }}
[data-testid="stVerticalBlock"] {{ gap:0; }}
a {{ color:var(--primary); }}
p, li {{ color:inherit; }}

/* NAVBAR */
.navbar {{ position:fixed; top:0; left:0; right:0; z-index:999; display:flex; align-items:center; justify-content:space-between;
  padding:.8rem 2.5rem; background:var(--nav); backdrop-filter:blur(18px); -webkit-backdrop-filter:blur(18px);
  border-bottom:1px solid var(--border); }}
.brand {{ font-weight:800; font-size:1.15rem; letter-spacing:-.02em; color:var(--text) !important; text-decoration:none !important;
  display:flex; align-items:center; gap:.55rem; }}
.brand-dot {{ width:10px; height:10px; border-radius:50%; background:var(--primary); box-shadow:0 0 0 4px var(--tint); }}
.brand b {{ color:var(--primary); font-weight:800; }}
.nav-links {{ display:flex; gap:.35rem; align-items:center; }}
.nav-link {{ padding:.45rem 1rem; border-radius:999px; font-size:.86rem; font-weight:600; color:var(--muted) !important;
  text-decoration:none !important; transition:all .2s; }}
.nav-link:hover {{ background:var(--tint); color:var(--text) !important; }}
.nav-link.active {{ background:var(--primary); color:#fff !important; }}
.theme-btn {{ width:38px; height:38px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-left:.4rem;
  border:1px solid var(--border); background:var(--card); text-decoration:none !important; font-size:1rem; transition:all .2s; }}
.theme-btn:hover {{ border-color:var(--primary); transform:rotate(15deg); }}

/* LAYOUT */
.section {{ padding:4.5rem 2rem; border-top:1px solid var(--border); }}
.section.alt {{ background:var(--bg2); }}
.container {{ max-width:1160px; margin:0 auto; }}
.section-head {{ text-align:center; margin-bottom:2.75rem; }}
.eyebrow {{ display:inline-block; font-size:.72rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase; color:var(--primary);
  background:var(--tint); border:1px solid var(--tint-border); padding:.3rem 1rem; border-radius:999px; }}
.section-head h2 {{ font-size:2.2rem; font-weight:800; letter-spacing:-.03em; margin:.8rem 0 .4rem; color:var(--text); }}
.section-head p {{ color:var(--muted); max-width:620px; margin:0 auto; font-size:1rem; line-height:1.6; }}

/* HERO */
.hero {{ padding:8rem 2rem 4.5rem; position:relative; overflow:hidden;
  background:radial-gradient(ellipse at 75% 10%, var(--glow) 0%, transparent 55%), radial-gradient(ellipse at 10% 90%, var(--glow) 0%, transparent 50%); }}
.hero-grid {{ max-width:1160px; margin:0 auto; display:grid; grid-template-columns:auto 1fr; gap:3.5rem; align-items:center; }}
.photo-wrap {{ position:relative; width:230px; height:230px; }}
.photo-wrap::before {{ content:""; position:absolute; inset:-10px; border-radius:50%;
  background:conic-gradient(from 200deg, var(--primary), var(--accent), var(--primary)); opacity:.75; }}
.photo {{ position:relative; width:230px; height:230px; border-radius:50%; object-fit:cover; border:5px solid var(--bg); display:block; }}
.photo-fallback {{ position:relative; width:230px; height:230px; border-radius:50%; border:5px solid var(--bg); background:var(--primary-strong);
  color:#fff; display:flex; align-items:center; justify-content:center; font-size:4rem; font-weight:800; }}
.status {{ display:inline-flex; align-items:center; gap:.5rem; font-size:.8rem; font-weight:700; color:var(--primary);
  background:var(--tint); border:1px solid var(--tint-border); padding:.3rem .9rem; border-radius:999px; }}
.status i {{ width:8px; height:8px; border-radius:50%; background:#22C55E; box-shadow:0 0 0 3px rgba(34,197,94,.25); }}
.hero h1 {{ font-size:3.3rem; font-weight:900; letter-spacing:-.04em; line-height:1.05; margin:.9rem 0 .35rem; color:var(--text); }}
.hero .role {{ font-size:1.05rem; font-weight:700; color:var(--accent); letter-spacing:.02em; }}
.hero .lead {{ font-size:1.07rem; color:var(--muted); line-height:1.7; max-width:620px; margin:1rem 0 1.4rem; }}
.chips {{ display:flex; flex-wrap:wrap; gap:.45rem; }}
.chip {{ font-size:.78rem; font-weight:600; color:var(--text); background:var(--card); border:1px solid var(--border);
  padding:.35rem .8rem; border-radius:10px; }}
.cta {{ display:flex; flex-wrap:wrap; gap:.7rem; margin-top:1.8rem; }}
.btn {{ display:inline-flex; align-items:center; gap:.45rem; padding:.72rem 1.4rem; border-radius:12px; font-weight:700; font-size:.9rem;
  text-decoration:none !important; transition:all .2s; border:1px solid transparent; }}
.btn-primary {{ background:var(--primary); color:#fff !important; }}
.btn-primary:hover {{ background:var(--primary-strong); transform:translateY(-2px); }}
.btn-ghost {{ background:var(--card); color:var(--text) !important; border-color:var(--border); }}
.btn-ghost:hover {{ border-color:var(--primary); transform:translateY(-2px); }}

/* KPI */
.kpi-grid {{ display:grid; grid-template-columns:repeat(5,1fr); gap:1rem; }}
.kpi {{ background:var(--card); border:1px solid var(--border); border-radius:18px; padding:1.4rem 1.1rem; text-align:center;
  box-shadow:var(--shadow); transition:all .25s; }}
.kpi:hover {{ transform:translateY(-4px); border-color:var(--border-hover); }}
.kpi .ico {{ font-size:1.4rem; }}
.kpi .val {{ font-size:1.9rem; font-weight:900; letter-spacing:-.03em; color:var(--primary); margin:.35rem 0 .2rem; }}
.kpi .lbl {{ font-size:.8rem; color:var(--muted); line-height:1.4; }}

/* TIMELINE */
.timeline {{ position:relative; max-width:900px; margin:0 auto; }}
.timeline::before {{ content:""; position:absolute; left:15px; top:6px; bottom:6px; width:2px;
  background:linear-gradient(var(--primary), var(--accent), transparent); }}
.t-item {{ position:relative; padding-left:52px; margin-bottom:1.4rem; }}
.t-dot {{ position:absolute; left:7px; top:22px; width:18px; height:18px; border-radius:50%; background:var(--primary);
  border:4px solid var(--bg2); box-shadow:0 0 0 2px var(--primary); }}
.t-card {{ background:var(--card); border:1px solid var(--border); border-radius:18px; padding:1.4rem 1.6rem; box-shadow:var(--shadow); transition:all .25s; }}
.t-card:hover {{ border-color:var(--border-hover); transform:translateX(4px); }}
.t-top {{ display:flex; justify-content:space-between; align-items:flex-start; gap:1rem; flex-wrap:wrap; }}
.t-role {{ font-size:1.12rem; font-weight:800; color:var(--text); }}
.t-org {{ font-size:.92rem; font-weight:600; color:var(--primary); margin-top:.15rem; }}
.t-date {{ font-size:.75rem; font-weight:800; color:var(--primary); background:var(--tint); border:1px solid var(--tint-border);
  padding:.25rem .8rem; border-radius:999px; white-space:nowrap; }}
.t-card ul {{ margin:.8rem 0 .8rem 1.1rem; padding:0; }}
.t-card li {{ color:var(--muted); font-size:.93rem; line-height:1.6; margin-bottom:.25rem; }}
.tag {{ display:inline-block; font-size:.72rem; font-weight:700; color:var(--primary); background:var(--tint);
  border:1px solid var(--tint-border); padding:.2rem .6rem; border-radius:7px; margin:.15rem .25rem .15rem 0; }}

/* PROJETOS */
.grid-2 {{ display:grid; grid-template-columns:repeat(2,1fr); gap:1.25rem; }}
.card {{ background:var(--card); border:1px solid var(--border); border-radius:20px; padding:1.7rem; box-shadow:var(--shadow);
  transition:all .25s; display:flex; flex-direction:column; }}
.card:hover {{ transform:translateY(-5px); border-color:var(--border-hover); }}
.card .p-ico {{ width:52px; height:52px; border-radius:14px; background:var(--tint); display:flex; align-items:center; justify-content:center; font-size:1.6rem; }}
.card h3 {{ font-size:1.18rem; font-weight:800; margin:1rem 0 .5rem; color:var(--text); }}
.card p {{ color:var(--muted); font-size:.93rem; line-height:1.65; margin-bottom:1rem; flex:1; }}
.card .btn {{ align-self:flex-start; margin-top:1rem; padding:.5rem 1.1rem; font-size:.84rem; }}

/* COMPETÊNCIAS */
.grid-skills {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:1rem; }}
.skill {{ background:var(--card); border:1px solid var(--border); border-radius:16px; padding:1.2rem 1.3rem; }}
.skill h4 {{ font-size:1rem; font-weight:800; color:var(--text); margin-bottom:.6rem; display:flex; gap:.5rem; align-items:center; }}

/* FORMAÇÃO */
.edu-grid {{ display:grid; grid-template-columns:1fr 1.4fr; gap:1.25rem; }}
.edu-item {{ display:flex; gap:.9rem; align-items:flex-start; padding:.9rem 0; border-bottom:1px solid var(--border); }}
.edu-item:last-child {{ border-bottom:none; }}
.edu-item .e-ico {{ font-size:1.3rem; }}
.edu-item b {{ display:block; color:var(--text); font-size:.95rem; }}
.edu-item span {{ color:var(--muted); font-size:.84rem; }}
.course {{ display:flex; justify-content:space-between; gap:1rem; align-items:center; padding:.75rem 0; border-bottom:1px solid var(--border); }}
.course:last-child {{ border-bottom:none; }}
.course b {{ display:block; color:var(--text); font-size:.9rem; font-weight:600; }}
.course span {{ color:var(--muted); font-size:.8rem; }}
.pill {{ font-size:.72rem; font-weight:800; padding:.2rem .7rem; border-radius:999px; white-space:nowrap; }}
.pill.ok {{ color:var(--primary); background:var(--tint); }}
.pill.wip {{ color:var(--accent); background:rgba(242,181,68,.14); }}
.bar {{ width:90px; height:6px; border-radius:999px; background:var(--border); overflow:hidden; margin-top:.35rem; }}
.bar i {{ display:block; height:100%; background:var(--accent); }}

/* FOOTER */
.footer {{ padding:4rem 2rem 2.5rem; text-align:center; border-top:1px solid var(--border); background:var(--bg2); }}
.footer h3 {{ font-size:2rem; font-weight:900; letter-spacing:-.03em; color:var(--text); margin:1rem 0 .4rem; }}
.footer .sub {{ color:var(--muted); margin-bottom:1.4rem; }}
.links {{ display:flex; justify-content:center; flex-wrap:wrap; gap:.6rem; margin:1.6rem 0; }}
.copy {{ text-align:center; color:var(--subtle); font-size:.8rem; padding-top:1.4rem; border-top:1px solid var(--border); max-width:700px; margin:0 auto; }}

/* PÁGINAS DE ANÁLISE */
.page-head {{ padding:7.5rem 2rem 1.5rem; text-align:center;
  background:radial-gradient(ellipse at 50% 0%, var(--glow) 0%, transparent 65%); }}
.page-head h1 {{ font-size:2.4rem; font-weight:900; letter-spacing:-.03em; color:var(--text); }}
.page-head p {{ color:var(--muted); margin-top:.4rem; }}
.note {{ display:inline-block; margin-top:.9rem; font-size:.78rem; font-weight:700; color:var(--accent);
  background:rgba(242,181,68,.12); border:1px solid rgba(242,181,68,.3); padding:.3rem .9rem; border-radius:999px; }}
.metric-row {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:1rem; margin:1rem 0 1.5rem; }}
.metric {{ background:var(--card); border:1px solid var(--border); border-radius:16px; padding:1.1rem 1.2rem; }}
.metric .m-lbl {{ font-size:.74rem; font-weight:700; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); }}
.metric .m-val {{ font-size:1.65rem; font-weight:900; color:var(--text); margin-top:.3rem; letter-spacing:-.02em; }}
.metric .m-sub {{ font-size:.78rem; color:var(--primary); font-weight:600; margin-top:.2rem; }}
.chart-title {{ font-size:1.05rem; font-weight:800; color:var(--text); margin:1rem 0 .3rem; }}
.chart-desc {{ font-size:.88rem; color:var(--muted); margin-bottom:.6rem; }}
div[data-testid="stTabs"] button p {{ font-weight:700; color:var(--muted); }}
[data-testid="stSelectbox"] [class*="ComboBox"] > div, [data-testid="stMultiSelect"] [class*="react-aria"] > div,
[data-baseweb="select"] > div {{ background:var(--card) !important; border:1px solid var(--border) !important; }}
[data-testid="stSelectbox"] input, [data-testid="stSelectbox"] button, [data-testid="stMultiSelect"] input,
[data-testid="stMultiSelect"] button, [data-testid="stSelectbox"] svg, [data-testid="stMultiSelect"] svg {{ color:var(--text) !important; }}
div[data-testid="stTabs"] button {{ opacity:1 !important; }}
[data-testid="stCaptionContainer"], .stSlider [data-testid="stTickBarMin"], .stSlider [data-testid="stTickBarMax"] {{ color:var(--muted) !important; }}
[data-testid="stExpander"] summary p {{ color:var(--text); }}
div[data-testid="stTabs"] [aria-selected="true"] p {{ color:var(--primary) !important; }}
label, .stSelectbox label p, .stMultiSelect label p {{ color:var(--muted) !important; font-weight:600; }}
[data-testid="stExpander"] {{ border:1px solid var(--border) !important; border-radius:14px !important; background:var(--card); }}

.st-key-conteudo {{ max-width:1160px; margin:0 auto; padding:0 1.5rem; }}
/* RESPONSIVO */
@media (max-width: 1000px) {{ .kpi-grid {{ grid-template-columns:repeat(3,1fr); }} .edu-grid {{ grid-template-columns:1fr; }} }}
@media (max-width: 820px) {{
  .navbar {{ padding:.7rem 1rem; }} .nav-link {{ padding:.4rem .65rem; font-size:.8rem; }} .brand {{ font-size:1rem; }}
  .hero {{ padding:6.5rem 1.2rem 3rem; }} .hero-grid {{ grid-template-columns:1fr; text-align:center; gap:2rem; }}
  .photo-wrap {{ margin:0 auto; width:180px; height:180px; }} .photo, .photo-fallback {{ width:180px; height:180px; }}
  .hero h1 {{ font-size:2.3rem; }} .hero .lead {{ margin-left:auto; margin-right:auto; }}
  .chips, .cta {{ justify-content:center; }}
  .section {{ padding:3rem 1.1rem; }} .section-head h2 {{ font-size:1.7rem; }}
  .kpi-grid {{ grid-template-columns:repeat(2,1fr); }} .grid-2 {{ grid-template-columns:1fr; }}
  .t-item {{ padding-left:40px; }} .timeline::before {{ left:9px; }} .t-dot {{ left:1px; }}
}}
@media (max-width: 520px) {{ .nav-links .hide-sm {{ display:none; }} }}
</style>
""", unsafe_allow_html=True)


def br(v, casas=0):
    """Formata número no padrão brasileiro: 1.234,5"""
    return f"{v:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def brl(v, casas=0):
    return f"R$ {br(v, casas)}"


def html(markup):
    """Renderiza um bloco HTML completo de uma vez (Streamlit fecha tags abertas entre chamadas)."""
    st.markdown(markup, unsafe_allow_html=True)


def style_fig(fig, height=380):
    fig.update_layout(
        template=C["plotly"], height=height, margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=C["text"], size=12),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title_text=""),
    )
    fig.update_xaxes(gridcolor=C["border"], zeroline=False)
    fig.update_yaxes(gridcolor=C["border"], zeroline=False)
    return fig


# ============================================================================
# NAVBAR
# ============================================================================
def render_nav():
    other = "light" if theme == "dark" else "dark"
    icon = "☀️" if theme == "dark" else "🌙"
    items = [("home", "Início", ""), ("analytics", "Análises", ""), ("dashboard", "Dashboard", "hide-sm")]
    links = "".join(
        f'<a href="{url(p)}" target="_self" class="nav-link {cls} {"active" if page == p else ""}">{label}</a>'
        for p, label, cls in items
    )
    html(f"""
<nav class="navbar">
  <a href="{url('home')}" target="_self" class="brand"><span class="brand-dot"></span>Raphael <b>Pires</b></a>
  <div class="nav-links">{links}
    <a href="{url(theme_name=other)}" target="_self" class="theme-btn" title="Alternar tema">{icon}</a>
  </div>
</nav>""")


# ============================================================================
# PÁGINA INICIAL
# ============================================================================
def render_home():
    ct = CV["contato"]
    if foto_path:
        mime = "image/png" if foto_path.endswith(".png") else "image/jpeg"
        foto = f'<img class="photo" src="{file_to_data_uri(foto_path, mime)}" alt="Foto de {CV["nome_curto"]}">'
    else:
        foto = '<div class="photo-fallback">RP</div>'
    cv_btn = ""
    if pdf_path:
        cv_btn = (f'<a class="btn btn-ghost" href="{file_to_data_uri(pdf_path, "application/pdf")}" '
                  f'download="Curriculo_Raphael_Pires.pdf">📄 Baixar currículo</a>')
    chips = "".join(f'<span class="chip">{c}</span>' for c in
                    ["Power BI", "Excel / VBA", "SQL", "Python", "Indicadores", "Processos", "Dashboards", "IA Generativa"])

    html(f"""
<section class="hero" id="topo">
  <div class="hero-grid">
    <div class="photo-wrap">{foto}</div>
    <div>
      <span class="status"><i></i>Disponível para novas oportunidades</span>
      <h1>{CV['nome']}</h1>
      <div class="role">{CV['cargo']}</div>
      <p class="lead">{CV['perfil']}</p>
      <div class="chips">{chips}</div>
      <div class="cta">
        <a class="btn btn-primary" href="https://wa.me/{ct['whatsapp']}" target="_blank">💬 Falar no WhatsApp</a>
        {cv_btn}
        <a class="btn btn-ghost" href="#experiencia" target="_self">Ver trajetória ↓</a>
      </div>
    </div>
  </div>
</section>""")

    kpis = "".join(
        f'<div class="kpi"><div class="ico">{i}</div><div class="val">{v}</div><div class="lbl">{l}</div></div>'
        for i, v, l in CV["kpis"]
    )
    html(f"""
<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Resultados</span><h2>Números da trajetória</h2>
      <p>Resultados registrados no currículo, de automação bancária a projetos com dados públicos.</p></div>
    <div class="kpi-grid">{kpis}</div>
  </div>
</section>""")

    items = ""
    for e in CV["experiencias"]:
        bullets = "".join(f"<li>{b}</li>" for b in e["itens"])
        tags = "".join(f'<span class="tag">{t}</span>' for t in e["tags"])
        items += f"""
<div class="t-item"><div class="t-dot"></div><div class="t-card">
  <div class="t-top"><div><div class="t-role">{e['cargo']}</div><div class="t-org">{e['empresa']}</div></div>
  <span class="t-date">{e['periodo']}</span></div>
  <ul>{bullets}</ul><div>{tags}</div>
</div></div>"""
    html(f"""
<section class="section alt" id="experiencia">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Trajetória</span><h2>Experiência profissional</h2>
      <p>Gestão administrativa, indicadores e automação aplicados a negócios reais.</p></div>
    <div class="timeline">{items}</div>
  </div>
</section>""")

    cards = ""
    for p in CV["projetos"]:
        tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        cards += f"""
<div class="card"><div class="p-ico">{p['icone']}</div><h3>{p['nome']}</h3><p>{p['desc']}</p>
  <div>{tags}</div><a class="btn btn-primary" href="{p['link']}" target="_blank">🔗 {p['cta']}</a></div>"""
    html(f"""
<section class="section" id="projetos">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Portfólio</span><h2>Projetos de análise de dados</h2>
      <p>Aplicações publicadas com dados públicos reais, construídas em Python e Streamlit.</p></div>
    <div class="grid-2">{cards}</div>
  </div>
</section>""")

    skills = "".join(
        f'<div class="skill"><h4>{i} {t}</h4><div>{"".join(f"<span class=tag>{x}</span>" for x in xs)}</div></div>'
        for i, t, xs in CV["competencias"]
    )
    html(f"""
<section class="section alt" id="competencias">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Competências</span><h2>O que eu uso no dia a dia</h2>
      <p>Da rotina administrativa à análise de dados.</p></div>
    <div class="grid-skills">{skills}</div>
  </div>
</section>""")

    edu = "".join(f'<div class="edu-item"><span class="e-ico">{i}</span><div><b>{t}</b><span>{s}</span></div></div>'
                  for i, t, s in CV["formacao"])
    edu += "".join(f'<div class="edu-item"><span class="e-ico">🗣️</span><div><b>{l}</b><span>{n}</span></div></div>'
                   for l, n in CV["idiomas"])
    courses = ""
    for nome, inst, status in CV["cursos"]:
        if status == "Concluído":
            right = '<span class="pill ok">✓ Concluído</span>'
        else:
            right = f'<div style="text-align:right"><span class="pill wip">Em andamento · {status}</span><div class="bar"><i style="width:{status}"></i></div></div>'
        courses += f'<div class="course"><div><b>{nome}</b><span>{inst}</span></div>{right}</div>'
    html(f"""
<section class="section" id="formacao">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Formação</span><h2>Formação e cursos</h2></div>
    <div class="edu-grid">
      <div class="card">{edu}</div>
      <div class="card">{courses}</div>
    </div>
  </div>
</section>""")


# ============================================================================
# ANÁLISES
# ============================================================================
def render_analytics():
    html("""
<div class="page-head"><h1>📊 Análises interativas</h1>
<p>Demonstrações em Streamlit + Plotly</p></div>""")
    with st.container(key="conteudo"):
        tabs = st.tabs(["⚡ Caso real: automação no BB", "🇧🇷 Renegociação de dívidas", "⛽ Preços de combustíveis"])

        with tabs[0]:
            html("""<div class="chart-title">Macros VBA no Banco do Brasil</div>
<div class="chart-desc">Números do currículo: a rotina que levava 2h passou a levar 15 min, em 20 agências.</div>""")
            html("""<div class="metric-row">
<div class="metric"><div class="m-lbl">Antes</div><div class="m-val">120 min</div><div class="m-sub">por execução da rotina</div></div>
<div class="metric"><div class="m-lbl">Depois</div><div class="m-val">15 min</div><div class="m-sub">com as macros VBA</div></div>
<div class="metric"><div class="m-lbl">Redução</div><div class="m-val">87,5%</div><div class="m-sub">do tempo operacional</div></div>
<div class="metric"><div class="m-lbl">Alcance</div><div class="m-val">20</div><div class="m-sub">agências atendidas</div></div></div>""")
            execs = st.slider("Simule: quantas vezes por mês cada agência executa a rotina?", 1, 30, 4)
            horas_antes = 20 * execs * 2.0
            horas_depois = 20 * execs * 0.25
            fig = go.Figure(go.Bar(
                x=[horas_antes, horas_depois], y=["Antes", "Depois"], orientation="h",
                marker_color=[C["chart"][1], C["chart"][0]],
                text=[f"{br(horas_antes)} h", f"{br(horas_depois)} h"],
                textposition="outside", cliponaxis=False,
            ))
            style_fig(fig, 240)
            fig.update_layout(showlegend=False, xaxis_title="horas por mês (20 agências)",
                              xaxis_range=[0, horas_antes * 1.18], margin=dict(l=10, r=30, t=10, b=10))
            st.plotly_chart(fig, width="stretch", config={"displayModeBar": False}, theme=None)
            st.caption(f"Com {execs} execução(ões) por mês, a economia estimada é de "
                       f"{br(horas_antes - horas_depois)} horas por mês nas 20 agências.")

        with tabs[1]:
            html("""<div class="chart-desc"><span class="note">Dados simulados para demonstração</span> —
a versão com dados reais do Banco Central está no app <a href="https://desenrolabrasil.streamlit.app" target="_blank">Desenrola Brasil</a>.</div>""")
            rng = np.random.default_rng(42)
            regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
            status = ["Renegociado", "Em negociação", "Inadimplente"]
            df = pd.DataFrame({
                "Região": rng.choice(regioes, 400, p=[.45, .28, .15, .07, .05]),
                "Valor": rng.lognormal(8.5, 1.2, 400),
                "Status": rng.choice(status, 400, p=[.65, .25, .10]),
            })
            c1, c2 = st.columns(2)
            reg = c1.multiselect("Região", regioes, default=regioes)
            stt = c2.multiselect("Status", status, default=status)
            f = df[df["Região"].isin(reg) & df["Status"].isin(stt)]
            if f.empty:
                st.info("Nenhum registro com esses filtros.")
            else:
                html(f"""<div class="metric-row">
<div class="metric"><div class="m-lbl">Contratos</div><div class="m-val">{br(len(f))}</div></div>
<div class="metric"><div class="m-lbl">Valor total</div><div class="m-val">{brl(f['Valor'].sum() / 1e6, 1)} mi</div></div>
<div class="metric"><div class="m-lbl">Renegociados</div><div class="m-val">{br((f['Status'] == 'Renegociado').mean() * 100, 1)}%</div></div></div>""")
                a, b = st.columns(2)
                with a:
                    html('<div class="chart-title">Valor por região</div>')
                    g = f.groupby("Região", as_index=False)["Valor"].sum().sort_values("Valor")
                    fig1 = px.bar(g, x="Valor", y="Região", orientation="h", color_discrete_sequence=[C["chart"][0]])
                    st.plotly_chart(style_fig(fig1, 340), width="stretch", config={"displayModeBar": False}, theme=None)
                with b:
                    html('<div class="chart-title">Contratos por status</div>')
                    s = f["Status"].value_counts().reindex(status).dropna().reset_index()
                    s.columns = ["Status", "Contratos"]
                    fig2 = px.bar(s, x="Status", y="Contratos", color="Status", color_discrete_sequence=C["chart"])
                    fig2.update_layout(showlegend=False)
                    st.plotly_chart(style_fig(fig2, 340), width="stretch", config={"displayModeBar": False}, theme=None)

        with tabs[2]:
            html('<div class="chart-desc"><span class="note">Dados simulados para demonstração</span></div>')
            estados = ["RJ", "SP", "MG", "PR"]
            meses = pd.date_range("2026-01-01", periods=9, freq="MS")
            rng = np.random.default_rng(1)
            rows = []
            for e in estados:
                preco = 5.9 + rng.normal(0, .15)
                for m in meses:
                    preco += rng.normal(0.01, .08)
                    rows.append([e, m, preco])
            df = pd.DataFrame(rows, columns=["Estado", "Mês", "Preço"])
            sel = st.multiselect("Estados", estados, default=["RJ", "SP"])
            f = df[df["Estado"].isin(sel)]
            if f.empty:
                st.info("Escolha ao menos um estado.")
            else:
                html(f"""<div class="metric-row">
<div class="metric"><div class="m-lbl">Preço médio</div><div class="m-val">{brl(f['Preço'].mean(), 2)}</div></div>
<div class="metric"><div class="m-lbl">Mínimo</div><div class="m-val">{brl(f['Preço'].min(), 2)}</div></div>
<div class="metric"><div class="m-lbl">Máximo</div><div class="m-val">{brl(f['Preço'].max(), 2)}</div></div></div>""")
                fig = px.line(f, x="Mês", y="Preço", color="Estado", markers=True, color_discrete_sequence=C["chart"])
                fig.update_traces(line=dict(width=3))
                fig.update_yaxes(title="R$ / litro")
                st.plotly_chart(style_fig(fig, 400), width="stretch", config={"displayModeBar": False}, theme=None)


# ============================================================================
# DASHBOARD
# ============================================================================
@st.cache_data
def dados_dashboard():
    rng = np.random.default_rng(42)
    fim = pd.Timestamp(datetime.now().date())
    datas = pd.date_range(fim - timedelta(days=729), fim, freq="D")
    categorias = ["Moda feminina", "Moda masculina", "Acessórios", "Calçados", "Infantil"]
    canais = ["Loja física", "WhatsApp", "Instagram", "Site"]
    n = 3000
    df = pd.DataFrame({
        "Data": rng.choice(datas, n),
        "Categoria": rng.choice(categorias, n, p=[.34, .2, .18, .18, .1]),
        "Canal": rng.choice(canais, n, p=[.5, .22, .18, .1]),
        "Receita": rng.lognormal(5.2, .55, n).round(2),
    })
    df["Margem %"] = (rng.normal(42, 6, n)).clip(20, 65).round(1)
    df["Lucro"] = (df["Receita"] * df["Margem %"] / 100).round(2)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mês"] = df["Data"].dt.to_period("M").dt.to_timestamp()
    return df




def render_dashboard():
    html("""
<div class="page-head"><h1>📈 Dashboard de varejo</h1>
<p>Modelo de painel gerencial no estilo dos que montei para meus negócios</p>
<span class="note">Dados simulados para demonstração</span></div>""")
    df = dados_dashboard()
    with st.container(key="conteudo"):
        c1, c2, c3 = st.columns(3)
        periodo = c1.selectbox("Período", ["Últimos 6 meses", "Últimos 12 meses", "Últimos 24 meses"], index=1)
        cat = c2.selectbox("Categoria", ["Todas"] + sorted(df["Categoria"].unique()))
        canal = c3.selectbox("Canal", ["Todos"] + sorted(df["Canal"].unique()))
        dias = {"Últimos 6 meses": 180, "Últimos 12 meses": 365, "Últimos 24 meses": 730}[periodo]
        f = df[df["Data"] >= df["Data"].max() - timedelta(days=dias)]
        if cat != "Todas":
            f = f[f["Categoria"] == cat]
        if canal != "Todos":
            f = f[f["Canal"] == canal]
        if f.empty:
            st.info("Nenhuma venda com esses filtros.")
            return

        html(f"""<div class="metric-row">
<div class="metric"><div class="m-lbl">Receita</div><div class="m-val">{brl(f['Receita'].sum())}</div></div>
<div class="metric"><div class="m-lbl">Vendas</div><div class="m-val">{br(len(f))}</div></div>
<div class="metric"><div class="m-lbl">Ticket médio</div><div class="m-val">{brl(f['Receita'].mean())}</div></div>
<div class="metric"><div class="m-lbl">Margem média</div><div class="m-val">{br(f['Lucro'].sum() / f['Receita'].sum() * 100, 1)}%</div></div>
</div>""")

        a, b = st.columns([1.5, 1])
        with a:
            html('<div class="chart-title">Receita e lucro por mês</div>')
            m = f.groupby("Mês", as_index=False)[["Receita", "Lucro"]].sum()
            # mostra só meses completos (o primeiro e o atual ficam parciais)
            mes_atual = pd.Timestamp(datetime.now().date()).to_period("M").to_timestamp()
            m = m[(m["Mês"] > m["Mês"].min()) & (m["Mês"] < mes_atual)]
            fig = px.line(m.melt("Mês", var_name="Indicador", value_name="R$"), x="Mês", y="R$", color="Indicador",
                          markers=True, color_discrete_sequence=C["chart"])
            fig.update_traces(line=dict(width=3))
            st.plotly_chart(style_fig(fig, 360), width="stretch", config={"displayModeBar": False}, theme=None)
        with b:
            html('<div class="chart-title">Receita por canal</div>')
            g = f.groupby("Canal", as_index=False)["Receita"].sum().sort_values("Receita")
            fig = px.bar(g, x="Receita", y="Canal", orientation="h", color_discrete_sequence=[C["chart"][0]])
            st.plotly_chart(style_fig(fig, 360), width="stretch", config={"displayModeBar": False}, theme=None)

        a, b = st.columns(2)
        with a:
            html('<div class="chart-title">Receita por categoria</div>')
            g = f.groupby("Categoria", as_index=False)["Receita"].sum().sort_values("Receita")
            fig = px.bar(g, x="Receita", y="Categoria", orientation="h", color_discrete_sequence=[C["chart"][1]])
            st.plotly_chart(style_fig(fig, 320), width="stretch", config={"displayModeBar": False}, theme=None)
        with b:
            html('<div class="chart-title">Margem média por categoria</div>')
            g = f.groupby("Categoria").apply(lambda x: x["Lucro"].sum() / x["Receita"].sum() * 100, include_groups=False)
            g = g.reset_index(name="Margem %").sort_values("Margem %")
            fig = px.bar(g, x="Margem %", y="Categoria", orientation="h", color_discrete_sequence=[C["chart"][2]])
            st.plotly_chart(style_fig(fig, 320), width="stretch", config={"displayModeBar": False}, theme=None)

        with st.expander("📋 Ver dados detalhados"):
            st.dataframe(f.sort_values("Data", ascending=False).drop(columns="Mês"), width="stretch", hide_index=True)


# ============================================================================
# RODAPÉ / CONTATO
# ============================================================================
def render_footer():
    ct = CV["contato"]
    modos = "".join(f'<span class="chip">{m}</span>' for m in CV["modalidades"])
    html(f"""
<div class="footer" id="contato">
  <span class="status"><i></i>Disponível para novas oportunidades</span>
  <h3>Vamos conversar?</h3>
  <p class="sub">Vagas administrativas, de análise de dados e BI · {CV['cidade']}</p>
  <div class="chips" style="justify-content:center">{modos}</div>
  <div class="links">
    <a class="btn btn-primary" href="https://wa.me/{ct['whatsapp']}" target="_blank">💬 WhatsApp {ct['celular']}</a>
    <a class="btn btn-ghost" href="mailto:{ct['email']}">✉️ {ct['email']}</a>
    <a class="btn btn-ghost" href="{ct['linkedin']}" target="_blank">💼 LinkedIn</a>
    <a class="btn btn-ghost" href="{ct['github']}" target="_blank">💻 GitHub</a>
  </div>
  <p class="copy">© {datetime.now().year} {CV['nome']} · Feito com Python e Streamlit</p>
</div>""")


# ============================================================================
# MAIN
# ============================================================================
load_css()
render_nav()
if page == "analytics":
    render_analytics()
elif page == "dashboard":
    render_dashboard()
else:
    render_home()
render_footer()
