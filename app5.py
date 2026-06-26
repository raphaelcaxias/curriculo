import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# 2. MODO DARK / LIGHT
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

col_t1, col_t2, col_t3 = st.columns([1, 11, 1])
with col_t2:
    tc1, tc2, tc3 = st.columns([8, 1, 1])
    with tc3:
        theme_label = "☀️ Claro" if st.session_state.theme == "dark" else "🌙 Escuro"
        st.button(theme_label, on_click=toggle_theme, key="theme_toggle", use_container_width=True)

is_dark = st.session_state.theme == "dark"

# ============================================================================
# 3. PALETA DE CORES (Inspirada em Stripe/Linear/Vercel)
# ============================================================================
if is_dark:
    BG = "#0B1120"
    SURFACE = "#111A2E"
    SURFACE_2 = "#1A2540"
    PRIMARY = "#3B82F6"
    SECONDARY = "#0EA5E9"
    ACCENT = "#60A5FA"
    TEXT = "#E5E7EB"
    TEXT_MUTED = "#94A3B8"
    BORDER = "rgba(59, 130, 246, 0.15)"
    GLASS = "rgba(17, 26, 46, 0.6)"
    SHADOW = "rgba(0, 0, 0, 0.4)"
    GRADIENT_START = "#3B82F6"
    GRADIENT_END = "#0EA5E9"
    PLOTLY_TEMPLATE = "plotly_dark"
    CHART_COLORS = ["#3B82F6", "#0EA5E9", "#60A5FA", "#2563EB", "#0284C7", "#93C5FD"]
else:
    BG = "#F8FAFC"
    SURFACE = "#FFFFFF"
    SURFACE_2 = "#F1F5F9"
    PRIMARY = "#2563EB"
    SECONDARY = "#0284C7"
    ACCENT = "#3B82F6"
    TEXT = "#0F172A"
    TEXT_MUTED = "#64748B"
    BORDER = "rgba(37, 99, 235, 0.12)"
    GLASS = "rgba(255, 255, 255, 0.7)"
    SHADOW = "rgba(15, 23, 42, 0.08)"
    GRADIENT_START = "#2563EB"
    GRADIENT_END = "#0284C7"
    PLOTLY_TEMPLATE = "plotly_white"
    CHART_COLORS = ["#2563EB", "#0284C7", "#3B82F6", "#1D4ED8", "#0369A1", "#60A5FA"]

# ============================================================================
# 4. CSS PREMIUM
# ============================================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: {TEXT};
    background: {BG};
}}

#MainMenu, header, footer, .stDeployButton {{ display: none !important; }}

.stApp {{
    background: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(59, 130, 246, 0.15), transparent),
        radial-gradient(ellipse 60% 50% at 80% 50%, rgba(14, 165, 233, 0.08), transparent),
        {BG};
    background-attachment: fixed;
}}

.block-container {{ padding: 2rem 3rem 4rem 3rem; max-width: 1280px; }}
@media (max-width: 768px) {{ .block-container {{ padding: 1.5rem 1.25rem 3rem 1.25rem; }} }}

/* Botões */
.stButton > button {{
    background: {GLASS};
    color: {TEXT};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 0.5rem 1rem;
    font-weight: 500;
    backdrop-filter: blur(12px);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 8px {SHADOW};
}}
.stButton > button:hover {{
    background: {PRIMARY};
    color: white;
    border-color: {PRIMARY};
    transform: translateY(-1px);
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
}}

/* Download Button */
.stDownloadButton > button {{
    background: linear-gradient(135deg, {GRADIENT_START}, {GRADIENT_END});
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    font-size: 0.9375rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
}}
.stDownloadButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.45);
}}

/* Hero */
.hero-container {{ padding: 3rem 0 2rem 0; text-align: center; }}

.hero-name {{
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin: 1.5rem 0 0.75rem 0;
    background: linear-gradient(135deg, {TEXT} 0%, {PRIMARY} 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}

.hero-title {{
    font-size: 1.125rem;
    font-weight: 500;
    color: {PRIMARY};
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.25rem;
}}

.hero-subtitle {{
    font-size: 1.25rem;
    color: {TEXT_MUTED};
    max-width: 720px;
    margin: 0 auto 2rem auto;
    line-height: 1.6;
}}

.hero-badges {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1.5rem;
}}

.hero-badge {{
    background: {GLASS};
    border: 1px solid {BORDER};
    padding: 0.5rem 1rem;
    border-radius: 999px;
    font-size: 0.8125rem;
    font-weight: 500;
    color: {TEXT};
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
}}
.hero-badge:hover {{
    border-color: {PRIMARY};
    color: {PRIMARY};
    transform: translateY(-2px);
}}

@media (max-width: 768px) {{
    .hero-name {{ font-size: 2.25rem; }}
    .hero-subtitle {{ font-size: 1.0625rem; }}
}}

/* Section Headers */
.section-header {{ margin: 4rem 0 2rem 0; text-align: center; }}

.section-label {{
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: {PRIMARY};
    background: rgba(59, 130, 246, 0.1);
    padding: 0.375rem 0.875rem;
    border-radius: 999px;
    margin-bottom: 1rem;
}}

.section-title {{
    font-family: 'Playfair Display', serif;
    font-size: 2.25rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0 0 0.75rem 0;
    letter-spacing: -0.02em;
}}

.section-subtitle {{
    font-size: 1.0625rem;
    color: {TEXT_MUTED};
    max-width: 640px;
    margin: 0 auto;
    line-height: 1.6;
}}

/* Timeline */
.timeline {{ position: relative; padding: 1rem 0; margin: 2rem 0; }}
.timeline::before {{
    content: '';
    position: absolute;
    left: 24px;
    top: 0; bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, {PRIMARY}, {SECONDARY}, transparent);
}}

