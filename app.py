import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
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
# TEMA (DARK / LIGHT)
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def get_colors():
    dark = st.session_state.theme == "dark"
    if dark:
        return {
            "primary": "#3B82F6",
            "secondary": "#0EA5E9",
            "bg": "#0B0F1A",
            "text": "#F1F5F9",
            "text_muted": "#94A3B8",
            "card_bg": "rgba(255,255,255,0.04)",
            "border": "rgba(255,255,255,0.08)",
            "tag_bg": "rgba(59,130,246,0.15)",
            "tag_border": "rgba(59,130,246,0.25)",
            "primary_light": "rgba(59,130,246,0.2)",
            "navbar_bg": "rgba(11,15,26,0.75)",
            "navbar_border": "rgba(255,255,255,0.06)",
            "nav_hover": "rgba(255,255,255,0.06)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.08) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(59,130,246,0.15) 0%, transparent 60%)",
            "section_bg": "rgba(11,15,26,0.5)",
            "section_alt_bg": "rgba(255,255,255,0.02)",
            "shadow": "0 8px 32px rgba(0,0,0,0.4)",
            "shadow_hover": "0 12px 40px rgba(59,130,246,0.2)",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6","#0EA5E9","#60A5FA","#2563EB","#0284C7"]
        }
    else:
        return {
            "primary": "#1D4ED8",
            "secondary": "#0EA5E9",
            "bg": "#F8FAFC",
            "text": "#0F172A",
            "text_muted": "#475569",
            "card_bg": "rgba(255,255,255,0.7)",
            "border": "rgba(0,0,0,0.06)",
            "tag_bg": "#DBEAFE",
            "tag_border": "#93C5FD",
            "primary_light": "#DBEAFE",
            "navbar_bg": "rgba(248,250,252,0.8)",
            "navbar_border": "rgba(0,0,0,0.04)",
            "nav_hover": "rgba(0,0,0,0.04)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.04) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(29,78,216,0.08) 0%, transparent 60%)",
            "section_bg": "rgba(255,255,255,0.5)",
            "section_alt_bg": "rgba(0,0,0,0.01)",
            "shadow": "0 8px 32px rgba(0,0,0,0.06)",
            "shadow_hover": "0 12px 40px rgba(29,78,216,0.1)",
            "plotly_template": "plotly_white",
            "chart_colors": ["#1D4ED8","#0EA5E9","#3B82F6","#2563EB","#0284C7"]
        }

# ============================================================================
# FUNÇÕES AUXILIARES (FOTO, PDF)
# ============================================================================
def get_foto_path():
    candidatos = [
        "assets/rapha.jpeg", "assets/rapha.jpg",
        "rapha.jpeg", "rapha.jpg",
        "foto.jpeg", "foto.jpg",
        "perfil.jpeg", "perfil.jpg"
    ]
    for caminho in candidatos:
        if os.path.exists(caminho):
            return caminho
    return None

def get_foto_url():
    caminho = get_foto_path()
    if caminho:
        return caminho
    return "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff"

