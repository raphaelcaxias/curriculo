# -*- coding: utf-8 -*-
"""
Premium Portfolio - Raphael Pires (Versão Final Corrigida)
Streamlit App com design customizado, linha do tempo, cards de projetos e layout profissional.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import os
import requests
from io import BytesIO

# ------------------------------------------------------------------------------
# CONFIGURAÇÃO INICIAL
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Raphael Pires | Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------------------------
# CARREGAMENTO DE IMAGEM E PDF
# ------------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_image():
    if os.path.exists("rapha.jpeg"):
        return Image.open("rapha.jpeg")
    urls = [
        "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/rapha.jpeg",
        "https://avatars.githubusercontent.com/raphaelcaxias",
    ]
    for url in urls:
        try:
            r = requests.get(url, timeout=6)
            if r.status_code == 200:
                return Image.open(BytesIO(r.content))
        except Exception:
            pass
    return None

@st.cache_data(show_spinner=False)
def load_cv():
    try:
        r = requests.get(
            "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/Curriculo_Raphael_Premium_Final.pdf",
            timeout=8)
        if r.status_code == 200:
            return r.content
    except Exception:
        pass
    for p in ["Curriculo_Raphael_Premium_Final.pdf", "assets/Curriculo_Raphael_Premium_Final.pdf"]:
        if os.path.exists(p):
            with open(p, "rb") as f:
                return f.read()
    return None

profile_image = load_image()
cv_pdf = load_cv()

# ------------------------------------------------------------------------------
# CSS PERSONALIZADO (MODERN TECH MINIMALIST) - CORRIGIDO
# ------------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body, .stApp {
    background-color: #F4F7F6 !important;
    font-family: 'Inter', sans-serif;
    color: #1D2C4D;
}

/* Esconde elementos padrão do Streamlit */
#MainMenu, footer, header, .stDeployButton {
    display: none !important;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Barra de navegação centralizada */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(255,255,255,0.96);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid #e0e8e6;
    padding: 1rem 0;
    z-index: 1000;
    text-align: center;
}

.navbar a {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 0.9rem;
    color: #1D2C4D;
    text-decoration: none;
    margin: 0 1.2rem;
    padding: 0.25rem 0;
    transition: color 0.2s, border-bottom 0.2s;
    border-bottom: 2px solid transparent;
}

.navbar a:hover {
    color: #007BFF;
    border-bottom-color: #007BFF;
}

/* Container principal para compensar navbar */
.main-container {
    padding-top: 80px;
    max-width: 1200px;
    margin: 0 auto;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Seções */
.section {
    margin-bottom: 4rem;
    scroll-margin-top: 80px;
}

.section-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 2rem;
    letter-spacing: -0.01em;
    color: #1D2C4D;
    position: relative;
    display: inline-block;
}

.section-title:after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 50px;
    height: 3px;
    background: #007BFF;
    border-radius: 3px;
}

/* Cards de impacto */
.impact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.impact-card {
    background: white;
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 10px 25px -8px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.02);
    transition: transform 0.2s, box-shadow 0.2s;
    text-align: center;
}

.impact-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 30px -12px rgba(0,123,255,0.1);
}

.impact-number {
    font-size: 2.8rem;
    font-weight: 800;
    color: #007BFF;
    line-height: 1.2;
    margin-bottom: 0.5rem;
}

.impact-text {
    font-size: 0.85rem;
    color: #5a6e7a;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    font-weight: 500;
}

/* Perfil / Apresentação */
.profile-container {
    display: flex;
    align-items: center;
    gap: 2.5rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.profile-pic {
    width: 160px;
    height: 160px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #007BFF;
    box-shadow: 0 12px 24px -12px rgba(0,123,255,0.3);
}

.profile-name {
    font-size: 2.8rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
    color: #1D2C4D;
}

.profile-title {
    font-size: 1.2rem;
    color: #007BFF;
    font-weight: 500;
    margin-bottom: 0.8rem;
}

.profile-summary {
    font-size: 1rem;
    line-height: 1.5;
    color: #2c3e50;
    max-width: 600px;
    margin: 0.8rem 0;
}

/* Botões pílula */
.pill-buttons {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.pill-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: white;
    border: 1px solid #d0dad8;
    padding: 0.5rem 1.2rem;
    border-radius: 40px;
    font-weight: 500;
    color: #1D2C4D;
    text-decoration: none;
    transition: all 0.2s;
    font-size: 0.85rem;
}

.pill-btn:hover {
    border-color: #007BFF;
    background: #f0f9ff;
    color: #007BFF;
    transform: translateY(-2px);
}

/* Sobre - diferenciais com ícones */
.diff-list {
    list-style: none;
    padding-left: 0;
}
.diff-list li {
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}
.diff-icon {
    color: #007BFF;
    font-weight: bold;
}

/* Linha do tempo vertical */
.timeline {
    position: relative;
    margin-left: 1rem;
}
.timeline-item {
    display: flex;
    margin-bottom: 2rem;
    position: relative;
}
.timeline-left {
    width: 120px;
    flex-shrink: 0;
    text-align: right;
    padding-right: 1.5rem;
    font-weight: 600;
    color: #007BFF;
}
.timeline-line {
    position: relative;
    width: 2px;
    background: #cbdcd9;
    margin-right: 1.5rem;
}
.timeline-dot {
    position: absolute;
    left: -5px;
    top: 6px;
    width: 12px;
    height: 12px;
    background: #007BFF;
    border-radius: 50%;
    border: 2px solid white;
    box-shadow: 0 0 0 2px #007BFF30;
}
.timeline-content {
    flex: 1;
    padding-bottom: 0.5rem;
}
.timeline-title {
    font-weight: 700;
    font-size: 1.1rem;
}
.timeline-company {
    color: #5a6e7a;
    margin-bottom: 0.5rem;
    font-weight: 500;
}
.timeline-desc {
    font-size: 0.9rem;
    color: #2c3e50;
    margin: 0.3rem 0;
    line-height: 1.4;
}

/* Projects cards (CORRIGIDO - ESTILO DIRETO) */
.project-card {
    background: white;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 10px 20px -8px rgba(0,0,0,0.05);
    transition: transform 0.25s, box-shadow 0.25s;
    margin-bottom: 1.5rem;
}
.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 30px -12px rgba(0,0,0,0.15);
}
.project-img {
    width: 100%;
    height: 120px;
    background: #eef3f2;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
}
.project-content {
    padding: 1.2rem;
}
.project-title {
    font-weight: 700;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}
.project-desc {
    font-size: 0.85rem;
    color: #5a6e7a;
    margin-bottom: 1rem;
    line-height: 1.4;
}
.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 1rem;
}
.tech-tag {
    background: #edf2f1;
    padding: 0.2rem 0.6rem;
    border-radius: 30px;
    font-size: 0.7rem;
    color: #1D2C4D;
}
.project-links a {
    font-size: 0.8rem;
    margin-right: 1rem;
    color: #007BFF;
    text-decoration: none;
}
.project-links a:hover {
    text-decoration: underline;
}

/* Stack técnica - chips refinados */
.stack-category {
    margin-bottom: 2rem;
}
.stack-title {
    font-weight: 600;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.1rem;
}
.stack-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
}
.chip {
    background: #e9f0ef;
    color: #1D2C4D;
    padding: 0.4rem 1rem;
    border-radius: 40px;
    font-size: 0.8rem;
    font-weight: 500;
    transition: all 0.2s;
}
.chip:hover {
    background: #d0e2df;
    transform: scale(0.98);
}

/* Formação e certificações grid */
.edu-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}
.edu-block {
    background: white;
    border-radius: 20px;
    padding: 1.2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}
.edu-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}
.cert-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
}
.cert-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
}

/* Rodapé de impacto */
.footer-impact {
    background: #1D2C4D;
    border-radius: 30px;
    padding: 2rem;
    color: white;
    text-align: center;
    margin-top: 2rem;
}
.footer-impact a {
    color: #9fc9ff;
    text-decoration: none;
    margin: 0 0.5rem;
}
.footer-impact a:hover {
    text-decoration: underline;
}
.footer-links {
    margin-top: 1rem;
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
}
</style>
""", unsafe_allow_html=True)