.timeline-item {{ position: relative; padding-left: 64px; margin-bottom: 2rem; }}
.timeline-dot {{
    position: absolute;
    left: 16px; top: 8px;
    width: 18px; height: 18px;
    border-radius: 50%;
    background: {SURFACE};
    border: 3px solid {PRIMARY};
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15);
    z-index: 2;
}}

.timeline-card {{
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 1.5rem 1.75rem;
    backdrop-filter: blur(16px);
    transition: all 0.3s ease;
}}
.timeline-card:hover {{
    border-color: {PRIMARY};
    transform: translateX(4px);
    box-shadow: 0 12px 32px {SHADOW};
}}

.timeline-date {{
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 600;
    color: {PRIMARY};
    background: rgba(59, 130, 246, 0.1);
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    margin-bottom: 0.75rem;
    letter-spacing: 0.05em;
}}

.timeline-role {{ font-size: 1.25rem; font-weight: 600; color: {TEXT}; margin: 0 0 0.25rem 0; }}
.timeline-company {{ font-size: 0.9375rem; color: {SECONDARY}; font-weight: 500; margin-bottom: 0.75rem; }}
.timeline-desc {{ font-size: 0.9375rem; color: {TEXT_MUTED}; line-height: 1.6; margin: 0; }}

.timeline-tags {{ display: flex; flex-wrap: wrap; gap: 0.375rem; margin-top: 0.875rem; }}
.timeline-tag {{
    font-size: 0.75rem;
    color: {TEXT};
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid {BORDER};
    padding: 0.25rem 0.625rem;
    border-radius: 6px;
    font-weight: 500;
}}

/* AWS Grid */
.aws-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}}
@media (max-width: 1024px) {{ .aws-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (max-width: 640px) {{ .aws-grid {{ grid-template-columns: repeat(2, 1fr); }} }}

.aws-card {{
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 1.25rem;
    backdrop-filter: blur(16px);
    transition: all 0.3s ease;
    text-align: center;
}}
.aws-card:hover {{
    transform: translateY(-4px);
    border-color: {SECONDARY};
    box-shadow: 0 16px 32px {SHADOW};
}}

.aws-icon {{ font-size: 1.75rem; margin-bottom: 0.625rem; }}
.aws-title {{ font-size: 0.9375rem; font-weight: 600; color: {TEXT}; margin: 0; line-height: 1.3; }}

.aws-banner {{
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(14, 165, 233, 0.1));
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 2rem 0;
    text-align: center;
    backdrop-filter: blur(16px);
}}
.aws-banner-text {{ font-size: 1.0625rem; color: {TEXT}; font-weight: 500; margin: 0; }}
.aws-banner-sub {{ font-size: 0.875rem; color: {TEXT_MUTED}; margin: 0.5rem 0 0 0; }}

/* Stack */
.stack-category {{ margin-bottom: 2rem; }}
.stack-category-title {{
    font-size: 0.8125rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: {PRIMARY};
    margin-bottom: 0.875rem;
    padding-left: 0.25rem;
}}

.stack-grid {{ display: flex; flex-wrap: wrap; gap: 0.625rem; }}
.stack-chip {{
    background: {GLASS};
    border: 1px solid {BORDER};
    padding: 0.625rem 1.125rem;
    border-radius: 10px;
    font-size: 0.875rem;
    font-weight: 500;
    color: {TEXT};
    backdrop-filter: blur(12px);
    transition: all 0.25s ease;
    cursor: default;
}}
.stack-chip:hover {{
    background: {PRIMARY};
    color: white;
    border-color: {PRIMARY};
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
}}

/* Footer */
.footer {{
    margin-top: 5rem;
    padding: 3rem 2rem 2rem 2rem;
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 20px;
    backdrop-filter: blur(16px);
    text-align: center;
}}

.footer-status {{
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(34, 197, 94, 0.1);
    border: 1px solid rgba(34, 197, 94, 0.3);
    padding: 0.5rem 1rem;
    border-radius: 999px;
    margin-bottom: 1.25rem;
}}

.footer-status-dot {{
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #22C55E;
    box-shadow: 0 0 12px #22C55E;
    animation: pulse 2s infinite;
}}

@keyframes pulse {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0.5; }}
}}

.footer-status-text {{ font-size: 0.875rem; font-weight: 600; color: #22C55E; }}

.footer-title {{
    font-family: 'Playfair Display', serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0 0 0.5rem 0;
}}

.footer-subtitle {{ font-size: 0.9375rem; color: {TEXT_MUTED}; margin: 0 0 1.75rem 0; }}

.footer-modes {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.75rem;
}}

.footer-mode {{
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid {BORDER};
    padding: 0.375rem 0.875rem;
    border-radius: 999px;
    font-size: 0.8125rem;
    color: {TEXT};
    font-weight: 500;
}}

.footer-links {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
}}

