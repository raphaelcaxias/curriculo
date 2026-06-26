import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime
import os

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & Business Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# MODO DARK / LIGHT
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

col_toggle, _, _ = st.columns([1, 10, 1])
with col_toggle:
    st.markdown("")
    theme_label = "☀️ Claro" if st.session_state.theme == "dark" else "🌙 Escuro"
    st.button(theme_label, on_click=toggle_theme, key="theme_toggle", use_container_width=True)

is_dark = st.session_state.theme == "dark"

# ============================================================================
# PALETA DE CORES
# ============================================================================
if is_dark:
    BG = "#0B1120"           # Grafite profundo
    SURFACE = "#111A2E"      # Grafite médio
    SURFACE_2 = "#1A2540"    # Grafite claro
    PRIMARY = "#3B82F6"      # Azul royal
    SECONDARY = "#0EA5E9"    # Azul petróleo
    ACCENT = "#60A5FA"       # Azul suave
    TEXT = "#E5E7EB"         # Cinza claro
    TEXT_MUTED = "#94A3B8"   # Cinza médio
    BORDER = "rgba(59, 130, 246, 0.15)"
    GLASS = "rgba(17, 26, 46, 0.6)"
    SHADOW = "rgba(0, 0, 0, 0.4)"
    GRADIENT_START = "#3B82F6"
    GRADIENT_END = "#0EA5E9"
else:
    BG = "#F8FAFC"           # Branco gelo
    SURFACE = "#FFFFFF"      # Branco puro
    SURFACE_2 = "#F1F5F9"    # Cinza suave
    PRIMARY = "#2563EB"      # Azul elegante
    SECONDARY = "#0284C7"    # Azul petróleo
    ACCENT = "#3B82F6"       # Azul royal
    TEXT = "#0F172A"         # Grafite
    TEXT_MUTED = "#64748B"   # Cinza
    BORDER = "rgba(37, 99, 235, 0.12)"
    GLASS = "rgba(255, 255, 255, 0.7)"
    SHADOW = "rgba(15, 23, 42, 0.08)"
    GRADIENT_START = "#2563EB"
    GRADIENT_END = "#0284C7"

# ============================================================================
# CSS COMPLETO — DESIGN PREMIUM
# ============================================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

/* Reset global */
html, body, [class*="css"] {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: {TEXT};
    background: {BG};
    scroll-behavior: smooth;
}}

/* Esconder elementos padrão Streamlit */
#MainMenu, header, footer {{
    display: none !important;
}}
.stDeployButton {{
    display: none !important;
}}

/* Fundo global com gradiente sutil */
.stApp {{
    background: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(59, 130, 246, 0.15), transparent),
        radial-gradient(ellipse 60% 50% at 80% 50%, rgba(14, 165, 233, 0.08), transparent),
        {BG};
    background-attachment: fixed;
}}

/* Container principal */
.block-container {{
    padding: 2rem 3rem 4rem 3rem;
    max-width: 1280px;
}}

@media (max-width: 768px) {{
    .block-container {{
        padding: 1.5rem 1.25rem 3rem 1.25rem;
    }}
}}

/* Botão de toggle de tema */
.stButton > button {{
    background: {GLASS};
    color: {TEXT};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 0.5rem 1rem;
    font-weight: 500;
    font-size: 0.875rem;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
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

/* ===================== HERO SECTION ===================== */
.hero-container {{
    padding: 4rem 0 3rem 0;
    text-align: center;
    position: relative;
}}

.hero-avatar-wrapper {{
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
    position: relative;
}}

.hero-avatar {{
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid {BORDER};
    box-shadow: 
        0 0 0 8px {GLASS},
        0 20px 60px {SHADOW},
        0 0 80px rgba(59, 130, 246, 0.2);
    transition: all 0.4s ease;
}}
.hero-avatar:hover {{
    transform: scale(1.03);
    box-shadow: 
        0 0 0 8px {GLASS},
        0 25px 70px {SHADOW},
        0 0 100px rgba(59, 130, 246, 0.35);
}}

.hero-name {{
    font-family: 'Playfair Display', serif;
    font-size: 3.75rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin: 0 0 0.75rem 0;
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
    font-size: 1.375rem;
    font-weight: 400;
    color: {TEXT_MUTED};
    max-width: 680px;
    margin: 0 auto 2rem auto;
    line-height: 1.6;
}}

.hero-badges {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.625rem;
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
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.3s ease;
}}
.hero-badge:hover {{
    border-color: {PRIMARY};
    color: {PRIMARY};
    transform: translateY(-2px);
}}

@media (max-width: 768px) {{
    .hero-name {{ font-size: 2.5rem; }}
    .hero-subtitle {{ font-size: 1.125rem; }}
    .hero-avatar {{ width: 150px; height: 150px; }}
}}

/* ===================== SECTION HEADERS ===================== */
.section-header {{
    margin: 4rem 0 2rem 0;
    text-align: center;
}}

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
    font-size: 2.5rem;
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

/* ===================== KPI CARDS ===================== */
.kpi-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 1rem;
    margin: 2rem 0 3rem 0;
}}

