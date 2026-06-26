import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import os

# =============================================================================
# CONFIGURAÇÃO DA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# TEMA (DARK/LIGHT) - com session_state
# =============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

is_dark = st.session_state.theme == "dark"

# Cores
if is_dark:
    PRIMARY = "#3B82F6"
    SECONDARY = "#0EA5E9"
    BG = "#0B1120"
    TEXT = "#E5E7EB"
    TEXT_MUTED = "#94A3B8"
    CARD_BG = "rgba(59, 130, 246, 0.05)"
    BORDER = "rgba(59, 130, 246, 0.15)"
    PLOTLY_TEMPLATE = "plotly_dark"
    CHART_COLORS = ["#3B82F6", "#0EA5E9", "#60A5FA", "#2563EB", "#0284C7"]
else:
    PRIMARY = "#2563EB"
    SECONDARY = "#0284C7"
    BG = "#F8FAFC"
    TEXT = "#0F172A"
    TEXT_MUTED = "#64748B"
    CARD_BG = "rgba(59, 130, 246, 0.03)"
    BORDER = "rgba(59, 130, 246, 0.1)"
    PLOTLY_TEMPLATE = "plotly_white"
    CHART_COLORS = ["#2563EB", "#0284C7", "#3B82F6", "#1D4ED8", "#0369A1"]

