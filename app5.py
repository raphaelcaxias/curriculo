# -*- coding: utf-8 -*-
"""
Portfolio - Raphael Pires (Versão Moderna 2026)
Arquivo: app.py
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
# CONFIGURAÇÃO DA PÁGINA
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Raphael Pires | Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------------------
# CARREGAMENTO DE IMAGEM (foto e PDF)
# ------------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_image():
    # Tenta primeiro o arquivo local enviado (rapha.jpeg)
    if os.path.exists("rapha.jpeg"):
        return Image.open("rapha.jpeg")
    # Caso contrário, tenta URLs do GitHub
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
    # Se nada der certo, retorna None (será tratado depois)
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
# CSS PERSONALIZADO (Moderno, responsivo, com sombras e fontes atuais)
# ------------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body, .stApp {
    background-color: #f8fafc !important;
    font-family: 'Inter', sans-serif;
    color: #0f172a;
}

/* Esconde elementos padrão do Streamlit */
#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 1rem !important;
    max-width: 1200px;
    margin: 0 auto;
}

/* Sidebar moderna */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
    border-right: none !important;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] a {
    color: #94a3b8 !important;
    text-decoration: none;
    transition: color 0.2s;
}

[data-testid="stSidebar"] a:hover {
    color: #fbbf24 !important;
}

[data-testid="stSidebar"] hr {
    border-color: #334155 !important;
}

[data-testid="stSidebar"] .stDownloadButton > button {
    background: #3b82f6 !important;
    color: white !important;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    width: 100%;
    transition: background 0.2s;
}

[data-testid="stSidebar"] .stDownloadButton > button:hover {
    background: #2563eb !important;
}

/* Cards e containers principais */
.main-card {
    background: white;
    border-radius: 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.02), 0 1px 2px rgba(0,0,0,0.03);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    transition: transform 0.2s, box-shadow 0.2s;
}

.main-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 24px -12px rgba(0,0,0,0.15);
}

/* Cabeçalho com foto e nome */
.profile-header {
    display: flex;
    align-items: center;
    gap: 2rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.profile-pic {
    border-radius: 50%;
    object-fit: cover;
    width: 120px;
    height: 120px;
    border: 3px solid white;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.profile-info h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    color: #0f172a;
}

.profile-info .subtitle {
    font-size: 1rem;
    color: #475569;
    margin-top: 0.25rem;
    border-left: 4px solid #3b82f6;
    padding-left: 1rem;
}

/* Botões e links */
.btn-primary {
    background: #0f172a;
    color: white;
    padding: 0.5rem 1.2rem;
    border-radius: 40px;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.875rem;
    transition: background 0.2s;
    display: inline-block;
}

.btn-primary:hover {
    background: #1e293b;
}

.btn-outline {
    border: 1.5px solid #0f172a;
    background: transparent;
    color: #0f172a;
    padding: 0.5rem 1.2rem;
    border-radius: 40px;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.875rem;
    transition: all 0.2s;
    display: inline-block;
}

.btn-outline:hover {
    background: #0f172a;
    color: white;
}

/* Seção título */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.75rem;
    font-weight: 700;
    margin: 2rem 0 1.5rem 0;
    letter-spacing: -0.01em;
    border-left: 5px solid #3b82f6;
    padding-left: 1rem;
}

/* KPI cards */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}

.kpi-card {
    background: white;
    border-radius: 20px;
    padding: 1.2rem;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    border: 1px solid #e2e8f0;
    transition: all 0.2s;
}

.kpi-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 8px 20px -12px rgba(0,0,0,0.1);
}

.kpi-number {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
}

.kpi-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #475569;
    margin-top: 0.5rem;
}

/* Timeline de experiência */
.timeline-item {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    border-left: 2px solid #e2e8f0;
    padding-left: 1.5rem;
    position: relative;
}

.timeline-dot {
    position: absolute;
    left: -6px;
    top: 6px;
    width: 10px;
    height: 10px;
    background: #3b82f6;
    border-radius: 50%;
}

.timeline-date {
    font-family: 'Inter', monospace;
    font-size: 0.75rem;
    color: #3b82f6;
    font-weight: 600;
    min-width: 100px;
}

.timeline-content {
    flex: 1;
}

.timeline-title {
    font-weight: 700;
    font-size: 1.1rem;
    margin-bottom: 0.25rem;
}

.timeline-company {
    font-size: 0.85rem;
    color: #475569;
    margin-bottom: 0.5rem;
}

.timeline-desc {
    font-size: 0.85rem;
    color: #334155;
    margin: 0.25rem 0;
    padding-left: 0;
}

/* Project cards */
.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.project-card {
    background: white;
    border-radius: 20px;
    padding: 1.25rem;
    border: 1px solid #e2e8f0;
    transition: all 0.2s;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px -12px rgba(0,0,0,0.15);
    border-color: #cbd5e1;
}

.project-title {
    font-weight: 700;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}

.project-desc {
    font-size: 0.85rem;
    color: #475569;
    margin-bottom: 1rem;
    flex: 1;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 1rem;
}

.tech-badge {
    background: #f1f5f9;
    color: #0f172a;
    font-size: 0.7rem;
    padding: 0.2rem 0.6rem;
    border-radius: 30px;
}

.project-links a {
    font-size: 0.8rem;
    margin-right: 0.8rem;
    text-decoration: none;
}

/* Stack técnica */
.stack-category {
    background: #f8fafc;
    border-radius: 16px;
    padding: 1rem;
    margin-bottom: 1rem;
    border: 1px solid #e2e8f0;
}

.stack-title {
    font-weight: 600;
    margin-bottom: 0.75rem;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.stack-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.stack-tag {
    background: white;
    border: 1px solid #cbd5e1;
    padding: 0.25rem 0.75rem;
    border-radius: 40px;
    font-size: 0.75rem;
}

/* Contato */
.contact-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-radius: 24px;
    padding: 2rem;
    color: white;
    margin-top: 1.5rem;
}

.contact-card a {
    color: #fbbf24;
    text-decoration: none;
}

.contact-card a:hover {
    text-decoration: underline;
}

/* Footer */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    font-size: 0.7rem;
    color: #94a3b8;
    border-top: 1px solid #e2e8f0;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------------------------
with st.sidebar:
    if profile_image:
        st.image(profile_image, use_container_width=True, output_format="JPEG")
    else:
        st.markdown("""
        <div style="background:#1e293b;border-radius:20px;height:150px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;">
            <span style="font-family:'Playfair Display',serif;font-size:3rem;color:white;">RP</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧭 Navegação")
    st.markdown("""
- [🏠 Início](#inicio)
- [👤 Sobre](#sobre)
- [💼 Experiência](#experiencia)
- [🚀 Projetos](#projetos)
- [⚙️ Stack](#stack)
- [📬 Contato](#contato)
    """)
    st.markdown("---")
    if cv_pdf:
        st.download_button(
            label="📄 Baixar Currículo (PDF)",
            data=cv_pdf,
            file_name="Raphael_Pires_Curriculo.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("PDF não disponível no momento.")
    st.markdown("---")
    st.markdown("### 🔗 Links rápidos")
    st.markdown("""
[🔗 LinkedIn](https://linkedin.com/in/raphael-pires-caxias)  
[💻 GitHub](https://github.com/raphaelcaxias)  
[📧 Email](mailto:raphael_caxias@hotmail.com)  
[📱 WhatsApp](https://wa.me/5524992275226)
    """)
    st.caption("Portfolio atualizado · 2026")

# ------------------------------------------------------------------------------
# CONTEÚDO PRINCIPAL
# ------------------------------------------------------------------------------
# Hero / Cabeçalho com foto
col1, col2 = st.columns([1, 3], gap="large")
with col1:
    if profile_image:
        st.image(profile_image, width=150, output_format="JPEG")
    else:
        st.markdown('<div style="width:150px;height:150px;background:#e2e8f0;border-radius:50%;"></div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif;font-size:2.8rem;font-weight:700;margin:0;">Raphael Pires</h1>
    <p style="font-size:1.2rem;color:#334155;margin-top:0.25rem;">Analista de Dados & Business Intelligence</p>
    <p style="color:#475569;border-left:4px solid #3b82f6;padding-left:1rem;">+15 anos de experiência real em operações, automação e indicadores de negócio</p>
    <div>
        <a class="btn-primary" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
        <a class="btn-outline" href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
        <a class="btn-outline" href="https://wa.me/5524992275226" target="_blank">📱 WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div id="sobre"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Sobre</div>', unsafe_allow_html=True)

col_a, col_b = st.columns([2,1], gap="large")
with col_a:
    st.markdown("""
    <div style="background:#f1f5f9;padding:1.5rem;border-radius:24px;border-left:5px solid #3b82f6;">
    Profissional com <strong>+15 anos de operação real</strong> em varejo e instituição financeira (Banco do Brasil).<br><br>
    Construí minha experiência em dados na prática – estoque, faturamento, fluxo de caixa, automação – antes mesmo de “Data Analyst” ser um cargo comum.<br><br>
    Atualmente focado em transformar rotinas operacionais em dashboards interativos, indicadores de performance e automação inteligente, conectando o mundo do negócio com a tecnologia.
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    **✔ Diferenciais**  
    - Visão operacional de ponta a ponta  
    - Domínio de Power BI, SQL e Python  
    - Comunicação direta com áreas não técnicas  
    - Foco em resultado, não em gráficos bonitos  
    """)

# ------------------------------------------------------------------------------
# KPIs (métricas de impacto)
st.markdown('<div class="section-title">Impacto em números</div>', unsafe_allow_html=True)
kpis = [
    ("70%", "Redução operacional\nBanco do Brasil"),
    ("2h → 15min", "Ciclo de análise\notimizado"),
    ("20 agências", "Automação com VBA"),
    ("213k+", "Registros processados"),
]
cols = st.columns(4)
for i, (num, desc) in enumerate(kpis):
    with cols[i]:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-number">{num}</div>
            <div class="kpi-label">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# EXPERIÊNCIA PROFISSIONAL
st.markdown('<div id="experiencia"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Trajetória profissional</div>', unsafe_allow_html=True)

experiences = [
    {
        "date": "2014 – 2026",
        "title": "Analista de KPIs & Operações",
        "company": "J Sintonía Calçados Ltda",
        "desc": [
            "Monitoramento de vendas, margem e giro de estoque com dashboards em Power BI e Looker Studio.",
            "Criação de relatórios automatizados para suporte à gestão estratégica.",
            "Aplicação de SQL e Python na consolidação de bases históricas."
        ]
    },
    {
        "date": "2009 – presente",
        "title": "Gestão Comercial & Dados",
        "company": "Jardim do Éden",
        "desc": [
            "Redução do ciclo de análise de 2h para 15min com dashboards em Power BI/Looker.",
            "Automação de relatórios via Python e IA generativa.",
            "Estruturação de fluxo analítico para faturamento, margem e controle de estoque."
        ]
    },
    {
        "date": "2008 – 2010",
        "title": "Estagiário de Dados & Automação",
        "company": "Banco do Brasil",
        "desc": [
            "Automação de processos em 20 agências usando Excel/VBA – redução de 70% no tempo operacional.",
            "Consolidação e padronização de relatórios gerenciais."
        ]
    },
    {
        "date": "2002 – 2009",
        "title": "Suporte Operacional & Controle",
        "company": "NSM Comércio e Serviço",
        "desc": [
            "Centralização de dados operacionais de 7 unidades, eliminando inconsistências.",
            "Controle de estoque e suporte administrativo."
        ]
    },
]

for exp in experiences:
    with st.container():
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-date">{exp['date']}</div>
            <div class="timeline-content">
                <div class="timeline-title">{exp['title']}</div>
                <div class="timeline-company">{exp['company']}</div>
                {''.join([f'<div class="timeline-desc">— {item}</div>' for item in exp['desc']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# PROJETOS EM DESTAQUE
st.markdown('<div id="projetos"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Projetos em destaque</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Desenrola Brasil – Painel Executivo",
        "desc": "Dashboard interativo com dados oficiais do Banco Central (R$ 50 bi renegociados, 15M contratos). Análise de concentração de mercado (HHI), clusterização K-Means e previsão Holt-Winters.",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "app": "https://desenrolabrasil.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/DESENROLA_BRASIL"
    },
    {
        "title": "CNPq Analytics",
        "desc": "Processamento de 213 mil bolsas de pesquisa (R$ 1,2 bi). Identificação de desigualdades regionais e rankings dinâmicos.",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit", "PostgreSQL"],
        "app": "https://cnpq-analytics.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/CNPq-Analytics"
    },
    {
        "title": "ANP – Preços de Combustíveis",
        "desc": "Dashboard com dados públicos da ANP para análise temporal e regional de preços de combustíveis.",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app": None,
        "code": "https://github.com/raphaelcaxias/anp-combustiveis-dashboard"
    },
]

for proj in projects:
    tech_badges = "".join(f'<span class="tech-badge">{t}</span>' for t in proj["tech"])
    links = ""
    if proj["app"]:
        links += f'<a href="{proj["app"]}" target="_blank" style="margin-right:1rem;">🔗 Aplicação</a>'
    if proj["code"]:
        links += f'<a href="{proj["code"]}" target="_blank">📄 Código</a>'
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{proj['title']}</div>
        <div class="project-desc">{proj['desc']}</div>
        <div class="project-tech">{tech_badges}</div>
        <div class="project-links">{links}</div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# STACK TÉCNICA
st.markdown('<div id="stack"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Stack técnica</div>', unsafe_allow_html=True)

stack_categories = {
    "Dados & ETL": ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy", "ETL/Saneamento"],
    "BI & Visualização": ["Power BI", "Looker Studio", "Plotly", "Streamlit", "Excel Avançado"],
    "Análise & Indicadores": ["KPIs", "Controle de Fluxo", "Margem & Giro", "Dashboards Gerenciais"],
    "Automação & Ferramentas": ["Excel/VBA", "Git", "IA Generativa", "Padronização de Processos"],
}

cols = st.columns(2)
for i, (cat, items) in enumerate(stack_categories.items()):
    with cols[i % 2]:
        badges = "".join(f'<span class="stack-tag">{item}</span>' for item in items)
        st.markdown(f"""
        <div class="stack-category">
            <div class="stack-title">📌 {cat}</div>
            <div class="stack-tags">{badges}</div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# DEMONSTRAÇÃO INTERATIVA (opcional, igual ao original)
st.markdown('<div class="section-title">Demonstração interativa</div>', unsafe_allow_html=True)
st.caption("Exemplo do tipo de análise que construo – explore os filtros abaixo.")

tab1, tab2 = st.tabs(["📈 Vendas vs Meta", "🗺️ Distribuição Regional"])

with tab1:
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    vendas_base = [120, 145, 132, 168, 189, 201]
    meta_base = [130, 140, 145, 160, 180, 200]

    crescimento = st.slider("Simular crescimento de vendas (%)", -20, 50, 0, 5)
    vendas_adj = [int(v * (1 + crescimento/100)) for v in vendas_base]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=meses, y=meta_base, name='Meta', marker_color='#e2e8f0'))
    fig.add_trace(go.Scatter(x=meses, y=vendas_adj, name='Realizado',
        mode='lines+markers', line=dict(color='#3b82f6', width=3), marker=dict(size=9)))
    fig.update_layout(height=350, margin=dict(t=20, b=10), plot_bgcolor='white', paper_bgcolor='white')
    st.plotly_chart(fig, use_container_width=True)

    total_real = sum(vendas_adj)
    total_meta = sum(meta_base)
    ating = total_real / total_meta * 100
    col1, col2, col3 = st.columns(3)
    col1.metric("Total realizado", f"{total_real}", f"{crescimento:+d}% ajuste")
    col2.metric("Atingimento da meta", f"{ating:.1f}%")
    col3.metric("Melhor mês", meses[vendas_adj.index(max(vendas_adj))])

with tab2:
    regioes = ['Sudeste', 'Nordeste', 'Sul', 'Centro-Oeste', 'Norte']
    valores = [42, 28, 15, 10, 5]
    cores = ['#1e3a8a', '#2563eb', '#3b82f6', '#60a5fa', '#93c5fd']
    fig2 = go.Figure(data=[go.Pie(labels=regioes, values=valores, hole=0.4,
                                   marker=dict(colors=cores), textinfo='label+percent')])
    fig2.update_layout(height=350, margin=dict(t=0, b=0), paper_bgcolor='white')
    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------------------------
# FORMAÇÃO E CERTIFICAÇÕES (simplificado, mas bonito)
st.markdown('<div class="section-title">Formação & certificações</div>', unsafe_allow_html=True)
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("""
    <div class="stack-category">
        <div class="stack-title">🎓 Formação acadêmica</div>
        <p><strong>Sistemas de Informação</strong><br>UniFOA – 2010</p>
        <p><strong>Técnico em Informática</strong><br>CIBA – 2005</p>
    </div>
    """, unsafe_allow_html=True)
with col_f2:
    st.markdown("""
    <div class="stack-category">
        <div class="stack-title">📜 Certificações (Hashtag Treinamentos)</div>
        <ul style="margin:0;padding-left:1.2rem;">
            <li>SQL para Análise de Dados</li>
            <li>Power BI Expert</li>
            <li>Python para Análise de Dados (Pandas)</li>
            <li>Algoritmos e IA aplicada</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# CONTATO FINAL
st.markdown('<div id="contato"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-card">
    <div style="font-size:1.5rem;font-weight:700;margin-bottom:0.5rem;">Vamos trabalhar juntos?</div>
    <p>Busco oportunidades como Analista de Dados, BI ou Automação. Total disponibilidade para remoto.</p>
    <p>📧 <a href="mailto:raphael_caxias@hotmail.com">raphael_caxias@hotmail.com</a> &nbsp;|&nbsp; 📱 <a href="https://wa.me/5524992275226">(24) 99227-5226</a></p>
    <div style="margin-top:1rem;">
        <a class="btn-primary" href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">LinkedIn</a>
        <a class="btn-outline" href="https://github.com/raphaelcaxias" target="_blank">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">© 2026 Raphael Pires • Portfolio desenvolvido com Streamlit • Dados e BI com propósito</div>', unsafe_allow_html=True)