@media (max-width: 1024px) {{
    .kpi-grid {{ grid-template-columns: repeat(3, 1fr); }}
}}
@media (max-width: 640px) {{
    .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}

.kpi-card {{
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 1.5rem 1.25rem;
    text-align: center;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}}

.kpi-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, {GRADIENT_START}, {GRADIENT_END});
    opacity: 0;
    transition: opacity 0.3s ease;
}}

.kpi-card:hover {{
    transform: translateY(-4px);
    border-color: {PRIMARY};
    box-shadow: 0 20px 40px {SHADOW};
}}
.kpi-card:hover::before {{
    opacity: 1;
}}

.kpi-value {{
    font-family: 'Inter', sans-serif;
    font-size: 2.25rem;
    font-weight: 700;
    background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 0.5rem;
}}

.kpi-label {{
    font-size: 0.8125rem;
    color: {TEXT_MUTED};
    font-weight: 500;
    line-height: 1.4;
}}

/* ===================== TIMELINE ===================== */
.timeline {{
    position: relative;
    padding: 1rem 0;
    margin: 2rem 0;
}}

.timeline::before {{
    content: '';
    position: absolute;
    left: 24px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, {PRIMARY}, {SECONDARY}, transparent);
}}

.timeline-item {{
    position: relative;
    padding-left: 64px;
    margin-bottom: 2rem;
}}

.timeline-dot {{
    position: absolute;
    left: 16px;
    top: 8px;
    width: 18px;
    height: 18px;
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
    -webkit-backdrop-filter: blur(16px);
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

.timeline-role {{
    font-size: 1.25rem;
    font-weight: 600;
    color: {TEXT};
    margin: 0 0 0.25rem 0;
}}

.timeline-company {{
    font-size: 0.9375rem;
    color: {SECONDARY};
    font-weight: 500;
    margin-bottom: 0.75rem;
}}

.timeline-desc {{
    font-size: 0.9375rem;
    color: {TEXT_MUTED};
    line-height: 1.6;
    margin: 0;
}}

.timeline-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.375rem;
    margin-top: 0.875rem;
}}

.timeline-tag {{
    font-size: 0.75rem;
    color: {TEXT};
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid {BORDER};
    padding: 0.25rem 0.625rem;
    border-radius: 6px;
    font-weight: 500;
}}

/* ===================== PROJECT CARDS ===================== */
.project-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
    margin: 2rem 0;
}}

@media (max-width: 768px) {{
    .project-grid {{ grid-template-columns: 1fr; }}
}}

.project-card {{
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 18px;
    padding: 1.75rem;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}}

.project-card::after {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.05), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}}

.project-card:hover {{
    transform: translateY(-6px);
    border-color: {PRIMARY};
    box-shadow: 0 24px 48px {SHADOW};
}}
.project-card:hover::after {{
    opacity: 1;
}}

.project-icon {{
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
}}

.project-title {{
    font-size: 1.25rem;
    font-weight: 600;
    color: {TEXT};
    margin: 0 0 0.5rem 0;
}}

.project-desc {{
    font-size: 0.9375rem;
    color: {TEXT_MUTED};
    line-height: 1.6;
    margin: 0 0 1rem 0;
}}

.project-link {{
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    color: {PRIMARY};
    font-weight: 500;
    font-size: 0.875rem;
    text-decoration: none;
    transition: all 0.2s ease;
}}
.project-link:hover {{
    gap: 0.625rem;
    color: {ACCENT};
}}

/* ===================== AWS CLOUD JOURNEY ===================== */
.aws-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}}

@media (max-width: 1024px) {{
    .aws-grid {{ grid-template-columns: repeat(3, 1fr); }}
}}
@media (max-width: 640px) {{
    .aws-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}

.aws-card {{
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 1.25rem;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.3s ease;
    text-align: center;
}}

.aws-card:hover {{
    transform: translateY(-4px);
    border-color: {SECONDARY};
    box-shadow: 0 16px 32px {SHADOW};
}}

.aws-icon {{
    font-size: 1.75rem;
    margin-bottom: 0.625rem;
}}

.aws-title {{
    font-size: 0.9375rem;
    font-weight: 600;
    color: {TEXT};
    margin: 0 0 0.25rem 0;
    line-height: 1.3;
}}

.aws-banner {{
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(14, 165, 233, 0.1));
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 2rem 0;
    text-align: center;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
}}

