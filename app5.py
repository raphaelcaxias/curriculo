# -*- coding: utf-8 -*-
"""
Portfolio - Raphael Pires | app5.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import os
import requests
from io import BytesIO

st.set_page_config(
    page_title="Raphael Pires | Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,400&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

:root {
    --ink: #0d0f14; --ink2: #2e3340; --slate: #64748b;
    --rule: #e2e5eb; --paper: #fafaf8; --cream: #f4f1ea;
    --red: #c8392b; --blue: #1a4480;
}
html, body, .stApp { background: var(--paper) !important; }
.stApp { font-family: 'DM Sans', system-ui, sans-serif; color: var(--ink); }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0.5rem !important; max-width: 1060px; }

/* Sidebar */
[data-testid="stSidebar"] { background: #0d0f14 !important; }
[data-testid="stSidebar"] * { color: #b0b8c6 !important; font-family: 'DM Sans', sans-serif !important; }
[data-testid="stSidebar"] a { color: #e2c97e !important; }
[data-testid="stSidebar"] hr { border-color: #1e2430 !important; }
[data-testid="stSidebar"] .stDownloadButton > button {
    background: #c8392b !important; color: white !important; border: none !important;
    font-family: 'DM Mono', monospace !important; font-size: 0.75rem !important;
    letter-spacing: 0.06em; border-radius: 3px !important; width: 100%;
}
[data-testid="stSidebar"] img { border-radius: 8px; }

/* Hero */
.hero { border-bottom: 3px double var(--rule); padding-bottom: 1.5rem; margin-bottom: 1.5rem; }
.hero-label { font-family: 'DM Mono', monospace; font-size: 0.68rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--red); margin-bottom: 0.6rem; }
.hero-name { font-family: 'Playfair Display', Georgia, serif; font-size: 3rem; font-weight: 900; line-height: 1.05; color: var(--ink); letter-spacing: -1px; margin-bottom: 0.5rem; }
.hero-name em { font-style: italic; color: var(--blue); }
.hero-role { font-size: 1rem; font-weight: 300; color: var(--slate); border-left: 3px solid var(--red); padding-left: 0.75rem; margin: 0.75rem 0 1rem; line-height: 1.6; }
.hero-pill { display: inline-block; font-family: 'DM Mono', monospace; font-size: 0.68rem; background: var(--cream); border: 1px solid var(--rule); color: var(--ink2); padding: 0.28rem 0.75rem; border-radius: 2px; margin: 0.15rem; }
.cta-dark { background: var(--ink); color: white !important; padding: 0.6rem 1.3rem; text-decoration: none !important; font-weight: 600; font-size: 0.85rem; border-radius: 3px; margin-right: 0.4rem; display: inline-block; }
.cta-out { background: transparent; color: var(--ink) !important; border: 1.5px solid var(--ink); padding: 0.6rem 1.3rem; text-decoration: none !important; font-weight: 500; font-size: 0.85rem; border-radius: 3px; margin-right: 0.4rem; display: inline-block; }

/* Section header */
.sec { display: flex; align-items: baseline; gap: 0.6rem; margin: 2rem 0 1rem; border-top: 1px solid var(--rule); padding-top: 0.9rem; }
.sec-n { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: var(--red); letter-spacing: 0.1em; }
.sec-t { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: var(--ink); margin: 0; line-height: 1; }

/* About */
.about-quote { font-family: 'Playfair Display', serif; font-size: 1.05rem; line-height: 1.75; color: var(--ink2); border-left: 4px solid var(--red); padding-left: 1.1rem; background: var(--cream); padding: 1.3rem 1.3rem 1.3rem 1.5rem; border-radius: 0 4px 4px 0; margin-bottom: 0; }

/* KPI */
.kpi { background: white; border: 1px solid var(--rule); border-top: 3px solid var(--blue); padding: 1.1rem 1rem; text-align: left; }
.kpi-v { font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700; color: var(--ink); line-height: 1; }
.kpi-d { font-family: 'DM Mono', monospace; font-size: 0.62rem; color: var(--slate); text-transform: uppercase; letter-spacing: 0.04em; line-height: 1.5; margin-top: 0.3rem; }

/* Timeline item */
.tl-wrap { display: flex; gap: 0; margin-bottom: 0; }
.tl-left-col { width: 120px; min-width: 120px; text-align: right; padding-top: 0.1rem; padding-right: 1.2rem; }
.tl-period { font-family: 'DM Mono', monospace; font-size: 0.66rem; letter-spacing: 0.03em; display: block; margin-bottom: 0.15rem; }
.tl-co { font-family: 'DM Sans', sans-serif; font-weight: 700; font-size: 0.78rem; color: var(--ink2); display: block; }
.tl-right-col { border-left: 2px solid var(--rule); padding-left: 1.3rem; padding-bottom: 1.5rem; position: relative; flex: 1; }
.tl-dot { position: absolute; left: -5px; top: 8px; width: 8px; height: 8px; border-radius: 50%; }
.tl-role { font-family: 'Playfair Display', serif; font-size: 1.05rem; font-weight: 700; color: var(--ink); margin-bottom: 0.3rem; }
.tl-badge { display: inline-block; font-family: 'DM Mono', monospace; font-size: 0.62rem; padding: 0.18rem 0.55rem; border-radius: 2px; margin-bottom: 0.4rem; letter-spacing: 0.03em; }
.tl-badge-red { background: #fff4f4; color: var(--red); border: 1px solid #fad2cf; }
.tl-badge-blue { background: #edf2fb; color: var(--blue); border: 1px solid #c3d4f0; }

/* Project card */
.proj-card { background: white; border: 1px solid var(--rule); padding: 1.3rem; position: relative; overflow: hidden; margin-bottom: 0.3rem; border-radius: 2px; }
.proj-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #c8392b, #1a4480); }
.proj-ghost { background: var(--cream); border: 1px dashed #ccc; }
.proj-idx { font-family: 'DM Mono', monospace; font-size: 0.6rem; color: var(--slate); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem; }
.proj-ttl { font-family: 'Playfair Display', serif; font-size: 1.05rem; font-weight: 700; color: var(--ink); margin-bottom: 0.4rem; line-height: 1.3; }
.proj-ttl-gray { color: var(--slate); }
.proj-desc { font-size: 0.83rem; color: var(--slate); line-height: 1.65; margin-bottom: 0.7rem; }
.proj-tag { font-family: 'DM Mono', monospace; font-size: 0.6rem; background: var(--cream); color: var(--ink2); padding: 0.18rem 0.5rem; border-radius: 2px; display: inline-block; margin: 0.1rem; }
.proj-btn-d { background: var(--ink); color: white !important; text-decoration: none !important; padding: 0.38rem 0.85rem; border-radius: 3px; font-size: 0.77rem; font-weight: 600; margin-right: 0.35rem; display: inline-block; margin-top: 0.5rem; }
.proj-btn-o { border: 1.5px solid var(--ink); color: var(--ink) !important; text-decoration: none !important; padding: 0.38rem 0.85rem; border-radius: 3px; font-size: 0.77rem; display: inline-block; margin-top: 0.5rem; }

/* Stack */
.stack-box { background: white; border: 1px solid var(--rule); padding: 1rem 1.2rem; margin-bottom: 0.7rem; }
.stack-cat { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--red); margin-bottom: 0.6rem; }
.stack-tag { font-size: 0.8rem; font-weight: 500; background: var(--cream); color: var(--ink2); padding: 0.28rem 0.65rem; border-radius: 2px; display: inline-block; margin: 0.15rem; }

/* Edu */
.edu-box { background: var(--cream); padding: 1.3rem; border-radius: 2px; height: 100%; }
.edu-cat { font-family: 'DM Mono', monospace; font-size: 0.6rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--red); margin-bottom: 0.9rem; }
.edu-ttl { font-weight: 600; font-size: 0.88rem; color: var(--ink); }
.edu-sub { font-size: 0.77rem; color: var(--slate); margin: 0.1rem 0 0.8rem; }
.cert-row { font-size: 0.81rem; color: var(--ink2); padding: 0.3rem 0; border-bottom: 1px dashed #ddd; display: flex; gap: 0.4rem; }
.cert-row:last-child { border-bottom: none; }

/* Contact */
.contact-box { background: var(--ink); color: white; padding: 2rem; border-radius: 3px; }
.contact-h { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: white; margin-bottom: 0.5rem; }
.contact-sub { color: #8896a7; font-size: 0.85rem; line-height: 1.85; }
.contact-sub a { color: #e2c97e !important; text-decoration: none; }
.clink { display: inline-block; background: rgba(255,255,255,0.08); color: white !important; text-decoration: none !important; padding: 0.55rem 1rem; border-radius: 3px; font-size: 0.8rem; font-weight: 500; border: 1px solid rgba(255,255,255,0.12); margin: 0.2rem; }

/* Footer */
.foot { border-top: 1px solid var(--rule); margin-top: 2.5rem; padding: 1.2rem 0; font-family: 'DM Mono', monospace; font-size: 0.62rem; color: var(--slate); }

/* Diff list via streamlit */
div[data-testid="stMarkdownContainer"] ul { padding-left: 0 !important; list-style: none !important; }
div[data-testid="stMarkdownContainer"] ul li { padding: 0.4rem 0; border-bottom: 1px dashed #e2e5eb; font-size: 0.88rem; color: #2e3340; }
div[data-testid="stMarkdownContainer"] ul li:last-child { border-bottom: none; }
</style>
""", unsafe_allow_html=True)

