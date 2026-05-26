# -*- coding: utf-8 -*-
"""
Portfolio Profissional - Raphael Pires
Analista Operacional de Dados & BI
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import os
import requests
from io import BytesIO

st.set_page_config(
    page_title="Raphael Pires | Dados & BI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CSS
# =============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,400&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

:root {
    --ink:      #0d0f14;
    --ink-soft: #2e3340;
    --slate:    #64748b;
    --rule:     #e2e5eb;
    --paper:    #fafaf8;
    --cream:    #f4f1ea;
    --red:      #c8392b;
    --blue:     #1a4480;
    --gold:     #b5892a;
}
html, body, .stApp { background: var(--paper) !important; }
.stApp { font-family: 'DM Sans', system-ui, sans-serif; color: var(--ink); }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; max-width: 1060px; }

/* SIDEBAR */
[data-testid="stSidebar"] { background: #0d0f14 !important; }
[data-testid="stSidebar"] * { color: #b0b8c6 !important; font-family: 'DM Sans', sans-serif !important; }
[data-testid="stSidebar"] a { color: #e2c97e !important; }
[data-testid="stSidebar"] hr { border-color: #1e2430 !important; }
[data-testid="stSidebar"] .stDownloadButton button {
    background: #c8392b !important; color: white !important; border: none !important;
    font-family: 'DM Mono', monospace !important; font-size: 0.75rem !important;
    letter-spacing: 0.05em; border-radius: 3px !important;
}

/* HERO */
.hero { border-bottom: 3px double var(--rule); padding-bottom: 2rem; margin-bottom: 2rem; }
.hero-label { font-family: 'DM Mono', monospace; font-size: 0.7rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--red); margin-bottom: 0.75rem; }
.hero-name { font-family: 'Playfair Display', Georgia, serif; font-size: clamp(2.4rem, 5vw, 3.6rem); font-weight: 900; line-height: 1.05; color: var(--ink); margin-bottom: 0.6rem; letter-spacing: -1px; }
.hero-name em { font-style: italic; color: var(--blue); }
.hero-role { font-size: 1rem; font-weight: 300; color: var(--slate); border-left: 3px solid var(--red); padding-left: 0.75rem; margin: 1rem 0 1.25rem; line-height: 1.6; }
.hero-pills { display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 1.25rem; }
.hero-pill { font-family: 'DM Mono', monospace; font-size: 0.7rem; background: var(--cream); border: 1px solid var(--rule); color: var(--ink-soft); padding: 0.3rem 0.8rem; border-radius: 2px; }
.hero-ctas { display: flex; gap: 0.6rem; flex-wrap: wrap; }
.hero-btn-dark { background: var(--ink); color: white !important; padding: 0.65rem 1.4rem; text-decoration: none !important; font-weight: 600; font-size: 0.85rem; border-radius: 3px; }
.hero-btn-outline { background: transparent; color: var(--ink) !important; border: 1.5px solid var(--ink); padding: 0.65rem 1.4rem; text-decoration: none !important; font-weight: 500; font-size: 0.85rem; border-radius: 3px; }

/* KPI ROW */
.kpi-row { display: grid; grid-template-columns: repeat(4,1fr); gap: 1rem; margin-bottom: 0.5rem; }
.kpi { background: white; border: 1px solid var(--rule); border-top: 3px solid var(--blue); padding: 1.2rem; }
.kpi-val { font-family: 'Playfair Display', serif; font-size: 1.9rem; font-weight: 700; color: var(--ink); line-height: 1; margin-bottom: 0.3rem; }
.kpi-desc { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: var(--slate); text-transform: uppercase; letter-spacing: 0.04em; line-height: 1.5; }

/* SECTION HEADER */
.sec-hd { display: flex; align-items: baseline; gap: 0.75rem; margin: 2.5rem 0 1.25rem; border-top: 1px solid var(--rule); padding-top: 1rem; }
.sec-num { font-family: 'DM Mono', monospace; font-size: 0.68rem; color: var(--red); letter-spacing: 0.1em; }
.sec-title { font-family: 'Playfair Display', serif; font-size: 1.55rem; font-weight: 700; color: var(--ink); margin: 0; line-height: 1; }

/* ABOUT */
.about-wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; background: var(--cream); padding: 2rem; border-radius: 3px; }
.about-quote { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 400; line-height: 1.7; color: var(--ink-soft); border-left: 4px solid var(--red); padding-left: 1.2rem; }
.diff-list { list-style: none; padding: 0; margin: 0; }
.diff-list li { font-size: 0.88rem; padding: 0.45rem 0; border-bottom: 1px dashed var(--rule); color: var(--ink-soft); display: flex; gap: 0.5rem; }
.diff-list li:last-child { border-bottom: none; }

/* TIMELINE */
.tl-item { display: grid; grid-template-columns: 110px 1fr; gap: 1.5rem; margin-bottom: 1.75rem; }
.tl-left { text-align: right; padding-top: 0.15rem; }
.tl-period { font-family: 'DM Mono', monospace; font-size: 0.68rem; color: var(--red); letter-spacing: 0.04em; display: block; margin-bottom: 0.2rem; }
.tl-company { font-family: 'DM Sans', sans-serif; font-weight: 600; font-size: 0.78rem; color: var(--ink-soft); display: block; }
.tl-current .tl-period { color: var(--blue); }
.tl-right { border-left: 2px solid var(--rule); padding-left: 1.4rem; position: relative; }
.tl-right::before { content: ''; position: absolute; left: -5px; top: 8px; width: 8px; height: 8px; background: var(--red); border-radius: 50%; }
.tl-current .tl-right { border-left-color: var(--blue); }
.tl-current .tl-right::before { background: var(--blue); width: 10px; height: 10px; left: -6px; }
.tl-role { font-family: 'Playfair Display', serif; font-size: 1.05rem; font-weight: 700; color: var(--ink); }
.tl-badge { display: inline-block; background: #fff4f4; color: var(--red); border: 1px solid #fad2cf; font-family: 'DM Mono', monospace; font-size: 0.65rem; padding: 0.2rem 0.6rem; border-radius: 2px; margin: 0.4rem 0; letter-spacing: 0.04em; }
.tl-badge-blue { background: #edf2fb; color: var(--blue); border-color: #c3d4f0; }
.tl-list { list-style: none; padding: 0; margin: 0.6rem 0 0; }
.tl-list li { font-size: 0.86rem; color: var(--ink-soft); line-height: 1.65; padding: 0.2rem 0 0.2rem 1rem; position: relative; }
.tl-list li::before { content: '—'; position: absolute; left: 0; color: var(--slate); font-size: 0.75rem; top: 0.25rem; }

/* PROJECTS */
.proj { background: white; border: 1px solid var(--rule); padding: 1.4rem; position: relative; overflow: hidden; margin-bottom: 1rem; }
.proj::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--red), var(--blue)); }
.proj-idx { font-family: 'DM Mono', monospace; font-size: 0.63rem; color: var(--slate); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.6rem; }
.proj-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: var(--ink); margin-bottom: 0.5rem; line-height: 1.3; }
.proj-desc { font-size: 0.84rem; color: var(--slate); line-height: 1.65; margin-bottom: 0.8rem; }
.proj-tags { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 0.9rem; }
.proj-tag { font-family: 'DM Mono', monospace; font-size: 0.63rem; background: var(--cream); color: var(--ink-soft); padding: 0.2rem 0.55rem; border-radius: 2px; }
.proj-links { display: flex; gap: 0.5rem; }
.proj-btn { font-family: 'DM Sans', sans-serif; font-size: 0.78rem; font-weight: 600; text-decoration: none !important; padding: 0.4rem 0.9rem; border-radius: 3px; }
.proj-btn-dark { background: var(--ink); color: white !important; }
.proj-btn-outline { border: 1.5px solid var(--ink); color: var(--ink) !important; }
.proj-ghost { background: var(--cream); border: 1px dashed var(--rule); }
.proj-ghost .proj-title { color: var(--slate); }

/* STACK */
.stack-block { background: white; border: 1px solid var(--rule); padding: 1.1rem 1.3rem; margin-bottom: 1rem; }
.stack-cat { font-family: 'DM Mono', monospace; font-size: 0.63rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--red); margin-bottom: 0.7rem; }
.stack-items { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.stack-item { font-size: 0.82rem; font-weight: 500; background: var(--cream); color: var(--ink-soft); padding: 0.3rem 0.7rem; border-radius: 2px; border: 1px solid transparent; }

/* EDUCATION */
.edu-block { background: var(--cream); padding: 1.4rem; border-radius: 2px; }
.edu-cat { font-family: 'DM Mono', monospace; font-size: 0.63rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--red); margin-bottom: 1rem; }
.edu-item { margin-bottom: 0.9rem; padding-bottom: 0.9rem; border-bottom: 1px dashed var(--rule); }
.edu-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.edu-title { font-weight: 600; font-size: 0.88rem; color: var(--ink); }
.edu-sub { font-size: 0.78rem; color: var(--slate); margin-top: 0.15rem; }
.cert-item { font-size: 0.82rem; color: var(--ink-soft); padding: 0.35rem 0; border-bottom: 1px dashed var(--rule); display: flex; gap: 0.5rem; }
.cert-item:last-child { border-bottom: none; }

/* CONTACT */
.contact-box { background: var(--ink); color: white; padding: 2.5rem; border-radius: 3px; display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: center; }
.contact-heading { font-family: 'Playfair Display', serif; font-size: 1.55rem; font-weight: 700; color: white; margin-bottom: 0.5rem; }
.contact-sub { color: #8896a7; font-size: 0.86rem; line-height: 1.8; }
.contact-sub a { color: #e2c97e !important; text-decoration: none; }
.contact-links { display: flex; flex-direction: column; gap: 0.6rem; }
.contact-link { display: block; background: rgba(255,255,255,0.07); color: white !important; text-decoration: none !important; padding: 0.6rem 1.1rem; border-radius: 3px; font-size: 0.82rem; font-weight: 500; border: 1px solid rgba(255,255,255,0.1); white-space: nowrap; }

/* FOOTER */
.site-footer { border-top: 1px solid var(--rule); margin-top: 3rem; padding: 1.5rem 0; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; }
.site-footer span { font-family: 'DM Mono', monospace; font-size: 0.65rem; color: var(--slate); letter-spacing: 0.04em; }

@media (max-width: 768px) {
    .kpi-row { grid-template-columns: repeat(2,1fr); }
    .about-wrap { grid-template-columns: 1fr; }
    .tl-item { grid-template-columns: 1fr; }
    .tl-left { text-align: left; }
    .contact-box { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# LOADERS
# =============================================================================
@st.cache_data
def load_image():
    try:
        r = requests.get("https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/rapha.jpeg", timeout=5)
        if r.status_code == 200:
            return Image.open(BytesIO(r.content))
    except Exception:
        pass
    for p in ["rapha.jpeg", "assets/rapha.jpeg"]:
        if os.path.exists(p):
            return Image.open(p)
    return None

@st.cache_data
def load_cv():
    try:
        r = requests.get("https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/Curriculo_Raphael_Premium_Final.pdf", timeout=8)
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

# =============================================================================
# SIDEBAR
# =============================================================================
with st.sidebar:
    if profile_image:
        st.image(profile_image, use_column_width=True)
    else:
        st.image("https://via.placeholder.com/220x220/0d0f14/ffffff?text=RP", use_column_width=True)

    st.markdown("### 🧭 Navegação")
    st.markdown("""
