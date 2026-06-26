import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# TEMA DARK/LIGHT
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

is_dark = st.session_state.theme == "dark"

# ============================================================================
# CORES
# ============================================================================
if is_dark:
    PRIMARY = "#3B82F6"
    SECONDARY = "#0EA5E9"
    BG = "#0B1120"
    TEXT = "#E5E7EB"
    TEXT_MUTED = "#94A3B8"
    PLOTLY_TEMPLATE = "plotly_dark"
    CHART_COLORS = ["#3B82F6", "#0EA5E9", "#60A5FA", "#2563EB", "#0284C7"]
else:
    PRIMARY = "#2563EB"
    SECONDARY = "#0284C7"
    BG = "#F8FAFC"
    TEXT = "#0F172A"
    TEXT_MUTED = "#64748B"
    PLOTLY_TEMPLATE = "plotly_white"
    CHART_COLORS = ["#2563EB", "#0284C7", "#3B82F6", "#1D4ED8", "#0369A1"]

# ============================================================================
# CSS OTIMIZADO E CORRIGIDO
# ============================================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    background: {BG};
    color: {TEXT};
}}

#MainMenu, header, footer, .stDeployButton {{ display: none !important; }}

.stApp {{
    background: {BG};
}}

.block-container {{
    padding: 1rem 3rem 3rem 3rem;
    max-width: 1280px;
}}

@media (max-width: 768px) {{
    .block-container {{ padding: 1rem 1.25rem 2rem 1.25rem; }}
}}

/* ==================================================================
   THEME TOGGLE - FLUTUANTE NO CANTO
   ================================================================== */
.theme-toggle-float {{
    position: fixed;
    top: 1.5rem;
    right: 1.5rem;
    z-index: 999;
}}

.theme-toggle-float button {{
    background: rgba(59, 130, 246, 0.1) !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    border-radius: 50% !important;
    width: 44px !important;
    height: 44px !important;
    font-size: 1.2rem !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.15) !important;
}}

.theme-toggle-float button:hover {{
    background: {PRIMARY} !important;
    transform: scale(1.1) !important;
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3) !important;
}}

/* ==================================================================
   HERO SECTION - LAYOUT MODERNO (FOTO ESQUERDA + TEXTO DIREITA)
   ================================================================== */
.hero-wrapper {{
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 3rem;
    align-items: center;
    padding: 3rem 0 2rem 0;
    margin-bottom: 2rem;
}}

@media (max-width: 768px) {{
    .hero-wrapper {{
        grid-template-columns: 1fr;
        text-align: center;
        gap: 1.5rem;
        padding: 2rem 0 1rem 0;
    }}
}}

/* Foto circular com wrapper */
.hero-photo-wrapper {{
    position: relative;
    width: 220px;
    height: 220px;
    flex-shrink: 0;
}}

@media (max-width: 768px) {{
    .hero-photo-wrapper {{
        width: 160px;
        height: 160px;
        margin: 0 auto;
    }}
}}

.hero-photo-wrapper::before {{
    content: '';
    position: absolute;
    inset: -8px;
    border-radius: 50%;
    background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
    opacity: 0.3;
    z-index: 0;
    animation: pulse-ring 3s ease-in-out infinite;
}}

@keyframes pulse-ring {{
    0%, 100% {{ transform: scale(1); opacity: 0.3; }}
    50% {{ transform: scale(1.05); opacity: 0.15; }}
}}

.hero-photo-wrapper img,
.hero-photo-placeholder {{
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid {BG};
    box-shadow: 0 20px 60px rgba(59, 130, 246, 0.25);
    z-index: 1;
}}

.hero-photo-placeholder {{
    background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    font-weight: 700;
    color: white;
}}

.hero-content {{
    min-width: 0;
}}

.hero-name {{
    font-family: 'Playfair Display', serif;
    font-size: 2.75rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.02em;
    line-height: 1.1;
}}

@media (max-width: 768px) {{
    .hero-name {{ font-size: 2rem; }}
}}

.hero-title {{
    font-size: 1rem;
    font-weight: 600;
    color: {PRIMARY};
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 0 0 1.25rem 0;
}}