# =============================================================================
# CSS (com as cores dinâmicas)
# =============================================================================
st.markdown(f"""
<style>
/* Reset e fontes */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    background: {BG};
    color: {TEXT};
}}

#MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
.stApp {{ background: {BG}; }}

.block-container {{
    padding: 2rem 4rem 3rem 4rem;
    max-width: 1200px;
}}

@media (max-width: 768px) {{
    .block-container {{ padding: 1.5rem; }}
}}

/* Hero Section */
.hero-section {{
    text-align: center;
    padding: 2rem 0;
    margin-bottom: 2rem;
}}

.hero-name {{
    font-family: 'Playfair Display', serif;
    font-size: 2.75rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.02em;
}}

.hero-title {{
    font-size: 1rem;
    font-weight: 600;
    color: {PRIMARY};
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 0 0 1.5rem 0;
}}

.hero-subtitle {{
    font-size: 1.125rem;
    color: {TEXT_MUTED};
    max-width: 700px;
    margin: 0 auto 2rem auto;
    line-height: 1.6;
}}

.tech-badges {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1.5rem 0;
}}

.tech-badge {{
    background: rgba(59, 130, 246, 0.1);
    border: 1px solid rgba(59, 130, 246, 0.2);
    padding: 0.5rem 1rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 500;
    color: {TEXT};
}}

/* Section Headers */
.section-header {{
    margin: 3rem 0 2rem 0;
    text-align: center;
}}

.section-label {{
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: {PRIMARY};
    background: rgba(59, 130, 246, 0.1);
    padding: 0.4rem 1rem;
    border-radius: 999px;
    margin-bottom: 1rem;
}}

.section-title {{
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0;
}}

/* KPIs */
.kpi-box {{
    background: {CARD_BG};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 1.5rem 1rem;
    text-align: center;
    transition: all 0.3s ease;
}}

.kpi-box:hover {{
    transform: translateY(-4px);
    border-color: {PRIMARY};
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.15);
}}

.kpi-value {{
    font-size: 2rem;
    font-weight: 700;
    color: {PRIMARY};
    margin-bottom: 0.5rem;
}}

.kpi-label {{
    font-size: 0.85rem;
    color: {TEXT_MUTED};
    font-weight: 500;
}}

/* Timeline */
.timeline {{
    position: relative;
    padding: 2rem 0;
}}

.timeline::before {{
    content: '';
    position: absolute;
    left: 30px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, {PRIMARY}, {SECONDARY}, transparent);
}}

.timeline-item {{
    position: relative;
    padding-left: 80px;
    margin-bottom: 2rem;
}}

.timeline-dot {{
    position: absolute;
    left: 22px;
    top: 5px;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: {PRIMARY};
    border: 3px solid {BG};
    box-shadow: 0 0 0 3px {PRIMARY};
}}

.timeline-card {{
    background: {CARD_BG};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
}}

.timeline-card:hover {{
    border-color: {PRIMARY};
    background: rgba(59, 130, 246, 0.08);
    transform: translateX(4px);
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
}}

.timeline-role {{
    font-size: 1.15rem;
    font-weight: 600;
    color: {TEXT};
    margin: 0 0 0.25rem 0;
}}

.timeline-company {{
    font-size: 0.95rem;
    color: {SECONDARY};
    font-weight: 500;
    margin-bottom: 0.75rem;
}}

.timeline-desc {{
    font-size: 0.95rem;
    color: {TEXT_MUTED};
    line-height: 1.6;
    margin: 0;
}}

.timeline-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 1rem;
}}

.timeline-tag {{
    font-size: 0.75rem;
    padding: 0.25rem 0.6rem;
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid rgba(59, 130, 246, 0.15);
    border-radius: 6px;
    color: {TEXT};
    font-weight: 500;
}}

/* Stack */
.stack-category {{
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: {PRIMARY};
    margin-bottom: 0.75rem;
}}

.stack-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}}

.stack-chip {{
    background: rgba(59, 130, 246, 0.08);
    border: 1px solid rgba(59, 130, 246, 0.15);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 500;
    color: {TEXT};
    transition: all 0.2s ease;
}}

.stack-chip:hover {{
    background: {PRIMARY};
    color: white;
    border-color: {PRIMARY};
    transform: translateY(-2px);
}}

/* Footer */
.footer {{
    margin-top: 4rem;
    padding: 3rem 2rem;
    background: {CARD_BG};
    border: 1px solid {BORDER};
    border-radius: 16px;
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
    margin-bottom: 1.5rem;
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
    font-size: 0.85rem;
    font-weight: 600;
    color: #22C55E;
}}

.footer-title {{
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: {TEXT};
    margin: 0 0 0.5rem 0;
}}

.footer-subtitle {{
    font-size: 0.95rem;
    color: {TEXT_MUTED};
    margin: 0 0 1.5rem 0;
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
    padding: 0.4rem 0.8rem;
    border-radius: 999px;
    font-size: 0.8rem;
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
    background: rgba(59, 130, 246, 0.05);
    border: 1px solid rgba(59, 130, 246, 0.15);
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    color: {TEXT};
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}}

.footer-link:hover {{
    background: {PRIMARY};
    color: white;
    border-color: {PRIMARY};
    transform: translateY(-2px);
}}

.footer-copy {{
    font-size: 0.85rem;
    color: {TEXT_MUTED};
    margin: 1.5rem 0 0 0;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(59, 130, 246, 0.1);
}}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 0.5rem;
    background: transparent;
}}

.stTabs [data-baseweb="tab"] {{
    background: rgba(59, 130, 246, 0.05);
    border: 1px solid rgba(59, 130, 246, 0.1);
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
    color: {TEXT};
    font-weight: 500;
}}

.stTabs [aria-selected="true"] {{
    background: {PRIMARY} !important;
    color: white !important;
    border-color: {PRIMARY} !important;
}}

/* Scrollbar */
::-webkit-scrollbar {{ width: 8px; height: 8px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: rgba(59, 130, 246, 0.3); border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: {PRIMARY}; }}

.stMarkdown, h1, h2, h3, h4 {{ color: {TEXT}; }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# TEMA TOGGLE (botão)
# =============================================================================
col1, col2, col3 = st.columns([10, 1, 1])
with col3:
    theme_label = "☀️" if is_dark else "🌙"
    st.button(theme_label, on_click=toggle_theme, key="theme_btn", use_container_width=True)

# =============================================================================
# HERO SECTION
# =============================================================================
st.markdown('<div class="hero-section">', unsafe_allow_html=True)

# Foto
col_f1, col_f2, col_f3 = st.columns([4, 2, 4])
with col_f2:
    # Tenta carregar foto da raiz
    foto_carregada = False
    for fname in ["rapha.jpeg", "rapha.jpg", "assets/rapha.jpeg", "assets/rapha.jpg"]:
        if os.path.exists(fname):
            st.image(fname, width=180)
            foto_carregada = True
            break
    if not foto_carregada:
        # Placeholder
        st.markdown(f"""
        <div style="
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background: linear-gradient(135deg, {PRIMARY}, {SECONDARY});
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            font-weight: 700;
            color: white;
            box-shadow: 0 10px 40px rgba(59, 130, 246, 0.3);
            margin: 0 auto 1.5rem auto;
            border: 3px solid {PRIMARY};
        ">RP</div>
        """, unsafe_allow_html=True)

st.markdown(f"""
<h1 class="hero-name">Raphael Fernando da Silva Pires</h1>
<div class="hero-title">Analista de Dados & Business Intelligence</div>
<p class="hero-subtitle">
    Transformando dados brutos em decisões estratégicas. Mais de <strong>16 anos</strong> 
    construindo inteligência de negócios, automações e governança de dados que geram 
    impacto real e mensurável.
</p>
<div class="tech-badges">
    <span class="tech-badge">📊 Power BI</span>
    <span class="tech-badge">🐍 Python</span>
    <span class="tech-badge">🗄️ SQL</span>
    <span class="tech-badge">☁️ AWS</span>
    <span class="tech-badge">🤖 IA Generativa</span>
    <span class="tech-badge">📈 Dashboards</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Download CV
col_d1, col_d2, col_d3 = st.columns([4, 2, 4])
with col_d2:
    cv_path = None
    for fname in ["Curriculo_Raphael_v2.pdf", "assets/Curriculo_Raphael_v2.pdf"]:
        if os.path.exists(fname):
            cv_path = fname
            break
    if cv_path:
        with open(cv_path, "rb") as f:
            st.download_button(
                label="📄 Download Currículo PDF",
                data=f.read(),
                file_name="Curriculo_Raphael_Pires.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.info("📄 Currículo PDF disponível")

st.divider()

# =============================================================================
# KPIs
# =============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-label">Impacto Mensurável</span>
    <h2 class="section-title">Números que contam histórias</h2>
</div>
""", unsafe_allow_html=True)

kpis = [("16+", "anos de experiência"), ("70%", "redução operacional"), 
        ("213k", "registros processados"), ("2h→15m", "análises reduzidas"), 
        ("R$50bi", "dados analisados")]
cols_kpi = st.columns(5)
for col, (val, lab) in zip(cols_kpi, kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-value">{val}</div>
            <div class="kpi-label">{lab}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =============================================================================
# EXPERIÊNCIA (timeline)
# =============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-label">Trajetória</span>
    <h2 class="section-title">Experiência profissional</h2>
</div>
<div class="timeline">
""", unsafe_allow_html=True)

experiencias = [
    {
        "date": "Experiência Corporativa",
        "role": "Automação de Processos com VBA",
        "company": "Banco do Brasil",
        "desc": "Desenvolvimento de automações em VBA que resultaram em redução de 70% do tempo operacional.",
        "tags": ["VBA", "Automação", "Eficiência"]
    },
    {
        "date": "Fundador & Analista",
        "role": "Fundador",
        "company": "Jardim do Éden",
        "desc": "Dashboards, Power BI, Python, SQL, KPIs e IA Generativa. Redução de 2h para 15min.",
        "tags": ["Power BI", "Python", "SQL", "IA"]
    },
    {
        "date": "Gestão Comercial",
        "role": "Gestão Comercial & BI",
        "company": "J Sintonía",
        "desc": "Business Intelligence, indicadores, dashboards e análise de viabilidade econômica.",
        "tags": ["BI", "KPIs", "Dashboards"]
    },
    {
        "date": "Dados & Operação",
        "role": "Analista de Dados",
        "company": "NSM",
        "desc": "Centralização de dados e controle operacional com construção de indicadores.",
        "tags": ["Dados", "Governança", "Indicadores"]
    }
]

for exp in experiencias:
    tags_html = "".join([f'<span class="timeline-tag">{tag}</span>' for tag in exp["tags"]])
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
            <span class="timeline-date">{exp["date"]}</span>
            <h3 class="timeline-role">{exp["role"]}</h3>
            <div class="timeline-company">{exp["company"]}</div>
            <p class="timeline-desc">{exp["desc"]}</p>
            <div class="timeline-tags">{tags_html}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# =============================================================================
# STACK TECNOLÓGICA
# =============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-label">Stack</span>
    <h2 class="section-title">Tecnologias</h2>
</div>
""", unsafe_allow_html=True)

tech_stack = {
    "📊 Dados": ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy"],
    "📈 Business Intelligence": ["Power BI", "Plotly", "Looker Studio", "Streamlit"],
    "☁️ Cloud & Versionamento": ["AWS", "Git", "GitHub"],
    "⚡ Automação & IA": ["Excel VBA", "IA Generativa"]
}

for cat, techs in tech_stack.items():
    st.markdown(f'<div class="stack-category">{cat}</div>', unsafe_allow_html=True)
    chips = "".join([f'<span class="stack-chip">{t}</span>' for t in techs])
    st.markdown(f'<div class="stack-chips">{chips}</div>', unsafe_allow_html=True)

st.divider()

# =============================================================================
# GRÁFICO DE COMPETÊNCIAS
# =============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-label">Competências</span>
    <h2 class="section-title">Domínio tecnológico</h2>
</div>
""", unsafe_allow_html=True)