# ── LOADERS ───────────────────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_image():
    urls = [
        "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/rapha.jpeg",
        "https://avatars.githubusercontent.com/raphaelcaxias",
    ]
    for url in urls:
        try:
            r = requests.get(url, timeout=6)
            if r.status_code == 200:
                return Image.open(BytesIO(r.content))
        except Exception:
            pass
    for p in ["rapha.jpeg", "assets/rapha.jpeg"]:
        if os.path.exists(p):
            return Image.open(p)
    return None

@st.cache_data(show_spinner=False)
def load_cv():
    try:
        r = requests.get(
            "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/Curriculo_Raphael_Premium_Final.pdf",
            timeout=8)
        if r.status_code == 200:
            return r.content
    except Exception:
        pass
    for p in ["Curriculo_Raphael_Premium_Final.pdf", "assets/Curriculo_Raphael_Premium_Final.pdf"]:
        if os.path.exists(p):
            with open(p, "rb") as f:
                return f.read()
    return None

profile_image = load_image()
cv_pdf = load_cv()

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    if profile_image:
        st.image(profile_image, use_column_width=True)
    else:
        # placeholder com iniciais
        st.markdown("""
        <div style="background:#1a4480;border-radius:8px;height:180px;display:flex;
                    align-items:center;justify-content:center;margin-bottom:0.5rem;">
            <span style="font-family:Playfair Display,serif;font-size:3rem;
                         font-weight:900;color:white;letter-spacing:-2px;">RP</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧭 Ir para")
    st.markdown("""
- [🏠 Início](#inicio)
- [👤 Sobre](#sobre)
- [💼 Experiência](#experiencia)
- [🚀 Projetos](#projetos)
- [🛠 Stack](#stack)
- [🎓 Formação](#formacao)
- [📬 Contato](#contato)
    """)
    st.markdown("---")
    st.markdown("### 📥 Currículo em PDF")
    if cv_pdf:
        st.download_button(
            "↓  Baixar CV — PDF",
            data=cv_pdf,
            file_name="Curriculo_Raphael_Pires.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("PDF não localizado no repositório.")
    st.markdown("---")
    st.markdown("### 🔗 Links")
    st.markdown("""
[🔗 LinkedIn](https://linkedin.com/in/raphael-pires-caxias)  
[💻 GitHub](https://github.com/raphaelcaxias)  
[📧 E-mail](mailto:raphael_caxias@hotmail.com)  
[💬 WhatsApp](https://wa.me/5524992275226)
    """)
    st.markdown("---")
    st.caption("Portfolio atualizado · 2026")

# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
st.markdown('<a id="inicio"></a>', unsafe_allow_html=True)
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<p class="hero-label">◈ Portfólio Profissional — Volta Redonda, RJ</p>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-name">Raphael <em>Pires</em></h1>', unsafe_allow_html=True)
st.markdown("""<p class="hero-role">
    Analista Operacional de Dados &amp; Business Intelligence<br>
    <span style="font-size:0.88rem;">+20 anos de experiência real em gestão, automação e indicadores de negócio</span>
</p>""", unsafe_allow_html=True)

pills = ["SQL · PostgreSQL", "Python · Pandas", "Power BI · Looker Studio", "Excel / VBA", "Streamlit · Plotly", "Remoto ✓"]
st.markdown("".join(f'<span class="hero-pill">{p}</span>' for p in pills), unsafe_allow_html=True)

st.markdown("""<div style="margin-top:1.1rem;">
    <a class="cta-dark" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
    <a class="cta-out" href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
    <a class="cta-out" href="https://wa.me/5524992275226" target="_blank">💬 WhatsApp</a>
</div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# KPIs — st.columns nativo (funciona em mobile)
# ═══════════════════════════════════════════════════════════════
k1, k2, k3, k4 = st.columns(4)
for col, val, desc in [
    (k1, "20+",    "Anos de experiência\noperacional real"),
    (k2, "–70%",   "Tempo operacional\nBanco do Brasil (VBA)"),
    (k3, "2h→15'", "Ciclo de análise\notimizado"),
    (k4, "213K+",  "Registros\nprocessados"),
]:
    with col:
        st.markdown(f"""<div class="kpi">
            <div class="kpi-v">{val}</div>
            <div class="kpi-d">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SOBRE
# ═══════════════════════════════════════════════════════════════
st.markdown('<a id="sobre"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec"><span class="sec-n">01 ·</span><h2 class="sec-t">Sobre</h2></div>', unsafe_allow_html=True)

col_q, col_d = st.columns([3, 2], gap="large")
with col_q:
    st.markdown("""<div class="about-quote">
        Profissional com <strong>+20 anos de operação real</strong> — estoque, faturamento, agência bancária —
        que aprendeu dados na prática antes do termo "Data Analyst" existir.<br><br>
        Atuo na intersecção entre <strong>processo de negócio, indicadores e automação</strong>:
        transformo rotinas administrativas em dashboards acionáveis e decisões mais rápidas.
    </div>""", unsafe_allow_html=True)

with col_d:
    st.markdown("**O que me diferencia:**")
    st.markdown("""
- ✅ Entendo a rotina operacional — não só o dado
- ✅ Especialista em KPIs, controle de fluxo e saneamento
- ✅ Ponte entre operação e tecnologia
- ✅ Foco em resultado prático, sem buzzword
- ✅ Experiência corporativa verificável (BB, NSM)
- ✅ Disponível 100% remoto
    """)

# ═══════════════════════════════════════════════════════════════
# EXPERIÊNCIA — loop nativo, sem HTML interno problemático
# ═══════════════════════════════════════════════════════════════
st.markdown('<a id="experiencia"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec"><span class="sec-n">02 ·</span><h2 class="sec-t">Trajetória Profissional</h2></div>', unsafe_allow_html=True)

experiences = [
    {
        "period": "2014 — 2026",
        "company": "J Sintonía",
        "role": "Analista de KPIs & Operações",
        "badge": ("● POSIÇÃO ATUAL", "blue"),
        "current": True,
        "items": [
            "Monitoramento contínuo de KPIs de vendas, margem de contribuição e giro de estoque com dashboards em Power BI e Looker Studio",
            "Desenvolvimento de relatórios automatizados para suporte à gestão estratégica e tomada de decisão",
            "Aplicação de SQL e Python/Pandas para consolidação e análise de bases históricas",
        ]
    },
    {
        "period": "2009 — hoje",
        "company": "Jardim do Éden",
        "role": "Gestão Comercial & Dados",
        "badge": None,
        "current": True,
        "items": [
            "Estruturação de fluxo analítico: dashboards reduziram ciclo de análise de **2h para 15 min**",
            "SQL e automação para suporte a faturamento, margem de lucro e controle de estoque",
            "IA generativa aplicada à automação de tarefas operacionais repetitivas",
        ]
    },
    {
        "period": "2008 — 2010",
        "company": "Banco do Brasil",
        "role": "Estagiário de Dados & Automação",
        "badge": ("★ EXPERIÊNCIA CORPORATIVA VERIFICÁVEL", "red"),
        "current": False,
        "items": [
            "Automação de processos em **20 agências** utilizando Excel/VBA",
            "Consolidação e padronização de relatórios operacionais regionais",
            "Redução de **70% no tempo operacional** com macros e planilhas inteligentes",
        ]
    },
    {
        "period": "2002 — 2009",
        "company": "NSM Comércio e Serviço",
        "role": "Suporte Operacional & Controle Administrativo",
        "badge": ("◆ BASE: 7 ANOS DE OPERAÇÃO REAL", "red"),
        "current": False,
        "items": [
            "Centralização e organização de informações operacionais descentralizadas",
            "Controle de estoque, fluxo administrativo e saneamento de inconsistências",
            "Suporte à tomada de decisão com registros estruturados — BI analógico antes da digitalização",
        ]
    },
]

for exp in experiences:
    color = "#1a4480" if exp["current"] else "#c8392b"
    dot_size = "10px" if exp["current"] else "8px"
    dot_left = "-6px" if exp["current"] else "-5px"
    border_color = "#1a4480" if exp["current"] else "#e2e5eb"

    # cabeçalho do item
    left_col, right_col = st.columns([1, 4], gap="small")
    with left_col:
        st.markdown(f"""
        <div style="text-align:right;padding-top:0.1rem;">
            <span style="font-family:'DM Mono',monospace;font-size:0.66rem;color:{color};display:block;">{exp["period"]}</span>
            <span style="font-family:'DM Sans',sans-serif;font-weight:700;font-size:0.78rem;color:#2e3340;display:block;">{exp["company"]}</span>
        </div>""", unsafe_allow_html=True)

    with right_col:
        badge_html = ""
        if exp["badge"]:
            badge_text, badge_type = exp["badge"]
            badge_class = "tl-badge-blue" if badge_type == "blue" else "tl-badge-red"
            badge_html = f'<span class="tl-badge {badge_class}">{badge_text}</span><br>'

        st.markdown(f"""
        <div style="border-left:2px solid {border_color};padding-left:1.2rem;padding-bottom:1.2rem;position:relative;">
            <span style="position:absolute;left:{dot_left};top:8px;width:{dot_size};height:{dot_size};
                         background:{color};border-radius:50%;display:block;"></span>
            <div class="tl-role">{exp["role"]}</div>
            {badge_html}
        </div>""", unsafe_allow_html=True)

        # bullets via markdown nativo (sem HTML interno)
        with st.container():
            for item in exp["items"]:
                st.markdown(f"<div style='border-left:2px solid {border_color};padding-left:1.2rem;'>"
                            f"<p style='font-size:0.86rem;color:#2e3340;margin:0.15rem 0;padding-left:0;'>"
                            f"— {item}</p></div>", unsafe_allow_html=True)
            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# PROJETOS
# ═══════════════════════════════════════════════════════════════
st.markdown('<a id="projetos"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec"><span class="sec-n">03 ·</span><h2 class="sec-t">Projetos em Destaque</h2></div>', unsafe_allow_html=True)

projects = [
    {
        "idx": "Projeto 01 · Dashboard Público",
        "title": "Desenrola Brasil — Painel Executivo",
        "desc": "Dashboard com dados oficiais do Banco Central sobre o programa de renegociação de dívidas. KPIs, segmentação por região e valor, análise de padrões sobre 213K+ registros.",
        "tags": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "app": "https://desenrolabrasil.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/DESENROLA_BRASIL",
        "ghost": False,
    },
    {
        "idx": "Projeto 02 · Análise Social",
        "title": "Bolsa Família — Análise de Benefícios",
        "desc": "Dashboard analítico sobre distribuição de benefícios por região, faixa etária e valor médio. Filtros interativos para identificação de públicos prioritários.",
        "tags": ["Python", "Pandas", "Plotly", "Streamlit", "ETL"],
        "app": "https://bolsa-familia-kqrkzbzsrucybh3chpicxt.streamlit.app/",
        "code": "https://github.com/raphaelcaxias",
        "ghost": False,
    },
    {
        "idx": "Projeto 03 · Dados Regulatórios",
        "title": "ANP — Preços de Combustíveis",
        "desc": "Painel com dados públicos da ANP: filtros regionais dinâmicos, análise temporal de preços de combustíveis e comparações entre estados e municípios.",
        "tags": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app": None,
        "code": "https://github.com/raphaelcaxias/anp-combustiveis-dashboard",
        "ghost": False,
    },
    {
        "idx": "Em desenvolvimento ⚙️",
        "title": "Próximo Projeto",
        "desc": "Dashboard operacional de indicadores de gestão para PMEs — integração com fontes abertas e exportação automática de relatórios.",
        "tags": ["PostgreSQL", "Power BI", "Python", "Automação"],
        "app": None,
        "code": None,
        "ghost": True,
    },
]

pc1, pc2 = st.columns(2, gap="medium")
for i, p in enumerate(projects):
    col = pc1 if i % 2 == 0 else pc2
    tags_html = " ".join(f'<span class="proj-tag">{t}</span>' for t in p["tags"])
    ghost_style = "background:var(--cream);border:1px dashed #ccc;" if p["ghost"] else ""
    title_color = "color:var(--slate);" if p["ghost"] else ""
    links = ""
    if p.get("app"):
        links += f'<a class="proj-btn-d" href="{p["app"]}" target="_blank">↗ Ver App</a>'
    if p.get("code"):
        links += f'<a class="proj-btn-o" href="{p["code"]}" target="_blank">{{}} Código</a>'

    with col:
        st.markdown(f"""
<div class="proj-card" style="{ghost_style}">
    <div class="proj-idx">{p["idx"]}</div>
    <div class="proj-ttl" style="{title_color}">{p["title"]}</div>
    <p class="proj-desc">{p["desc"]}</p>
    <div>{tags_html}</div>
    <div style="margin-top:0.5rem;">{links}</div>
</div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# STACK — colunas nativas
# ═══════════════════════════════════════════════════════════════
st.markdown('<a id="stack"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec"><span class="sec-n">04 ·</span><h2 class="sec-t">Stack Técnica</h2></div>', unsafe_allow_html=True)

stack = [
    ("Dados & ETL", ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy", "ETL / Saneamento"]),
    ("BI & Visualização", ["Power BI", "Looker Studio", "Plotly", "Streamlit", "Excel Avançado"]),
    ("Análise Operacional", ["KPIs", "Controle de Fluxo", "Indicadores de Gestão", "Margem & Giro"]),
    ("Automação & Ferramentas", ["Excel / VBA", "Git", "IA Generativa", "Padronização de Processos"]),
]

sc1, sc2 = st.columns(2, gap="medium")
for i, (cat, items) in enumerate(stack):
    col = sc1 if i % 2 == 0 else sc2
    tags = " ".join(f'<span class="stack-tag">{it}</span>' for it in items)
    with col:
        st.markdown(f"""<div class="stack-box">
            <div class="stack-cat">{cat}</div>
            <div>{tags}</div>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# DASHBOARD DEMO INTERATIVO
# ═══════════════════════════════════════════════════════════════
st.markdown('<div class="sec"><span class="sec-n">★ ·</span><h2 class="sec-t">Demonstração Interativa</h2></div>', unsafe_allow_html=True)
st.caption("Exemplo do tipo de análise que construo — explore os filtros!")

tab1, tab2 = st.tabs(["📈 Vendas vs Meta", "🗺️ Distribuição Regional"])

with tab1:
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    vendas_base = [120, 145, 132, 168, 189, 201]
    meta_base = [130, 140, 145, 160, 180, 200]

    crescimento = st.slider("Simule crescimento de vendas (%)", -20, 50, 0, 5)
    vendas_adj = [int(v * (1 + crescimento/100)) for v in vendas_base]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=meses, y=meta_base, name='Meta', marker_color='#e2e5eb', opacity=0.8))
    fig.add_trace(go.Scatter(x=meses, y=vendas_adj, name='Realizado',
        mode='lines+markers', line=dict(color='#1a4480', width=3), marker=dict(size=9)))
    fig.update_layout(
        height=320, margin=dict(t=20, b=10, l=0, r=0),
        hovermode='x unified', legend=dict(orientation='h', y=1.08),
        plot_bgcolor='#fafaf8', paper_bgcolor='#fafaf8',
        yaxis=dict(gridcolor='#e2e5eb'), xaxis=dict(gridcolor='#e2e5eb'),
        barmode='overlay'
    )
    st.plotly_chart(fig, use_container_width=True)

    m1, m2, m3 = st.columns(3)
    total_real = sum(vendas_adj)
    total_meta = sum(meta_base)
    ating = total_real / total_meta * 100
    m1.metric("Total Realizado", f"{total_real}", f"{crescimento:+d}% ajuste")
    m2.metric("Atingimento da Meta", f"{ating:.1f}%", f"{ating-100:+.1f}pp")
    m3.metric("Melhor Mês", meses[vendas_adj.index(max(vendas_adj))], f"{max(vendas_adj)} un.")

with tab2:
    regioes = ['Sudeste', 'Nordeste', 'Sul', 'Centro-Oeste', 'Norte']
    valores = [42, 28, 15, 10, 5]
    cores = ['#1a4480', '#2c5f9e', '#4a7dbf', '#7aa3d4', '#adc6e8']

    fig2 = go.Figure(go.Pie(
        labels=regioes, values=valores,
        marker=dict(colors=cores),
        hole=0.45,
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>%{value}% dos registros<extra></extra>'
    ))
    fig2.update_layout(
        height=300, margin=dict(t=10, b=10, l=0, r=0),
        paper_bgcolor='#fafaf8',
        showlegend=False
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Distribuição simulada — baseada no perfil real dos dados processados.")

# ═══════════════════════════════════════════════════════════════
# FORMAÇÃO
# ═══════════════════════════════════════════════════════════════
st.markdown('<a id="formacao"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec"><span class="sec-n">05 ·</span><h2 class="sec-t">Formação &amp; Certificações</h2></div>', unsafe_allow_html=True)

ec1, ec2 = st.columns(2, gap="medium")

with ec1:
    st.markdown("""<div class="edu-box">
        <div class="edu-cat">Formação Acadêmica</div>
        <div class="edu-ttl">Sistemas de Informação</div>
        <div class="edu-sub">UniFOA — Centro Universitário de Volta Redonda</div>
        <div class="edu-ttl">Técnico em Informática</div>
        <div class="edu-sub">CIBA — Centro de Informática e Business Administration</div>
    </div>""", unsafe_allow_html=True)

with ec2:
    certs = [
        ("✓", "SQL para Análise de Dados — Hashtag Treinamentos"),
        ("✓", "Power BI Completo (Básico ao Avançado)"),
        ("✓", "Python para Análise de Dados (Pandas)"),
        ("✓", "Algoritmos e Lógica de Programação"),
        ("✓", "IA Aplicada a Negócios — Hashtag"),
        ("◆", "+20 anos de prática operacional em ambientes reais"),
    ]
    rows = "".join(f'<div class="cert-row"><span>{ico}</span><span>{txt}</span></div>' for ico, txt in certs)
    st.markdown(f'<div class="edu-box"><div class="edu-cat">Cursos &amp; Certificações</div>{rows}</div>',
                unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# CONTATO
# ═══════════════════════════════════════════════════════════════
st.markdown('<a id="contato"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec"><span class="sec-n">06 ·</span><h2 class="sec-t">Contato</h2></div>', unsafe_allow_html=True)

ct1, ct2 = st.columns([3, 2], gap="large")
with ct1:
    st.markdown("""<div class="contact-box">
        <div class="contact-h">Vamos trabalhar juntos?</div>
        <div class="contact-sub">
            Busco oportunidades como <strong style="color:white;">Analista de Dados Operacional</strong>,
            BI de Negócio ou Consultoria de Automação.<br><br>
            📧 <a href="mailto:raphael_caxias@hotmail.com">raphael_caxias@hotmail.com</a><br>
            📱 <a href="https://wa.me/5524992275226">(24) 99227-5226</a><br>
            📍 Volta Redonda – RJ · Disponível para remoto
        </div>
        <div style="margin-top:1.2rem;">
            <a class="clink" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
            <a class="clink" href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
            <a class="clink" href="https://desenrolabrasil.streamlit.app/" target="_blank">↗ Projeto ao Vivo</a>
            <a class="clink" href="https://wa.me/5524992275226" target="_blank">💬 WhatsApp</a>
        </div>
    </div>""", unsafe_allow_html=True)

with ct2:
    st.markdown("**Por que me contratar?**")
    st.info("🎯 Muitos sabem fazer gráfico bonito. Poucos entenderam a rotina de um estoque, um faturamento ou uma agência bancária. **Eu entendi.**")
    st.markdown("**Disponibilidade:**")
    st.success("✅ Disponível para trabalho remoto imediatamente")
    st.markdown("**Projetos online:**")
    st.markdown("""
- [🇧🇷 Desenrola Brasil →](https://desenrolabrasil.streamlit.app/)
- [🤝 Bolsa Família →](https://bolsa-familia-kqrkzbzsrucybh3chpicxt.streamlit.app/)
    """)

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("""<div class="foot">
    ◈ Raphael Fernando da Silva Pires · Analista Operacional de Dados &amp; BI ·
    <a href="https://github.com/raphaelcaxias/curriculo" style="color:#64748b;">
    github.com/raphaelcaxias/curriculo</a> · © 2026
</div>""", unsafe_allow_html=True)