.hero-subtitle {{
    font-size: 1.05rem;
    color: {TEXT_MUTED};
    line-height: 1.7;
    margin: 0 0 1.5rem 0;
    max-width: 600px;
}}

.tech-badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1.5rem 0;
}}

@media (max-width: 768px) {{
    .tech-badges {{ justify-content: center; }}
}}

.tech-badge {{
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid rgba(59, 130, 246, 0.2);
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 500;
    color: {TEXT};
    transition: all 0.2s ease;
}}

.tech-badge:hover {{
    background: rgba(59, 130, 246, 0.15);
    border-color: {PRIMARY};
    transform: translateY(-1px);
}}

/* ==================================================================
   SECTION HEADERS
   ================================================================== */
.section-header {{
    margin: 3rem 0 2rem 0;
    text-align: center;
}}

.section-label {{
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: {PRIMARY};
    background: rgba(59, 130, 246, 0.1);
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    margin-bottom: 0.75rem;
}}

.section-title {{
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0;
}}

/* ==================================================================
   KPIs
   ================================================================== */
.kpi-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}}

@media (max-width: 1024px) {{
    .kpi-grid {{ grid-template-columns: repeat(3, 1fr); }}
}}
@media (max-width: 640px) {{
    .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}

.kpi-box {{
    background: rgba(59, 130, 246, 0.04);
    border: 1px solid rgba(59, 130, 246, 0.12);
    border-radius: 14px;
    padding: 1.5rem 1rem;
    text-align: center;
    transition: all 0.3s ease;
}}

.kpi-box:hover {{
    transform: translateY(-4px);
    border-color: {PRIMARY};
    box-shadow: 0 12px 28px rgba(59, 130, 246, 0.12);
}}

.kpi-value {{
    font-size: 1.85rem;
    font-weight: 700;
    color: {PRIMARY};
    margin-bottom: 0.4rem;
    line-height: 1.1;
}}

.kpi-label {{
    font-size: 0.8rem;
    color: {TEXT_MUTED};
    font-weight: 500;
    line-height: 1.3;
}}

/* ==================================================================
   TIMELINE
   ================================================================== */
.timeline {{
    position: relative;
    padding: 1rem 0;
}}

.timeline::before {{
    content: '';
    position: absolute;
    left: 20px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, {PRIMARY}, {SECONDARY}, transparent);
}}

@media (max-width: 768px) {{
    .timeline::before {{ left: 12px; }}
}}

.timeline-item {{
    position: relative;
    padding-left: 60px;
    margin-bottom: 1.5rem;
}}

@media (max-width: 768px) {{
    .timeline-item {{ padding-left: 40px; }}
}}

.timeline-dot {{
    position: absolute;
    left: 13px;
    top: 1.5rem;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: {PRIMARY};
    border: 3px solid {BG};
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}}

@media (max-width: 768px) {{
    .timeline-dot {{ left: 5px; }}
}}

.timeline-card {{
    background: rgba(59, 130, 246, 0.03);
    border: 1px solid rgba(59, 130, 246, 0.1);
    border-radius: 14px;
    padding: 1.5rem;
    transition: all 0.3s ease;
}}

.timeline-card:hover {{
    border-color: {PRIMARY};
    background: rgba(59, 130, 246, 0.06);
    transform: translateX(4px);
}}

.timeline-date {{
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 600;
    color: {PRIMARY};
    background: rgba(59, 130, 246, 0.1);
    padding: 0.2rem 0.7rem;
    border-radius: 999px;
    margin-bottom: 0.6rem;
    letter-spacing: 0.05em;
}}

.timeline-role {{
    font-size: 1.1rem;
    font-weight: 600;
    color: {TEXT};
    margin: 0 0 0.2rem 0;
}}

.timeline-company {{
    font-size: 0.9rem;
    color: {SECONDARY};
    font-weight: 500;
    margin-bottom: 0.6rem;
}}

.timeline-desc {{
    font-size: 0.9rem;
    color: {TEXT_MUTED};
    line-height: 1.6;
    margin: 0;
}}

.timeline-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-top: 0.8rem;
}}

.timeline-tag {{
    font-size: 0.7rem;
    padding: 0.2rem 0.55rem;
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid rgba(59, 130, 246, 0.15);
    border-radius: 6px;
    color: {TEXT};
    font-weight: 500;
}}