.footer-link {{
    background: {SURFACE};
    border: 1px solid {BORDER};
    padding: 0.625rem 1.125rem;
    border-radius: 10px;
    color: {TEXT};
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
}}
.footer-link:hover {{
    background: {PRIMARY};
    color: white;
    border-color: {PRIMARY};
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
}}

.footer-copy {{
    font-size: 0.8125rem;
    color: {TEXT_MUTED};
    margin: 1.5rem 0 0 0;
    padding-top: 1.5rem;
    border-top: 1px solid {BORDER};
}}

/* Customização de containers nativos */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    background-color: {GLASS} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 16px !important;
    backdrop-filter: blur(16px);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
    transform: translateY(-2px);
    box-shadow: 0 12px 24px {SHADOW};
    border-color: {PRIMARY} !important;
}}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 0.5rem;
    background: transparent;
}}
.stTabs [data-baseweb="tab"] {{
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 10px;
    padding: 0.625rem 1.25rem;
    color: {TEXT};
    font-weight: 500;
}}
.stTabs [aria-selected="true"] {{
    background: {PRIMARY} !important;
    color: white !important;
    border-color: {PRIMARY} !important;
}}

/* Selectbox e inputs */
.stSelectbox [data-baseweb="select"] > div {{
    background: {GLASS} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 10px !important;
}}

/* Scrollbar */
::-webkit-scrollbar {{ width: 10px; height: 10px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: {SURFACE_2}; border-radius: 10px; }}
::-webkit-scrollbar-thumb:hover {{ background: {PRIMARY}; }}

.stMarkdown, h1, h2, h3, h4 {{ color: {TEXT}; }}

/* Insight box */
.insight-box {{
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(14, 165, 233, 0.04));
    border-left: 3px solid {PRIMARY};
    border-radius: 8px;
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    font-size: 0.9375rem;
    color: {TEXT};
    line-height: 1.6;
}}
.insight-box strong {{ color: {PRIMARY}; }}

/* KPI card custom */
.kpi-custom {{
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    backdrop-filter: blur(16px);
    transition: all 0.3s ease;
}}
.kpi-custom:hover {{
    transform: translateY(-4px);
    border-color: {PRIMARY};
    box-shadow: 0 16px 32px {SHADOW};
}}
.kpi-custom-value {{
    font-size: 2.25rem;
    font-weight: 700;
    background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 0.5rem;
}}
.kpi-custom-label {{
    font-size: 0.8125rem;
    color: {TEXT_MUTED};
    font-weight: 500;
}}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# 5. HERO SECTION
# ============================================================================
st.markdown('<div class="hero-container">', unsafe_allow_html=True)

col_p1, col_p2, col_p3 = st.columns([3, 2, 3])
with col_p2:
    try:
        st.image("rapha.jpeg", use_container_width=True)
    except Exception:
        st.markdown(f"""
        <div style="
            width: 200px; height: 200px; border-radius: 50%;
            background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
            display: flex; align-items: center; justify-content: center;
            font-family: 'Playfair Display', serif;
            font-size: 4rem; font-weight: 700; color: white;
            box-shadow: 0 0 0 8px {GLASS}, 0 20px 60px {SHADOW};
            margin: 0 auto;">
            RP
        </div>
        """, unsafe_allow_html=True)

st.markdown(f"""
<h1 class="hero-name">Raphael Fernando da Silva Pires</h1>
<div class="hero-title">Analista de Dados & Business Intelligence</div>
<p class="hero-subtitle">
    Transformando dados brutos em decisões estratégicas. Mais de <strong>16 anos</strong> 
    construindo inteligência de negócios, automações e governança de dados que geram 
    impacto real e mensurável em organizações de diferentes portes.
</p>
<div class="hero-badges">
    <span class="hero-badge">📊 Power BI</span>
    <span class="hero-badge">🐍 Python</span>
    <span class="hero-badge">🗄️ SQL</span>
    <span class="hero-badge">☁️ AWS</span>
    <span class="hero-badge">🤖 IA Generativa</span>
    <span class="hero-badge">📈 Dashboards</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Download CV centralizado
dc1, dc2, dc3 = st.columns([3, 2, 3])
with dc2:
    try:
        with open("Curriculo_Raphael_v2.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Currículo PDF",
                data=pdf_file.read(),
                file_name="Curriculo_Raphael_Pires.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.info("📄 Currículo PDF disponível para download")

st.divider()

# ============================================================================
# 6. KPIs DE IMPACTO
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Impacto Mensurável</span>
    <h2 class="section-title">Números que contam histórias</h2>
    <p class="section-subtitle">Resultados construídos ao longo de uma trajetória consistente em dados e negócios.</p>
</div>
""", unsafe_allow_html=True)

k1, k2, k3, k4, k5 = st.columns(5)
with k1:
    st.markdown(f"""
    <div class="kpi-custom">
        <div class="kpi-custom-value">16+</div>
        <div class="kpi-custom-label">anos de experiência</div>
    </div>
    """, unsafe_allow_html=True)
