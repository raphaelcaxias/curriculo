# -*- coding: utf-8 -*-
"""
Premium Personal Product - Raphael Pires
Versão: 5.0 - Corrigido erro de hash do PIL Image
"""

import streamlit as st
from PIL import Image
import os
import requests
from io import BytesIO
import base64

# ------------------------------------------------------------------------------
# CONFIGURAÇÃO INICIAL
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Raphael Pires | Dados · Automação · BI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------------------------
# CARREGAMENTO DE IMAGEM E PDF (SEM CACHE NOS OBJETOS PIL)
# ------------------------------------------------------------------------------
def load_image():
    """Carrega a imagem sem cache para evitar erro de hash"""
    # Tenta URL raw do GitHub
    url = "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/rapha.jpeg"
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return Image.open(BytesIO(r.content))
    except Exception:
        pass
    
    # Tenta arquivo local como fallback
    for p in ["rapha.jpeg", "rapha.jpg", "assets/rapha.jpeg"]:
        if os.path.exists(p):
            return Image.open(p)
    return None

def get_image_base64(img):
    """Converte imagem PIL para base64"""
    if img:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    return None

@st.cache_data(show_spinner=False)
def load_cv():
    """Cache apenas para o PDF"""
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

# Carrega imagem e converte para base64
profile_image = load_image()
profile_base64 = get_image_base64(profile_image) if profile_image else None
cv_pdf = load_cv()