/* ==================================================================
   AWS GRID
   ================================================================== */
.aws-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 0.85rem;
    margin: 1.5rem 0;
}}

.aws-card {{
    background: rgba(59, 130, 246, 0.03);
    border: 1px solid rgba(59, 130, 246, 0.1);
    border-radius: 12px;
    padding: 1.1rem 0.8rem;
    text-align: center;
    transition: all 0.3s ease;
}}

.aws-card:hover {{
    border-color: {PRIMARY};
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(59, 130, 246, 0.1);
}}

.aws-icon {{
    font-size: 1.75rem;
    margin-bottom: 0.4rem;
}}

.aws-title {{
    font-size: 0.85rem;
    font-weight: 600;
    color: {TEXT};
    margin: 0;
    line-height: 1.3;
}}

.aws-banner {{
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(14, 165, 233, 0.04));
    border: 1px solid rgba(59, 130, 246, 0.15);
    border-radius: 14px;
    padding: 1.25rem;
    text-align: center;
    margin: 1.5rem 0;
}}

.aws-banner p {{
    margin: 0;
    font-size: 1rem;
    color: {TEXT};
}}

/* ==================================================================
   STACK
   ================================================================== */
.stack-section {{
    margin-bottom: 1.5rem;
}}

.stack-category-title {{
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: {PRIMARY};
    margin-bottom: 0.7rem;
}}

.stack-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}}

.stack-chip {{
    background: rgba(59, 130, 246, 0.06);
    border: 1px solid rgba(59, 130, 246, 0.15);
    padding: 0.45rem 0.9rem;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 500;
    color: {TEXT};
    transition: all 0.2s ease;
}}

.stack-chip:hover {{
    background: {PRIMARY};
    color: white;
    border-color: {PRIMARY};
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(59, 130, 246, 0.2);
}}

/* ==================================================================
   FOOTER
   ================================================================== */
.footer {{
    margin-top: 4rem;
    padding: 2.5rem 2rem;
    background: rgba(59, 130, 246, 0.03);
    border: 1px solid rgba(59, 130, 246, 0.1);
    border-radius: 18px;
    text-align: center;
}}

.footer-status {{
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(34, 197, 94, 0.08);
    border: 1px solid rgba(34, 197, 94, 0.25);
    padding: 0.45rem 1rem;
    border-radius: 999px;
    margin-bottom: 1.25rem;
}}

.footer-status-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #22C55E;
    box-shadow: 0 0 10px #22C55E;
    animation: pulse 2s infinite;
}}

@keyframes pulse {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0.5; }}
}}

.footer-status-text {{
    font-size: 0.8rem;
    font-weight: 600;
    color: #22C55E;
}}

.footer-title {{
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0 0 0.4rem 0;
}}

.footer-subtitle {{
    font-size: 0.9rem;
    color: {TEXT_MUTED};
    margin: 0 0 1.25rem 0;
}}

.footer-modes {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}}

.footer-mode {{
    background: rgba(59, 130, 246, 0.05);
    border: 1px solid rgba(59, 130, 246, 0.1);
    padding: 0.35rem 0.75rem;
    border-radius: 999px;
    font-size: 0.75rem;
    color: {TEXT};
    font-weight: 500;
}}

.footer-links {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 1.5rem;
}}

.footer-link {{
    background: rgba(59, 130, 246, 0.05);
    border: 1px solid rgba(59, 130, 246, 0.15);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    color: {TEXT};
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    transition: all 0.2s ease;
}}

.footer-link:hover {{
    background: {PRIMARY};
    color: white;
    border-color: {PRIMARY};
    transform: translateY(-2px);
}}

.footer-copy {{
    font-size: 0.8rem;
    color: {TEXT_MUTED};
    margin: 1.25rem 0 0 0;
    padding-top: 1.25rem;
    border-top: 1px solid rgba(59, 130, 246, 0.1);
}}

/* ==================================================================
   STREAMLIT NATIVOS
   ================================================================== */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    background: rgba(59, 130, 246, 0.03) !important;
    border: 1px solid rgba(59, 130, 246, 0.1) !important;
    border-radius: 14px !important;
    transition: all 0.3s ease;
}}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
    border-color: {PRIMARY} !important;
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.08);
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 0.4rem;
    background: transparent;
}}