def get_pdf_path():
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
# CSS (com espaçamento reduzido)
# ============================================================================
def load_css():
    colors = get_colors()
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap');

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, sans-serif;
            background: {colors['bg']};
            color: {colors['text']};
            scroll-behavior: smooth;
        }}
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: {colors['bg']}; }}
        .block-container {{ padding: 0 !important; max-width: 100%; }}

        /* Navbar */
        .navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 999;
            background: {colors['navbar_bg']};
            backdrop-filter: blur(16px) saturate(180%);
            -webkit-backdrop-filter: blur(16px) saturate(180%);
            border-bottom: 1px solid {colors['navbar_border']};
            padding: 0.75rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .navbar-brand {{ font-weight: 700; font-size: 1.25rem; letter-spacing: -0.02em; color: {colors['text']}; text-decoration: none; }}
        .navbar-brand span {{ color: {colors['primary']}; }}
        .navbar-links {{ display: flex; gap: 0.5rem; align-items: center; }}
        .nav-link {{
            padding: 0.4rem 1rem; border-radius: 999px; font-size: 0.875rem;
            font-weight: 500; text-decoration: none; transition: all 0.2s;
            color: {colors['text_muted']}; background: transparent;
            cursor: pointer;
        }}
        .nav-link:hover {{ background: {colors['nav_hover']}; color: {colors['text']}; }}
        .nav-link.active {{
            background: {colors['primary']}; color: white;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
        }}

        /* Hero – espaçamento reduzido */
        .hero-full {{
            min-height: 70vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 4rem 2rem 2rem;
            background: {colors['hero_bg']};
            position: relative;
            overflow: hidden;
        }}
        .hero-full::before {{
            content: ''; position: absolute; inset: 0;
            background: {colors['hero_glow']};
            opacity: 0.4; pointer-events: none;
        }}
        .hero-content {{
            max-width: 1200px; width: 100%;
            display: grid; grid-template-columns: 1fr 2fr;
            gap: 2rem;
            align-items: center;
            position: relative; z-index: 1;
        }}
        @media (max-width: 768px) {{
            .hero-content {{ grid-template-columns: 1fr; text-align: center; }}
        }}
        .hero-photo img {{
            width: 220px; height: 220px; border-radius: 50%;
            object-fit: cover; border: 4px solid {colors['primary']};
            box-shadow: 0 20px 60px rgba(59,130,246,0.25);
        }}
        .hero-text h1 {{ font-size: 2.8rem; font-weight: 800; letter-spacing: -0.03em; line-height: 1.1; color: {colors['text']}; }}
        .hero-text h1 span {{ color: {colors['primary']}; }}
        .hero-text .subtitle {{ font-size: 1.1rem; color: {colors['text_muted']}; margin: 0.5rem 0 1rem; line-height: 1.6; }}
        .hero-text .badge-group {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }}
        .hero-text .badge {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.3rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 500; color: {colors['text']};
        }}
        .hero-text .cta-group {{ display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem; }}
        .btn-primary {{
            background: {colors['primary']}; color: white;
            padding: 0.6rem 1.5rem; border-radius: 999px;
            font-weight: 600; text-decoration: none; transition: 0.2s;
            display: inline-block; border: none; cursor: pointer;
        }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(59,130,246,0.35); }}
        .btn-secondary {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']};
            padding: 0.6rem 1.5rem; border-radius: 999px;
            font-weight: 500; color: {colors['text']}; text-decoration: none;
            transition: 0.2s; display: inline-block;
        }}
        .btn-secondary:hover {{ background: {colors['nav_hover']}; }}

        /* Seções */
        .section-glass {{
            padding: 3rem 2rem;
            background: {colors['section_bg']};
            backdrop-filter: blur(4px);
            border-top: 1px solid {colors['border']};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .section-header {{ text-align: center; margin-bottom: 2rem; }}
        .section-header .label {{
            display: inline-block;
            background: {colors['primary_light']};
            padding: 0.2rem 1rem; border-radius: 999px;
            font-size: 0.7rem; font-weight: 600; text-transform: uppercase;
            letter-spacing: 0.08em; color: {colors['primary']};
        }}
        .section-header h2 {{ font-size: 2.2rem; font-weight: 700; margin-top: 0.5rem; color: {colors['text']}; letter-spacing: -0.02em; }}
        .section-header p {{ color: {colors['text_muted']}; max-width: 600px; margin: 0.5rem auto 0; }}

        .glass-card {{
            background: {colors['card_bg']};
            backdrop-filter: blur(8px);
            border: 1px solid {colors['border']};
            border-radius: 24px;
            padding: 1.5rem;
            transition: all 0.25s ease;
            box-shadow: {colors['shadow']};
        }}
        .glass-card:hover {{ transform: translateY(-6px); border-color: {colors['primary']}; box-shadow: {colors['shadow_hover']}; }}

        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
            width: 2px; background: linear-gradient(to bottom, {colors['primary']}, {colors['secondary']}, transparent);
        }}
        .timeline-item {{ position: relative; padding-left: 80px; margin-bottom: 2rem; }}
        .timeline-dot {{
            position: absolute; left: 20px; top: 6px; width: 18px; height: 18px;
            border-radius: 50%; background: {colors['primary']};
            border: 3px solid {colors['bg']}; box-shadow: 0 0 0 4px {colors['primary']};
        }}
        .timeline-card {{
            background: {colors['card_bg']};
            backdrop-filter: blur(4px);
            border: 1px solid {colors['border']};
            border-radius: 20px; padding: 1.5rem;
            transition: 0.25s;
        }}
        .timeline-card:hover {{ border-color: {colors['primary']}; transform: translateX(6px); }}
        .timeline-date {{
            display: inline-block; font-size: 0.7rem; font-weight: 600;
            background: {colors['primary_light']}; color: {colors['primary']};
            padding: 0.2rem 0.8rem; border-radius: 999px;
        }}
        .timeline-badge {{
            background: {colors['primary']}; color: white;
            font-size: 0.6rem; font-weight: 700; padding: 0.15rem 0.6rem;
            border-radius: 999px; margin-left: 0.5rem; display: inline-block;
        }}
        .timeline-role {{ font-size: 1.1rem; font-weight: 700; margin: 0.3rem 0; }}
        .timeline-company {{ color: {colors['secondary']}; font-weight: 600; }}
        .timeline-desc {{ color: {colors['text_muted']}; line-height: 1.6; }}
        .timeline-tag {{
            font-size: 0.7rem; background: {colors['tag_bg']};
            border: 1px solid {colors['tag_border']}; padding: 0.2rem 0.6rem;
            border-radius: 6px; display: inline-block; margin: 0.2rem;
        }}

        .testimonial-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
        @media (max-width: 768px) {{ .testimonial-grid {{ grid-template-columns: 1fr; }} }}

        .footer {{
            padding: 2.5rem 2rem; text-align: center;
            border-top: 1px solid {colors['border']};
            background: {colors['card_bg']};
            backdrop-filter: blur(4px);
        }}
        .footer .status {{
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.2);
            padding: 0.3rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 500; color: #22C55E;
        }}
        .footer .status-dot {{
            width: 8px; height: 8px; border-radius: 50%;
            background: #22C55E; box-shadow: 0 0 12px #22C55E;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} }}
        .footer-links {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; }}
        .footer-link {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.4rem 1rem; border-radius: 999px;
            color: {colors['text']}; text-decoration: none;
            font-size: 0.85rem; transition: 0.2s;
        }}
        .footer-link:hover {{ background: {colors['primary']}; color: white; }}
        .footer-copy {{ color: {colors['text_muted']}; font-size: 0.8rem; }}

        @media (max-width: 768px) {{
            .navbar {{ padding: 0.5rem 1rem; flex-wrap: wrap; }}
            .navbar-links {{ gap: 0.3rem; flex-wrap: wrap; }}
            .hero-full {{ padding: 3rem 1rem 1.5rem; min-height: auto; }}
            .hero-text h1 {{ font-size: 1.8rem; }}
            .hero-photo img {{ width: 140px; height: 140px; }}
            .section-glass {{ padding: 2rem 1rem; }}
        }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# RENDERIZAÇÃO DAS PÁGINAS
# ============================================================================

def render_home():
    colors = get_colors()
    foto_path = get_foto_path()
    foto_url = foto_path if foto_path else "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff"
    pdf_path = get_pdf_path()

    st.markdown('<section class="hero-full">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    with col1:
        if foto_path:
            st.image(foto_path, width=220)
        else:
            st.image(foto_url, width=220)

    with col2:
        st.markdown(f"""
        <div class="hero-text">
            <h1>Raphael <span>Pires</span></h1>
            <p class="subtitle">Analista de Dados &amp; Business Intelligence<br>Mais de <strong>16 anos</strong> transformando dados em decisões estratégicas.</p>
            <div class="badge-group">
                <span class="badge">📊 Power BI</span>
                <span class="badge">🐍 Python</span>
                <span class="badge">🗄️ SQL</span>
                <span class="badge">☁️ AWS</span>
                <span class="badge">🤖 IA Generativa</span>
                <span class="badge">📈 Dashboards</span>
            </div>
            <div class="cta-group">
                <a href="#experiencia" class="btn-primary">Ver trajetória ↓</a>
                {'<a href="' + pdf_path + '" download class="btn-secondary">📄 Baixar CV</a>' if pdf_path else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</section>', unsafe_allow_html=True)

    # KPIs
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Impacto Mensurável</span>
                <h2>Números que contam histórias</h2>
            </div>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("16+", "anos de experiência")
    col2.metric("70%", "redução operacional")
    col3.metric("213k", "registros processados")
    col4.metric("2h→15m", "tempo de análise")
    col5.metric("R$50bi", "dados analisados")
    st.markdown("</div></div>", unsafe_allow_html=True)

    # Experiência
    st.markdown("""
    <div class="section-glass" id="experiencia">
        <div class="container">
            <div class="section-header">
                <span class="label">Trajetória</span>
                <h2>Experiência profissional</h2>
            </div>
            <div class="timeline">
    """, unsafe_allow_html=True)

    experiences = [
        {"date":"2014 – Presente · 10+ anos","role":"Analista de Dados & BI","company":"NSM Comércio","desc":"Centralização de dados, construção de indicadores estratégicos, automação de relatórios e governança. Redução de 70% do tempo operacional.","tags":["Dados","Governança","Indicadores","Automação"],"badge":"Atual"},
        {"date":"2012 – Presente · 12+ anos","role":"Fundador & Analista de Dados","company":"Jardim do Éden (Varejo de Moda)","desc":"Estruturação da base de dados, modelagem, limpeza, integração e desenvolvimento de dashboards gerenciais com SQL, Python, Power BI e Looker Studio — reduzindo ciclo de análise de 2h para 15 min.","tags":["Power BI","Python","SQL","IA Generativa"],"badge":""},
        {"date":"2010 – 2014 · 4 anos","role":"Fundador & Analista de KPIs","company":"J Sintonía (Varejo Especializado)","desc":"Monitoramento de KPIs de vendas, margem e rentabilidade com relatórios automatizados. Análise de viabilidade econômica que fundamentou encerramento estratégico planejado em 2026, evitando prejuízo.","tags":["BI","KPIs","Dashboards"],"badge":""},
        {"date":"2009 – 2010 · 1 ano","role":"Estagiário de Automação e Dados","company":"Banco do Brasil S.A.","desc":"Desenvolvimento de macros VBA em 20 agências, reduzindo 70% do tempo operacional. Saneou e padronizou bases de dados gerenciais internas.","tags":["VBA","Automação","Eficiência"],"badge":""}
    ]

    for exp in experiences:
        tags = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        badge = f'<span class="timeline-badge">{exp["badge"]}</span>' if exp["badge"] else ""
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span> {badge}
                <div class="timeline-role">{exp["role"]}</div>
                <div class="timeline-company">{exp["company"]}</div>
                <div class="timeline-desc">{exp["desc"]}</div>
                <div>{tags}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div></div>", unsafe_allow_html=True)

    # Projetos
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Portfólio</span>
                <h2>Projetos de Analytics</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
                <div class="glass-card">
                    <h3>🇧🇷 Desenrola Brasil</h3>
                    <p style="color:var(--text-muted);">Painel analítico executivo com Python, Pandas, Plotly e Streamlit. Processamento de dados oficiais do Banco Central com KPIs, séries temporais e análise de concentração de mercado (HHI).</p>
                    <a href="https://desenrolabrasil.streamlit.app" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">🔗 Ver App</a>
                </div>
                <div class="glass-card">
                    <h3>🔬 CNPq Analytics</h3>
                    <p style="color:var(--text-muted);">ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos, evidenciando desigualdades regionais. Dashboard interativo com filtros dinâmicos.</p>
                    <a href="https://cnpa-analytics.streamlit.app" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">🔗 Ver App</a>
                </div>
                <div class="glass-card">
                    <h3>⛽ Análise de Preços de Combustíveis (ANP)</h3>
                    <p style="color:var(--text-muted);">Dashboard interativo com filtros temporais e regionais utilizando dados oficiais da Agência Nacional do Petróleo.</p>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">📊 Ver Projeto</a>
                </div>
                <div class="glass-card">
                    <h3>💎 Portfólio Premium</h3>
                    <p style="color:var(--text-muted);">Este portfólio construído em Streamlit com design premium, glassmorphism e navegação fixa. Código aberto no GitHub.</p>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">💻 Ver Código</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Certificações
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Certificações</span>
                <h2>Formação contínua</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5rem;">
                <div class="glass-card" style="text-align:center;">
                    <div style="font-size:2rem;">📘</div>
                    <h4>Hashtag Treinamentos</h4>
                    <p style="color:var(--text-muted);font-size:0.9rem;">SQL Avançado · Power BI · Python para Análise de Dados · Algoritmos e IA Aplicada</p>
                </div>
                <div class="glass-card" style="text-align:center;">
                    <div style="font-size:2rem;">☁️</div>
                    <h4>AWS Educate</h4>
                    <p style="color:var(--text-muted);font-size:0.9rem;">8 módulos concluídos: Cloud Computing, Console, Storage, ML Foundations, Sustainability, Cloud Support</p>
                    <span style="background:var(--primary);color:white;padding:0.2rem 0.8rem;border-radius:999px;font-size:0.7rem;font-weight:600;">40%</span>
                </div>
                <div class="glass-card" style="text-align:center;">
                    <div style="font-size:2rem;">🎯</div>
                    <h4>Meta 2026</h4>
                    <p style="color:var(--text-muted);font-size:0.9rem;">Certificação AWS Cloud Practitioner — em preparação ativa</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # AWS Journey
    st.markdown(f"""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Cloud Journey</span>
                <h2>☁️ AWS em progresso</h2>
                <p style="color:var(--text-muted);">Atualmente em trilha de certificação, com foco em arquitetura de dados e machine learning na nuvem.</p>
            </div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;text-align:center;">
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">📘</div><div>Cloud 101</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🖥️</div><div>AWS Console</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">💾</div><div>Storage</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🤖</div><div>ML Foundations</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🌱</div><div>Sustainability</div></div>
            </div>
            <div style="text-align:center;margin-top:1.5rem;">
                <span style="background:{colors['primary_light']};color:{colors['primary']};padding:0.2rem 1.2rem;border-radius:999px;font-size:0.8rem;font-weight:600;">🎯 Meta 2026: AWS Cloud Practitioner</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Skills
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Competências</span>
                <h2>Domínio tecnológico</h2>
            </div>
    """, unsafe_allow_html=True)
    render_skills_chart()
    st.markdown("</div></div>", unsafe_allow_html=True)

def render_skills_chart():
    colors = get_colors()
    df = pd.DataFrame({
        "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
        "Proficiência": [95, 92, 88, 95, 85, 60, 82],
        "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
    })
    fig = px.bar(
        df,
        x="Proficiência",
        y="Tecnologia",
        color="Categoria",
        orientation="h",
        color_discrete_sequence=colors["chart_colors"],
        template=colors["plotly_template"],
        text="Proficiência"
    )
    fig.update_layout(
        height=380,
        margin=dict(l=20, r=40, t=20, b=40),
        xaxis=dict(range=[0, 105], showgrid=True, gridcolor="rgba(148,163,184,0.15)"),
        yaxis=dict(showgrid=False),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Inter", color=colors["text"]),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    fig.update_traces(textposition="outside", textfont=dict(color=colors["text"], size=11))
    st.plotly_chart(fig, use_container_width=True)

def render_analytics():
    colors = get_colors()
    st.title("📊 Analytics Interativo")
    st.caption("Demonstrações construídas em Streamlit + Plotly")
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ ANP", "📈 Impacto Operacional"])

    with tabs[0]:
        np.random.seed(42)
        regioes = ["Sudeste","Nordeste","Sul","Centro-Oeste","Norte"]
        status = ["Renegociado","Em Negociação","Inadimplente"]
        df = pd.DataFrame({
            "Região": np.random.choice(regioes, 400, p=[.45,.28,.15,.07,.05]),
            "Valor": np.random.lognormal(8.5, 1.2, 400),
            "Status": np.random.choice(status, 400, p=[.65,.25,.10])
        })
        col1, col2 = st.columns(2)
        reg = col1.multiselect("Região", regioes, default=regioes)
        stat = col2.multiselect("Status", status, default=status)
        filtro = df[df["Região"].isin(reg) & df["Status"].isin(stat)]
        if filtro.empty:
            st.info("Nenhum registro encontrado.")
        else:
            k1, k2, k3 = st.columns(3)
            k1.metric("Contratos", f"{len(filtro):,}")
            k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f} M")
            k3.metric("Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
            a, b = st.columns(2)
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=.6, template=colors["plotly_template"])
            fig2 = px.histogram(filtro, x="Status", color="Status", template=colors["plotly_template"])
            a.plotly_chart(fig1, use_container_width=True)
            b.plotly_chart(fig2, use_container_width=True)

    with tabs[1]:
        estados = ["SP","RJ","MG","PR"]
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]
        dados = []
        np.random.seed(1)
        for e in estados:
            preco = 5.4
            for m in meses:
                preco += np.random.normal(0, .10)
                dados.append([e, m, preco])
        df = pd.DataFrame(dados, columns=["Estado","Mês","Preço"])
        estado = st.selectbox("Estado", estados)
        f = df[df["Estado"] == estado]
        st.metric("Preço Médio", f"R$ {f['Preço'].mean():.2f}")
        fig = px.line(f, x="Mês", y="Preço", markers=True, template=colors["plotly_template"])
        st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        antes = [120,125,118,130,122,128,126,124,129,127,125,130]
        depois = [95,70,55,45,38,35,33,32,30,29,28,27]
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        df = pd.DataFrame({
            "Mês": meses*2,
            "Horas": antes + depois,
            "Período": ["Antes"]*12 + ["Depois"]*12
        })
        fig = px.area(df, x="Mês", y="Horas", color="Período", template=colors["plotly_template"])
        st.plotly_chart(fig, use_container_width=True)
        k1, k2, k3 = st.columns(3)
        k1.metric("Horas Economizadas", "1.108 h", "+93%")
        k2.metric("Custo Evitado", "R$ 185 mil", "+185 mil")
        k3.metric("Projetos", "24", "+60%")

def render_dashboard():
    colors = get_colors()
    st.title("📊 Dashboard Interativo")
    st.caption("Simulação de indicadores de negócio com dados aleatórios.")

    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    projetos = ["Análise de Churn","Dashboard de Vendas","Otimização de Preços","Segmentação de Clientes","Previsão de Demanda","Análise de Sentimento","Modelo de Propensão","Automação de Relatórios","Análise de ROI","Monitoramento de KPIs"]
    regioes = ["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
    status = ["Concluído","Em Andamento","Planejado"]
    data=[]
    for i in range(150):
        data.append({
            "Projeto": np.random.choice(projetos),
            "Data": np.random.choice(dates),
            "Região": np.random.choice(regioes, p=[0.45,0.20,0.18,0.10,0.07]),
            "Status": np.random.choice(status, p=[0.55,0.30,0.15]),
            "Valor": round(np.random.lognormal(9,0.8),2),
            "Horas": np.random.randint(20,400),
            "Satisfacao": np.random.randint(60,100),
            "Complexidade": np.random.choice(["Baixa","Média","Alta"], p=[0.2,0.5,0.3])
        })
    df = pd.DataFrame(data)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].dt.strftime("%Y-%m")

    col1, col2, col3 = st.columns(3)
    with col1:
        periodo = st.selectbox("Período", ["Últimos 6 meses","Últimos 12 meses","Últimos 24 meses"], index=1)
    with col2:
        regiao = st.selectbox("Região", ["Todas"] + sorted(df["Região"].unique().tolist()), index=0)
    with col3:
        status_filtro = st.selectbox("Status", ["Todos"] + sorted(df["Status"].unique().tolist()), index=0)

    df_filtrado = df.copy()
    ultima_data = df["Data"].max()
    if periodo == "Últimos 6 meses":
        data_corte = ultima_data - timedelta(days=180)
    elif periodo == "Últimos 12 meses":
        data_corte = ultima_data - timedelta(days=365)
    else:
        data_corte = ultima_data - timedelta(days=730)
    df_filtrado = df_filtrado[df_filtrado["Data"] >= data_corte]
    if regiao != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Região"] == regiao]
    if status_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status"] == status_filtro]

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total de Projetos", f"{len(df_filtrado):,}")
    k2.metric("Receita Total", f"R$ {df_filtrado['Valor'].sum()/1e6:.1f}M")
    k3.metric("Ticket Médio", f"R$ {df_filtrado['Valor'].mean():,.0f}".replace(",","."))
    k4.metric("Satisfação Média", f"{df_filtrado['Satisfacao'].mean():.1f}%")

    fig1 = px.bar(df_filtrado.groupby("Mes").size().reset_index(name="Quantidade").sort_values("Mes"), x="Mes", y="Quantidade", title="Projetos por Mês", color_discrete_sequence=[colors["chart_colors"][0]], template=colors["plotly_template"])
    fig1.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    fig2 = px.pie(df_filtrado.groupby("Região")["Valor"].sum().reset_index(), names="Região", values="Valor", title="Receita por Região", hole=0.4, color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
    fig2.update_layout(height=350, margin=dict(l=10,r=10,t=50,b=20), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    fig3 = px.line(df_filtrado.groupby("Mes")["Valor"].sum().reset_index().sort_values("Mes"), x="Mes", y="Valor", title="Evolução da Receita", markers=True, color_discrete_sequence=[colors["chart_colors"][1]], template=colors["plotly_template"])
    fig3.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    fig4 = px.scatter(df_filtrado, x="Horas", y="Valor", color="Complexidade", size="Satisfacao", title="Esforço vs. Retorno", color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
    fig4.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    fig5 = px.bar(df_filtrado["Status"].value_counts().reset_index(), x="count", y="Status", orientation="h", title="Status dos Projetos", color="Status", color_discrete_sequence=colors["chart_colors"][3:], template=colors["plotly_template"])
    fig5.update_layout(height=300, margin=dict(l=20,r=20,t=50,b=20), showlegend=False, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))

    c1, c2 = st.columns(2)
    c1.plotly_chart(fig1, use_container_width=True)
    c2.plotly_chart(fig2, use_container_width=True)
    c1, c2 = st.columns(2)
    c1.plotly_chart(fig3, use_container_width=True)
    c2.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("📋 Dados detalhados"):
        st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)

def render_footer():
    st.markdown("""
    <div class="footer">
        <div class="status">
            <span class="status-dot"></span>
            Disponível para oportunidades
        </div>
        <h3 style="font-size:1.5rem;font-weight:700;margin:1rem 0 0.3rem;">Vamos conversar sobre dados?</h3>
        <p style="color:var(--text-muted);margin-bottom:1.5rem;">Aberto a projetos em Dados, BI e Cloud</p>
        <div style="display:flex;justify-content:center;gap:0.5rem;flex-wrap:wrap;margin-bottom:1.5rem;">
            <span class="footer-mode" style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">🏠 Remoto</span>
            <span class="footer-mode" style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">🏢 Híbrido</span>
            <span class="footer-mode" style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">📍 Presencial</span>
            <span class="footer-mode" style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">✈️ Viagens</span>
        </div>
        <div class="footer-links">
            <a href="https://www.linkedin.com/in/raphaelpires" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="https://github.com/raphaelcaxias" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="mailto:contato@raphaelpires.com" class="footer-link">✉️ E-mail</a>
            <a href="tel:+5511999999999" class="footer-link">📱 Telefone</a>
        </div>
        <p class="footer-copy">© 2026 Raphael Fernando da Silva Pires</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN
# ============================================================================
def main():
    load_css()

    # Botão de tema
    col1, col2, col3 = st.columns([10, 1, 1])
    with col3:
        theme_label = "☀️" if st.session_state.theme == "dark" else "🌙"
        st.button(theme_label, on_click=toggle_theme, key="theme_btn", use_container_width=True)

    # Navbar
    page = st.query_params.get("page", "home")
    st.markdown(f"""
    <nav class="navbar">
        <a href="/" class="navbar-brand">Raphael <span>Pires</span></a>
        <div class="navbar-links">
            <a href="?page=home" class="nav-link {'active' if page == 'home' else ''}">Início</a>
            <a href="?page=analytics" class="nav-link {'active' if page == 'analytics' else ''}">Análises</a>
            <a href="?page=dashboard" class="nav-link {'active' if page == 'dashboard' else ''}">Dashboard</a>
        </div>
    </nav>
    """, unsafe_allow_html=True)

    # Conteúdo
    if page == "home":
        render_home()
    elif page == "analytics":
        render_analytics()
    elif page == "dashboard":
        render_dashboard()
    else:
        render_home()

    render_footer()

if __name__ == "__main__":
    main()