.aws-banner-text {{
    font-size: 1.0625rem;
    color: {TEXT};
    font-weight: 500;
    margin: 0;
}}

.aws-banner-sub {{
    font-size: 0.875rem;
    color: {TEXT_MUTED};
    margin: 0.5rem 0 0 0;
}}

/* ===================== STACK ===================== */
.stack-category {{
    margin-bottom: 2rem;
}}

.stack-category-title {{
    font-size: 0.8125rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: {PRIMARY};
    margin-bottom: 0.875rem;
    padding-left: 0.25rem;
}}

.stack-grid {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.625rem;
}}

.stack-chip {{
    background: {GLASS};
    border: 1px solid {BORDER};
    padding: 0.625rem 1.125rem;
    border-radius: 10px;
    font-size: 0.875rem;
    font-weight: 500;
    color: {TEXT};
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
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

/* ===================== FOOTER ===================== */
.footer {{
    margin-top: 5rem;
    padding: 3rem 2rem 2rem 2rem;
    background: {GLASS};
    border: 1px solid {BORDER};
    border-radius: 20px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
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
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #22C55E;
    box-shadow: 0 0 12px #22C55E;
    animation: pulse 2s infinite;
}}

@keyframes pulse {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0.5; }}
}}

.footer-status-text {{
    font-size: 0.875rem;
    font-weight: 600;
    color: #22C55E;
}}

.footer-title {{
    font-family: 'Playfair Display', serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0 0 0.5rem 0;
}}

.footer-subtitle {{
    font-size: 0.9375rem;
    color: {TEXT_MUTED};
    margin: 0 0 1.75rem 0;
}}

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

/* ===================== UTILITÁRIOS ===================== */
.divider {{
    height: 1px;
    background: linear-gradient(90deg, transparent, {BORDER}, transparent);
    margin: 3rem 0;
}}

/* Scrollbar customizada */
::-webkit-scrollbar {{
    width: 10px;
    height: 10px;
}}
::-webkit-scrollbar-track {{
    background: {BG};
}}
::-webkit-scrollbar-thumb {{
    background: {SURFACE_2};
    border-radius: 10px;
}}
::-webkit-scrollbar-thumb:hover {{
    background: {PRIMARY};
}}

/* Ajustes Streamlit nativos */
.stMarkdown {{
    color: {TEXT};
}}
h1, h2, h3, h4 {{
    color: {TEXT};
}}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================
st.markdown('<div class="hero-container">', unsafe_allow_html=True)