.stTabs [data-baseweb="tab"] {{
    background: rgba(59, 130, 246, 0.05);
    border: 1px solid rgba(59, 130, 246, 0.1);
    border-radius: 8px;
    padding: 0.5rem 1rem;
    color: {TEXT};
    font-weight: 500;
    font-size: 0.85rem;
}}

.stTabs [aria-selected="true"] {{
    background: {PRIMARY} !important;
    color: white !important;
    border-color: {PRIMARY} !important;
}}

::-webkit-scrollbar {{ width: 8px; height: 8px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: rgba(59, 130, 246, 0.3); border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: {PRIMARY}; }}

.stMarkdown, h1, h2, h3, h4 {{ color: {TEXT}; }}

/* Esconde o label dos widgets quando vazio */
.stDownloadButton > button {{
    background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 1.25rem;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 16px rgba(59, 130, 246, 0.25);
}}

.stDownloadButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.35);
}}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# THEME TOGGLE - FLUTUANTE
# ============================================================================
st.markdown('<div class="theme-toggle-float">', unsafe_allow_html=True)
theme_label = "☀️" if is_dark else "🌙"
if st.button(theme_label, key="theme_btn", help="Alternar tema"):
    toggle_theme()
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# HERO SECTION - LAYOUT MODERNO (FOTO ESQUERDA + CONTEÚDO DIREITA)
# ============================================================================
# Foto em HTML para garantir o formato circular
photo_html = ""
if os.path.exists("rapha.jpeg"):
    photo_html = f'<img src="app/rapha.jpeg" class="hero-photo" alt="Raphael Pires">'
else:
    photo_html = f'<div class="hero-photo-placeholder">RP</div>'

# Também tenta o caminho relativo direto
photo_html = f'''
<div class="hero-photo-wrapper">
    <img src="rapha.jpeg" 
         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
         alt="Raphael Pires">
    <div class="hero-photo-placeholder" style="display:none;">RP</div>
</div>
'''

