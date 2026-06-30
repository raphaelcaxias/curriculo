import streamlit as st
import plotly.express as px
import pandas as pd
import os
from config import get_colors

# ===== DETECÇÃO DE FOTO =====
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

# ===== DETECÇÃO DE PDF =====
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

# ===== RODAPÉ =====
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

# ===== GRÁFICO DE HABILIDADES =====
def render_skills_chart():
    c = get_colors()
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
        color_discrete_sequence=c["chart_colors"],
        template=c["plotly_template"],
        text="Proficiência"
    )
    fig.update_layout(
        height=380,
        margin=dict(l=20, r=40, t=20, b=40),
        xaxis=dict(range=[0, 105], showgrid=True, gridcolor="rgba(148,163,184,0.15)"),
        yaxis=dict(showgrid=False),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Inter", color=c["text"]),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    fig.update_traces(textposition="outside", textfont=dict(color=c["text"], size=11))
    st.plotly_chart(fig, use_container_width=True)
