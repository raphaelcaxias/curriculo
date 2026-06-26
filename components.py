import streamlit as st
import plotly.express as px
import pandas as pd
from config import get_colors
import os

def render_theme_toggle():
    col1, col2, col3 = st.columns([10,1,1])
    with col3:
        is_dark = st.session_state.theme == "dark"
        label = "☀️" if is_dark else "🌙"
        st.button(label, on_click=toggle_theme, key="theme_btn", use_container_width=True)

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def render_hero():
    colors = get_colors()
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([4,2,4])
    with col2:
        if os.path.exists("rapha.jpeg"):
            st.image("rapha.jpeg", width=160)
        else:
            st.markdown(f"""
            <div style="width:160px;height:160px;border-radius:50%;background:linear-gradient(135deg,{colors['primary']},{colors['secondary']});
            display:flex;align-items:center;justify-content:center;font-size:3.5rem;font-weight:700;color:white;margin:0 auto 1.5rem;border:3px solid {colors['primary']};">
            RP</div>""", unsafe_allow_html=True)
    st.markdown(f"""
    <h1 class="hero-name">Raphael Fernando da Silva Pires</h1>
    <div class="hero-title">Analista de Dados & Business Intelligence</div>
    <p class="hero-subtitle">
        Transformando dados brutos em decisões estratégicas. Mais de <strong>16 anos</strong> construindo inteligência de negócios,
        automações e governança de dados que geram impacto real e mensurável.
    </p>
    <div>
        <span class="hero-badge">📊 Power BI</span>
        <span class="hero-badge">🐍 Python</span>
        <span class="hero-badge">🗄️ SQL</span>
        <span class="hero-badge">☁️ AWS</span>
        <span class="hero-badge">🤖 IA Generativa</span>
        <span class="hero-badge">📈 Dashboards</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Download CV
    col1, col2, col3 = st.columns([4,2,4])
    with col2:
        if os.path.exists("Curriculo_Raphael_v2.pdf"):
            with open("Curriculo_Raphael_v2.pdf", "rb") as f:
                st.download_button("📄 Download Currículo PDF", data=f.read(), file_name="Curriculo_Raphael_Pires.pdf", mime="application/pdf", use_container_width=True)
        else:
            st.info("📄 Currículo PDF disponível")

def render_kpis():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Impacto Mensurável</span>
        <h2 class="section-title">Números que contam histórias</h2>
    </div>
    """, unsafe_allow_html=True)
    kpis = [
        ("16 anos", "transformando dados em decisões"),
        ("70%", "redução de tempo em relatórios manuais"),
        ("+213 mil", "registros processados com automação"),
        ("2h → 15min", "de análise com IA"),
        ("R$ 50 bi", "em dados analisados")
    ]
    cols = st.columns(5)
    for col, (val, label) in zip(cols, kpis):
        with col:
            st.markdown(f'<div class="kpi-box"><div class="kpi-value">{val}</div><div class="kpi-label">{label}</div></div>', unsafe_allow_html=True)

def render_skills_chart():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Competências</span>
        <h2 class="section-title">Domínio tecnológico</h2>
    </div>
    """, unsafe_allow_html=True)
    colors = get_colors()
    df = pd.DataFrame({
        "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
        "Proficiência": [95, 92, 88, 95, 85, 60, 82],
        "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
    })
    fig = px.bar(df, x="Proficiência", y="Tecnologia", color="Categoria", orientation="h",
                 color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"], text="Proficiência")
    fig.update_layout(height=380, margin=dict(l=20,r=40,t=20,b=40),
                      xaxis=dict(range=[0,105], showgrid=True, gridcolor=colors["border"]),
                      yaxis=dict(showgrid=False), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                      font=dict(family="Inter", color=colors["text"]), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_traces(textposition="outside", textfont=dict(color=colors["text"], size=11))
    st.plotly_chart(fig, use_container_width=True)

def render_certification():
    colors = get_colors()
    st.markdown(f"""
    <div class="section-header">
        <span class="section-label">Certificação</span>
        <h2 class="section-title">Próximo objetivo</h2>
    </div>
    <div class="cert-badge">
        <div class="cert-badge-icon">🎯</div>
        <div class="cert-badge-title">AWS Cloud Practitioner</div>
        <div class="cert-badge-sub">Meta para 2026 · Certificação em andamento</div>
        <div style="margin-top: 0.8rem;">
            <span style="background: {colors['primary']}15; padding: 0.2rem 0.8rem; border-radius: 999px; font-size: 0.75rem; color: {colors['primary']};">
                ☁️ Cloud Computing
            </span>
            <span style="background: {colors['primary']}15; padding: 0.2rem 0.8rem; border-radius: 999px; font-size: 0.75rem; color: {colors['primary']};">
                📘 AWS Console
            </span>
            <span style="background: {colors['primary']}15; padding: 0.2rem 0.8rem; border-radius: 999px; font-size: 0.75rem; color: {colors['primary']};">
                💾 Storage
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-status"><span class="footer-status-dot"></span><span class="footer-status-text">Disponível para oportunidades</span></div>
        <h3 class="footer-title">Vamos conversar sobre dados?</h3>
        <p class="footer-subtitle">Aberto a projetos em Dados, BI e Cloud</p>
        <div>
            <span class="footer-mode">🏠 Remoto</span>
            <span class="footer-mode">🏢 Híbrido</span>
            <span class="footer-mode">📍 Presencial</span>
            <span class="footer-mode">✈️ Viagens</span>
        </div>
        <div>
            <a href="https://www.linkedin.com/in/raphaelpires" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="https://github.com/raphaelcaxias" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="mailto:contato@raphaelpires.com" class="footer-link">✉️ E-mail</a>
            <a href="tel:+5511999999999" class="footer-link">📱 Telefone</a>
        </div>
        <p class="footer-copy">© 2026 Raphael Fernando da Silva Pires</p>
    </div>
    """, unsafe_allow_html=True)