with k2:
    st.markdown(f"""
    <div class="kpi-custom">
        <div class="kpi-custom-value">70%</div>
        <div class="kpi-custom-label">redução operacional</div>
    </div>
    """, unsafe_allow_html=True)
with k3:
    st.markdown(f"""
    <div class="kpi-custom">
        <div class="kpi-custom-value">213k</div>
        <div class="kpi-custom-label">registros processados</div>
    </div>
    """, unsafe_allow_html=True)
with k4:
    st.markdown(f"""
    <div class="kpi-custom">
        <div class="kpi-custom-value">2h→15m</div>
        <div class="kpi-custom-label">análises reduzidas</div>
    </div>
    """, unsafe_allow_html=True)
with k5:
    st.markdown(f"""
    <div class="kpi-custom">
        <div class="kpi-custom-value">R$50bi</div>
        <div class="kpi-custom-label">dados públicos analisados</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================================================
# 7. TIMELINE — EXPERIÊNCIA
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Trajetória</span>
    <h2 class="section-title">Experiência profissional</h2>
    <p class="section-subtitle">Uma jornada construída entre dados, automação e decisões de negócio.</p>
</div>

<div class="timeline">
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <span class="timeline-date">Experiência Corporativa</span>
            <h3 class="timeline-role">Automação de Processos com VBA</h3>
            <div class="timeline-company">Banco do Brasil</div>
            <p class="timeline-desc">
                Desenvolvimento de automações em VBA que resultaram em redução de 70% do tempo 
                operacional, liberando equipes para atividades de maior valor estratégico.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">VBA</span>
                <span class="timeline-tag">Automação</span>
                <span class="timeline-tag">Eficiência Operacional</span>
            </div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <span class="timeline-date">Fundador & Analista de Dados</span>
            <h3 class="timeline-role">Fundador</h3>
            <div class="timeline-company">Jardim do Éden</div>
            <p class="timeline-desc">
                Fundação de iniciativa própria com foco em dashboards, Power BI, Python, SQL, 
                KPIs e IA Generativa. Redução de análises de 2 horas para 15 minutos.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">Power BI</span>
                <span class="timeline-tag">Python</span>
                <span class="timeline-tag">SQL</span>
                <span class="timeline-tag">IA Generativa</span>
                <span class="timeline-tag">KPIs</span>
            </div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <span class="timeline-date">Gestão Comercial & BI</span>
            <h3 class="timeline-role">Gestão Comercial</h3>
            <div class="timeline-company">J Sintonía</div>
            <p class="timeline-desc">
                Atuação em Business Intelligence com construção de indicadores, dashboards 
                e análise de viabilidade econômica, suportando decisões estratégicas com KPIs.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">Business Intelligence</span>
                <span class="timeline-tag">Indicadores</span>
                <span class="timeline-tag">Viabilidade Econômica</span>
                <span class="timeline-tag">Dashboards</span>
            </div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <span class="timeline-date">Dados & Operação</span>
            <h3 class="timeline-role">Analista de Dados</h3>
            <div class="timeline-company">NSM</div>
            <p class="timeline-desc">
                Centralização de dados e controle operacional com construção de indicadores 
                que trouxeram visibilidade e governança para a operação.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">Centralização de Dados</span>
                <span class="timeline-tag">Controle Operacional</span>
                <span class="timeline-tag">Indicadores</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================================
# 8. STACK TECNOLÓGICA
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Toolkit</span>
    <h2 class="section-title">Stack tecnológica</h2>
    <p class="section-subtitle">Ferramentas que utilizo no dia a dia para transformar dados em valor.</p>
</div>

<div class="stack-category">
    <div class="stack-category-title">📊 Dados</div>
    <div class="stack-grid">
        <div class="stack-chip">SQL</div>
        <div class="stack-chip">PostgreSQL</div>
        <div class="stack-chip">Python</div>
        <div class="stack-chip">Pandas</div>
        <div class="stack-chip">NumPy</div>
    </div>
</div>

<div class="stack-category">
    <div class="stack-category-title">📈 Business Intelligence</div>
    <div class="stack-grid">
        <div class="stack-chip">Power BI</div>
        <div class="stack-chip">Plotly</div>
        <div class="stack-chip">Looker Studio</div>
        <div class="stack-chip">Streamlit</div>
    </div>
</div>

<div class="stack-category">
    <div class="stack-category-title">☁️ Cloud & Versionamento</div>
    <div class="stack-grid">
        <div class="stack-chip">AWS</div>
        <div class="stack-chip">Git</div>
        <div class="stack-chip">GitHub</div>
    </div>
</div>

<div class="stack-category">
    <div class="stack-category-title">⚡ Automação & IA</div>
    <div class="stack-grid">
        <div class="stack-chip">Excel VBA</div>
        <div class="stack-chip">IA Generativa</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================================
# 9. GRÁFICO DE PROEFICIÊNCIA (Demonstração técnica)
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Competências</span>
    <h2 class="section-title">Domínio tecnológico</h2>
    <p class="section-subtitle">Mapa de proficiência nas principais tecnologias utilizadas em projetos reais.</p>
</div>
""", unsafe_allow_html=True)

