# -*- coding: utf-8 -*-
"""
🎯 Portfólio Profissional - Raphael Pires
Analista Operacional de Dados & BI
GitHub: github.com/raphaelcaxias/curriculo
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import os
import requests
from io import BytesIO

# =============================================================================
# CONFIGURAÇÃO DA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Raphael Pires | Dados & BI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CSS PERSONALIZADO — ESTÉTICA EDITORIAL / REVISTA TÉCNICA
# =============================================================================
def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

        :root {
            --ink:      #0d0f14;
            --ink-soft: #2e3340;
            --slate:    #64748b;
            --rule:     #e2e5eb;
            --paper:    #fafaf8;
            --cream:    #f4f1ea;
            --accent:   #c8392b;       /* vermelho editorial */
            --accent2:  #1a4480;       /* azul profundo */
            --gold:     #b5892a;
            --mono:     'DM Mono', monospace;
            --serif:    'Playfair Display', Georgia, serif;
            --sans:     'DM Sans', system-ui, sans-serif;
        }

        /* ── Reset & Base ── */
        html, body, .stApp { background: var(--paper) !important; }
        .stApp { font-family: var(--sans); color: var(--ink); }

        /* Remove streamlit chrome */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding-top: 1rem !important; max-width: 1100px; }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background: var(--ink) !important;
            border-right: none !important;
        }
        [data-testid="stSidebar"] * { color: #c9cdd6 !important; }
        [data-testid="stSidebar"] a { color: #e2c97e !important; text-decoration: none; font-size: 0.85rem; }
        [data-testid="stSidebar"] a:hover { color: white !important; }
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] .sidebar-label {
            color: #ffffff !important;
            font-family: var(--mono) !important;
            font-size: 0.7rem !important;
            letter-spacing: 0.15em;
            text-transform: uppercase;
        }
        [data-testid="stSidebar"] hr { border-color: #2e3340 !important; }
        [data-testid="stSidebar"] .stDownloadButton button {
            background: var(--accent) !important;
            color: white !important;
            border: none !important;
            font-family: var(--mono) !important;
            font-size: 0.75rem !important;
            letter-spacing: 0.05em;
            border-radius: 3px !important;
            transition: opacity 0.2s;
        }
        [data-testid="stSidebar"] .stDownloadButton button:hover { opacity: 0.85; }

        /* ── HERO ── */
        .hero {
            border-bottom: 3px double var(--rule);
            padding-bottom: 2rem;
            margin-bottom: 2.5rem;
        }
        .hero-label {
            font-family: var(--mono);
            font-size: 0.7rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 0.75rem;
        }
        .hero-name {
            font-family: var(--serif);
            font-size: clamp(2.4rem, 5vw, 3.8rem);
            font-weight: 900;
            line-height: 1.05;
            color: var(--ink);
            margin-bottom: 0.6rem;
            letter-spacing: -1px;
        }
        .hero-name em {
            font-style: normal;
            color: var(--accent2);
        }
        .hero-role {
            font-family: var(--sans);
            font-size: 1.05rem;
            font-weight: 300;
            color: var(--slate);
            border-left: 3px solid var(--accent);
            padding-left: 0.75rem;
            margin: 1rem 0 1.5rem;
            line-height: 1.5;
        }
        .hero-pills { display: flex; gap: 0.5rem; flex-wrap: wrap; }
        .hero-pill {
            font-family: var(--mono);
            font-size: 0.72rem;
            background: var(--cream);
            border: 1px solid var(--rule);
            color: var(--ink-soft);
            padding: 0.35rem 0.9rem;
            border-radius: 2px;
            letter-spacing: 0.05em;
        }
        .hero-ctas { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem; }
        .hero-cta-primary {
            background: var(--ink);
            color: white !important;
            padding: 0.7rem 1.6rem;
            text-decoration: none !important;
            font-family: var(--sans);
            font-weight: 600;
            font-size: 0.85rem;
            border-radius: 3px;
            letter-spacing: 0.02em;
            transition: background 0.2s;
        }
        .hero-cta-primary:hover { background: var(--accent2) !important; }
        .hero-cta-secondary {
            background: transparent;
            color: var(--ink) !important;
            border: 1.5px solid var(--ink);
            padding: 0.7rem 1.6rem;
            text-decoration: none !important;
            font-family: var(--sans);
            font-weight: 500;
            font-size: 0.85rem;
            border-radius: 3px;
            transition: all 0.2s;
        }
        .hero-cta-secondary:hover { background: var(--ink) !important; color: white !important; }

        /* ── Section Headers ── */
        .section-header {
            display: flex;
            align-items: baseline;
            gap: 1rem;
            margin: 2.5rem 0 1.5rem;
            border-top: 1px solid var(--rule);
            padding-top: 1.2rem;
        }
        .section-number {
            font-family: var(--mono);
            font-size: 0.7rem;
            color: var(--accent);
            letter-spacing: 0.1em;
        }
        .section-title {
            font-family: var(--serif);
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--ink);
            margin: 0;
            line-height: 1;
        }

        /* ── About ── */
        .about-block {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            background: var(--cream);
            padding: 2rem;
            border-radius: 4px;
        }
        .about-quote {
            font-family: var(--serif);
            font-size: 1.25rem;
            font-weight: 400;
            line-height: 1.65;
            color: var(--ink-soft);
            border-left: 4px solid var(--accent);
            padding-left: 1.2rem;
        }
        .about-quote strong { color: var(--ink); }
        .about-differentials { padding-left: 0; list-style: none; }
        .about-differentials li {
            font-size: 0.9rem;
            padding: 0.5rem 0;
            border-bottom: 1px dashed var(--rule);
            color: var(--ink-soft);
            display: flex;
            gap: 0.5rem;
        }
        .about-differentials li:last-child { border-bottom: none; }

        /* ── KPI Cards ── */
        .kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }
        .kpi {
            background: white;
            border: 1px solid var(--rule);
            border-top: 3px solid var(--accent2);
            padding: 1.3rem 1.2rem;
            transition: box-shadow 0.2s;
        }
        .kpi:hover { box-shadow: 0 6px 24px rgba(0,0,0,0.08); }
        .kpi-val {
            font-family: var(--serif);
            font-size: 2rem;
            font-weight: 700;
            color: var(--ink);
            line-height: 1;
            margin-bottom: 0.4rem;
        }
        .kpi-desc {
            font-family: var(--mono);
            font-size: 0.68rem;
            color: var(--slate);
            letter-spacing: 0.05em;
            text-transform: uppercase;
            line-height: 1.5;
        }

        /* ── Timeline (Experiência) ── */
        .timeline { position: relative; padding-left: 0; }
        .tl-item {
            display: grid;
            grid-template-columns: 120px 1fr;
            gap: 1.5rem;
            margin-bottom: 2rem;
            position: relative;
        }
        .tl-left { text-align: right; padding-top: 0.2rem; }
        .tl-period {
            font-family: var(--mono);
            font-size: 0.72rem;
            color: var(--accent);
            letter-spacing: 0.05em;
            display: block;
            margin-bottom: 0.25rem;
        }
        .tl-company {
            font-family: var(--sans);
            font-weight: 600;
            font-size: 0.8rem;
            color: var(--ink-soft);
            display: block;
        }
        .tl-right {
            border-left: 2px solid var(--rule);
            padding-left: 1.5rem;
            position: relative;
        }
        .tl-right::before {
            content: '';
            position: absolute;
            left: -5px;
            top: 8px;
            width: 8px;
            height: 8px;
            background: var(--accent);
            border-radius: 50%;
        }
        .tl-role {
            font-family: var(--serif);
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--ink);
            margin-bottom: 0.2rem;
        }
        .tl-highlights {
            list-style: none;
            padding: 0;
            margin: 0.75rem 0 0;
        }
        .tl-highlights li {
            font-size: 0.88rem;
            color: var(--ink-soft);
            line-height: 1.6;
            padding: 0.25rem 0;
            padding-left: 1rem;
            position: relative;
        }
        .tl-highlights li::before {
            content: '—';
            position: absolute;
            left: 0;
            color: var(--slate);
            font-size: 0.75rem;
        }
        .tl-badge {
            display: inline-block;
            background: #fff4f4;
            color: var(--accent);
            border: 1px solid #fad2cf;
            font-family: var(--mono);
            font-size: 0.68rem;
            padding: 0.25rem 0.65rem;
            border-radius: 2px;
            margin: 0.5rem 0;
            letter-spacing: 0.04em;
        }
        .tl-current .tl-right { border-left-color: var(--accent2); }
        .tl-current .tl-right::before { background: var(--accent2); width: 10px; height: 10px; left: -6px; }
        .tl-current .tl-period { color: var(--accent2); }

        /* ── Projects ── */
        .projects-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; }
        .proj {
            background: white;
            border: 1px solid var(--rule);
            padding: 1.5rem;
            transition: all 0.25s;
            position: relative;
            overflow: hidden;
        }
        .proj::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent2) 100%);
        }
        .proj:hover { box-shadow: 0 12px 36px rgba(0,0,0,0.1); transform: translateY(-3px); }
        .proj-index {
            font-family: var(--mono);
            font-size: 0.65rem;
            color: var(--slate);
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }
        .proj-title {
            font-family: var(--serif);
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--ink);
            margin-bottom: 0.6rem;
            line-height: 1.3;
        }
        .proj-desc {
            font-size: 0.85rem;
            color: var(--slate);
            line-height: 1.65;
            margin-bottom: 1rem;
        }
        .proj-tags { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 1rem; }
        .proj-tag {
            font-family: var(--mono);
            font-size: 0.65rem;
            background: var(--cream);
            color: var(--ink-soft);
            padding: 0.2rem 0.6rem;
            border-radius: 2px;
        }
        .proj-links { display: flex; gap: 0.6rem; }
        .proj-link {
            font-family: var(--sans);
            font-size: 0.78rem;
            font-weight: 600;
            text-decoration: none !important;
            padding: 0.45rem 1rem;
            border-radius: 3px;
            transition: all 0.2s;
        }
        .proj-link-primary { background: var(--ink); color: white !important; }
        .proj-link-primary:hover { background: var(--accent2) !important; }
        .proj-link-secondary { border: 1.5px solid var(--ink); color: var(--ink) !important; }
        .proj-link-secondary:hover { background: var(--ink) !important; color: white !important; }

        /* ── Tech Stack ── */
        .stack-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }
        .stack-block {
            background: white;
            border: 1px solid var(--rule);
            padding: 1.2rem 1.4rem;
        }
        .stack-cat {
            font-family: var(--mono);
            font-size: 0.65rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 0.75rem;
        }
        .stack-items { display: flex; flex-wrap: wrap; gap: 0.4rem; }
        .stack-item {
            font-family: var(--sans);
            font-size: 0.82rem;
            font-weight: 500;
            background: var(--cream);
            color: var(--ink-soft);
            padding: 0.35rem 0.75rem;
            border-radius: 2px;
            border: 1px solid transparent;
            transition: all 0.15s;
        }
        .stack-item:hover { border-color: var(--accent2); color: var(--accent2); }

        /* ── Education ── */
        .edu-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
        .edu-block { background: var(--cream); padding: 1.5rem; border-radius: 2px; }
        .edu-block h4 {
            font-family: var(--mono);
            font-size: 0.68rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 1rem;
        }
        .edu-item { margin-bottom: 1rem; padding-bottom: 1rem; border-bottom: 1px dashed var(--rule); }
        .edu-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
        .edu-title { font-weight: 600; font-size: 0.9rem; color: var(--ink); }
        .edu-sub { font-size: 0.8rem; color: var(--slate); margin-top: 0.2rem; }
        .cert-item {
            font-size: 0.83rem;
            color: var(--ink-soft);
            padding: 0.35rem 0;
            border-bottom: 1px dashed var(--rule);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .cert-item:last-child { border-bottom: none; }

        /* ── Contact ── */
        .contact-block {
            background: var(--ink);
            color: white;
            padding: 2.5rem;
            border-radius: 4px;
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 2rem;
            align-items: center;
        }
        .contact-heading {
            font-family: var(--serif);
            font-size: 1.6rem;
            font-weight: 700;
            color: white;
            margin-bottom: 0.5rem;
        }
        .contact-sub { color: #8896a7; font-size: 0.88rem; line-height: 1.7; }
        .contact-sub a { color: #e2c97e !important; text-decoration: none; }
        .contact-links { display: flex; flex-direction: column; gap: 0.75rem; }
        .contact-link {
            display: block;
            background: rgba(255,255,255,0.08);
            color: white !important;
            text-decoration: none !important;
            padding: 0.65rem 1.2rem;
            border-radius: 3px;
            font-size: 0.83rem;
            font-weight: 500;
            font-family: var(--sans);
            border: 1px solid rgba(255,255,255,0.1);
            transition: background 0.2s;
            white-space: nowrap;
        }
        .contact-link:hover { background: rgba(255,255,255,0.15) !important; }

        /* ── Footer ── */
        .site-footer {
            border-top: 1px solid var(--rule);
            margin-top: 3rem;
            padding: 1.5rem 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .site-footer span {
            font-family: var(--mono);
            font-size: 0.68rem;
            color: var(--slate);
            letter-spacing: 0.05em;
        }

        /* ── Responsive ── */
        @media (max-width: 768px) {
            .kpi-row { grid-template-columns: repeat(2, 1fr); }
            .projects-grid { grid-template-columns: 1fr; }
            .about-block { grid-template-columns: 1fr; }
            .tl-item { grid-template-columns: 1fr; }
            .tl-left { text-align: left; }
            .contact-block { grid-template-columns: 1fr; }
            .edu-row { grid-template-columns: 1fr; }
            .stack-grid { grid-template-columns: 1fr; }
        }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# =============================================================================
# CARREGAMENTO DE ARQUIVOS
# =============================================================================
@st.cache_data
def load_image():
    try:
        img_url = "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/rapha.jpeg"
        response = requests.get(img_url, timeout=5)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
    except Exception:
        pass
    for path in ["rapha.jpeg", "assets/rapha.jpeg"]:
        if os.path.exists(path):
            return Image.open(path)
    return None

@st.cache_data
def load_cv():
    try:
        pdf_url = "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/Curriculo_Raphael_Premium_Final.pdf"
        response = requests.get(pdf_url, timeout=8)
        if response.status_code == 200:
            return response.content
    except Exception:
        pass
    for path in ["Curriculo_Raphael_Premium_Final.pdf", "assets/Curriculo_Raphael_Premium_Final.pdf"]:
        if os.path.exists(path):
            with open(path, "rb") as f:
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
        st.download_button(
            label="↓  Baixar PDF",
            data=cv_pdf,
            file_name="Curriculo_Raphael_Pires.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.caption("PDF não localizado.")

    st.markdown("---")
    st.markdown("### 🔗 Contato Direto")
    st.markdown("""
