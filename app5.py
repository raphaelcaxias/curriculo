import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
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

# Botão de alternar tema no topo direito
col_t1, col_t2 = st.columns([11, 1])
with col_t2:
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
            width: 180px; height: 180px; border-radius: 50%;
            background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
            display: flex; align-items: center; justify-content: center;
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem; font-weight: 700; color: white;
            box-shadow: 0 0 0 8px {GLASS}, 0 20px 60px {SHADOW};
            margin: 0 auto 1.5rem auto;">
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

# Cache de Download do CV para evitar IO repetitivo do disco
@st.cache_data
def load_cv_file():
    try:
        with open("Curriculo_Raphael_v2.pdf", "rb") as pdf_file:
            return pdf_file.read()
    except FileNotFoundError:
        return None

cv_data = load_cv_file()
dc1, dc2, dc3 = st.columns([3, 2, 3])
with dc2:
    if cv_data:
        st.download_button(
            label="📄 Download Currículo PDF",
            data=cv_data,
            file_name="Curriculo_Raphael_Pires.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
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
    st.markdown(f'<div class="kpi-custom"><div class="kpi-custom-value">16+</div><div class="kpi-custom-label">anos de experiência</div></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="kpi-custom"><div class="kpi-custom-value">70%</div><div class="kpi-custom-label">redução operacional</div></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="kpi-custom"><div class="kpi-custom-value">213k</div><div class="kpi-custom-label">registros processados</div></div>', unsafe_allow_html=True)
with k4:
    st.markdown(f'<div class="kpi-custom"><div class="kpi-custom-value">2h→15m</div><div class="kpi-custom-label">análises reduzidas</div></div>', unsafe_allow_html=True)
with k5:
    st.markdown(f'<div class="kpi-custom"><div class="kpi-custom-value">R$50bi</div><div class="kpi-custom-label">dados públicos analisados</div></div>', unsafe_allow_html=True)

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
        {"".join(f'<div class="stack-chip">{tech}</div>' for tech in ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy"])}
    </div>
</div>

<div class="stack-category">
    <div class="stack-category-title">📈 Business Intelligence</div>
    <div class="stack-grid">
        {"".join(f'<div class="stack-chip">{tech}</div>' for tech in ["Power BI", "Plotly", "Looker Studio", "Streamlit"])}
    </div>
</div>

<div class="stack-category">
    <div class="stack-category-title">☁️ Cloud & Versionamento</div>
    <div class="stack-grid">
        {"".join(f'<div class="stack-chip">{tech}</div>' for tech in ["AWS", "Git", "GitHub"])}
    </div>
</div>

<div class="stack-category">
    <div class="stack-category-title">⚡ Automação & IA</div>
    <div class="stack-grid">
        {"".join(f'<div class="stack-chip">{tech}</div>' for tech in ["Excel VBA", "IA Generativa"])}
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================================
# 9. GRÁFICO DE PROFICIÊNCIA
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
    "Proficiência (%)": [95, 92, 88, 95, 85, 60, 75, 82],
    "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "Inovação", "BI"]
}
df_skills = pd.DataFrame(skills_data)

fig_skills = px.bar(
    df_skills,
    x="Proficiência (%)",
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
    text="Proficiência (%)"
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
    <div class="aws-card"><div class="aws-icon">☁️</div><h4 class="aws-title">Cloud Computing</h4></div>
    <div class="aws-card"><div class="aws-icon">📘</div><h4 class="aws-title">Cloud 101</h4></div>
    <div class="aws-card"><div class="aws-icon">🖥️</div><h4 class="aws-title">AWS Console</h4></div>
    <div class="aws-card"><div class="aws-icon">💾</div><h4 class="aws-title">Storage</h4></div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================================
# 12. ANÁLISE DE DADOS INTERATIVA (Cached)
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Análise ao Vivo</span>
    <h2 class="section-title">Demonstração de capacidade analítica</h2>
    <p class="section-subtitle">Dashboards interativos construídos com dados simulados baseados em cenários reais dos meus projetos.</p>
</div>
""", unsafe_allow_html=True)

# Cache dos dados mockados para o app não re-gerar números aleatórios a cada clique
@st.cache_data
def get_mock_desenrola_data():
    np.random.seed(42)
    regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
    faixas_divida = ["Até R$ 5.000", "R$ 5.001 - R$ 15.000", "R$ 15.001 - R$ 50.000", "Acima de R$ 50.000"]
    return pd.DataFrame({
        "Região": np.random.choice(regioes, 500, p=[0.45, 0.28, 0.15, 0.07, 0.05]),
        "Faixa de Dívida": np.random.choice(faixas_divida, 500, p=[0.55, 0.28, 0.12, 0.05]),
        "Valor Renegociado (R$)": np.random.lognormal(mean=8.5, sigma=1.2, size=500),
        "Status": np.random.choice(["Renegociado", "Em Negociação", "Inadimplente"], 500, p=[0.65, 0.25, 0.10])
    })

df_desenrola = get_mock_desenrola_data()

analysis_tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Mercado de Combustíveis", "🔬 Fomento à Pesquisa", "📊 Impacto Operacional"])

with analysis_tabs[0]:
    st.markdown("### 📈 Análise de Renegociações — Desenrola Brasil")
    
    regioes_validas = list(df_desenrola["Região"].unique())
    status_validos = list(df_desenrola["Status"].unique())
    
    fc1, fc2 = st.columns(2)
    with fc1:
        regiao_sel = st.multiselect("Filtrar por Região", regioes_validas, default=regioes_validas)
    with fc2:
        status_sel = st.multiselect("Filtrar por Status", status_validos, default=status_validos)
        
    # Filtragem segura evitando arrays vazios
    if not regiao_sel: regiao_sel = regioes_validas
    if not status_sel: status_sel = status_validos
        
    df_filtered = df_desenrola[
        (df_desenrola["Região"].isin(regiao_sel)) & 
        (df_desenrola["Status"].isin(status_sel))
    ]
    
    fig_filtered = px.histogram(
        df_filtered, 
        x="Faixa de Dívida", 
        y="Valor Renegociado (R$)", 
        color="Status",
        barmode="group",
        template=PLOTLY_TEMPLATE,
        color_discrete_sequence=CHART_COLORS
    )
    fig_filtered.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=TEXT)
    )
    st.plotly_chart(fig_filtered, use_container_width=True)

with analysis_tabs[1]:
    st.info("⛽ Painel interativo do Mercado de Combustíveis (ANP) em desenvolvimento.")

with analysis_tabs[2]:
    st.info("🔬 Análise de Fomento à Pesquisa Científica (CNPq) em desenvolvimento.")

with analysis_tabs[3]:
    st.info("📊 Mapeamento e métricas de ganho e impacto operacional em desenvolvimento.")