- [Sobre](#sobre)
- [Experiência](#experiencia)
- [Projetos](#projetos)
- [Stack](#stack)
- [Formação](#formacao)
- [Contato](#contato)
    """)
    st.markdown("---")
    st.markdown("### 📥 Currículo")
    if cv_pdf:
        st.download_button("↓ Baixar PDF", data=cv_pdf,
                           file_name="Curriculo_Raphael_Pires.pdf",
                           mime="application/pdf", use_container_width=True)
    else:
        st.caption("PDF não localizado.")
    st.markdown("---")
    st.markdown("### 🔗 Contato")
    st.markdown("""
[LinkedIn →](https://linkedin.com/in/raphael-pires-caxias)  
[GitHub →](https://github.com/raphaelcaxias)  
[Email](mailto:raphael_caxias@hotmail.com)  
[(24) 99227-5226](https://wa.me/5524992275226)
    """)
    st.markdown("---")
    st.caption("Portfólio · 2026")

# =============================================================================
# HERO
# =============================================================================
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="hero-label">◈ Portfólio Profissional — Volta Redonda, RJ</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-name">Raphael <em>Pires</em></div>', unsafe_allow_html=True)
st.markdown('''<div class="hero-role">
    Analista Operacional de Dados &amp; Business Intelligence<br>
    <span style="font-size:0.9rem;">+20 anos de experiência real em gestão, automação e indicadores de negócio</span>
</div>''', unsafe_allow_html=True)
st.markdown('''<div class="hero-pills">
    <span class="hero-pill">SQL · PostgreSQL</span>
    <span class="hero-pill">Python · Pandas</span>
    <span class="hero-pill">Power BI · Looker Studio</span>
    <span class="hero-pill">Excel / VBA</span>
    <span class="hero-pill">Streamlit · Plotly</span>
    <span class="hero-pill">Remoto</span>
</div>''', unsafe_allow_html=True)
st.markdown('''<div class="hero-ctas">
    <a class="hero-btn-dark" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
    <a class="hero-btn-outline" href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
    <a class="hero-btn-outline" href="https://wa.me/5524992275226" target="_blank">💬 WhatsApp</a>
</div>''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# KPIs
# =============================================================================
st.markdown('<div class="kpi-row">', unsafe_allow_html=True)
kpis = [
    ("20+", "Anos de Experiência<br>Operacional Real"),
    ("–70%", "Tempo Operacional<br>Banco do Brasil (VBA)"),
    ("2h→15'", "Ciclo de Análise<br>Otimizado"),
    ("213K+", "Registros<br>Processados"),
]
for val, desc in kpis:
    st.markdown(f'<div class="kpi"><div class="kpi-val">{val}</div><div class="kpi-desc">{desc}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# SOBRE
# =============================================================================
st.markdown('<a id="sobre"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-hd"><span class="sec-num">01 ·</span><h2 class="sec-title">Sobre</h2></div>', unsafe_allow_html=True)
st.markdown('''<div class="about-wrap">
    <div class="about-quote">
        Profissional com <strong>+20 anos de operação real</strong> — estoque, faturamento, agência bancária —
        que aprendeu dados na prática antes do termo "Data Analyst" existir.<br><br>
        Atuo na intersecção entre <strong>processo de negócio, indicadores e automação</strong>:
        transformo rotinas administrativas em dashboards acionáveis e decisões mais rápidas.
    </div>
    <ul class="diff-list">
        <li><strong>✅</strong> Entendo a rotina operacional — não só o dado</li>
        <li><strong>✅</strong> Especialista em KPIs, controle de fluxo e saneamento</li>
        <li><strong>✅</strong> Ponte entre operação e tecnologia</li>
        <li><strong>✅</strong> Foco em resultado prático, não em buzzwords</li>
        <li><strong>✅</strong> Experiência corporativa verificável (BB, NSM)</li>
        <li><strong>✅</strong> Disponível para trabalho 100% remoto</li>
    </ul>
</div>''', unsafe_allow_html=True)

# =============================================================================
# EXPERIÊNCIA — mais recente primeiro, renderizado item a item
# =============================================================================
st.markdown('<a id="experiencia"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-hd"><span class="sec-num">02 ·</span><h2 class="sec-title">Trajetória Profissional</h2></div>', unsafe_allow_html=True)

experiences = [
    {
        "period": "2014 — 2026",
        "company": "J Sintonía",
        "role": "Analista de KPIs &amp; Operações",
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
        "role": "Gestão Comercial &amp; Dados",
        "badge": None,
        "current": True,
        "items": [
            "Estruturação de fluxo analítico comercial: dashboards reduziram ciclo de análise de <strong>2h para 15 min</strong>",
            "SQL e automação para suporte a faturamento, margem de lucro e controle de estoque",
            "IA generativa aplicada à automação de tarefas operacionais repetitivas",
        ]
    },
    {
        "period": "2008 — 2010",
        "company": "Banco do Brasil",
        "role": "Estagiário de Dados &amp; Automação",
        "badge": ("★ EXPERIÊNCIA CORPORATIVA VERIFICÁVEL", "red"),
        "current": False,
        "items": [
            "Automação de processos em <strong>20 agências</strong> utilizando Excel/VBA",
            "Consolidação e padronização de relatórios operacionais regionais",
            "Redução de <strong>70% no tempo operacional</strong> com macros e planilhas inteligentes",
        ]
    },
    {
        "period": "2002 — 2009",
        "company": "NSM Comércio e Serviço",
        "role": "Suporte Operacional &amp; Controle Administrativo",
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
    cls = "tl-item tl-current" if exp["current"] else "tl-item"
    period_color = "var(--blue)" if exp["current"] else "var(--red)"
    dot_color = "var(--blue)" if exp["current"] else "var(--red)"
    border_color = "var(--blue)" if exp["current"] else "var(--rule)"
    dot_size = "10px" if exp["current"] else "8px"
    dot_offset = "-6px" if exp["current"] else "-5px"

    badge_html = ""
    if exp["badge"]:
        badge_text, badge_color = exp["badge"]
        extra = " tl-badge-blue" if badge_color == "blue" else ""
        badge_html = f'<span class="tl-badge{extra}">{badge_text}</span>'

    items_html = "".join(f"<li>{it}</li>" for it in exp["items"])

    st.markdown(f'''
<div style="display:grid;grid-template-columns:110px 1fr;gap:1.5rem;margin-bottom:1.75rem;">
    <div style="text-align:right;padding-top:0.15rem;">
        <span style="font-family:DM Mono,monospace;font-size:0.68rem;color:{period_color};letter-spacing:0.04em;display:block;margin-bottom:0.2rem;">{exp["period"]}</span>
        <span style="font-family:DM Sans,sans-serif;font-weight:600;font-size:0.78rem;color:#2e3340;display:block;">{exp["company"]}</span>
    </div>
    <div style="border-left:2px solid {border_color};padding-left:1.4rem;position:relative;">
        <span style="position:absolute;left:{dot_offset};top:8px;width:{dot_size};height:{dot_size};background:{dot_color};border-radius:50%;display:block;"></span>
        <div style="font-family:Playfair Display,serif;font-size:1.05rem;font-weight:700;color:#0d0f14;">{exp["role"]}</div>
        {badge_html}
        <ul style="list-style:none;padding:0;margin:0.6rem 0 0;">
            {items_html}
        </ul>
    </div>
</div>
''', unsafe_allow_html=True)

# =============================================================================
# PROJETOS — renderizados em 2 colunas via st.columns
# =============================================================================
st.markdown('<a id="projetos"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-hd"><span class="sec-num">03 ·</span><h2 class="sec-title">Projetos em Destaque</h2></div>', unsafe_allow_html=True)

projects = [
    {
        "idx": "Projeto 01 · Dashboard Público",
        "title": "Desenrola Brasil — Painel Executivo",
        "desc": "Dashboard interativo com dados oficiais do Banco Central sobre o programa de renegociação de dívidas. KPIs, segmentação por região e valor, análise de padrões sobre 213K+ registros.",
        "tags": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "app": "https://desenrolabrasil.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/DESENROLA_BRASIL",
    },
    {
        "idx": "Projeto 02 · Análise Social",
        "title": "Bolsa Família — Análise de Benefícios",
        "desc": "Dashboard analítico sobre distribuição de benefícios por região, faixa etária e valor médio. Filtros interativos para análise estratégica e identificação de públicos prioritários.",
        "tags": ["Python", "Pandas", "Plotly", "Streamlit", "ETL"],
        "app": "https://bolsa-familia-kqrkzbzsrucybh3chpicxt.streamlit.app/",
        "code": "https://github.com/raphaelcaxias",
    },
    {
        "idx": "Projeto 03 · Dados Regulatórios",
        "title": "ANP — Preços de Combustíveis",
        "desc": "Painel com dados públicos da ANP: filtros regionais dinâmicos, análise temporal de preços de combustíveis no varejo brasileiro e comparações entre estados e municípios.",
        "tags": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app": None,
        "code": "https://github.com/raphaelcaxias/anp-combustiveis-dashboard",
    },
    {
        "idx": "Em desenvolvimento",
        "title": "Próximo Projeto",
        "desc": "Dashboard operacional de indicadores de gestão para PMEs — integração com fontes abertas e exportação automática de relatórios.",
        "tags": ["PostgreSQL", "Power BI", "Python", "Automação"],
        "app": None,
        "code": None,
        "ghost": True,
    },
]

col_a, col_b = st.columns(2, gap="medium")
for i, proj in enumerate(projects):
    col = col_a if i % 2 == 0 else col_b
    ghost = proj.get("ghost", False)
    tags_html = "".join(f'<span class="proj-tag">{t}</span>' for t in proj["tags"])
    links_html = ""
    if proj.get("app"):
        links_html += f'<a class="proj-btn proj-btn-dark" href="{proj["app"]}" target="_blank">&#8599; Ver App</a>'
    if proj.get("code"):
        links_html += f'<a class="proj-btn proj-btn-outline" href="{proj["code"]}" target="_blank">&#123;&#125; Código</a>'

    ghost_style = 'background:var(--cream);border:1px dashed var(--rule);' if ghost else ''
    title_style = 'color:var(--slate);' if ghost else ''

    with col:
        st.markdown(f'''
<div class="proj" style="{ghost_style}">
    <div class="proj-idx">{proj["idx"]}</div>
    <div class="proj-title" style="{title_style}">{proj["title"]}</div>
    <p class="proj-desc">{proj["desc"]}</p>
    <div class="proj-tags">{tags_html}</div>
    <div class="proj-links">{links_html}</div>
</div>
''', unsafe_allow_html=True)

# =============================================================================
# TECH STACK — 2 colunas via st.columns
# =============================================================================
st.markdown('<a id="stack"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-hd"><span class="sec-num">04 ·</span><h2 class="sec-title">Stack Técnica</h2></div>', unsafe_allow_html=True)

stack_data = [
    ("Dados & ETL", ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy", "ETL / Saneamento"]),
    ("BI & Visualização", ["Power BI", "Looker Studio", "Plotly", "Streamlit", "Excel Avançado"]),
    ("Análise Operacional", ["KPIs", "Controle de Fluxo", "Indicadores de Gestão", "Margem & Giro", "Faturamento"]),
    ("Automação & Ferramentas", ["Excel / VBA", "Git", "IA Generativa", "Padronização de Processos"]),
]

sc1, sc2 = st.columns(2, gap="medium")
for i, (cat, items) in enumerate(stack_data):
    col = sc1 if i % 2 == 0 else sc2
    items_html = "".join(f'<span class="stack-item">{it}</span>' for it in items)
    with col:
        st.markdown(f'''
<div class="stack-block">
    <div class="stack-cat">{cat}</div>
    <div class="stack-items">{items_html}</div>
</div>
''', unsafe_allow_html=True)

# =============================================================================
# FORMAÇÃO
# =============================================================================
st.markdown('<a id="formacao"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-hd"><span class="sec-num">05 ·</span><h2 class="sec-title">Formação &amp; Certificações</h2></div>', unsafe_allow_html=True)

ec1, ec2 = st.columns(2, gap="medium")
with ec1:
    st.markdown('''
<div class="edu-block">
    <div class="edu-cat">Formação Acadêmica</div>
    <div class="edu-item">
        <div class="edu-title">Sistemas de Informação</div>
        <div class="edu-sub">UniFOA — Centro Universitário de Volta Redonda</div>
    </div>
    <div class="edu-item">
        <div class="edu-title">Técnico em Informática</div>
        <div class="edu-sub">CIBA — Centro de Informática e Business Administration</div>
    </div>
</div>
''', unsafe_allow_html=True)

with ec2:
    certs = [
        ("✓", "SQL para Análise de Dados — Hashtag Treinamentos"),
        ("✓", "Power BI Completo (Básico ao Avançado) — Hashtag"),
        ("✓", "Python para Análise de Dados (Pandas) — Hashtag"),
        ("✓", "Algoritmos e Lógica de Programação — Hashtag"),
        ("✓", "IA Aplicada a Negócios — Hashtag Treinamentos"),
        ("◆", "+20 anos de prática operacional em ambientes reais"),
    ]
    items_html = "".join(f'<div class="cert-item"><span>{ico}</span><span>{txt}</span></div>' for ico, txt in certs)
    st.markdown(f'<div class="edu-block"><div class="edu-cat">Cursos &amp; Certificações</div>{items_html}</div>', unsafe_allow_html=True)

# =============================================================================
# CONTATO
# =============================================================================
st.markdown('<a id="contato"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-hd"><span class="sec-num">06 ·</span><h2 class="sec-title">Contato</h2></div>', unsafe_allow_html=True)
st.markdown('''
<div class="contact-box">
    <div>
        <div class="contact-heading">Vamos trabalhar juntos?</div>
        <div class="contact-sub">
            Busco oportunidades como <strong style="color:white;">Analista de Dados Operacional</strong>,
            BI de Negócio ou Consultoria de Automação.<br><br>
            📧 <a href="mailto:raphael_caxias@hotmail.com">raphael_caxias@hotmail.com</a><br>
            📱 <a href="https://wa.me/5524992275226">(24) 99227-5226</a><br>
            📍 Volta Redonda – RJ · Disponível para remoto
        </div>
    </div>
    <div class="contact-links">
        <a class="contact-link" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
        <a class="contact-link" href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
        <a class="contact-link" href="https://desenrolabrasil.streamlit.app/" target="_blank">↗ Projeto ao Vivo</a>
        <a class="contact-link" href="https://wa.me/5524992275226" target="_blank">💬 WhatsApp</a>
    </div>
</div>
''', unsafe_allow_html=True)

# =============================================================================
# DEMO INTERATIVA
# =============================================================================
with st.expander("📊 Demonstração — Análise Interativa de Vendas vs Meta", expanded=False):
    df_demo = pd.DataFrame({
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Vendas': [120, 145, 132, 168, 189, 201],
        'Meta':   [130, 140, 145, 160, 180, 200]
    })
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_demo['Mês'], y=df_demo['Vendas'], name='Realizado',
        mode='lines+markers', line=dict(color='#1a4480', width=3), marker=dict(size=8, color='#1a4480')))
    fig.add_trace(go.Scatter(x=df_demo['Mês'], y=df_demo['Meta'], name='Meta',
        mode='lines', line=dict(color='#c8392b', width=2, dash='dot')))
    fig.update_layout(
        title=dict(text='Vendas Realizadas vs Meta', font=dict(family='Georgia, serif', size=15)),
        height=310, margin=dict(t=45,b=10,l=0,r=0), hovermode='x unified',
        legend=dict(orientation='h', y=1.08),
        plot_bgcolor='#fafaf8', paper_bgcolor='#fafaf8',
        yaxis=dict(gridcolor='#e2e5eb'), xaxis=dict(gridcolor='#e2e5eb')
    )
    st.plotly_chart(fig, use_container_width=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Crescimento", "+67,5%", "+12,3%")
    c2.metric("Atingimento da Meta", "100,5%", "+0,5pp")
    c3.metric("Melhor Mês", "Junho", "201 unidades")

# =============================================================================
# FOOTER
# =============================================================================
st.markdown('''
<div class="site-footer">
    <span>◈ Raphael Fernando da Silva Pires · Analista Operacional de Dados &amp; BI</span>
    <span>Desenvolvido com Streamlit · <a href="https://github.com/raphaelcaxias/curriculo" target="_blank" style="color:#64748b;">github.com/raphaelcaxias/curriculo</a> · © 2026</span>
</div>
''', unsafe_allow_html=True)