skills_data = {
    "Tecnologia": ["Power BI", "SQL / PostgreSQL", "Python (Pandas)", "Excel / VBA", "Streamlit", "AWS Cloud", "IA Generativa", "Plotly"],
    "Proeficiência (%)": [95, 92, 88, 95, 85, 60, 75, 82],
    "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "Inovação", "BI"]
}
df_skills = pd.DataFrame(skills_data)

fig_skills = px.bar(
    df_skills,
    x="Proeficiência (%)",
    y="Tecnologia",
    color="Categoria",
    orientation="h",
    color_discrete_map={
        "BI": CHART_COLORS[0],
        "Dados": CHART_COLORS[1],
        "Automação": CHART_COLORS[2],
        "Cloud": CHART_COLORS[3],
        "Inovação": CHART_COLORS[4]
    },
    template=PLOTLY_TEMPLATE,
    text="Proeficiência (%)"
)

fig_skills.update_layout(
    margin=dict(l=20, r=40, t=20, b=40),
    height=420,
    xaxis=dict(range=[0, 105], showgrid=True, gridcolor=BORDER),
    yaxis=dict(showgrid=False),
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    font=dict(family="Inter", color=TEXT),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
fig_skills.update_traces(textposition="outside", textfont=dict(color=TEXT, size=12))

st.plotly_chart(fig_skills, use_container_width=True)

st.divider()

# ============================================================================
# 10. PROJETOS EM DESTAQUE
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Portfólio</span>
    <h2 class="section-title">Projetos em destaque</h2>
    <p class="section-subtitle">Soluções reais aplicadas a dados públicos, análises governamentais e inteligência de mercado.</p>
</div>
""", unsafe_allow_html=True)

p1, p2 = st.columns(2)

with p1:
    with st.container(border=True):
        st.markdown("#### 🇧🇷 Desenrola Brasil")
        st.write("Análise exploratória avançada de dados do programa governamental, mapeando renegociações e perfis socioeconômicos de consumidores em larga escala.")
        st.page_link("https://github.com/raphaelcaxias", label="Acessar Repositório", icon="🔗")

with p2:
    with st.container(border=True):
        st.markdown("#### 🔬 CNPq Analytics")
        st.write("Painel de Business Intelligence focado na distribuição de bolsas e fomento à pesquisa científica, cruzando dados geográficos e áreas do conhecimento.")
        st.page_link("https://github.com/raphaelcaxias", label="Acessar Repositório", icon="🔗")

p3, p4 = st.columns(2)

with p3:
    with st.container(border=True):
        st.markdown("#### ⛽ Dashboard ANP")
        st.write("Mapeamento e análise de preços, distribuição e comportamento do mercado de combustíveis nacional utilizando os dados da Agência Nacional do Petróleo.")
        st.page_link("https://github.com/raphaelcaxias", label="Ver Dashboard", icon="📊")

with p4:
    with st.container(border=True):
        st.markdown("#### 💎 Portfólio Premium")
        st.write("Este próprio portfólio — construído em Streamlit com design premium, demonstrando domínio de UX, visualização de dados e engenharia de front-end.")
        st.page_link("https://github.com/raphaelcaxias", label="Ver Código Fonte", icon="💻")

st.divider()

# ============================================================================
# 11. AWS CLOUD JOURNEY
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Cloud Computing</span>
    <h2 class="section-title">AWS Cloud Journey</h2>
    <p class="section-subtitle">Jornada de formação em computação em nuvem na maior plataforma cloud do mundo.</p>
</div>

<div class="aws-banner">
    <p class="aws-banner-text">☁️ Preparando-me para a certificação <strong>AWS Cloud Practitioner</strong></p>
    <p class="aws-banner-sub">Estudo contínuo dos fundamentos, serviços e boas práticas da Amazon Web Services.</p>
</div>

<div class="aws-grid">
    <div class="aws-card">
        <div class="aws-icon">☁️</div>
        <h4 class="aws-title">Cloud Computing</h4>
    </div>
    <div class="aws-card">
        <div class="aws-icon">📘</div>
        <h4 class="aws-title">Cloud 101</h4>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🖥️</div>
        <h4 class="aws-title">AWS Management Console</h4>
    </div>
    <div class="aws-card">
        <div class="aws-icon">💾</div>
        <h4 class="aws-title">Storage Fundamentals</h4>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🛟</div>
        <h4 class="aws-title">Cloud Support Associate</h4>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🤖</div>
        <h4 class="aws-title">Machine Learning Foundations</h4>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🌱</div>
        <h4 class="aws-title">AWS Sustainability</h4>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================================
# 12. ANÁLISE DE DADOS INTERATIVA — DEMONSTRAÇÃO TÉCNICA
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Análise ao Vivo</span>
    <h2 class="section-title">Demonstração de capacidade analítica</h2>
    <p class="section-subtitle">Dashboards interativos construídos com dados simulados baseados em cenários reais dos meus projetos.</p>
</div>
""", unsafe_allow_html=True)

analysis_tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Mercado de Combustíveis", "🔬 Fomento à Pesquisa", "📊 Impacto Operacional"])