# Foto de perfil - CORREÇÃO: nome correto do arquivo
col_photo_l, col_photo, col_photo_r = st.columns([3, 2, 3])
with col_photo:
    try:
        st.image("rapha.jpeg", width=200, output_format="JPEG")
    except Exception:
        st.markdown(f"""
        <div class="hero-avatar-wrapper">
            <div class="hero-avatar" style="
                width: 200px; height: 200px; border-radius: 50%;
                background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
                display: flex; align-items: center; justify-content: center;
                font-family: 'Playfair Display', serif;
                font-size: 4rem; font-weight: 700; color: white;
                box-shadow: 0 0 0 8px {GLASS}, 0 20px 60px {SHADOW};
                margin: 0 auto;">
                RP
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown(f"""
<h1 class="hero-name">Raphael Fernando da Silva Pires</h1>
<div class="hero-title">Analista de Dados & Business Intelligence</div>
<p class="hero-subtitle">
    Transformando dados em decisões estratégicas. Mais de 16 anos construindo 
    inteligência de negócios que geram impacto real em organizações de diferentes portes.
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

# ============================================================================
# BOTÃO DOWNLOAD CURRÍCULO
# ============================================================================
st.markdown(f"""
<div style="text-align: center; margin: 2rem 0;">
""", unsafe_allow_html=True)

try:
    with open("Curriculo_Raphael_v2.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download Currículo PDF",
            data=pdf_bytes,
            file_name="Curriculo_Raphael_v2.pdf",
            mime="application/pdf",
            use_container_width=False
        )
except Exception as e:
    st.warning("📄 Currículo PDF não encontrado no repositório")

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# KPIs
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Impacto Mensurável</span>
    <h2 class="section-title">Números que contam histórias</h2>
    <p class="section-subtitle">Resultados construídos ao longo de uma trajetória consistente em dados e negócios.</p>
</div>

<div class="kpi-grid">
    <div class="kpi-card">
        <div class="kpi-value">16</div>
        <div class="kpi-label">anos de experiência profissional</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">70%</div>
        <div class="kpi-label">redução do tempo operacional</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">213k</div>
        <div class="kpi-label">registros processados</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">2h → 15min</div>
        <div class="kpi-label">análises reduzidas</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">R$50bi</div>
        <div class="kpi-label">dados públicos analisados</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# TIMELINE — EXPERIÊNCIA
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
                KPIs e IA Generativa. Redução de análises de 2 horas para 15 minutos através 
                de automação e modelagem inteligente de dados.
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
                e análise de viabilidade econômica, suportando decisões estratégicas com KPIs 
                estruturados.
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

# ============================================================================
# PROJETOS
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Portfólio</span>
    <h2 class="section-title">Projetos em destaque</h2>
    <p class="section-subtitle">Soluções reais aplicadas a dados públicos, análises governamentais e inteligência de mercado.</p>
</div>

<div class="project-grid">
    <div class="project-card">
        <div class="project-icon">🇧🇷</div>
        <h3 class="project-title">Desenrola Brasil</h3>
        <p class="project-desc">
            Análise de dados do programa governamental Desenrola Brasil, explorando renegociações, 
            perfis de consumidores e impacto social em larga escala.
        </p>
        <a href="#" class="project-link">Ver projeto →</a>
    </div>

    <div class="project-card">
        <div class="project-icon">🔬</div>
        <h3 class="project-title">CNPq Analytics</h3>
        <p class="project-desc">
            Dashboard analítico sobre bolsas e fomento do CNPq, com cruzamento de dados de pesquisa, 
            instituições e áreas do conhecimento em todo o Brasil.
        </p>
        <a href="#" class="project-link">Ver projeto →</a>
    </div>

    <div class="project-card">
        <div class="project-icon">⛽</div>
        <h3 class="project-title">Dashboard ANP</h3>
        <p class="project-desc">
            Inteligência de dados da Agência Nacional do Petróleo, com análise de preços, 
            distribuição e produção de combustíveis em território nacional.
        </p>
        <a href="#" class="project-link">Ver projeto →</a>
    </div>

    <div class="project-card">
        <div class="project-icon">💎</div>
        <h3 class="project-title">Portfólio Premium</h3>
        <p class="project-desc">
            Este próprio portfólio — construído em Streamlit com design premium, 
            demonstrando domínio de UX, visualização de dados e engenharia de front-end.
        </p>
        <a href="#" class="project-link">Você está aqui →</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# AWS CLOUD JOURNEY
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

# ============================================================================
# STACK TECNOLÓGICA
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

# ============================================================================
# GRÁFICO PLOTLY — VISUALIZAÇÃO DE IMPACTO
# ============================================================================
st.markdown(f"""
<div class="section-header">
    <span class="section-label">Visualização</span>
    <h2 class="section-title">Impacto em números</h2>
    <p class="section-subtitle">Representação visual dos principais resultados da trajetória profissional.</p>
</div>
""", unsafe_allow_html=True)

# Dados do gráfico
df_impact = pd.DataFrame({
    "Área": ["Automação VBA", "Análises BI", "Processamento", "Dashboards", "IA Generativa"],
    "Ganho de Eficiência (%)": [70, 87, 65, 80, 55]
})

fig_impact = go.Figure()

fig_impact.add_trace(go.Bar(
    x=df_impact["Área"],
    y=df_impact["Ganho de Eficiência (%)"],
    marker=dict(
        color=df_impact["Ganho de Eficiência (%)"],
        colorscale=[[0, GRADIENT_START], [1, GRADIENT_END]],
        line=dict(width=0)
        # CORREÇÃO: removido cornerradius que não é válido
    ),
    text=df_impact["Ganho de Eficiência (%)"].apply(lambda x: f"{x}%"),
    textposition="outside",
    textfont=dict(color=TEXT, size=13, family="Inter"),
    hovertemplate="<b>%{x}</b><br>Ganho: %{y}%<extra></extra>"
))

fig_impact.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter", color=TEXT),
    height=420,
    margin=dict(l=20, r=20, t=20, b=60),
    xaxis=dict(
        showgrid=False,
        line=dict(color=BORDER),
        tickfont=dict(color=TEXT_MUTED, size=12),
        zeroline=False
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor=BORDER,
        gridwidth=1,
        line=dict(color=BORDER),
        tickfont=dict(color=TEXT_MUTED, size=12),
        zeroline=False,
        range=[0, 100]
    ),
    hoverlabel=dict(
        bgcolor=SURFACE,
        bordercolor=PRIMARY,
        font=dict(color=TEXT, family="Inter", size=13)
    ),
    showlegend=False
)

st.plotly_chart(fig_impact, use_container_width=True)

# ============================================================================
# FOOTER
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

# Espaçamento final
st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