st.markdown(f'''
<div class="hero-wrapper">
    {photo_html}
    <div class="hero-content">
        <h1 class="hero-name">Raphael Fernando da Silva Pires</h1>
        <div class="hero-title">Analista de Dados & Business Intelligence</div>
        <p class="hero-subtitle">
            Transformando dados brutos em decisões estratégicas. Mais de <strong>16 anos</strong> 
            construindo inteligência de negócios, automações e governança de dados que geram 
            impacto real e mensurável em organizações de diferentes portes.
        </p>
        <div class="tech-badges">
            <span class="tech-badge">📊 Power BI</span>
            <span class="tech-badge">🐍 Python</span>
            <span class="tech-badge">🗄️ SQL</span>
            <span class="tech-badge">☁️ AWS</span>
            <span class="tech-badge">🤖 IA Generativa</span>
            <span class="tech-badge">📈 Dashboards</span>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# Download CV
dl1, dl2, dl3 = st.columns([3, 2, 3])
with dl2:
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
        st.caption("📄 *Currículo disponível mediante solicitação*")

st.divider()

# ============================================================================
# KPIs DE IMPACTO
# ============================================================================
st.markdown(f'''
<div class="section-header">
    <span class="section-label">Impacto Mensurável</span>
    <h2 class="section-title">Números que contam histórias</h2>
</div>

<div class="kpi-grid">
    <div class="kpi-box">
        <div class="kpi-value">16+</div>
        <div class="kpi-label">anos de experiência</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">70%</div>
        <div class="kpi-label">redução operacional</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">213k</div>
        <div class="kpi-label">registros processados</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">2h→15m</div>
        <div class="kpi-label">análises reduzidas</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">R$50bi</div>
        <div class="kpi-label">dados analisados</div>
    </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ============================================================================
# EXPERIÊNCIA PROFISSIONAL - TIMELINE
# ============================================================================
st.markdown(f'''
<div class="section-header">
    <span class="section-label">Trajetória</span>
    <h2 class="section-title">Experiência profissional</h2>
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
                operacional, liberando equipes para atividades estratégicas.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">VBA</span>
                <span class="timeline-tag">Automação</span>
                <span class="timeline-tag">Eficiência</span>
            </div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <span class="timeline-date">Fundador & Analista</span>
            <h3 class="timeline-role">Fundador</h3>
            <div class="timeline-company">Jardim do Éden</div>
            <p class="timeline-desc">
                Dashboards, Power BI, Python, SQL, KPIs e IA Generativa. Redução de análises 
                de 2 horas para 15 minutos através de automação inteligente.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">Power BI</span>
                <span class="timeline-tag">Python</span>
                <span class="timeline-tag">SQL</span>
                <span class="timeline-tag">IA Generativa</span>
            </div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <span class="timeline-date">Gestão Comercial</span>
            <h3 class="timeline-role">Gestão Comercial & BI</h3>
            <div class="timeline-company">J Sintonía</div>
            <p class="timeline-desc">
                Business Intelligence, indicadores, dashboards e análise de viabilidade 
                econômica suportando decisões estratégicas.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">BI</span>
                <span class="timeline-tag">KPIs</span>
                <span class="timeline-tag">Dashboards</span>
                <span class="timeline-tag">Viabilidade</span>
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
                que trouxeram visibilidade e governança.
            </p>
            <div class="timeline-tags">
                <span class="timeline-tag">Dados</span>
                <span class="timeline-tag">Governança</span>
                <span class="timeline-tag">Indicadores</span>
            </div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ============================================================================
# STACK TECNOLÓGICA
# ============================================================================
st.markdown(f'''
<div class="section-header">
    <span class="section-label">Stack</span>
    <h2 class="section-title">Tecnologias</h2>
</div>

<div class="stack-section">
    <div class="stack-category-title">📊 Dados</div>
    <div class="stack-chips">
        <div class="stack-chip">SQL</div>
        <div class="stack-chip">PostgreSQL</div>
        <div class="stack-chip">Python</div>
        <div class="stack-chip">Pandas</div>
        <div class="stack-chip">NumPy</div>
    </div>
</div>

<div class="stack-section">
    <div class="stack-category-title">📈 Business Intelligence</div>
    <div class="stack-chips">
        <div class="stack-chip">Power BI</div>
        <div class="stack-chip">Plotly</div>
        <div class="stack-chip">Looker Studio</div>
        <div class="stack-chip">Streamlit</div>
    </div>
</div>

<div class="stack-section">
    <div class="stack-category-title">☁️ Cloud & Versionamento</div>
    <div class="stack-chips">
        <div class="stack-chip">AWS</div>
        <div class="stack-chip">Git</div>
        <div class="stack-chip">GitHub</div>
    </div>
</div>

<div class="stack-section">
    <div class="stack-category-title">⚡ Automação & IA</div>
    <div class="stack-chips">
        <div class="stack-chip">Excel VBA</div>
        <div class="stack-chip">IA Generativa</div>
    </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ============================================================================
# GRÁFICO DE COMPETÊNCIAS
# ============================================================================
st.markdown(f'''
<div class="section-header">
    <span class="section-label">Competências</span>
    <h2 class="section-title">Domínio tecnológico</h2>
</div>
''', unsafe_allow_html=True)

skills_data = {
    "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
    "Proeficiência (%)": [95, 92, 88, 95, 85, 60, 82],
    "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
}
df_skills = pd.DataFrame(skills_data)

fig_skills = px.bar(
    df_skills,
    x="Proeficiência (%)",
    y="Tecnologia",
    color="Categoria",
    orientation="h",
    color_discrete_sequence=CHART_COLORS,
    template=PLOTLY_TEMPLATE,
    text="Proeficiência (%)"
)

fig_skills.update_layout(
    margin=dict(l=20, r=40, t=20, b=40),
    height=380,
    xaxis=dict(range=[0, 105], showgrid=True, gridcolor="rgba(148, 163, 184, 0.1)"),
    yaxis=dict(showgrid=False),
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    font=dict(family="Inter", color=TEXT),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
fig_skills.update_traces(textposition="outside", textfont=dict(color=TEXT, size=11))

st.plotly_chart(fig_skills, use_container_width=True)

st.divider()

# ============================================================================
# PROJETOS
# ============================================================================
st.markdown(f'''
<div class="section-header">
    <span class="section-label">Portfólio</span>
    <h2 class="section-title">Projetos em destaque</h2>
</div>
''', unsafe_allow_html=True)

p1, p2 = st.columns(2)
with p1:
    with st.container(border=True):
        st.markdown("#### 🇧🇷 Desenrola Brasil")
        st.write("Análise de dados do programa governamental, explorando renegociações e perfis de consumidores.")
        st.page_link("https://github.com/raphaelcaxias", label="Acessar Repositório", icon="🔗")

with p2:
    with st.container(border=True):
        st.markdown("#### 🔬 CNPq Analytics")
        st.write("Dashboard analítico sobre bolsas e fomento do CNPq com cruzamento de dados de pesquisa.")
        st.page_link("https://github.com/raphaelcaxias", label="Acessar Repositório", icon="🔗")

p3, p4 = st.columns(2)
with p3:
    with st.container(border=True):
        st.markdown("#### ⛽ Dashboard ANP")
        st.write("Inteligência de dados da ANP com análise de preços e produção de combustíveis.")
        st.page_link("https://github.com/raphaelcaxias", label="Ver Dashboard", icon="📊")

with p4:
    with st.container(border=True):
        st.markdown("#### 💎 Portfólio Premium")
        st.write("Este portfólio construído em Streamlit com design premium e visualização de dados.")
        st.page_link("https://github.com/raphaelcaxias", label="Ver Código", icon="💻")

st.divider()

# ============================================================================
# AWS CLOUD JOURNEY
# ============================================================================
st.markdown(f'''
<div class="section-header">
    <span class="section-label">Cloud Computing</span>
    <h2 class="section-title">AWS Cloud Journey</h2>
</div>

<div class="aws-banner">
    <p>☁️ Preparando-me para a certificação <strong>AWS Cloud Practitioner</strong></p>
</div>

<div class="aws-grid">
    <div class="aws-card">
        <div class="aws-icon">☁️</div>
        <div class="aws-title">Cloud Computing</div>
    </div>
    <div class="aws-card">
        <div class="aws-icon">📘</div>
        <div class="aws-title">Cloud 101</div>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🖥️</div>
        <div class="aws-title">AWS Console</div>
    </div>
    <div class="aws-card">
        <div class="aws-icon">💾</div>
        <div class="aws-title">Storage</div>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🛟</div>
        <div class="aws-title">Cloud Support</div>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🤖</div>
        <div class="aws-title">ML Foundations</div>
    </div>
    <div class="aws-card">
        <div class="aws-icon">🌱</div>
        <div class="aws-title">Sustainability</div>
    </div>
</div>
''', unsafe_allow_html=True)

st.divider()

# ============================================================================
# ANÁLISE DE DADOS INTERATIVA - COM TRATAMENTO DE ERROS
# ============================================================================
st.markdown(f'''
<div class="section-header">
    <span class="section-label">Análise ao Vivo</span>
    <h2 class="section-title">Demonstração analítica</h2>
</div>
''', unsafe_allow_html=True)

analysis_tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Combustíveis ANP", "📊 Impacto Operacional"])

# ============================================================================
# TAB 1: DESENROLA BRASIL
# ============================================================================
with analysis_tabs[0]:
    st.markdown("### 📈 Análise de Renegociações")
    
    np.random.seed(42)
    regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
    faixas = ["Até R$ 5k", "R$ 5k-15k", "R$ 15k-50k", "Acima R$ 50k"]
    
    df_des = pd.DataFrame({
        "Região": np.random.choice(regioes, 400, p=[0.45, 0.28, 0.15, 0.07, 0.05]),
        "Faixa": np.random.choice(faixas, 400, p=[0.55, 0.28, 0.12, 0.05]),
        "Valor": np.random.lognormal(mean=8.5, sigma=1.2, size=400),
        "Status": np.random.choice(["Renegociado", "Em Negociação", "Inadimplente"], 400, p=[0.65, 0.25, 0.10])
    })
    
    fc1, fc2 = st.columns(2)
    with fc1:
        reg_sel = st.multiselect("Região", regioes, default=regioes, key="reg_des")
    with fc2:
        status_sel = st.multiselect("Status", df_des["Status"].unique().tolist(), 
                                   default=df_des["Status"].unique().tolist(), key="status_des")
    
    # CORREÇÃO: Tratar filtros vazios
    if not reg_sel or not status_sel:
        st.warning("⚠️ Selecione pelo menos uma região e um status para visualizar os dados.")
    else:
        df_f = df_des[(df_des["Região"].isin(reg_sel)) & (df_des["Status"].isin(status_sel))]
        
        if len(df_f) == 0:
            st.warning("⚠️ Nenhum dado encontrado para os filtros selecionados.")
        else:
            mk1, mk2, mk3 = st.columns(3)
            with mk1:
                st.metric("Contratos", f"{len(df_f):,}".replace(",", "."))
            with mk2:
                st.metric("Valor Total", f"R$ {df_f['Valor'].sum()/1e6:.1f}M")
            with mk3:
                taxa = (df_f['Status']=='Renegociado').mean()*100
                st.metric("Taxa Sucesso", f"{taxa:.1f}%")
            
            g1, g2 = st.columns(2)
            with g1:
                fig_reg = px.pie(df_f, names="Região", values="Valor", hole=0.55, 
                                color_discrete_sequence=CHART_COLORS, template=PLOTLY_TEMPLATE)
                fig_reg.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320,
                                    paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT))
                st.plotly_chart(fig_reg, use_container_width=True)
            
            with g2:
                agg_faixa = df_f.groupby("Faixa", observed=False)["Valor"].sum().reset_index()
                fig_faixa = px.bar(agg_faixa, x="Faixa", y="Valor", 
                                  color_discrete_sequence=[CHART_COLORS[0]], 
                                  template=PLOTLY_TEMPLATE)
                fig_faixa.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320,
                                       paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT),
                                       xaxis=dict(showgrid=False), 
                                       yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)"))
                st.plotly_chart(fig_faixa, use_container_width=True)

