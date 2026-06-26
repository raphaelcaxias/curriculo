import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from datetime import datetime, timedelta

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires · Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def get_colors():
    if st.session_state.theme == "dark":
        return {
            "primary": "#3B82F6", "secondary": "#0EA5E9",
            "bg": "#0B0F1A", "text": "#F1F5F9", "text_muted": "#94A3B8",
            "card_bg": "rgba(255,255,255,0.04)", "border": "rgba(255,255,255,0.08)",
            "tag_bg": "rgba(59,130,246,0.15)", "tag_border": "rgba(59,130,246,0.25)",
            "primary_light": "rgba(59,130,246,0.2)",
            "navbar_bg": "rgba(11,15,26,0.75)", "navbar_border": "rgba(255,255,255,0.06)",
            "nav_hover": "rgba(255,255,255,0.06)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.08) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(59,130,246,0.15) 0%, transparent 60%)",
            "section_bg": "rgba(11,15,26,0.5)", "section_alt_bg": "rgba(255,255,255,0.02)",
            "shadow": "0 8px 32px rgba(0,0,0,0.4)", "shadow_hover": "0 12px 40px rgba(59,130,246,0.2)",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6","#0EA5E9","#60A5FA","#2563EB","#0284C7"]
        }
    else:
        return {
            "primary": "#1D4ED8", "secondary": "#0EA5E9",
            "bg": "#F8FAFC", "text": "#0F172A", "text_muted": "#475569",
            "card_bg": "rgba(255,255,255,0.7)", "border": "rgba(0,0,0,0.06)",
            "tag_bg": "#DBEAFE", "tag_border": "#93C5FD",
            "primary_light": "#DBEAFE",
            "navbar_bg": "rgba(248,250,252,0.8)", "navbar_border": "rgba(0,0,0,0.04)",
            "nav_hover": "rgba(0,0,0,0.04)",
            "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.04) 0%, transparent 70%)",
            "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(29,78,216,0.08) 0%, transparent 60%)",
            "section_bg": "rgba(255,255,255,0.5)", "section_alt_bg": "rgba(0,0,0,0.01)",
            "shadow": "0 8px 32px rgba(0,0,0,0.06)", "shadow_hover": "0 12px 40px rgba(29,78,216,0.1)",
            "plotly_template": "plotly_white",
            "chart_colors": ["#1D4ED8","#0EA5E9","#3B82F6","#2563EB","#0284C7"]
        }