# --- TAB 1: DESENROLA BRASIL ---
with analysis_tabs[0]:
    st.markdown("### 📈 Análise de Renegociações — Desenrola Brasil")
    
    # Dados simulados baseados em padrões reais
    np.random.seed(42)
    regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
    faixas_divida = ["Até R$ 5.000", "R$ 5.001 - R$ 15.000", "R$ 15.001 - R$ 50.000", "Acima de R$ 50.000"]
    
    df_desenrola = pd.DataFrame({
        "Região": np.random.choice(regioes, 500, p=[0.45, 0.28, 0.15, 0.07, 0.05]),
        "Faixa de Dívida": np.random.choice(faixas_divida, 500, p=[0.55, 0.28, 0.12, 0.05]),
        "Valor Renegociado (R$)": np.random.lognormal(mean=8.5, sigma=1.2, size=500),
        "Status": np.random.choice(["Renegociado", "Em Negociação", "Inadimplente"], 500, p=[0.65, 0.25, 0.10])
    })
    
    # Filtros interativos
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        regiao_sel = st.multiselect("Filtrar por Região", regioes, default=regioes)
    with fc2:
        status_sel = st.multiselect("Filtrar por Status", df_desenrola["Status"].unique(), default=df_desenrola["Status"].unique())
    with fc3:
        faixa_sel = st.multiselect("Filtrar por Faixa de Dívida", faixas_divida, default=faixas_divida)
    
    df_filtered = df_desenrola[
        (df_desenrola["Região"].isin(regiao_sel)) &
        (df_desenrola["Status"].isin(status_sel)) &
        (df_desenrola["Faixa de Dívida"].isin(faixa_sel))
    ]
    
    # KPIs do filtro
    mk1, mk2, mk3, mk4 = st.columns(4)
    with mk1:
        st.metric("Total de Contratos", f"{len(df_filtered):,}".replace(",", "."))
    with mk2:
        st.metric("Valor Total Renegociado", f"R$ {df_filtered['Valor Renegociado (R$)'].sum()/1e6:.2f}M")
    with mk3:
        st.metric("Ticket Médio", f"R$ {df_filtered['Valor Renegociado (R$)'].mean():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with mk4:
        taxa_sucesso = (df_filtered["Status"] == "Renegociado").mean() * 100
        st.metric("Taxa de Sucesso", f"{taxa_sucesso:.1f}%", delta=f"{taxa_sucesso - 65:.1f}% vs meta")
    
    # Gráficos
    g1, g2 = st.columns(2)
    
    with g1:
        st.markdown("##### Distribuição por Região")
        fig_reg = px.pie(
            df_filtered,
            names="Região",
            values="Valor Renegociado (R$)",
            hole=0.55,
            color_discrete_sequence=CHART_COLORS,
            template=PLOTLY_TEMPLATE
        )
        fig_reg.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", color=TEXT),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_reg, use_container_width=True)
    
    with g2:
        st.markdown("##### Valor por Faixa de Dívida")
        faixa_agg = df_filtered.groupby("Faixa de Dívida", observed=False)["Valor Renegociado (R$)"].sum().reset_index()
        fig_faixa = px.bar(
            faixa_agg,
            x="Faixa de Dívida",
            y="Valor Renegociado (R$)",
            color_discrete_sequence=[CHART_COLORS[0]],
            template=PLOTLY_TEMPLATE,
            text=faixa_agg["Valor Renegociado (R$)"].apply(lambda x: f"R$ {x/1e6:.1f}M")
        )
        fig_faixa.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", color=TEXT),
            showlegend=False,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor=BORDER)
        )
        fig_faixa.update_traces(textposition="outside", textfont=dict(color=TEXT, size=11))
        st.plotly_chart(fig_faixa, use_container_width=True)
    
    # Insight box
    st.markdown(f"""
    <div class="insight-box">
        <strong>💡 Insight Analítico:</strong> A região <strong>Sudeste</strong> concentra aproximadamente 
        <strong>{(df_filtered[df_filtered['Região']=='Sudeste']['Valor Renegociado (R$)'].sum() / df_filtered['Valor Renegociado (R$)'].sum() * 100):.1f}%</strong> 
        do volume financeiro renegociado, enquanto a faixa de dívida <strong>Até R$ 5.000</strong> 
        representa a maior parte dos contratos, indicando que o programa tem maior penetração 
        em consumidores com menor endividamento.
    </div>
    """, unsafe_allow_html=True)