skills_data = {
    "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
    "Proficiência": [95, 92, 88, 95, 85, 60, 82],
    "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
}
df_skills = pd.DataFrame(skills_data)

fig = px.bar(
    df_skills,
    x="Proficiência",
    y="Tecnologia",
    color="Categoria",
    orientation="h",
    color_discrete_sequence=CHART_COLORS,
    template=PLOTLY_TEMPLATE,
    text="Proficiência"
)
fig.update_layout(
    margin=dict(l=20, r=40, t=20, b=40),
    height=380,
    xaxis=dict(range=[0, 105], showgrid=True, gridcolor="rgba(148,163,184,0.1)"),
    yaxis=dict(showgrid=False),
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    font=dict(family="Inter", color=TEXT),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
fig.update_traces(textposition="outside", textfont=dict(color=TEXT, size=11))
st.plotly_chart(fig, use_container_width=True)

st.divider()

# =============================================================================
# PROJETOS EM DESTAQUE (sem link_button, sem border)
# =============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-label">Portfólio</span>
    <h2 class="section-title">Projetos em destaque</h2>
</div>
""", unsafe_allow_html=True)

col_p1, col_p2 = st.columns(2)

with col_p1:
    st.markdown("### 🇧🇷 Desenrola Brasil")
    st.write("Análise de dados do programa governamental, explorando renegociações e perfis de consumidores.")
    st.markdown("[🔗 Acessar Repositório](https://github.com/raphaelcaxias)")
    st.write("---")
    st.markdown("### ⛽ Dashboard ANP")
    st.write("Inteligência de dados da ANP com análise de preços e produção de combustíveis.")
    st.markdown("[📊 Ver Dashboard](https://github.com/raphaelcaxias)")

with col_p2:
    st.markdown("### 🔬 CNPq Analytics")
    st.write("Dashboard analítico sobre bolsas e fomento do CNPq com cruzamento de dados de pesquisa.")
    st.markdown("[🔗 Acessar Repositório](https://github.com/raphaelcaxias)")
    st.write("---")
    st.markdown("### 💎 Portfólio Premium")
    st.write("Este portfólio construído em Streamlit com design premium e visualização de dados.")
    st.markdown("[💻 Ver Código](https://github.com/raphaelcaxias)")

st.divider()

# =============================================================================
# AWS CLOUD JOURNEY (opcional)
# =============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-label">Cloud Computing</span>
    <h2 class="section-title">AWS Cloud Journey</h2>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(14, 165, 233, 0.05));
    border: 1px solid rgba(59, 130, 246, 0.15);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    margin: 1.5rem 0;
">
    <p style="margin: 0; font-size: 1.05rem; color: {TEXT};">
        ☁️ Preparando-me para a certificação <strong>AWS Cloud Practitioner</strong>
    </p>
</div>
""", unsafe_allow_html=True)