[LinkedIn →](https://linkedin.com/in/raphael-pires-caxias)  
[GitHub →](https://github.com/raphaelcaxias)  
[raphael_caxias@hotmail.com](mailto:raphael_caxias@hotmail.com)  
[(24) 99227-5226](https://wa.me/5524992275226)
    """)
    st.markdown("---")
    st.caption("Portfólio · 2026")

# =============================================================================
# CONTEÚDO PRINCIPAL
# =============================================================================

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-label">◈ Portfólio Profissional — Volta Redonda, RJ</div>
    <div class="hero-name">Raphael <em>Pires</em></div>
    <div class="hero-role">
        Analista Operacional de Dados & Business Intelligence<br>
        <span style="font-size:0.9rem;">+20 anos de experiência real em gestão, automação e indicadores de negócio</span>
    </div>
    <div class="hero-pills">
        <span class="hero-pill">SQL · PostgreSQL</span>
        <span class="hero-pill">Python · Pandas</span>
        <span class="hero-pill">Power BI · Looker Studio</span>
        <span class="hero-pill">Excel / VBA</span>
        <span class="hero-pill">Streamlit · Plotly</span>
        <span class="hero-pill">Remoto</span>
    </div>
    <div class="hero-ctas">
        <a class="hero-cta-primary" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
        <a class="hero-cta-secondary" href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
        <a class="hero-cta-secondary" href="https://wa.me/5524992275226" target="_blank">💬 WhatsApp</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── KPIs ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="kpi-row">
    <div class="kpi">
        <div class="kpi-val">20+</div>
        <div class="kpi-desc">Anos de Experiência<br>Operacional Real</div>
    </div>
    <div class="kpi">
        <div class="kpi-val">–70%</div>
        <div class="kpi-desc">Tempo Operacional<br>Banco do Brasil (VBA)</div>
    </div>
    <div class="kpi">
        <div class="kpi-val">2h→15'</div>
        <div class="kpi-desc">Ciclo de Análise<br>Otimizado (Dashboard)</div>
    </div>
    <div class="kpi">
        <div class="kpi-val">213K+</div>
        <div class="kpi-desc">Registros<br>Processados</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SOBRE ─────────────────────────────────────────────────────────────────────
st.markdown('<a id="sobre"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-number">01 ·</span>
    <h2 class="section-title">Sobre</h2>
</div>
<div class="about-block">
    <div class="about-quote">
        Profissional com <strong>+20 anos de operação real</strong> — estoque, faturamento, agência bancária —
        que aprendeu dados na prática antes do termo "Data Analyst" existir.<br><br>
        Atuo na intersecção entre <strong>processo de negócio, indicadores e automação</strong>:
        transformo rotinas administrativas em dashboards acionáveis e decisões mais rápidas.
    </div>
    <ul class="about-differentials">
        <li><strong>✅</strong> Entendo a rotina operacional — não só o dado</li>
        <li><strong>✅</strong> Especialista em KPIs, controle de fluxo e saneamento</li>
        <li><strong>✅</strong> Ponte entre operação e tecnologia</li>
        <li><strong>✅</strong> Foco em resultado prático, não em buzzwords</li>
        <li><strong>✅</strong> Experiência corporativa verificável (BB, NSM)</li>
        <li><strong>✅</strong> Disponível para trabalho 100% remoto</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── EXPERIÊNCIA ───────────────────────────────────────────────────────────────
st.markdown('<a id="experiencia"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-number">02 ·</span>
    <h2 class="section-title">Trajetória Profissional</h2>
</div>

<div class="timeline">

    <!-- J Sintonía — mais recente -->
    <div class="tl-item tl-current">
        <div class="tl-left">
            <span class="tl-period">2014 — 2026</span>
            <span class="tl-company">J Sintonía</span>
        </div>
        <div class="tl-right">
            <div class="tl-role">Analista de KPIs & Operações</div>
            <span class="tl-badge">● POSIÇÃO ATUAL</span>
            <ul class="tl-highlights">
                <li>Monitoramento contínuo de KPIs de vendas, margem de contribuição e giro de estoque com dashboards em Power BI e Looker Studio</li>
                <li>Desenvolvimento de relatórios automatizados para suporte à gestão estratégica e tomada de decisão</li>
                <li>Aplicação de SQL e Python/Pandas para consolidação e análise de bases históricas</li>
            </ul>
        </div>
    </div>

    <!-- Jardim do Éden -->
    <div class="tl-item tl-current">
        <div class="tl-left">
            <span class="tl-period">2009 — hoje</span>
            <span class="tl-company">Jardim do Éden</span>
        </div>
        <div class="tl-right">
            <div class="tl-role">Gestão Comercial & Dados</div>
            <ul class="tl-highlights">
                <li>Estruturação de fluxo analítico comercial: dashboards reduziram ciclo de análise de <strong>2h para 15 min</strong></li>
                <li>SQL e automação para suporte a faturamento, margem de lucro e controle de estoque</li>
                <li>IA generativa aplicada à automação de tarefas operacionais repetitivas</li>
            </ul>
        </div>
    </div>

    <!-- Banco do Brasil -->
    <div class="tl-item">
        <div class="tl-left">
            <span class="tl-period">2008 — 2010</span>
            <span class="tl-company">Banco do Brasil</span>
        </div>
        <div class="tl-right">
            <div class="tl-role">Estagiário de Dados & Automação</div>
            <span class="tl-badge">★ EXPERIÊNCIA CORPORATIVA VERIFICÁVEL</span>
            <ul class="tl-highlights">
                <li>Automação de processos em <strong>20 agências</strong> utilizando Excel/VBA</li>
                <li>Consolidação e padronização de relatórios operacionais regionais</li>
                <li>Redução de <strong>70% no tempo operacional</strong> com macros e planilhas inteligentes</li>
            </ul>
        </div>
    </div>

    <!-- NSM -->
    <div class="tl-item">
        <div class="tl-left">
            <span class="tl-period">2002 — 2009</span>
            <span class="tl-company">NSM Comércio e Serviço</span>
        </div>
        <div class="tl-right">
            <div class="tl-role">Suporte Operacional & Controle Administrativo</div>
            <span class="tl-badge">◆ BASE: 7 ANOS DE OPERAÇÃO REAL</span>
            <ul class="tl-highlights">
                <li>Centralização e organização de informações operacionais descentralizadas</li>
                <li>Controle de estoque, fluxo administrativo e saneamento de inconsistências</li>
                <li>Suporte à tomada de decisão com registros estruturados — "BI analógico" antes da digitalização</li>
            </ul>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

# ── PROJETOS ──────────────────────────────────────────────────────────────────
st.markdown('<a id="projetos"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-number">03 ·</span>
    <h2 class="section-title">Projetos em Destaque</h2>
</div>
<div class="projects-grid">

    <div class="proj">
        <div class="proj-index">Projeto 01 · Dashboard Público</div>
        <div class="proj-title">Desenrola Brasil — Painel Executivo</div>
        <p class="proj-desc">Dashboard interativo com dados oficiais do Banco Central sobre o programa de renegociação de dívidas. KPIs, segmentação por região e valor, análise de padrões sobre 213K+ registros.</p>
        <div class="proj-tags">
            <span class="proj-tag">Python</span><span class="proj-tag">Pandas</span>
            <span class="proj-tag">Plotly</span><span class="proj-tag">Streamlit</span>
            <span class="proj-tag">PostgreSQL</span>
        </div>
        <div class="proj-links">
            <a class="proj-link proj-link-primary" href="https://desenrolabrasil.streamlit.app/" target="_blank">↗ Ver App</a>
            <a class="proj-link proj-link-secondary" href="https://github.com/raphaelcaxias/DESENROLA_BRASIL" target="_blank">{ } Código</a>
        </div>
    </div>

    <div class="proj">
        <div class="proj-index">Projeto 02 · Análise Social</div>
        <div class="proj-title">Bolsa Família — Análise de Benefícios</div>
        <p class="proj-desc">Dashboard analítico sobre distribuição de benefícios por região, faixa etária e valor médio. Filtros interativos para análise estratégica e identificação de públicos prioritários.</p>
        <div class="proj-tags">
            <span class="proj-tag">Python</span><span class="proj-tag">Pandas</span>
            <span class="proj-tag">Plotly</span><span class="proj-tag">Streamlit</span>
            <span class="proj-tag">ETL</span>
        </div>
        <div class="proj-links">
            <a class="proj-link proj-link-primary" href="https://bolsa-familia-kqrkzbzsrucybh3chpicxt.streamlit.app/" target="_blank">↗ Ver App</a>
            <a class="proj-link proj-link-secondary" href="https://github.com/raphaelcaxias" target="_blank">{ } Código</a>
        </div>
    </div>

    <div class="proj">
        <div class="proj-index">Projeto 03 · Dados Regulatórios</div>
        <div class="proj-title">ANP — Preços de Combustíveis</div>
        <p class="proj-desc">Painel com dados públicos da ANP: filtros regionais dinâmicos, análise temporal de preços de combustíveis no varejo brasileiro e comparações entre estados e municípios.</p>
        <div class="proj-tags">
            <span class="proj-tag">Python</span><span class="proj-tag">Pandas</span>
            <span class="proj-tag">Plotly</span><span class="proj-tag">Streamlit</span>
        </div>
        <div class="proj-links">
            <a class="proj-link proj-link-secondary" href="https://github.com/raphaelcaxias/anp-combustiveis-dashboard" target="_blank">{ } Ver Código</a>
        </div>
    </div>

    <div class="proj" style="background: var(--cream); border-style: dashed;">
        <div class="proj-index">Em desenvolvimento</div>
        <div class="proj-title" style="color: var(--slate);">Próximo Projeto</div>
        <p class="proj-desc" style="color: var(--slate);">Dashboard operacional de indicadores de gestão para pequenas e médias empresas — integração com fontes abertas e exportação automática de relatórios.</p>
        <div class="proj-tags">
            <span class="proj-tag">PostgreSQL</span><span class="proj-tag">Power BI</span>
            <span class="proj-tag">Python</span><span class="proj-tag">Automação</span>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

# ── TECH STACK ────────────────────────────────────────────────────────────────
st.markdown('<a id="stack"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-number">04 ·</span>
    <h2 class="section-title">Stack Técnica</h2>
</div>
<div class="stack-grid">
    <div class="stack-block">
        <div class="stack-cat">Dados & ETL</div>
        <div class="stack-items">
            <span class="stack-item">SQL</span>
            <span class="stack-item">PostgreSQL</span>
            <span class="stack-item">Python</span>
            <span class="stack-item">Pandas</span>
            <span class="stack-item">NumPy</span>
            <span class="stack-item">ETL / Saneamento</span>
        </div>
    </div>
    <div class="stack-block">
        <div class="stack-cat">BI & Visualização</div>
        <div class="stack-items">
            <span class="stack-item">Power BI</span>
            <span class="stack-item">Looker Studio</span>
            <span class="stack-item">Plotly</span>
            <span class="stack-item">Streamlit</span>
            <span class="stack-item">Excel Avançado</span>
        </div>
    </div>
    <div class="stack-block">
        <div class="stack-cat">Análise Operacional</div>
        <div class="stack-items">
            <span class="stack-item">KPIs</span>
            <span class="stack-item">Controle de Fluxo</span>
            <span class="stack-item">Indicadores de Gestão</span>
            <span class="stack-item">Margem & Giro</span>
            <span class="stack-item">Faturamento</span>
        </div>
    </div>
    <div class="stack-block">
        <div class="stack-cat">Automação & Ferramentas</div>
        <div class="stack-items">
            <span class="stack-item">Excel / VBA</span>
            <span class="stack-item">Git</span>
            <span class="stack-item">IA Generativa</span>
            <span class="stack-item">Padronização de Processos</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FORMAÇÃO ──────────────────────────────────────────────────────────────────
st.markdown('<a id="formacao"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-number">05 ·</span>
    <h2 class="section-title">Formação & Certificações</h2>
</div>
<div class="edu-row">
    <div class="edu-block">
        <h4>Formação Acadêmica</h4>
        <div class="edu-item">
            <div class="edu-title">Sistemas de Informação</div>
            <div class="edu-sub">UniFOA — Centro Universitário de Volta Redonda</div>
        </div>
        <div class="edu-item">
            <div class="edu-title">Técnico em Informática</div>
            <div class="edu-sub">CIBA — Centro de Informática e Business Administration</div>
        </div>
    </div>
    <div class="edu-block">
        <h4>Cursos & Certificações</h4>
        <div class="cert-item">✓ <span>SQL para Análise de Dados — Hashtag Treinamentos</span></div>
        <div class="cert-item">✓ <span>Power BI Completo (Básico ao Avançado) — Hashtag</span></div>
        <div class="cert-item">✓ <span>Python para Análise de Dados (Pandas) — Hashtag</span></div>
        <div class="cert-item">✓ <span>Algoritmos e Lógica de Programação — Hashtag</span></div>
        <div class="cert-item">✓ <span>IA Aplicada a Negócios — Hashtag Treinamentos</span></div>
        <div class="cert-item">◆ <span>+20 anos de prática operacional em ambientes reais</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CONTATO ───────────────────────────────────────────────────────────────────
st.markdown('<a id="contato"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-number">06 ·</span>
    <h2 class="section-title">Contato</h2>
</div>
<div class="contact-block">
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
        <a class="contact-link" href="https://desenrolabrasil.streamlit.app/" target="_blank">↗ Projeto Ao Vivo</a>
        <a class="contact-link" href="https://wa.me/5524992275226" target="_blank">💬 WhatsApp</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── DEMO INTERATIVA ───────────────────────────────────────────────────────────
with st.expander("📊 Demonstração — Análise Interativa de Vendas vs Meta", expanded=False):
    df_demo = pd.DataFrame({
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Vendas': [120, 145, 132, 168, 189, 201],
        'Meta':   [130, 140, 145, 160, 180, 200]
    })
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_demo['Mês'], y=df_demo['Vendas'], name='Realizado',
        mode='lines+markers',
        line=dict(color='#1a4480', width=3),
        marker=dict(size=8, color='#1a4480')
    ))
    fig.add_trace(go.Scatter(
        x=df_demo['Mês'], y=df_demo['Meta'], name='Meta',
        mode='lines',
        line=dict(color='#c8392b', width=2, dash='dot')
    ))
    fig.update_layout(
        title=dict(text='Vendas Realizadas vs Meta — Semestre', font=dict(family='Georgia, serif', size=16)),
        height=320,
        margin=dict(t=50, b=20, l=0, r=0),
        hovermode='x unified',
        legend=dict(orientation='h', y=1.08),
        plot_bgcolor='#fafaf8',
        paper_bgcolor='#fafaf8',
        yaxis=dict(gridcolor='#e2e5eb'),
        xaxis=dict(gridcolor='#e2e5eb')
    )
    st.plotly_chart(fig, use_container_width=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Crescimento", "+67,5%", "+12,3% vs período anterior")
    c2.metric("Atingimento da Meta", "100,5%", "+0,5pp")
    c3.metric("Melhor Mês", "Junho", "201 unidades")

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="site-footer">
    <span>◈ Raphael Fernando da Silva Pires · Analista Operacional de Dados & BI</span>
    <span>Desenvolvido com Streamlit · <a href="https://github.com/raphaelcaxias/curriculo" target="_blank" style="color:#64748b;">github.com/raphaelcaxias/curriculo</a> · © 2026</span>
</div>
""", unsafe_allow_html=True)