# ============================================================================
# TAB 2: COMBUSTÍVEIS
# ============================================================================
with analysis_tabs[1]:
    st.markdown("### ⛽ Preços de Combustíveis — ANP")
    
    np.random.seed(123)
    estados = ["SP", "RJ", "MG", "RS", "PR", "BA"]
    combustiveis = ["Gasolina", "Etanol", "Diesel"]
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    
    dados = []
    for estado in estados:
        for comb in combustiveis:
            base = {"Gasolina": 5.8, "Etanol": 3.5, "Diesel": 5.2}[comb]
            for i, mes in enumerate(meses):
                dados.append({
                    "Estado": estado, "Combustível": comb, "Mês": mes,
                    "Preço": base + np.random.normal(0, 0.15) + (i * 0.02)
                })
    df_anp = pd.DataFrame(dados)
    
    fc1, fc2 = st.columns(2)
    with fc1:
        est_sel = st.selectbox("Estado", estados, index=0, key="est_anp")
    with fc2:
        comb_sel = st.selectbox("Combustível", combustiveis, index=0, key="comb_anp")
    
    df_f = df_anp[(df_anp["Estado"] == est_sel) & (df_anp["Combustível"] == comb_sel)]
    
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        preco_atual = df_f[df_f['Mês']=='Jun']['Preço'].values
        if len(preco_atual) > 0:
            st.metric("Preço Atual (Jun)", f"R$ {preco_atual[0]:.2f}")
    with mc2:
        st.metric("Preço Mínimo", f"R$ {df_f['Preço'].min():.2f}")
    with mc3:
        variacao = ((df_f["Preço"].max() - df_f["Preço"].min()) / df_f["Preço"].min()) * 100
        st.metric("Variação Semestral", f"{variacao:.1f}%", delta=f"{variacao:.1f}%")
    
    fig = px.line(df_f, x="Mês", y="Preço", markers=True, 
                  color_discrete_sequence=[CHART_COLORS[0]], template=PLOTLY_TEMPLATE)
    fig.update_layout(title=f"{comb_sel} — {est_sel} (2026)", 
                     margin=dict(l=20, r=20, t=50, b=20),
                     height=350, paper_bgcolor="rgba(0,0,0,0)", 
                     font=dict(family="Inter", color=TEXT),
                     xaxis=dict(showgrid=False), 
                     yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)"))
    st.plotly_chart(fig, use_container_width=True)
    
    # Comparativo entre estados
    st.markdown("##### Comparativo entre Estados (Jun/2026)")
    df_jun = df_anp[(df_anp["Mês"] == "Jun") & (df_anp["Combustível"] == comb_sel)]
    fig_comp = px.bar(df_jun.sort_values("Preço"), x="Preço", y="Estado", 
                     orientation="h", color="Preço",
                     color_continuous_scale=[CHART_COLORS[1], CHART_COLORS[0]],
                     template=PLOTLY_TEMPLATE)
    fig_comp.update_layout(margin=dict(l=20, r=20, t=10, b=20), height=300,
                          paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT),
                          showlegend=False, coloraxis_showscale=False,
                          xaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)"),
                          yaxis=dict(showgrid=False))
    st.plotly_chart(fig_comp, use_container_width=True)