aws_items = ["☁️ Cloud Computing", "📘 Cloud 101", "🖥️ AWS Console", "💾 Storage", "🛟 Cloud Support", "🤖 ML Foundations", "🌱 Sustainability"]
cols_aws = st.columns(7)
for col, item in zip(cols_aws, aws_items):
    with col:
        st.markdown(f"""
        <div style="
            background: {CARD_BG};
            border: 1px solid {BORDER};
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
        ">
            <div style="font-size: 2rem;">{item.split()[0]}</div>
            <div style="font-size: 0.9rem; font-weight: 600; color: {TEXT};">
                {" ".join(item.split()[1:])}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =============================================================================
# ANÁLISE DE DADOS INTERATIVA (Tabs)
# =============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-label">Análise ao Vivo</span>
    <h2 class="section-title">Demonstração analítica</h2>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Combustíveis ANP", "📊 Impacto Operacional"])

with tab1:
    st.markdown("### Análise de Renegociações")
    np.random.seed(42)
    regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
    faixas = ["Até R$ 5k", "R$ 5k-15k", "R$ 15k-50k", "Acima R$ 50k"]
    
    df_des = pd.DataFrame({
        "Região": np.random.choice(regioes, 400, p=[0.45, 0.28, 0.15, 0.07, 0.05]),
        "Faixa": np.random.choice(faixas, 400, p=[0.55, 0.28, 0.12, 0.05]),
        "Valor": np.random.lognormal(mean=8.5, sigma=1.2, size=400),
        "Status": np.random.choice(["Renegociado", "Em Negociação", "Inadimplente"], 400, p=[0.65, 0.25, 0.10])
    })
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        reg_sel = st.multiselect("Região", regioes, default=regioes)
    with col_f2:
        status_sel = st.multiselect("Status", df_des["Status"].unique(), default=df_des["Status"].unique())
    
    df_filt = df_des[(df_des["Região"].isin(reg_sel)) & (df_des["Status"].isin(status_sel))]
    
    if len(df_filt) > 0:
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("Contratos", f"{len(df_filt):,}".replace(",", "."))
        with col_m2:
            st.metric("Valor Total", f"R$ {df_filt['Valor'].sum()/1e6:.1f}M")
        with col_m3:
            st.metric("Taxa Sucesso", f"{(df_filt['Status']=='Renegociado').mean()*100:.1f}%")
        
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            fig_pie = px.pie(df_filt, names="Região", values="Valor", hole=0.55,
                             color_discrete_sequence=CHART_COLORS, template=PLOTLY_TEMPLATE)
            fig_pie.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320,
                                  paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT))
            st.plotly_chart(fig_pie, use_container_width=True)
        with col_g2:
            fig_bar = px.bar(df_filt.groupby("Faixa", observed=False)["Valor"].sum().reset_index(),
                             x="Faixa", y="Valor", color_discrete_sequence=[CHART_COLORS[0]], template=PLOTLY_TEMPLATE)
            fig_bar.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=320,
                                  paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT),
                                  xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)"))
            st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")

with tab2:
    st.markdown("### Preços de Combustíveis")
    np.random.seed(123)
    estados = ["SP", "RJ", "MG", "RS", "PR", "BA"]
    combustiveis = ["Gasolina", "Etanol", "Diesel"]
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    
    dados = []
    for estado in estados:
        for comb in combustiveis:
            base = {"Gasolina": 5.8, "Etanol": 3.5, "Diesel": 5.2}[comb]
            for mes in meses:
                dados.append({
                    "Estado": estado, "Combustível": comb, "Mês": mes,
                    "Preço": base + np.random.normal(0, 0.15)
                })
    df_anp = pd.DataFrame(dados)
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        est_sel = st.selectbox("Estado", estados)
    with col_e2:
        comb_sel = st.selectbox("Combustível", combustiveis)
    
    df_filt_anp = df_anp[(df_anp["Estado"] == est_sel) & (df_anp["Combustível"] == comb_sel)]
    
    if len(df_filt_anp) > 0:
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            preco_atual = df_filt_anp[df_filt_anp["Mês"] == "Jun"]["Preço"].values[0]
            st.metric("Preço Atual", f"R$ {preco_atual:.2f}")
        with col_m2:
            variacao = ((df_filt_anp["Preço"].max() - df_filt_anp["Preço"].min()) / df_filt_anp["Preço"].min()) * 100
            st.metric("Variação Semestral", f"{variacao:.1f}%")
        
        fig_anp = px.line(df_filt_anp, x="Mês", y="Preço", markers=True,
                          color_discrete_sequence=[CHART_COLORS[0]], template=PLOTLY_TEMPLATE)
        fig_anp.update_layout(title=f"{comb_sel} - {est_sel}", margin=dict(l=20, r=20, t=50, b=20),
                              height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT),
                              xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)"))
        st.plotly_chart(fig_anp, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado.")

with tab3:
    st.markdown("### Impacto da Automação")
    meses_full = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    df_evo = pd.DataFrame({
        "Mês": meses_full * 2,
        "Tipo": ["Antes"] * 12 + ["Após"] * 12,
        "Horas": [120, 125, 118, 130, 122, 128, 126, 124, 129, 127, 125, 130] +
                [95, 70, 55, 45, 38, 35, 33, 32, 30, 29, 28, 27]
    })
    fig_evo = px.line(df_evo, x="Mês", y="Horas", color="Tipo", markers=True,
                      color_discrete_sequence=[CHART_COLORS[3], CHART_COLORS[0]], template=PLOTLY_TEMPLATE)
    fig_evo.update_layout(title="Evolução de Horas - Antes vs Após Automação",
                          margin=dict(l=20, r=20, t=60, b=20), height=380,
                          paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=TEXT),
                          xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)"))
    st.plotly_chart(fig_evo, use_container_width=True)
    
    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.metric("Horas Economizadas", "1.108 h", "+93% eficiência")
    with col_r2:
        st.metric("Custo Evitado", "R$ 185k", "vs. contratação")
    with col_r3:
        st.metric("Projetos Entregues", "24", "+60% vs. ano anterior")

st.divider()

# =============================================================================
# FOOTER
# =============================================================================
st.markdown(f"""
<div class="footer">
    <div class="footer-status">
        <span class="footer-status-dot"></span>
        <span class="footer-status-text">Disponível para oportunidades</span>
    </div>
    
    <h3 class="footer-title">Vamos conversar sobre dados?</h3>
    <p class="footer-subtitle">Aberto a projetos em Dados, BI e Cloud</p>
    
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
        <a href="tel:+5511999999999" class="footer-link">📱 Telefone</a>
    </div>
    
    <p class="footer-copy">© {datetime.now().year} Raphael Fernando da Silva Pires</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