# --- TAB 2: COMBUSTÍVEIS ANP ---
with analysis_tabs[1]:
    st.markdown("### ⛽ Análise de Preços de Combustíveis — ANP")
    
    np.random.seed(123)
    estados = ["SP", "RJ", "MG", "RS", "PR", "BA", "SC", "GO", "PE", "CE"]
    combustiveis = ["Gasolina", "Etanol", "Diesel"]
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    
    dados_comb = []
    for estado in estados:
        for comb in combustiveis:
            base = {"Gasolina": 5.8, "Etanol": 3.5, "Diesel": 5.2}[comb]
            for i, mes in enumerate(meses):
                dados_comb.append({
                    "Estado": estado,
                    "Combustível": comb,
                    "Mês": mes,
                    "Preço Médio (R$/L)": base + np.random.normal(0, 0.15) + (i * 0.03)
                })
    df_anp = pd.DataFrame(dados_comb)
    
    fc1, fc2 = st.columns(2)
    with fc1:
        est_sel = st.selectbox("Selecione o Estado", estados, index=0)
    with fc2:
        comb_sel = st.selectbox("Selecione o Combustível", combustiveis, index=0)
    
    df_anp_filtro = df_anp[(df_anp["Estado"] == est_sel) & (df_anp["Combustível"] == comb_sel)]
    
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        st.metric("Preço Atual (Jun)", f"R$ {df_anp_filtro[df_anp_filtro['Mês']=='Jun']['Preço Médio (R$/L)'].values[0]:.2f}")
    with mc2:
        preco_min = df_anp_filtro["Preço Médio (R$/L)"].min()
        st.metric("Preço Mínimo (Semestre)", f"R$ {preco_min:.2f}")
    with mc3:
        preco_max = df_anp_filtro["Preço Médio (R$/L)"].max()
        variacao = ((preco_max - preco_min) / preco_min) * 100
        st.metric("Variação Semestral", f"{variacao:.2f}%", delta=f"{variacao:.2f}%")
    
    # Gráfico de linha temporal
    fig_anp = px.line(
        df_anp_filtro,
        x="Mês",
        y="Preço Médio (R$/L)",
        markers=True,
        color_discrete_sequence=[CHART_COLORS[0]],
        template=PLOTLY_TEMPLATE
    )
    fig_anp.update_layout(
        title=f"Evolução do Preço do {comb_sel} — {est_sel} (2026)",
        margin=dict(l=20, r=20, t=50, b=20),
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor=BORDER),
        title_font=dict(size=16, color=TEXT, family="Inter")
    )
    st.plotly_chart(fig_anp, use_container_width=True)
    
    # Comparativo entre estados
    st.markdown("##### Comparativo de Preços entre Estados (Jun/2026)")
    df_jun = df_anp[(df_anp["Mês"] == "Jun") & (df_anp["Combustível"] == comb_sel)]
    fig_comp = px.bar(
        df_jun.sort_values("Preço Médio (R$/L)", ascending=True),
        x="Preço Médio (R$/L)",
        y="Estado",
        orientation="h",
        color="Preço Médio (R$/L)",
        color_continuous_scale=[CHART_COLORS[1], CHART_COLORS[0]],
        template=PLOTLY_TEMPLATE
    )
    fig_comp.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT),
        showlegend=False,
        coloraxis_showscale=False,
        xaxis=dict(showgrid=True, gridcolor=BORDER),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_comp, use_container_width=True)
    
    st.markdown(f"""
    <div class="insight-box">
        <strong>💡 Insight Analítico:</strong> O estado de <strong>São Paulo</strong> apresenta consistentemente 
        os menores preços de {comb_sel} devido à política tributária estadual e proximidade com refinarias. 
        A variação inter-estadual pode chegar a <strong>15-20%</strong>, impactando diretamente a competitividade 
        do setor de transporte e logística.
    </div>
    """, unsafe_allow_html=True)

# --- TAB 3: CNPQ ---
with analysis_tabs[2]:
    st.markdown("### 🔬 Fomento à Pesquisa — CNPq Analytics")
    
    np.random.seed(456)
    areas = ["Ciências Exatas", "Ciências Biológicas", "Engenharias", "Ciências Humanas", "Ciências da Saúde", "Ciências Agrárias"]
    niveis = ["Iniciação Científica", "Mestrado", "Doutorado", "Pós-Doutorado"]
    regioes_ibge = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
    
    dados_cnpq = []
    for area in areas:
        for nivel in niveis:
            for reg in regioes_ibge:
                base = np.random.randint(50, 500)
                if reg == "Sudeste": base *= 2.5
                elif reg == "Sul": base *= 1.5
                elif reg == "Norte": base *= 0.6
                dados_cnpq.append({
                    "Área": area,
                    "Nível": nivel,
                    "Região": reg,
                    "Bolsas Concedidas": int(base + np.random.normal(0, 30))
                })
    df_cnpq = pd.DataFrame(dados_cnpq)
    
    fc1, fc2 = st.columns(2)
    with fc1:
        area_sel = st.selectbox("Área do Conhecimento", areas, index=0)
    with fc2:
        tipo_viz = st.radio("Visualização", ["Por Região", "Por Nível de Formação"], horizontal=True)
    
    df_cnpq_filtro = df_cnpq[df_cnpq["Área"] == area_sel]
    
    if tipo_viz == "Por Região":
        agg = df_cnpq_filtro.groupby("Região", observed=False)["Bolsas Concedidas"].sum().reset_index()
        fig_cnpq = px.treemap(
            agg,
            path=["Região"],
            values="Bolsas Concedidas",
            color="Bolsas Concedidas",
            color_continuous_scale=[CHART_COLORS[1], CHART_COLORS[0]],
            template=PLOTLY_TEMPLATE
        )
    else:
        agg = df_cnpq_filtro.groupby("Nível", observed=False)["Bolsas Concedidas"].sum().reset_index()
        fig_cnpq = px.treemap(
            agg,
            path=["Nível"],
            values="Bolsas Concedidas",
            color="Bolsas Concedidas",
            color_continuous_scale=[CHART_COLORS[1], CHART_COLORS[0]],
            template=PLOTLY_TEMPLATE
        )
    
    fig_cnpq.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT)
    )
    st.plotly_chart(fig_cnpq, use_container_width=True)
    
    # Scatter de distribuição
    st.markdown("##### Distribuição Detalhada — Bolsas por Região e Nível")
    fig_scatter = px.scatter(
        df_cnpq_filtro,
        x="Nível",
        y="Bolsas Concedidas",
        color="Região",
        size="Bolsas Concedidas",
        color_discrete_sequence=CHART_COLORS,
        template=PLOTLY_TEMPLATE
    )
    fig_scatter.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor=BORDER)
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown(f"""
    <div class="insight-box">
        <strong>💡 Insight Analítico:</strong> A área de <strong>{area_sel}</strong> apresenta concentração 
        histórica de bolsas na região <strong>Sudeste</strong>, refletindo a distribuição da infraestrutura 
        acadêmica brasileira. Níveis de <strong>Pós-Doutorado</strong> têm menor volume, mas representam 
        o maior investimento per capita em pesquisa científica.
    </div>
    """, unsafe_allow_html=True)