# ============================================================================
# TAB 3: IMPACTO OPERACIONAL
# ============================================================================
with analysis_tabs[2]:
    st.markdown("### 📊 Impacto da Automação")
    
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    df_evo = pd.DataFrame({
        "Mês": meses * 2,
        "Tipo": ["Antes da Automação"] * 12 + ["Após Automação"] * 12,
        "Horas": [120, 125, 118, 130, 122, 128, 126, 124, 129, 127, 125, 130] +
                [95, 70, 55, 45, 38, 35, 33, 32, 30, 29, 28, 27]
    })
    
    fig_evo = px.line(df_evo, x="Mês", y="Horas", color="Tipo", markers=True,
                     color_discrete_sequence=[CHART_COLORS[3], CHART_COLORS[0]], 
                     template=PLOTLY_TEMPLATE)
    fig_evo.update_layout(title="Evolução de Horas — Antes vs Após Automação VBA",
                         margin=dict(l=20, r=20, t=60, b=20), height=380,
                         paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT),
                         xaxis=dict(showgrid=False), 
                         yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)", title="Horas/Mês"),
                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig_evo, use_container_width=True)
    
    # Radar de competências
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
            radialaxis=dict(visible=True, range=[0, 100], 
                          gridcolor="rgba(148,163,184,0.1)", 
                          tickfont=dict(color=TEXT_MUTED)),
            angularaxis=dict(gridcolor="rgba(148,163,184,0.1)", 
                           tickfont=dict(color=TEXT, size=11))
        ),
        margin=dict(l=40, r=40, t=20, b=20),
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT),
        showlegend=False
    )
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # KPIs de ROI
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.metric("Horas Economizadas", "1.108 h", "+93% eficiência")
    with r2:
        st.metric("Custo Evitado", "R$ 185k", "vs. contratação")
    with r3:
        st.metric("Projetos Entregues", "24", "+60% vs. ano anterior")
    with r4:
        st.metric("SLA de Análises", "98.5%", "+12% vs. meta")

