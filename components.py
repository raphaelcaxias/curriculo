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
            st.image("https://ui-avatars.com/api/?name=Raphael+Pires&size=160&background=1D4ED8&color=fff", width=160)
    st.markdown(f"""
    <h1 class="hero-name">Raphael Fernando da Silva Pires</h1>
    <div class="hero-title">Analista de Dados & Business Intelligence</div>
    <p class="hero-subtitle">
        Mais de <strong>16 anos</strong> transformando dados brutos em decisões estratégicas. 
        Especialista em automação, governança de dados e criação de dashboards de alto impacto.
    </p>
    <div>
        <span class="tech-badge">📊 Power BI</span>
        <span class="tech-badge">🐍 Python</span>
        <span class="tech-badge">🗄️ SQL</span>
        <span class="tech-badge">☁️ AWS</span>
        <span class="tech-badge">🤖 IA Generativa</span>
        <span class="tech-badge">📈 Dashboards</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
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
        ("16+", "anos de experiência em dados"),
        ("70%", "redução do tempo operacional"),
        ("213k", "registros processados com automação"),
        ("2h→15m", "tempo de análise reduzido"),
        ("R$50bi", "em dados analisados")
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
                      xaxis=dict(range=[0,105], showgrid=True, gridcolor="rgba(148,163,184,0.15)"),
                      yaxis=dict(showgrid=False), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                      font=dict(family="Inter", color=colors["text"]), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_traces(textposition="outside", textfont=dict(color=colors["text"], size=11))
    st.plotly_chart(fig, use_container_width=True)

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