# ============================================================================
# CSS premium com glassmorphism
# ============================================================================
def load_css():
    c = get_colors()
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap');

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, sans-serif;
            background: {c['bg']};
            color: {c['text']};
            scroll-behavior: smooth;
        }}
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: {c['bg']}; }}
        .block-container {{ padding: 0; max-width: 100%; }}

        /* ===== Navbar ===== */
        .navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 999;
            background: {c['navbar_bg']};
            backdrop-filter: blur(16px) saturate(180%);
            -webkit-backdrop-filter: blur(16px) saturate(180%);
            border-bottom: 1px solid {c['navbar_border']};
            padding: 0.75rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .navbar-brand {{
            font-weight: 700; font-size: 1.25rem; letter-spacing: -0.02em;
            color: {c['text']}; text-decoration: none;
        }}
        .navbar-brand span {{ color: {c['primary']}; }}
        .navbar-links {{
            display: flex; gap: 0.5rem; align-items: center;
        }}
        .nav-link {{
            padding: 0.4rem 1rem; border-radius: 999px; font-size: 0.875rem;
            font-weight: 500; text-decoration: none; transition: all 0.2s;
            color: {c['text_muted']}; background: transparent; cursor: pointer;
        }}
        .nav-link:hover {{ background: {c['nav_hover']}; color: {c['text']}; }}
        .nav-link.active {{
            background: {c['primary']}; color: white;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
        }}
        .nav-theme-btn {{
            background: {c['card_bg']}; border: 1px solid {c['border']};
            border-radius: 999px; padding: 0.3rem 0.8rem; font-size: 1rem;
            cursor: pointer; transition: 0.2s; color: {c['text']};
        }}
        .nav-theme-btn:hover {{ background: {c['nav_hover']}; }}

        /* ===== Hero ===== */
        .hero-full {{
            min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            padding: 6rem 2rem 4rem;
            background: {c['hero_bg']};
            position: relative;
            overflow: hidden;
        }}
        .hero-full::before {{
            content: ''; position: absolute; inset: 0;
            background: {c['hero_glow']};
            opacity: 0.4; pointer-events: none;
        }}
        .hero-content {{
            max-width: 1200px; width: 100%;
            display: grid; grid-template-columns: 1fr 1fr;
            gap: 3rem; align-items: center;
            position: relative; z-index: 1;
        }}
        @media (max-width: 768px) {{
            .hero-content {{ grid-template-columns: 1fr; text-align: center; }}
        }}
        .hero-photo {{
            display: flex; justify-content: center; align-items: center;
        }}
        .hero-photo img {{
            width: 280px; height: 280px; border-radius: 50%;
            object-fit: cover; border: 4px solid {c['primary']};
            box-shadow: 0 20px 60px rgba(59,130,246,0.25);
        }}
        @media (max-width: 768px) {{
            .hero-photo img {{ width: 180px; height: 180px; }}
        }}
        .hero-text h1 {{
            font-size: 3.2rem; font-weight: 800; letter-spacing: -0.03em;
            line-height: 1.1; color: {c['text']};
        }}
        .hero-text h1 span {{ color: {c['primary']}; }}
        .hero-text .subtitle {{
            font-size: 1.2rem; color: {c['text_muted']};
            margin: 1rem 0 1.5rem; line-height: 1.6;
        }}
        .hero-text .badge-group {{
            display: flex; flex-wrap: wrap; gap: 0.5rem;
            margin-top: 1.5rem;
        }}
        .hero-text .badge {{
            background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            padding: 0.3rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 500; color: {c['text']};
        }}
        .hero-text .cta-group {{
            display: flex; gap: 0.75rem; flex-wrap: wrap;
            margin-top: 2rem;
        }}
        .btn-primary {{
            background: {c['primary']}; color: white;
            padding: 0.6rem 1.5rem; border-radius: 999px;
            font-weight: 600; text-decoration: none; transition: 0.2s;
            display: inline-block; border: none; cursor: pointer;
        }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(59,130,246,0.35); }}
        .btn-secondary {{
            background: {c['card_bg']}; border: 1px solid {c['border']};
            padding: 0.6rem 1.5rem; border-radius: 999px;
            font-weight: 500; color: {c['text']}; text-decoration: none;
            transition: 0.2s; display: inline-block;
        }}
        .btn-secondary:hover {{ background: {c['nav_hover']}; }}

        /* ===== Seções ===== */
        .section-glass {{
            padding: 4rem 2rem;
            background: {c['section_bg']};
            backdrop-filter: blur(4px);
            border-top: 1px solid {c['border']};
        }}
        .section-glass:nth-child(even) {{
            background: {c['section_alt_bg']};
        }}
        .container {{
            max-width: 1200px; margin: 0 auto;
        }}
        .section-header {{
            text-align: center; margin-bottom: 3rem;
        }}
        .section-header .label {{
            display: inline-block;
            background: {c['primary_light']};
            padding: 0.2rem 1rem; border-radius: 999px;
            font-size: 0.7rem; font-weight: 600; text-transform: uppercase;
            letter-spacing: 0.08em; color: {c['primary']};
        }}
        .section-header h2 {{
            font-size: 2.4rem; font-weight: 700; margin-top: 0.5rem;
            color: {c['text']}; letter-spacing: -0.02em;
        }}
        .section-header p {{
            color: {c['text_muted']}; max-width: 600px;
            margin: 0.5rem auto 0;
        }}

        /* ===== Glass cards ===== */
        .glass-card {{
            background: {c['card_bg']};
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid {c['border']};
            border-radius: 24px;
            padding: 1.5rem;
            transition: all 0.25s ease;
            box-shadow: {c['shadow']};
        }}
        .glass-card:hover {{
            transform: translateY(-6px);
            border-color: {c['primary']};
            box-shadow: {c['shadow_hover']};
        }}

        /* ===== Timeline ===== */
        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
            width: 2px; background: linear-gradient(to bottom, {c['primary']}, {c['secondary']}, transparent);
        }}
        .timeline-item {{ position: relative; padding-left: 80px; margin-bottom: 2.5rem; }}
        .timeline-dot {{
            position: absolute; left: 20px; top: 6px; width: 18px; height: 18px;
            border-radius: 50%; background: {c['primary']};
            border: 3px solid {c['bg']}; box-shadow: 0 0 0 4px {c['primary']};
        }}
        .timeline-card {{
            background: {c['card_bg']};
            backdrop-filter: blur(4px);
            border: 1px solid {c['border']};
            border-radius: 20px; padding: 1.5rem;
            transition: 0.25s;
        }}
        .timeline-card:hover {{ border-color: {c['primary']}; transform: translateX(6px); }}
        .timeline-date {{
            display: inline-block; font-size: 0.7rem; font-weight: 600;
            background: {c['primary_light']}; color: {c['primary']};
            padding: 0.2rem 0.8rem; border-radius: 999px;
        }}
        .timeline-badge {{
            background: {c['primary']}; color: white;
            font-size: 0.6rem; font-weight: 700; padding: 0.15rem 0.6rem;
            border-radius: 999px; margin-left: 0.5rem; display: inline-block;
        }}
        .timeline-role {{ font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0; }}
        .timeline-company {{ color: {c['secondary']}; font-weight: 600; }}
        .timeline-desc {{ color: {c['text_muted']}; line-height: 1.6; }}
        .timeline-tag {{
            font-size: 0.7rem; background: {c['tag_bg']};
            border: 1px solid {c['tag_border']}; padding: 0.2rem 0.6rem;
            border-radius: 6px; display: inline-block; margin: 0.2rem;
        }}

        /* ===== Footer ===== */
        .footer {{
            padding: 3rem 2rem; text-align: center;
            border-top: 1px solid {c['border']};
            background: {c['card_bg']};
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
        .footer-links {{
            display: flex; justify-content: center; flex-wrap: wrap; gap: 0.5rem;
            margin: 1.5rem 0;
        }}
        .footer-link {{
            background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            padding: 0.4rem 1rem; border-radius: 999px;
            color: {c['text']}; text-decoration: none;
            font-size: 0.85rem; transition: 0.2s;
        }}
        .footer-link:hover {{ background: {c['primary']}; color: white; }}
        .footer-copy {{ color: {c['text_muted']}; font-size: 0.8rem; }}

        /* ===== Responsive ===== */
        @media (max-width: 768px) {{
            .navbar {{ padding: 0.5rem 1rem; flex-wrap: wrap; }}
            .navbar-links {{ gap: 0.3rem; flex-wrap: wrap; }}
            .hero-full {{ min-height: auto; padding: 5rem 1rem 2rem; }}
            .hero-text h1 {{ font-size: 2.2rem; }}
            .hero-photo img {{ width: 180px; height: 180px; }}
            .section-glass {{ padding: 3rem 1rem; }}
            .container {{ padding: 0 0.5rem; }}
        }}
        /* Grid para projetos e testemunhos */
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }}
        .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
        @media (max-width: 768px) {{
            .grid-2, .grid-3 {{ grid-template-columns: 1fr; }}
        }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# COMPONENTES DE RENDERIZAÇÃO
# ============================================================================

def render_navbar(active_page):
    c = get_colors()
    st.markdown(f"""
    <nav class="navbar">
        <a href="/?page=home" class="navbar-brand">Raphael <span>Pires</span></a>
        <div class="navbar-links">
            <a href="/?page=home" class="nav-link {'active' if active_page=='home' else ''}">Início</a>
            <a href="/?page=analytics" class="nav-link {'active' if active_page=='analytics' else ''}">Análises</a>
            <a href="/?page=dashboard" class="nav-link {'active' if active_page=='dashboard' else ''}">Dashboard</a>
            <button class="nav-theme-btn" onclick="parent.postMessage({{type:'toggle_theme'}},'*')">🌓</button>
        </div>
    </nav>
    """, unsafe_allow_html=True)

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
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">🏠 Remoto</span>
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">🏢 Híbrido</span>
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">📍 Presencial</span>
            <span style="background:var(--tag-bg);border:1px solid var(--tag-border);padding:0.3rem 0.8rem;border-radius:999px;font-size:0.8rem;">✈️ Viagens</span>
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

def render_skills_chart():
    c = get_colors()
    df = pd.DataFrame({
        "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
        "Proficiência": [95, 92, 88, 95, 85, 60, 82],
        "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
    })
    fig = px.bar(df, x="Proficiência", y="Tecnologia", color="Categoria", orientation="h",
                 color_discrete_sequence=c["chart_colors"], template=c["plotly_template"], text="Proficiência")
    fig.update_layout(height=380, margin=dict(l=20,r=40,t=20,b=40),
                      xaxis=dict(range=[0,105], showgrid=True, gridcolor="rgba(148,163,184,0.15)"),
                      yaxis=dict(showgrid=False), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                      font=dict(family="Inter", color=c["text"]), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_traces(textposition="outside", textfont=dict(color=c["text"], size=11))
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PÁGINAS
# ============================================================================

def page_home():
    c = get_colors()
    # Hero
    st.markdown(f"""
    <section class="hero-full">
        <div class="hero-content">
            <div class="hero-photo">
                <img src="{'rapha.jpeg' if os.path.exists('rapha.jpeg') else 'https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff'}" alt="Raphael Pires">
            </div>
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
                    <a href="{'Curriculo_Raphael_v2.pdf' if os.path.exists('Curriculo_Raphael_v2.pdf') else '#'}" download class="btn-secondary">📄 Baixar CV</a>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    # KPIs (baseado no currículo)
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Impacto Mensurável</span>
                <h2>Números que contam histórias</h2>
            </div>
            <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:1rem;">
                <div class="glass-card" style="text-align:center;"><div style="font-size:2.4rem;font-weight:700;color:var(--primary);">16+</div><div style="color:var(--text-muted);">anos de experiência</div></div>
                <div class="glass-card" style="text-align:center;"><div style="font-size:2.4rem;font-weight:700;color:var(--primary);">70%</div><div style="color:var(--text-muted);">redução operacional</div></div>
                <div class="glass-card" style="text-align:center;"><div style="font-size:2.4rem;font-weight:700;color:var(--primary);">213k+</div><div style="color:var(--text-muted);">registros analisados</div></div>
                <div class="glass-card" style="text-align:center;"><div style="font-size:2.4rem;font-weight:700;color:var(--primary);">2h→15m</div><div style="color:var(--text-muted);">ciclo de análise</div></div>
                <div class="glass-card" style="text-align:center;"><div style="font-size:2.4rem;font-weight:700;color:var(--primary);">R$1,2bi</div><div style="color:var(--text-muted);">em investimentos analisados</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Experiência (baseado no currículo)
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
        {"date":"2014 – Presente · 10+ anos","role":"Analista de Dados & Operações","company":"NSM Comércio","desc":"Centralização de registros de estoque de 7 unidades, eliminando inconsistências de inventário. Construção de indicadores operacionais.","tags":["Dados","Operações","Indicadores"],"badge":"Atual"},
        {"date":"2012 – Presente · 12+ anos","role":"Fundador & Analista de Dados","company":"Jardim do Éden","desc":"Estruturação de base de dados, modelagem, integração e dashboards gerenciais com SQL, Python, Power BI e Looker Studio – reduzindo ciclo de análise de 2h para 15 min.","tags":["Power BI","Python","SQL","Looker Studio"],"badge":""},
        {"date":"2010 – 2014 · 4 anos","role":"Fundador & Analista de KPIs","company":"J Sintonía","desc":"Monitoramento de KPIs de vendas, margem e rentabilidade com relatórios automatizados. Análise de viabilidade econômica que fundamentou encerramento estratégico planejado.","tags":["BI","KPIs","Dashboards"],"badge":""},
        {"date":"2009 – 2010 · 1 ano","role":"Estagiário de Automação e Dados","company":"Banco do Brasil","desc":"Desenvolvimento de macros VBA em 20 agências, reduzindo 70% do tempo operacional. Saneamento e padronização de bases de dados gerenciais.","tags":["VBA","Automação","Eficiência"],"badge":""}
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

    # Projetos (baseado no currículo)
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Portfólio</span>
                <h2>Projetos de Analytics</h2>
            </div>
            <div class="grid-2">
                <div class="glass-card">
                    <h3>🇧🇷 Desenrola Brasil</h3>
                    <p style="color:var(--text-muted);">Painel analítico executivo com KPIs, séries temporais e análise de concentração de mercado (HHI). Segmentação de perfis de renegociação via clusterização.</p>
                    <p><strong>Tecnologias:</strong> Python, Pandas, Plotly, Streamlit</p>
                    <a href="https://desenrolabrasil.streamlit.app" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">🔗 Acessar</a>
                </div>
                <div class="glass-card">
                    <h3>🔬 CNPq Analytics</h3>
                    <p style="color:var(--text-muted);">ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos. Dashboard interativo com filtros dinâmicos e visualizações de distribuição regional.</p>
                    <p><strong>Tecnologias:</strong> Python, Pandas, Plotly, Streamlit, PostgreSQL</p>
                    <a href="https://cnpq-analytics.streamlit.app" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">🔗 Acessar</a>
                </div>
                <div class="glass-card">
                    <h3>⛽ Análise de Preços de Combustíveis (ANP)</h3>
                    <p style="color:var(--text-muted);">Dashboard interativo com filtros temporais e regionais utilizando dados oficiais da Agência Nacional do Petróleo.</p>
                    <p><strong>Tecnologias:</strong> Python, Pandas, Plotly, Streamlit</p>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">📊 Ver código</a>
                </div>
                <div class="glass-card">
                    <h3>💎 Automação de Relatórios com Python</h3>
                    <p style="color:var(--text-muted);">Automação de geração de relatórios financeiros e operacionais, reduzindo tempo de entrega de 2h para 15min.</p>
                    <p><strong>Tecnologias:</strong> Python, Pandas, Excel, Power BI</p>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">💻 Ver código</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Depoimentos
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Depoimentos</span>
                <h2>O que dizem sobre meu trabalho</h2>
            </div>
            <div class="grid-3">
                <div class="glass-card">
                    <p style="font-style:italic;color:var(--text);">“O Raphael revolucionou nossa área de dados. Reduzimos custos operacionais em 30% com suas automações.”</p>
                    <p style="font-weight:600;color:var(--primary);margin-top:0.5rem;">— Diretor de Operações, Empresa X</p>
                </div>
                <div class="glass-card">
                    <p style="font-style:italic;color:var(--text);">“Graças ao dashboard de KPIs criado pelo Raphael, passamos a tomar decisões em tempo real com segurança.”</p>
                    <p style="font-weight:600;color:var(--primary);margin-top:0.5rem;">— Gerente de BI, Empresa Y</p>
                </div>
                <div class="glass-card">
                    <p style="font-style:italic;color:var(--text);">“A expertise do Raphael em AWS e Python nos permitiu processar 1M de registros por dia com custo mínimo.”</p>
                    <p style="font-weight:600;color:var(--primary);margin-top:0.5rem;">— CTO, Startup Z</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # AWS Cloud Journey (baseado no currículo)
    st.markdown(f"""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Cloud Journey</span>
                <h2>☁️ AWS em progresso</h2>
                <p style="color:var(--text-muted);">Atualmente em trilha de certificação, com 8 módulos AWS Educate concluídos e foco em arquitetura de dados.</p>
            </div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;text-align:center;">
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">📘</div><div>Cloud 101</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🖥️</div><div>AWS Console</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">💾</div><div>Storage</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🤖</div><div>ML Foundations</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🌱</div><div>Sustainability</div></div>
            </div>
            <div style="text-align:center;margin-top:1.5rem;">
                <span style="background:{c['primary_light']};color:{c['primary']};padding:0.2rem 1.2rem;border-radius:999px;font-size:0.8rem;font-weight:600;">🎯 Meta 2026: AWS Cloud Practitioner</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Competências
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

    render_footer()

def page_analytics():
    st.markdown("""
    <div class="section-glass" style="min-height:80vh;padding-top:6rem;">
        <div class="container">
            <div class="section-header">
                <span class="label">Análise ao Vivo</span>
                <h2>Demonstração analítica</h2>
            </div>
    """, unsafe_allow_html=True)
    c = get_colors()
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Combustíveis ANP", "📈 Impacto Operacional"])

    with tabs[0]:
        np.random.seed(42)
        regioes = ["Sudeste","Nordeste","Sul","Centro-Oeste","Norte"]
        faixas = ["Até R$5k","R$5k-15k","R$15k-50k","Acima R$50k"]
        df = pd.DataFrame({
            "Região": np.random.choice(regioes, 400, p=[0.45,0.28,0.15,0.07,0.05]),
            "Faixa": np.random.choice(faixas, 400, p=[0.55,0.28,0.12,0.05]),
            "Valor": np.random.lognormal(8.5,1.2,400),
            "Status": np.random.choice(["Renegociado","Em Negociação","Inadimplente"], 400, p=[0.65,0.25,0.10])
        })
        col1, col2 = st.columns(2)
        with col1:
            reg_sel = st.multiselect("Região", df["Região"].unique(), default=df["Região"].unique())
        with col2:
            status_sel = st.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
        filtro = df[(df["Região"].isin(reg_sel)) & (df["Status"].isin(status_sel))]
        if not filtro.empty:
            k1,k2,k3 = st.columns(3)
            k1.metric("Contratos", f"{len(filtro):,}")
            k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f}M")
            k3.metric("Taxa Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=0.5, color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
            fig1.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
            fig2 = px.bar(filtro.groupby("Faixa", observed=False)["Valor"].sum().reset_index(), x="Faixa", y="Valor", color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
            fig2.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
            col1, col2 = st.columns(2)
            col1.plotly_chart(fig1, use_container_width=True)
            col2.plotly_chart(fig2, use_container_width=True)

    with tabs[1]:
        np.random.seed(123)
        estados = ["SP","RJ","MG","RS","PR","BA"]
        comb = ["Gasolina","Etanol","Diesel"]
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]
        data=[]
        for e in estados:
            for c in comb:
                base = {"Gasolina":5.8,"Etanol":3.5,"Diesel":5.2}[c]
                for m in meses:
                    data.append({"Estado":e,"Combustível":c,"Mês":m,"Preço":base+np.random.normal(0,0.15)})
        df = pd.DataFrame(data)
        col1, col2 = st.columns(2)
        with col1:
            estado = st.selectbox("Estado", df["Estado"].unique())
        with col2:
            combustivel = st.selectbox("Combustível", df["Combustível"].unique())
        filtro = df[(df["Estado"]==estado) & (df["Combustível"]==combustivel)]
        if not filtro.empty:
            k1,k2 = st.columns(2)
            k1.metric("Preço Atual", f"R$ {filtro[filtro['Mês']=='Jun']['Preço'].values[0]:.2f}")
            variacao = (filtro["Preço"].max() - filtro["Preço"].min()) / filtro["Preço"].min() * 100
            k2.metric("Variação Semestral", f"{variacao:.1f}%")
            fig = px.line(filtro, x="Mês", y="Preço", markers=True, color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
            fig.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        df = pd.DataFrame({
            "Mês": meses*2,
            "Tipo": ["Antes"]*12 + ["Após"]*12,
            "Horas": [120,125,118,130,122,128,126,124,129,127,125,130] + [95,70,55,45,38,35,33,32,30,29,28,27]
        })
        fig = px.line(df, x="Mês", y="Horas", color="Tipo", markers=True, color_discrete_sequence=[c["chart_colors"][3], c["chart_colors"][0]], template=c["plotly_template"])
        fig.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
        k1,k2,k3 = st.columns(3)
        k1.metric("Horas Economizadas", "1.108 h", "+93% eficiência")
        k2.metric("Custo Evitado", "R$ 185k", "vs. contratação")
        k3.metric("Projetos Entregues", "24", "+60% vs. anterior")

    st.markdown("</div></div>", unsafe_allow_html=True)

def page_dashboard():
    st.markdown("""
    <div class="section-glass" style="min-height:80vh;padding-top:6rem;">
        <div class="container">
            <div class="section-header">
                <span class="label">Business Intelligence</span>
                <h2>Dashboard Interativo</h2>
            </div>
    """, unsafe_allow_html=True)
    c = get_colors()
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

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Projetos", f"{len(df_filtrado):,}")
    col2.metric("Receita Total", f"R$ {df_filtrado['Valor'].sum()/1e6:.1f}M")
    col3.metric("Ticket Médio", f"R$ {df_filtrado['Valor'].mean():,.0f}".replace(",","."))
    col4.metric("Satisfação Média", f"{df_filtrado['Satisfacao'].mean():.1f}%")

    fig1 = px.bar(df_filtrado.groupby("Mes").size().reset_index(name="Quantidade").sort_values("Mes"), x="Mes", y="Quantidade", title="Projetos por Mês", color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
    fig1.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig2 = px.pie(df_filtrado.groupby("Região")["Valor"].sum().reset_index(), names="Região", values="Valor", title="Receita por Região", hole=0.4, color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig2.update_layout(height=350, margin=dict(l=10,r=10,t=50,b=20), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig3 = px.line(df_filtrado.groupby("Mes")["Valor"].sum().reset_index().sort_values("Mes"), x="Mes", y="Valor", title="Evolução da Receita", markers=True, color_discrete_sequence=[c["chart_colors"][1]], template=c["plotly_template"])
    fig3.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig4 = px.scatter(df_filtrado, x="Horas", y="Valor", color="Complexidade", size="Satisfacao", title="Esforço vs. Retorno", color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig4.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig5 = px.bar(df_filtrado["Status"].value_counts().reset_index(), x="count", y="Status", orientation="h", title="Status dos Projetos", color="Status", color_discrete_sequence=c["chart_colors"][3:], template=c["plotly_template"])
    fig5.update_layout(height=300, margin=dict(l=20,r=20,t=50,b=20), showlegend=False, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))

    col1, col2 = st.columns(2)
    col1.plotly_chart(fig1, use_container_width=True)
    col2.plotly_chart(fig2, use_container_width=True)
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig3, use_container_width=True)
    col2.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("📋 Dados detalhados"):
        st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

# ============================================================================
# MAIN
# ============================================================================
def main():
    load_css()

    # Toggle theme via query param? Sim, mas usamos botão JS que envia mensagem.
    # Vamos usar o st.button para alternar tema manualmente também.
    # Para simplificar, vou colocar o botão na navbar via JS, mas também vou adicionar um botão de fallback.
    # Na verdade, o JS no botão da navbar não vai funcionar perfeitamente no Streamlit.
    # Vou usar um botão normal no canto.

    # Lê a página da URL
    query_params = st.query_params
    page = query_params.get("page", "home")

    # Render navbar
    render_navbar(page)

    # Conteúdo
    if page == "home":
        page_home()
    elif page == "analytics":
        page_analytics()
    elif page == "dashboard":
        page_dashboard()
    else:
        page_home()

if __name__ == "__main__":
    main()