# Barra de navegação HTML
st.markdown("""
<div class="navbar">
    <a href="#inicio">Início</a>
    <a href="#sobre">Sobre</a>
    <a href="#experiencia">Experiência</a>
    <a href="#habilidades">Habilidades</a>
    <a href="#portfolio">Portfólio</a>
    <a href="#contato">Contato</a>
</div>
""", unsafe_allow_html=True)

# Container principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ==============================================================================
# SEÇÃO DE APRESENTAÇÃO (INÍCIO)
# ==============================================================================
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    if profile_image:
        st.image(profile_image, width=160, output_format="JPEG")
    else:
        st.markdown('<div style="width:160px;height:160px;background:#e0e8e6;border-radius:50%;"></div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="profile-name">Raphael Pires</div>
    <div class="profile-title">Analista de Dados & Business Intelligence</div>
    <div class="profile-summary">+15 anos de experiência real em operações, automação e indicadores de negócio. Transformo dados em decisões práticas.</div>
    <div class="pill-buttons">
        <a class="pill-btn" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
        <a class="pill-btn" href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
        <a class="pill-btn" href="https://wa.me/5524992275226" target="_blank">📱 WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# SEÇÃO SOBRE
# ==============================================================================
st.markdown('<div id="sobre" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Sobre</div>', unsafe_allow_html=True)

col_sobre1, col_sobre2 = st.columns([2, 1], gap="large")
with col_sobre1:
    st.markdown("""
    Profissional com mais de 15 anos de atuação em operações comerciais reais, instituição financeira e gestão de negócio próprio.  
    Minha trajetória começou no chão da fábrica e passou por automação bancária, controle de estoque, análise de margem e criação de dashboards estratégicos.

    Atualmente, integro dados e negócio para entregar indicadores confiáveis, dashboards interativos e automação de processos.  
    Acredito que um analista de dados só é completo quando entende a operação que está analisando.
    """)
with col_sobre2:
    st.markdown("""
    <div style="background:white; border-radius:20px; padding:1rem;">
    <strong>✔ Diferenciais</strong>
    <ul class="diff-list" style="margin-top:0.5rem;">
        <li><span class="diff-icon">✓</span> Visão operacional de ponta a ponta</li>
        <li><span class="diff-icon">✓</span> Domínio de Power BI, SQL e Python</li>
        <li><span class="diff-icon">✓</span> Comunicação com áreas não técnicas</li>
        <li><span class="diff-icon">✓</span> Foco em resultado, não em gráficos bonitos</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# IMPACTO EM NÚMEROS (CARDS COM SOMBRA)
# ==============================================================================
st.markdown('<div class="section-title">Impacto em números</div>', unsafe_allow_html=True)
impact_data = [
    ("70%", "Redução operacional • Banco do Brasil"),
    ("2h → 15min", "Ciclo de análise otimizado"),
    ("20 agências", "Automação com VBA"),
    ("213k+", "Registros processados")
]
cols_impact = st.columns(4)
for i, (num, desc) in enumerate(impact_data):
    with cols_impact[i]:
        st.markdown(f"""
        <div class="impact-card">
            <div class="impact-number">{num}</div>
            <div class="impact-text">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TRAJETÓRIA PROFISSIONAL (LINHA DO TEMPO VERTICAL)
# ==============================================================================
st.markdown('<div id="experiencia" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Trajetória profissional</div>', unsafe_allow_html=True)

experiences = [
    {
        "periodo": "2014 – 2026",
        "titulo": "Analista de KPIs & Operações",
        "empresa": "J Sintonía Calçados",
        "descricoes": [
            "Monitoramento de vendas, margem e giro de estoque com dashboards em Power BI e Looker Studio.",
            "Criação de relatórios automatizados para suporte à gestão estratégica.",
            "Aplicação de SQL e Python na consolidação de bases históricas."
        ]
    },
    {
        "periodo": "2009 – presente",
        "titulo": "Gestão Comercial & Dados",
        "empresa": "Jardim do Éden",
        "descricoes": [
            "Redução do ciclo de análise de 2h para 15min com dashboards em Power BI/Looker.",
            "Automação de relatórios via Python e IA generativa.",
            "Estruturação de fluxo analítico para faturamento, margem e estoque."
        ]
    },
    {
        "periodo": "2008 – 2010",
        "titulo": "Estagiário de Dados & Automação",
        "empresa": "Banco do Brasil",
        "descricoes": [
            "Automação de processos em 20 agências usando Excel/VBA – redução de 70% no tempo operacional.",
            "Consolidação e padronização de relatórios gerenciais."
        ]
    },
    {
        "periodo": "2002 – 2009",
        "titulo": "Suporte Operacional & Controle",
        "empresa": "NSM Comércio e Serviço",
        "descricoes": [
            "Centralização de dados operacionais de 7 unidades, eliminando inconsistências.",
            "Controle de estoque e suporte administrativo."
        ]
    }
]

timeline_html = '<div class="timeline">'
for exp in experiences:
    timeline_html += f"""
    <div class="timeline-item">
        <div class="timeline-left">{exp['periodo']}</div>
        <div class="timeline-line" style="position:relative;">
            <div class="timeline-dot"></div>
        </div>
        <div class="timeline-content">
            <div class="timeline-title">{exp['titulo']}</div>
            <div class="timeline-company">{exp['empresa']}</div>
    """
    for desc in exp['descricoes']:
        timeline_html += f'<div class="timeline-desc">— {desc}</div>'
    timeline_html += '</div></div>'
timeline_html += '</div>'
st.markdown(timeline_html, unsafe_allow_html=True)

# ==============================================================================
# STACK TÉCNICA (CHIPS REFINADOS)
# ==============================================================================
st.markdown('<div id="habilidades" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Stack técnica</div>', unsafe_allow_html=True)

stack_cats = {
    "📌 Dados & ETL": ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy", "ETL / Saneamento"],
    "📊 BI & Visualização": ["Power BI", "Looker Studio", "Plotly", "Streamlit", "Excel Avançado"],
    "📈 Análise & Indicadores": ["KPIs", "Controle de Fluxo", "Margem & Giro", "Dashboards Gerenciais"],
    "⚙️ Automação & Ferramentas": ["Excel/VBA", "Git", "IA Generativa", "Padronização de Processos"]
}

for cat, items in stack_cats.items():
    st.markdown(f'<div class="stack-category"><div class="stack-title">{cat}</div><div class="stack-chips">', unsafe_allow_html=True)
    for item in items:
        st.markdown(f'<span class="chip">{item}</span>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

# ==============================================================================
# PROJETOS EM DESTAQUE (CORRIGIDO - SEM ERRO DE HTML)
# ==============================================================================
st.markdown('<div id="portfolio" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Portfólio de projetos</div>', unsafe_allow_html=True)

projects = [
    {
        "nome": "Desenrola Brasil – Painel Executivo",
        "desc": "Dashboard com dados oficiais do Banco Central (R$50 bi renegociados). Análise de concentração de mercado (HHI), clusterização K-Means e previsão Holt-Winters.",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "app_url": "https://desenrolabrasil.streamlit.app/",
        "code_url": "https://github.com/raphaelcaxias/DESENROLA_BRASIL",
        "img_char": "📊"
    },
    {
        "nome": "CNPq Analytics – Investimentos em Pesquisa",
        "desc": "Processamento de 213 mil bolsas de pesquisa (R$1,2 bi). Identificação de desigualdades regionais e rankings dinâmicos.",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "app_url": "https://cnpq-analytics.streamlit.app/",
        "code_url": "https://github.com/raphaelcaxias/CNPq-Analytics",
        "img_char": "🎓"
    },
    {
        "nome": "ANP – Preços de Combustíveis",
        "desc": "Dashboard com dados públicos da ANP para análise temporal e regional de preços de combustíveis.",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app_url": None,
        "code_url": "https://github.com/raphaelcaxias/anp-combustiveis-dashboard",
        "img_char": "⛽"
    }
]

# Exibir cada projeto como um card usando HTML puro (sem grid duplicado)
for proj in projects:
    tech_tags = ''.join([f'<span class="tech-tag">{t}</span>' for t in proj["tech"]])
    app_link = f'<a href="{proj["app_url"]}" target="_blank" style="margin-right:1rem;">🔗 Aplicação</a>' if proj["app_url"] else ''
    code_link = f'<a href="{proj["code_url"]}" target="_blank">📄 Código</a>' if proj["code_url"] else ''
    st.markdown(f"""
    <div class="project-card">
        <div class="project-img">{proj['img_char']} Dashboard</div>
        <div class="project-content">
            <div class="project-title">{proj['nome']}</div>
            <div class="project-desc">{proj['desc']}</div>
            <div class="project-tech">{tech_tags}</div>
            <div class="project-links">{app_link} {code_link}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# FORMAÇÃO & CERTIFICAÇÕES (LAYOUT ALTERNATIVO)
# ==============================================================================
st.markdown('<div class="section-title">Formação & Certificações</div>', unsafe_allow_html=True)
st.markdown('<div class="edu-grid">', unsafe_allow_html=True)
# Formação
st.markdown("""
<div class="edu-block">
    <div class="edu-icon">🎓</div>
    <strong>Sistemas de Informação</strong><br>UniFOA – 2010<br><br>
    <strong>Técnico em Informática</strong><br>CIBA – 2005
</div>
""", unsafe_allow_html=True)
# Certificações grid
st.markdown("""
<div class="edu-block">
    <div class="edu-icon">📜</div>
    <strong>Certificações (Hashtag Treinamentos)</strong>
    <div class="cert-grid" style="margin-top:0.8rem;">
        <div class="cert-item">✓ SQL para Análise de Dados</div>
        <div class="cert-item">✓ Power BI Expert</div>
        <div class="cert-item">✓ Python para Análise de Dados</div>
        <div class="cert-item">✓ IA Aplicada a Negócios</div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# RODAPÉ DE IMPACTO (VAMOS TRABALHAR JUNTOS?)
# ==============================================================================
st.markdown('<div id="contato" class="section"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer-impact">
    <h3 style="margin-bottom:0.5rem;">Vamos trabalhar juntos?</h3>
    <p>Busco oportunidades como Analista de Dados, BI ou Automação. Disponível para remoto ou híbrido.</p>
    <div class="footer-links">
        <a href="mailto:raphael_caxias@hotmail.com">📧 raphael_caxias@hotmail.com</a>
        <a href="tel:+5524992275226">📱 (24) 99227-5226</a>
        <a href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
        <a href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
    </div>
    <div style="margin-top:1rem; font-size:0.8rem;">
        <a href="https://github.com/raphaelcaxias/curriculo" target="_blank">Portfolio GitHub</a> • © 2026 Raphael Pires
    </div>
</div>
""", unsafe_allow_html=True)

# Botão de download do currículo (opcional)
if cv_pdf:
    st.download_button(
        label="📄 Baixar currículo (PDF)",
        data=cv_pdf,
        file_name="Raphael_Pires_Curriculo.pdf",
        mime="application/pdf",
        use_container_width=False,
        key="cv_download"
    )

st.markdown('</div>', unsafe_allow_html=True)  # fecha main-container