# ------------------------------------------------------------------------------
# CSS PREMIUM COMPLETO (mantido igual)
# ------------------------------------------------------------------------------
st.markdown("""
<style>
/* ==================== DESIGN SYSTEM ==================== */
:root {
    --bg-primary: #F8FAFC;
    --bg-secondary: #FFFFFF;
    --bg-tertiary: #F1F5F9;
    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-tertiary: #64748B;
    --accent-primary: #059669;
    --accent-primary-dark: #047857;
    --accent-secondary: #3B82F6;
    --border-light: #E2E8F0;
    --border-medium: #CBD5E1;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 20px;
    --radius-xl: 28px;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --transition-fast: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-normal: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg-primary: #0F172A;
        --bg-secondary: #1E293B;
        --bg-tertiary: #334155;
        --text-primary: #F8FAFC;
        --text-secondary: #CBD5E1;
        --text-tertiary: #94A3B8;
        --border-light: #334155;
        --border-medium: #475569;
    }
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body, .stApp { background-color: var(--bg-primary) !important; font-family: var(--font-sans); color: var(--text-primary); }
#MainMenu, footer, header, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* Animações */
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
@keyframes scaleIn { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }

.fade-in { animation: fadeIn 0.6s ease-out forwards; }
.slide-in { animation: slideInLeft 0.5s ease-out forwards; }
.scale-in { animation: scaleIn 0.4s ease-out forwards; }

/* Navbar */
.navbar { position: fixed; top: 0; left: 0; width: 100%; background: rgba(248, 250, 252, 0.8); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border-light); padding: 1rem 0; z-index: 1000; }
@media (prefers-color-scheme: dark) { .navbar { background: rgba(15, 23, 42, 0.8); } }
.navbar-container { max-width: 1200px; margin: 0 auto; padding: 0 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.navbar-logo { font-weight: 700; font-size: 1.2rem; color: var(--accent-primary); text-decoration: none; }
.navbar-links { display: flex; gap: 2rem; flex-wrap: wrap; }
.navbar-links a { font-weight: 500; font-size: 0.9rem; color: var(--text-secondary); text-decoration: none; transition: var(--transition-fast); position: relative; }
.navbar-links a:hover { color: var(--accent-primary); }
.navbar-links a::after { content: ''; position: absolute; bottom: -5px; left: 0; width: 0; height: 2px; background: var(--accent-primary); transition: var(--transition-fast); }
.navbar-links a:hover::after { width: 100%; }

/* Container */
.main-container { padding-top: 90px; max-width: 1200px; margin: 0 auto; padding-left: 2rem; padding-right: 2rem; }
.section { margin-bottom: 5rem; scroll-margin-top: 90px; animation: fadeIn 0.6s ease-out; }
.section-title { font-size: 2rem; font-weight: 700; margin-bottom: 2rem; letter-spacing: -0.02em; background: linear-gradient(135deg, var(--text-primary) 0%, var(--accent-primary) 100%); background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent; position: relative; display: inline-block; }
.section-title::after { content: ''; position: absolute; bottom: -8px; left: 0; width: 60px; height: 3px; background: var(--accent-primary); border-radius: 3px; }

/* Hero */
.hero-pic { width: 180px; height: 180px; border-radius: 50%; object-fit: cover; border: 3px solid var(--accent-primary); box-shadow: var(--shadow-xl); transition: var(--transition-normal); }
.hero-pic:hover { transform: scale(1.02); }
.hero-name { font-size: 3.5rem; font-weight: 800; letter-spacing: -0.02em; background: linear-gradient(135deg, var(--text-primary) 0%, var(--accent-primary) 100%); background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-title { font-size: 1.25rem; color: var(--accent-primary); font-weight: 500; margin-bottom: 1rem; }
.hero-description { font-size: 1rem; color: var(--text-secondary); line-height: 1.6; max-width: 600px; margin-bottom: 1.5rem; }
.hero-stats { display: flex; gap: 2rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.hero-stat-number { font-size: 1.5rem; font-weight: 700; color: var(--accent-primary); }
.hero-stat-label { font-size: 0.7rem; color: var(--text-tertiary); text-transform: uppercase; }

/* Botões */
.btn-group { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn-primary { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--accent-primary); color: white; padding: 0.7rem 1.5rem; border-radius: 40px; text-decoration: none; font-weight: 600; transition: var(--transition-fast); }
.btn-primary:hover { background: var(--accent-primary-dark); transform: translateY(-2px); }
.btn-secondary { display: inline-flex; align-items: center; gap: 0.5rem; background: transparent; border: 1px solid var(--border-medium); color: var(--text-primary); padding: 0.7rem 1.5rem; border-radius: 40px; text-decoration: none; font-weight: 500; transition: var(--transition-fast); }
.btn-secondary:hover { border-color: var(--accent-primary); color: var(--accent-primary); transform: translateY(-2px); }

/* Cards */
.impact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
.impact-card { background: var(--bg-secondary); border-radius: var(--radius-lg); padding: 1.5rem; text-align: center; border: 1px solid var(--border-light); transition: var(--transition-normal); }
.impact-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-xl); }
.impact-number { font-size: 2.5rem; font-weight: 800; color: var(--accent-primary); }

/* Timeline */
.timeline-item { display: flex; margin-bottom: 2rem; position: relative; }
.timeline-left { width: 120px; flex-shrink: 0; text-align: right; padding-right: 1.5rem; }
.timeline-year { font-weight: 700; color: var(--accent-primary); }
.timeline-line { position: relative; width: 2px; background: var(--border-light); margin-right: 1.5rem; }
.timeline-dot { position: absolute; left: -5px; top: 8px; width: 12px; height: 12px; background: var(--accent-primary); border-radius: 50%; border: 2px solid var(--bg-secondary); }
.timeline-title { font-weight: 700; font-size: 1.1rem; }
.timeline-company { color: var(--text-tertiary); font-size: 0.85rem; }
.timeline-desc { font-size: 0.85rem; color: var(--text-secondary); margin: 0.3rem 0; padding-left: 1rem; border-left: 2px solid var(--border-light); }

/* Project cards */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 2rem; }
.project-card { background: var(--bg-secondary); border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-light); transition: var(--transition-normal); }
.project-card:hover { transform: translateY(-8px); box-shadow: var(--shadow-xl); border-color: var(--accent-primary); }
.project-img { width: 100%; height: 180px; background: var(--bg-tertiary); display: flex; align-items: center; justify-content: center; font-size: 3rem; }
.project-content { padding: 1.5rem; }
.project-title { font-weight: 700; font-size: 1.2rem; }
.project-desc { font-size: 0.85rem; color: var(--text-secondary); margin: 0.5rem 0 1rem; }
.project-metrics { display: flex; gap: 1rem; margin-bottom: 1rem; }
.project-metric-value { font-weight: 700; color: var(--accent-primary); }
.tech-tag { background: var(--bg-tertiary); padding: 0.25rem 0.75rem; border-radius: 30px; font-size: 0.7rem; display: inline-block; margin-right: 0.5rem; margin-bottom: 0.5rem; }
.project-links a { font-size: 0.8rem; color: var(--accent-primary); text-decoration: none; margin-right: 1rem; }

/* Stack */
.stack-category { margin-bottom: 2rem; }
.stack-chips { display: flex; flex-wrap: wrap; gap: 0.75rem; }
.chip { background: var(--bg-tertiary); padding: 0.5rem 1.2rem; border-radius: 40px; font-size: 0.8rem; transition: var(--transition-fast); }
.chip:hover { background: var(--accent-primary); color: white; }

/* Method */
.method-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
.method-card { background: var(--bg-secondary); border-radius: var(--radius-lg); padding: 1.5rem; border: 1px solid var(--border-light); transition: var(--transition-normal); }
.method-card:hover { transform: translateY(-5px); border-color: var(--accent-primary); }

/* Footer */
.footer-impact { background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-tertiary) 100%); border-radius: var(--radius-xl); padding: 2.5rem; text-align: center; margin-top: 3rem; }
.footer-links { display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin: 1.5rem 0; }
.footer-links a { color: var(--text-secondary); text-decoration: none; }
.footer-links a:hover { color: var(--accent-primary); }

/* Responsivo */
@media (max-width: 768px) {
    .main-container { padding-left: 1rem; padding-right: 1rem; }
    .hero-name { font-size: 2.2rem; }
    .timeline-left { width: 80px; }
    .projects-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# NAVBAR
# ------------------------------------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="navbar-container">
        <a href="#inicio" class="navbar-logo">RP</a>
        <div class="navbar-links">
            <a href="#inicio">Início</a>
            <a href="#sobre">Sobre</a>
            <a href="#experiencia">Trajetória</a>
            <a href="#portfolio">Cases</a>
            <a href="#stack">Stack</a>
            <a href="#lab">Lab</a>
            <a href="#contato">Contato</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# MAIN CONTAINER
# ------------------------------------------------------------------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ==============================================================================
# HERO SECTION
# ==============================================================================
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)

hero_col1, hero_col2 = st.columns([1, 2], gap="large")
with hero_col1:
    if profile_base64:
        st.markdown(f'<img src="data:image/jpeg;base64,{profile_base64}" class="hero-pic">', unsafe_allow_html=True)
    else:
        st.markdown('<div style="width:180px;height:180px;background:var(--bg-tertiary);border-radius:50%;display:flex;align-items:center;justify-content:center;">📷</div>', unsafe_allow_html=True)

with hero_col2:
    st.markdown("""
    <h1 class="hero-name">Raphael Pires</h1>
    <div class="hero-title">Dados · Automação · Inteligência Operacional</div>
    <div class="hero-description">
    +15 anos transformando operações reais em inteligência acionável. 
    Da automação bancária à gestão de negócio próprio — dados não são teoria, são decisão.
    </div>
    <div class="hero-stats">
        <div><div class="hero-stat-number">15+</div><div class="hero-stat-label">anos operação</div></div>
        <div><div class="hero-stat-number">70%</div><div class="hero-stat-label">redução operacional</div></div>
        <div><div class="hero-stat-number">213k+</div><div class="hero-stat-label">registros</div></div>
        <div><div class="hero-stat-number">4+</div><div class="hero-stat-label">dashboards</div></div>
    </div>
    <div class="btn-group">
        <a class="btn-primary" href="#contato">📬 Vamos conversar</a>
        <a class="btn-secondary" href="#portfolio">📊 Ver Cases</a>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# METODOLOGIA
# ==============================================================================
st.markdown('<div id="sobre" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Como penso dados</div>', unsafe_allow_html=True)

st.markdown("""
<div class="method-grid">
    <div class="method-card"><div style="font-size:2rem;">🔍</div><h4>Entendo a operação</h4><p style="color:var(--text-secondary);">Antes de qualquer SQL, entendo o fluxo real. Números só fazem sentido com contexto.</p></div>
    <div class="method-card"><div style="font-size:2rem;">⚙️</div><h4>Automatizo o repetitivo</h4><p style="color:var(--text-secondary);">Planilha que abre em 14 minutos não é dado — é sofrimento. Crio pipelines que entregam análise.</p></div>
    <div class="method-card"><div style="font-size:2rem;">📊</div><h4>Traduzo para decisão</h4><p style="color:var(--text-secondary);">Gráfico bonito não aprova orçamento. Insight claro e acionável sim.</p></div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# IMPACT CARDS
# ==============================================================================
st.markdown('<div class="section-title">Impacto mensurável</div>', unsafe_allow_html=True)
impact_data = [("-70%", "Tempo operacional"), ("2h → 15min", "Ciclo de análise"), ("20", "Agências automatizadas"), ("213.735", "Registros processados")]
cols = st.columns(4)
for i, (num, desc) in enumerate(impact_data):
    with cols[i]:
        st.markdown(f'<div class="impact-card"><div class="impact-number">{num}</div><div class="impact-text">{desc}</div></div>', unsafe_allow_html=True)

# ==============================================================================
# EXPERIÊNCIA
# ==============================================================================
st.markdown('<div id="experiencia" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Trajetória profissional</div>', unsafe_allow_html=True)

experiences = [
    {"year": "2014 — 2026", "title": "Analista de KPIs & Operações", "company": "J Sintonía", "desc": ["Monitoramento de vendas, margem e giro", "Relatórios automatizados", "SQL e Python para consolidação"]},
    {"year": "2009 — presente", "title": "Gestão Comercial & Dados", "company": "Jardim do Éden", "desc": ["Redução de 2h para 15min no ciclo", "Automação com Python e IA", "Estruturação de fluxo analítico"]},
    {"year": "2008 — 2010", "title": "Estagiário — Automação & Dados", "company": "Banco do Brasil", "desc": ["Automação em 20 agências com VBA", "Redução de 70% no tempo", "Consolidação de relatórios"]},
    {"year": "2002 — 2009", "title": "Suporte Operacional", "company": "NSM Comércio", "desc": ["Centralização de dados de 7 unidades", "Controle de estoque"]}
]

for exp in experiences:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-left"><span class="timeline-year">{exp['year']}</span></div>
        <div class="timeline-line"><div class="timeline-dot"></div></div>
        <div class="timeline-content">
            <div class="timeline-title">{exp['title']}</div>
            <div class="timeline-company">{exp['company']}</div>
            {''.join([f'<div class="timeline-desc">— {d}</div>' for d in exp['desc']])}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# CASES
# ==============================================================================
st.markdown('<div id="portfolio" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Cases em destaque</div>', unsafe_allow_html=True)

projects = [
    {"name": "Desenrola Brasil", "desc": "Dashboard com dados do Banco Central (R$50 bi).", "tech": ["Python", "Pandas", "Plotly", "Streamlit"], "metrics": [("R$50B", "renegociados")], "app_url": "https://desenrolabrasil.streamlit.app/", "code_url": "https://github.com/raphaelcaxias/DESENROLA_BRASIL", "icon": "📊"},
    {"name": "CNPq Analytics", "desc": "Análise de 213 mil bolsas, R$1,2 bi.", "tech": ["Python", "Pandas", "Plotly", "Streamlit"], "metrics": [("213k+", "bolsas")], "app_url": "https://cnpq-analytics.streamlit.app/", "code_url": "https://github.com/raphaelcaxias/CNPq-Analytics", "icon": "🎓"},
    {"name": "Portfólio Premium (Este Site)", "desc": "Produto pessoal com design system, animações, responsividade.", "tech": ["Streamlit", "Python", "CSS3", "Design System"], "metrics": [("100%", "customizado")], "app_url": None, "code_url": "https://github.com/raphaelcaxias/curriculo", "icon": "⚡"}
]

for proj in projects:
    metrics_html = ''.join([f'<div class="project-metric"><div class="project-metric-value">{m[0]}</div><div class="project-metric-label">{m[1]}</div></div>' for m in proj['metrics']])
    tech_tags = ''.join([f'<span class="tech-tag">{t}</span>' for t in proj['tech']])
    app_link = f'<a href="{proj["app_url"]}" target="_blank">🔗 Aplicação</a>' if proj['app_url'] else ''
    code_link = f'<a href="{proj["code_url"]}" target="_blank">📄 Código</a>'
    st.markdown(f"""
    <div class="project-card">
        <div class="project-img">{proj['icon']} {proj['name']}</div>
        <div class="project-content">
            <div class="project-title">{proj['name']}</div>
            <div class="project-desc">{proj['desc']}</div>
            <div class="project-metrics">{metrics_html}</div>
            <div class="project-tech">{tech_tags}</div>
            <div class="project-links">{app_link} {code_link}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# STACK
# ==============================================================================
st.markdown('<div id="stack" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Stack técnica</div>', unsafe_allow_html=True)

stack_cats = {
    "📌 Dados & ETL": ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy"],
    "📊 BI & Visualização": ["Power BI", "Looker Studio", "Plotly", "Streamlit"],
    "📈 Análise & Indicadores": ["KPIs", "Dashboards", "ETL"],
    "⚙️ Automação & Ferramentas": ["Excel/VBA", "Git", "IA Generativa", "CSS Design"]
}

for cat, items in stack_cats.items():
    st.markdown(f'<div class="stack-category"><h4>{cat}</h4><div class="stack-chips">', unsafe_allow_html=True)
    for item in items:
        st.markdown(f'<span class="chip">{item}</span>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

# ==============================================================================
# LABORATÓRIO
# ==============================================================================
st.markdown('<div id="lab" class="section"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Laboratório</div>', unsafe_allow_html=True)

lab_items = [("⚡", "Portfólio Premium", "Concluído"), ("🤖", "IA para relatórios", "Em desenvolvimento"), ("📊", "Dashboard fluxo de caixa", "Prototipado")]

cols_lab = st.columns(3)
for i, (icon, title, status) in enumerate(lab_items):
    with cols_lab[i]:
        st.markdown(f"""
        <div class="method-card" style="text-align:center;">
            <div style="font-size:2rem;">{icon}</div>
            <div style="font-weight:600;">{title}</div>
            <div style="font-size:0.7rem;color:var(--accent-primary);">{status}</div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# FORMAÇÃO
# ==============================================================================
st.markdown('<div class="section-title">Formação & Certificações</div>', unsafe_allow_html=True)
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("""
    <div style="background:var(--bg-secondary);border-radius:20px;padding:1.5rem;">
        <div style="font-size:1.5rem;">🎓</div>
        <strong>Sistemas de Informação</strong> — UniFOA (2010)<br>
        <strong>Técnico em Informática</strong> — CIBA (2005)
    </div>
    """, unsafe_allow_html=True)
with col_f2:
    st.markdown("""
    <div style="background:var(--bg-secondary);border-radius:20px;padding:1.5rem;">
        <div style="font-size:1.5rem;">📜</div>
        <strong>Certificações (Hashtag)</strong><br>
        • SQL · Power BI · Python · IA Aplicada
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# CONTATO
# ==============================================================================
st.markdown('<div id="contato" class="section"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer-impact">
    <h3>Transformando operações em inteligência acionável</h3>
    <p>Disponível para remoto ou híbrido</p>
    <div class="footer-links">
        <a href="mailto:raphael_caxias@hotmail.com">📧 raphael_caxias@hotmail.com</a>
        <a href="tel:+5524992275226">📱 (24) 99227-5226</a>
        <a href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">🔗 LinkedIn</a>
        <a href="https://github.com/raphaelcaxias" target="_blank">💻 GitHub</a>
    </div>
    <div style="font-size:0.75rem;">© 2026 Raphael Pires · Dados com propósito</div>
</div>
""", unsafe_allow_html=True)

if cv_pdf:
    st.download_button("📄 Baixar currículo (PDF)", data=cv_pdf, file_name="Raphael_Pires_Curriculo.pdf", mime="application/pdf")

st.markdown('</div>', unsafe_allow_html=True)