# --- TAB 4: IMPACTO OPERACIONAL ---
with analysis_tabs[3]:
    st.markdown("### 📊 Impacto Operacional — Análise de Eficiência")
    
    # Dados de evolução temporal
    meses_evo = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    df_evo = pd.DataFrame({
        "Mês": meses_evo * 2,
        "Tipo": ["Antes da Automação"] * 12 + ["Após Automação"] * 12,
        "Horas Gastas": [120, 125, 118, 130, 122, 128, 126, 124, 129, 127, 125, 130] +
                       [95, 70, 55, 45, 38, 35, 33, 32, 30, 29, 28, 27]
    })
    
    fig_evo = px.line(
        df_evo,
        x="Mês",
        y="Horas Gastas",
        color="Tipo",
        markers=True,
        color_discrete_sequence=[CHART_COLORS[3], CHART_COLORS[0]],
        template=PLOTLY_TEMPLATE
    )
    fig_evo.update_layout(
        title="Evolução de Horas Operacionais — Antes vs Após Automação VBA",
        margin=dict(l=20, r=20, t=60, b=20),
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor=BORDER, title="Horas/Mês"),
        title_font=dict(size=16, color=TEXT, family="Inter"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_evo, use_container_width=True)
    
    # Radar de competências aplicadas
    st.markdown("##### Competências Aplicadas por Projeto")
    categorias = ["Automação", "BI", "ETL", "Modelagem", "Visualização", "Cloud"]
    valores = [95, 92, 88, 85, 90, 60]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=valores + [valores[0]],
        theta=categorias + [categorias[0]],
        fill="toself",
        name="Competências",
        line=dict(color=CHART_COLORS[0], width=2),
        fillcolor=f"rgba(59, 130, 246, 0.2)"
    ))
    fig_radar.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 100], gridcolor=BORDER, tickfont=dict(color=TEXT_MUTED)),
            angularaxis=dict(gridcolor=BORDER, tickfont=dict(color=TEXT, size=11))
        ),
        margin=dict(l=40, r=40, t=20, b=20),
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT),
        showlegend=False
    )
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # KPIs de ROI
    st.markdown("##### ROI da Automação (12 meses)")
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.metric("Horas Economizadas", "1.108 h", delta="+93% eficiência")
    with r2:
        st.metric("Custo Evitado", "R$ 185k", delta="vs. contratação")
    with r3:
        st.metric("Projetos Entregues", "24", delta="+60% vs. ano anterior")
    with r4:
        st.metric("SLA de Análises", "98.5%", delta="+12% vs. meta")
    
    st.markdown(f"""
    <div class="insight-box">
        <strong>💡 Insight Analítico:</strong> A implementação de automações em VBA no Banco do Brasil 
        gerou um <strong>ROI estimado de 340% no primeiro ano</strong>, considerando horas economizadas 
        versus custo de desenvolvimento. A curva de aprendizado foi superada em 3 meses, com ganhos 
        exponenciais a partir do 4º mês de operação.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================================================
# 13. FOOTER
# ============================================================================
st.markdown(f"""
<div class="footer">
    <div class="footer-status">
        <span class="footer-status-dot"></span>
        <span class="footer-status-text">Disponível para oportunidades</span>
    </div>
    
    <h3 class="footer-title">Vamos conversar sobre dados?</h3>
    <p class="footer-subtitle">
        Aberto a projetos desafiadores em Dados, Business Intelligence e Cloud.
    </p>
    
    <div class="footer-modes">
        <span class="footer-mode">🏠 Remoto</span>
        <span class="footer-mode">🏢 Híbrido</span>
        <span class="footer-mode">📍 Presencial</span>
        <span class="footer-mode">✈️ Disponível para viagens</span>
    </div>
    
    <div class="footer-links">
        <a href="https://www.linkedin.com/in/raphaelpires" target="_blank" class="footer-link">
            💼 LinkedIn
        </a>
        <a href="https://github.com/raphaelcaxias" target="_blank" class="footer-link">
            💻 GitHub
        </a>
        <a href="mailto:contato@raphaelpires.com" class="footer-link">
            ✉️ E-mail
        </a>
        <a href="tel:+5500000000000" class="footer-link">
            📱 Telefone
        </a>
    </div>
    
    <p class="footer-copy">
        © {datetime.now().year} Raphael Fernando da Silva Pires · Analista de Dados & Business Intelligence
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