st.divider()

# ============================================================================
# FOOTER
# ============================================================================
st.markdown(f'''
<div class="footer">
    <div class="footer-status">
        <span class="footer-status-dot"></span>
        <span class="footer-status-text">Disponível para oportunidades</span>
    </div>
    
    <h3 class="footer-title">Vamos conversar sobre dados?</h3>
    <p class="footer-subtitle">Aberto a projetos desafiadores em Dados, BI e Cloud</p>
    
    <div class="footer-modes">
        <span class="footer-mode">🏠 Remoto</span>
        <span class="footer-mode">🏢 Híbrido</span>
        <span class="footer-mode">📍 Presencial</span>
        <span class="footer-mode">✈️ Viagens</span>
    </div>
    
    <div class="footer-links">
        <a href="https://www.linkedin.com/in/raphaelpires" target="_blank" class="footer-link">💼 LinkedIn</a>
        <a href="https://github.com/raphaelcaxias" target="_blank" class="footer-link">💻 GitHub</a>
        <a href="mailto:contato@raphaelpires.com" class="footer-link">✉️ E-mail</a>
        <a href="tel:+5500000000000" class="footer-link">📱 Telefone</a>
    </div>
    
    <p class="footer-copy">© {datetime.now().year} Raphael Fernando da Silva Pires · Analista de Dados & BI</p>
</div>
''', unsafe_allow_html=True)

st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
