# -*- coding: utf-8 -*-
"""
Portfolio Premium — Raphael Pires
Versão: 6.0 — Redesign editorial luxury dark
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
    page_title="Raphael Pires — Dados & Automação",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------------------------
# CARREGAMENTO DE IMAGEM E PDF
# ------------------------------------------------------------------------------
def load_image():
    url = "https://raw.githubusercontent.com/raphaelcaxias/curriculo/main/rapha.jpeg"
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return Image.open(BytesIO(r.content))
    except Exception:
        pass
    for p in ["rapha.jpeg", "rapha.jpg", "assets/rapha.jpeg"]:
        if os.path.exists(p):
            return Image.open(p)
    return None

def get_image_base64(img):
    if img:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
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
profile_base64 = get_image_base64(profile_image) if profile_image else None
cv_pdf = load_cv()

# ------------------------------------------------------------------------------
# DESIGN SYSTEM — EDITORIAL DARK LUXURY
# ------------------------------------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap" rel="stylesheet">

<style>
:root {
    --ink:        #0A0A0B;
    --ink-soft:   #1A1A1E;
    --ink-mid:    #2C2C32;
    --rule:       #2A2A30;
    --muted:      #6B6B78;
    --quiet:      #9696A0;
    --text:       #E8E8EC;
    --text-dim:   #A8A8B4;
    --gold:       #C9A84C;
    --gold-light: #E8C877;
    --gold-dim:   #7A6228;
    --teal:       #2DD4BF;
    --teal-dim:   #134E4A;
    --serif:      'DM Serif Display', Georgia, serif;
    --sans:       'DM Sans', system-ui, sans-serif;
    --ease:       cubic-bezier(0.4, 0, 0.2, 1);
}

*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

html, body, .stApp {
    background: var(--ink) !important;
    font-family: var(--sans);
    color: var(--text);
    -webkit-font-smoothing: antialiased;
}

#MainMenu, footer, header, .stDeployButton,
.stToolbar, [data-testid="stToolbar"] { display:none !important; }

.block-container { padding:0 !important; max-width:100% !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width:4px; }
::-webkit-scrollbar-track { background:var(--ink); }
::-webkit-scrollbar-thumb { background:var(--gold-dim); border-radius:2px; }

/* ── ANIMATIONS ── */
@keyframes rise {
    from { opacity:0; transform:translateY(32px); }
    to   { opacity:1; transform:translateY(0); }
}
@keyframes appear {
    from { opacity:0; }
    to   { opacity:1; }
}
@keyframes lineGrow {
    from { transform:scaleX(0); }
    to   { transform:scaleX(1); }
}

/* ── NAVBAR ── */
.navbar {
    position: fixed; top:0; left:0; width:100%;
    background: rgba(10,10,11,0.85);
    backdrop-filter: blur(16px) saturate(180%);
    border-bottom: 1px solid var(--rule);
    z-index: 1000;
    animation: appear 0.4s var(--ease);
}
.navbar-inner {
    max-width: 1280px; margin:0 auto;
    padding: 0 3rem;
    height: 68px;
    display: flex; align-items:center; justify-content:space-between;
}
.navbar-logo {
    font-family: var(--serif);
    font-size: 1.4rem;
    color: var(--gold);
    letter-spacing: 0.02em;
    text-decoration:none;
}
.navbar-nav { display:flex; gap:2.5rem; }
.navbar-nav a {
    font-size: 0.78rem;
    font-weight: 400;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--quiet);
    text-decoration:none;
    transition: color 0.2s;
}
.navbar-nav a:hover { color: var(--gold); }

/* ── PAGE WRAPPER ── */
.page { max-width:1280px; margin:0 auto; padding: 120px 3rem 0; }

/* ── SECTION ── */
.section { margin-bottom: 7rem; scroll-margin-top: 90px; }

.section-label {
    font-size: 0.7rem;
    font-weight: 400;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.75rem;
    display: flex; align-items:center; gap:0.75rem;
}
.section-label::before {
    content:'';
    display:inline-block;
    width:24px; height:1px;
    background: var(--gold);
}

.section-title {
    font-family: var(--serif);
    font-size: clamp(2rem, 4vw, 3.25rem);
    font-weight: 400;
    color: var(--text);
    line-height: 1.1;
    letter-spacing:-0.01em;
    margin-bottom: 3rem;
}

/* ── RULE ── */
.hr { border:none; border-top:1px solid var(--rule); margin: 4rem 0; }

/* ── HERO ── */
.hero-wrap {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 4rem;
    align-items: center;
    padding: 4rem 0 6rem;
    animation: rise 0.8s var(--ease);
}
.hero-photo-ring {
    width: 200px; height: 200px;
    border-radius: 50%;
    padding: 3px;
    background: linear-gradient(135deg, var(--gold), var(--gold-dim));
    flex-shrink:0;
}
.hero-photo-inner {
    width:100%; height:100%;
    border-radius:50%;
    overflow:hidden;
    background: var(--ink-soft);
    display:flex; align-items:center; justify-content:center;
    font-size:4rem;
}
.hero-photo-inner img { width:100%; height:100%; object-fit:cover; }

.hero-eyebrow {
    font-size:0.72rem; font-weight:400;
    letter-spacing:0.22em; text-transform:uppercase;
    color: var(--gold); margin-bottom:1rem;
}
.hero-name {
    font-family: var(--serif);
    font-size: clamp(3rem, 5vw, 5rem);
    font-weight:400;
    color: var(--text);
    line-height:1;
    letter-spacing:-0.02em;
    margin-bottom:0.5rem;
}
.hero-name em { font-style:italic; color: var(--gold); }

.hero-tagline {
    font-size:1.1rem;
    font-weight:300;
    color: var(--text-dim);
    max-width:500px;
    line-height:1.65;
    margin-bottom:2.5rem;
}
.hero-kpis {
    display:flex; gap:3rem; margin-bottom:2.5rem; flex-wrap:wrap;
}
.hero-kpi-val {
    font-family: var(--serif);
    font-size:2.4rem; font-weight:400;
    color: var(--gold);
    display:block; line-height:1;
}
.hero-kpi-lbl {
    font-size:0.68rem;
    letter-spacing:0.14em; text-transform:uppercase;
    color: var(--muted);
    margin-top:0.3rem; display:block;
}
.hero-actions { display:flex; gap:1rem; flex-wrap:wrap; }

.btn-gold {
    display:inline-flex; align-items:center; gap:0.5rem;
    background: var(--gold);
    color: var(--ink) !important;
    font-size:0.78rem; font-weight:500;
    letter-spacing:0.1em; text-transform:uppercase;
    padding:0.75rem 1.75rem;
    border-radius:2px;
    text-decoration:none;
    transition: background 0.2s, transform 0.2s;
    white-space:nowrap;
}
.btn-gold:hover { background: var(--gold-light); transform:translateY(-2px); }

.btn-ghost {
    display:inline-flex; align-items:center; gap:0.5rem;
    background: transparent;
    color: var(--text-dim) !important;
    font-size:0.78rem; font-weight:400;
    letter-spacing:0.1em; text-transform:uppercase;
    padding:0.75rem 1.75rem;
    border:1px solid var(--rule);
    border-radius:2px;
    text-decoration:none;
    transition: border-color 0.2s, color 0.2s, transform 0.2s;
    white-space:nowrap;
}
.btn-ghost:hover { border-color:var(--gold); color:var(--gold) !important; transform:translateY(-2px); }

/* ── IMPACT STRIP ── */
.impact-strip {
    display:grid;
    grid-template-columns: repeat(4,1fr);
    border: 1px solid var(--rule);
    border-radius:4px;
    overflow:hidden;
    margin-bottom:5rem;
    animation: rise 0.9s 0.15s var(--ease) both;
}
.impact-cell {
    padding:2rem 1.5rem;
    border-right:1px solid var(--rule);
    transition: background 0.25s;
}
.impact-cell:last-child { border-right:none; }
.impact-cell:hover { background:var(--ink-soft); }
.impact-num {
    font-family:var(--serif);
    font-size:2.75rem; font-weight:400;
    color: var(--gold);
    display:block; line-height:1;
    margin-bottom:0.5rem;
}
.impact-lbl {
    font-size:0.72rem;
    letter-spacing:0.14em; text-transform:uppercase;
    color: var(--muted);
}

/* ── METHOD CARDS ── */
.method-trio {
    display:grid; grid-template-columns:repeat(3,1fr); gap:1.5px;
    background:var(--rule); border-radius:4px; overflow:hidden;
    margin-bottom:2rem;
}
.method-card {
    background:var(--ink-soft);
    padding:2.5rem 2rem;
    transition:background 0.25s;
}
.method-card:hover { background:var(--ink-mid); }
.method-icon { font-size:1.75rem; margin-bottom:1.25rem; display:block; }
.method-title {
    font-family:var(--serif); font-size:1.25rem; color:var(--text);
    margin-bottom:0.75rem;
}
.method-desc { font-size:0.875rem; color:var(--text-dim); line-height:1.7; font-weight:300; }

/* ── TIMELINE ── */
.timeline { position:relative; }
.timeline::before {
    content:''; position:absolute; left:120px; top:0; bottom:0;
    width:1px; background:var(--rule);
}
.tl-item {
    display:grid; grid-template-columns:120px 1fr;
    gap:2.5rem; margin-bottom:3rem; position:relative;
}
.tl-item::before {
    content:''; position:absolute;
    left:115px; top:6px;
    width:11px; height:11px;
    border-radius:50%;
    background: var(--ink);
    border: 2px solid var(--gold);
}
.tl-year {
    font-size:0.72rem;
    letter-spacing:0.08em;
    color:var(--muted);
    padding-top:3px;
    text-align:right;
}
.tl-role {
    font-family:var(--serif); font-size:1.2rem; color:var(--text);
    margin-bottom:0.2rem;
}
.tl-company { font-size:0.8rem; color:var(--gold); letter-spacing:0.06em; margin-bottom:0.75rem; }
.tl-detail {
    font-size:0.82rem; color:var(--text-dim); font-weight:300;
    line-height:1.75;
    padding-left:0.75rem;
    border-left:1px solid var(--gold-dim);
    margin-bottom:0.4rem;
}

/* ── PROJECTS ── */
.projects-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5px; background:var(--rule); border-radius:4px; overflow:hidden; }
.proj-card {
    background:var(--ink-soft);
    padding:2rem;
    display:flex; flex-direction:column;
    transition:background 0.25s;
    position:relative; overflow:hidden;
}
.proj-card:hover { background:var(--ink-mid); }
.proj-card::after {
    content:''; position:absolute; bottom:0; left:0; right:0;
    height:2px; background:var(--gold);
    transform:scaleX(0); transform-origin:left;
    transition:transform 0.35s var(--ease);
}
.proj-card:hover::after { transform:scaleX(1); }
.proj-number {
    font-family:var(--serif); font-size:3rem; font-weight:400;
    color:var(--rule); line-height:1; margin-bottom:1.5rem;
}
.proj-icon { font-size:2rem; margin-bottom:1rem; }
.proj-title {
    font-family:var(--serif); font-size:1.3rem; color:var(--text);
    margin-bottom:0.75rem; line-height:1.2;
}
.proj-desc { font-size:0.82rem; color:var(--text-dim); line-height:1.7; font-weight:300; flex:1; margin-bottom:1.5rem; }
.proj-metric { font-size:0.72rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--gold); margin-bottom:1.25rem; }
.proj-tags { display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1.25rem; }
.tag {
    font-size:0.65rem; letter-spacing:0.1em; text-transform:uppercase;
    padding:0.3rem 0.65rem; border-radius:1px;
    border:1px solid var(--rule); color:var(--muted);
}
.proj-links { display:flex; gap:1.25rem; }
.proj-links a {
    font-size:0.72rem; letter-spacing:0.1em; text-transform:uppercase;
    color:var(--quiet); text-decoration:none;
    transition:color 0.2s;
}
.proj-links a:hover { color:var(--gold); }

/* ── STACK ── */
.stack-section { display:grid; grid-template-columns:repeat(2,1fr); gap:2rem; }
.stack-block { }
.stack-cat {
    font-size:0.7rem; letter-spacing:0.2em; text-transform:uppercase;
    color:var(--gold); margin-bottom:1rem;
    display:flex; align-items:center; gap:0.5rem;
}
.stack-cat::after { content:''; flex:1; height:1px; background:var(--rule); }
.stack-pills { display:flex; flex-wrap:wrap; gap:0.5rem; }
.pill {
    font-size:0.8rem; font-weight:300;
    padding:0.45rem 1rem; border-radius:2px;
    border:1px solid var(--rule);
    color:var(--text-dim);
    transition:border-color 0.2s, color 0.2s, background 0.2s;
    cursor:default;
}
.pill:hover { border-color:var(--gold); color:var(--gold); background:rgba(201,168,76,0.06); }

/* ── LAB ── */
.lab-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.lab-card {
    padding:1.75rem;
    border:1px solid var(--rule);
    border-radius:4px;
    transition:border-color 0.25s, transform 0.25s;
}
.lab-card:hover { border-color:var(--gold-dim); transform:translateY(-4px); }
.lab-card-icon { font-size:1.5rem; margin-bottom:1rem; }
.lab-card-title { font-family:var(--serif); font-size:1.1rem; color:var(--text); margin-bottom:0.35rem; }
.lab-status {
    font-size:0.65rem; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--gold); font-weight:400;
}

/* ── EDUCATION ── */
.edu-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1px; background:var(--rule); border-radius:4px; overflow:hidden; margin-bottom:2rem; }
.edu-card { background:var(--ink-soft); padding:2rem; }
.edu-icon { font-size:1.5rem; margin-bottom:1rem; }
.edu-degree { font-family:var(--serif); font-size:1.1rem; color:var(--text); margin-bottom:0.25rem; }
.edu-school { font-size:0.78rem; letter-spacing:0.08em; color:var(--muted); text-transform:uppercase; }

/* ── CONTACT ── */
.contact-footer {
    background: var(--ink-soft);
    border:1px solid var(--rule);
    border-radius:4px;
    padding:4rem;
    text-align:center;
    margin-bottom:4rem;
    position:relative; overflow:hidden;
}
.contact-footer::before {
    content:'';
    position:absolute; top:0; left:50%; transform:translateX(-50%);
    width:60%; height:1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}
.contact-headline {
    font-family:var(--serif);
    font-size:clamp(1.75rem, 3vw, 2.75rem);
    color:var(--text); font-weight:400;
    margin-bottom:0.75rem;
}
.contact-sub { font-size:0.95rem; color:var(--text-dim); font-weight:300; margin-bottom:2.5rem; }
.contact-links { display:flex; justify-content:center; gap:2rem; flex-wrap:wrap; margin-bottom:2.5rem; }
.contact-links a {
    font-size:0.78rem; letter-spacing:0.1em; text-transform:uppercase;
    color:var(--text-dim); text-decoration:none;
    transition:color 0.2s;
}
.contact-links a:hover { color:var(--gold); }
.copyright { font-size:0.7rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--muted); }

/* ── RESPONSIVE ── */
@media (max-width:960px) {
    .page { padding:100px 1.5rem 0; }
    .hero-wrap { grid-template-columns:1fr; gap:2rem; text-align:center; }
    .hero-photo-ring { margin:0 auto; }
    .hero-kpis { justify-content:center; }
    .hero-actions { justify-content:center; }
    .impact-strip { grid-template-columns:repeat(2,1fr); }
    .impact-cell:nth-child(2) { border-right:none; }
    .impact-cell:nth-child(3) { border-top:1px solid var(--rule); }
    .method-trio { grid-template-columns:1fr; }
    .projects-grid { grid-template-columns:1fr; }
    .stack-section { grid-template-columns:1fr; }
    .lab-grid { grid-template-columns:1fr; }
    .edu-grid { grid-template-columns:1fr; }
    .contact-footer { padding:2.5rem 1.5rem; }
    .timeline::before { left:80px; }
    .tl-item { grid-template-columns:80px 1fr; gap:1.5rem; }
    .tl-item::before { left:75px; }
    .navbar-inner { padding:0 1.5rem; }
    .navbar-nav { gap:1.5rem; }
}
@media (max-width:600px) {
    .navbar-nav { display:none; }
    .impact-strip { grid-template-columns:1fr 1fr; }
    .projects-grid { grid-template-columns:1fr; }
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# NAVBAR
# ------------------------------------------------------------------------------
st.markdown("""
<nav class="navbar">
  <div class="navbar-inner">
    <a href="#inicio" class="navbar-logo">Raphael Pires</a>
    <div class="navbar-nav">
      <a href="#sobre">Sobre</a>
      <a href="#trajetoria">Trajetória</a>
      <a href="#cases">Cases</a>
      <a href="#stack">Stack</a>
      <a href="#contato">Contato</a>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# PAGE WRAPPER
# ------------------------------------------------------------------------------
st.markdown('<div class="page">', unsafe_allow_html=True)
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)

# ==============================================================================
# HERO
# ==============================================================================
if profile_base64:
    photo_html = f'<img src="data:image/jpeg;base64,{profile_base64}" alt="Raphael Pires">'
else:
    photo_html = '<span>👤</span>'

st.markdown(f"""
<div class="hero-wrap">
  <div>
    <div class="hero-photo-ring">
      <div class="hero-photo-inner">{photo_html}</div>
    </div>
  </div>
  <div>
    <div class="hero-eyebrow">Dados · Automação · Inteligência Operacional</div>
    <h1 class="hero-name">Raphael <em>Pires</em></h1>
    <p class="hero-tagline">
      +15 anos transformando operações reais em inteligência acionável.
      Da automação bancária à gestão de negócio próprio — dados não são teoria, são decisão.
    </p>
    <div class="hero-kpis">
      <div>
        <span class="hero-kpi-val">15+</span>
        <span class="hero-kpi-lbl">Anos de operação</span>
      </div>
      <div>
        <span class="hero-kpi-val">−70%</span>
        <span class="hero-kpi-lbl">Redução operacional</span>
      </div>
      <div>
        <span class="hero-kpi-val">213k</span>
        <span class="hero-kpi-lbl">Registros processados</span>
      </div>
      <div>
        <span class="hero-kpi-val">4+</span>
        <span class="hero-kpi-lbl">Dashboards ativos</span>
      </div>
    </div>
    <div class="hero-actions">
      <a href="#contato" class="btn-gold">✉ Vamos conversar</a>
      <a href="#cases" class="btn-ghost">→ Ver cases</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# IMPACTO STRIP
# ==============================================================================
st.markdown("""
<div class="impact-strip">
  <div class="impact-cell">
    <span class="impact-num">2h→15'</span>
    <span class="impact-lbl">Ciclo de análise reduzido</span>
  </div>
  <div class="impact-cell">
    <span class="impact-num">20</span>
    <span class="impact-lbl">Agências automatizadas</span>
  </div>
  <div class="impact-cell">
    <span class="impact-num">R$1,2bi</span>
    <span class="impact-lbl">Volume de dados analisado</span>
  </div>
  <div class="impact-cell">
    <span class="impact-num">100%</span>
    <span class="impact-lbl">Remoto / Híbrido</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# SOBRE / METODOLOGIA
# ==============================================================================
st.markdown('<div id="sobre" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Metodologia</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Como penso dados</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="method-trio">
  <div class="method-card">
    <span class="method-icon">🔍</span>
    <div class="method-title">Entendo a operação</div>
    <p class="method-desc">Antes de qualquer SQL, entendo o fluxo real. Números só fazem sentido com contexto operacional.</p>
  </div>
  <div class="method-card">
    <span class="method-icon">⚙️</span>
    <div class="method-title">Automatizo o repetitivo</div>
    <p class="method-desc">Planilha que abre em 14 minutos não é dado — é sofrimento. Crio pipelines que entregam análise limpa e rápida.</p>
  </div>
  <div class="method-card">
    <span class="method-icon">📊</span>
    <div class="method-title">Traduzo para decisão</div>
    <p class="method-desc">Gráfico bonito não aprova orçamento. Insight claro e acionável sim. Foco total no que muda o próximo passo.</p>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

# ==============================================================================
# EXPERIÊNCIA
# ==============================================================================
st.markdown('<div id="trajetoria" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Trajetória</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Experiência profissional</h2>', unsafe_allow_html=True)

experiences = [
    {
        "year": "2014 – 2026",
        "role": "Analista de KPIs & Operações",
        "company": "J Sintonía",
        "items": ["Monitoramento contínuo de vendas, margem e giro de estoque", "Relatórios automatizados com Python e SQL", "Estruturação de indicadores operacionais"]
    },
    {
        "year": "2009 – presente",
        "role": "Gestão Comercial & Dados",
        "company": "Jardim do Éden",
        "items": ["Redução do ciclo de análise de 2h para 15 minutos", "Automação completa com Python e IA generativa", "Arquitetura do fluxo analítico do negócio"]
    },
    {
        "year": "2008 – 2010",
        "role": "Estagiário — Automação & Dados",
        "company": "Banco do Brasil",
        "items": ["Automação VBA implantada em 20 agências", "Redução de 70% no tempo operacional", "Consolidação de relatórios de múltiplas unidades"]
    },
    {
        "year": "2002 – 2009",
        "role": "Suporte Operacional",
        "company": "NSM Comércio",
        "items": ["Centralização de dados de 7 unidades", "Controle de estoque e indicadores comerciais"]
    }
]

st.markdown('<div class="timeline">', unsafe_allow_html=True)
for exp in experiences:
    details_html = ''.join([f'<div class="tl-detail">{d}</div>' for d in exp['items']])
    st.markdown(f"""
    <div class="tl-item">
      <div class="tl-year">{exp['year']}</div>
      <div>
        <div class="tl-role">{exp['role']}</div>
        <div class="tl-company">{exp['company']}</div>
        {details_html}
      </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

# ==============================================================================
# CASES
# ==============================================================================
st.markdown('<div id="cases" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Portfolio</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Cases em destaque</h2>', unsafe_allow_html=True)

projects = [
    {
        "num": "01",
        "icon": "📊",
        "title": "Desenrola Brasil",
        "desc": "Dashboard analítico com dados abertos do Banco Central — visualização de R$50 bilhões em renegociações de dívida por perfil, faixa e modalidade.",
        "metric": "R$ 50B em dados visualizados",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app": "https://desenrolabrasil.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/DESENROLA_BRASIL"
    },
    {
        "num": "02",
        "icon": "🎓",
        "title": "CNPq Analytics",
        "desc": "Análise de 213 mil bolsas científicas, representando R$1,2 bilhão em fomento à pesquisa no Brasil. Exploração por área, instituição e distribuição geográfica.",
        "metric": "213.735 bolsas · R$1,2bi",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app": "https://cnpq-analytics.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/CNPq-Analytics"
    },
    {
        "num": "03",
        "icon": "⚡",
        "title": "Portfólio Premium",
        "desc": "Produto pessoal desenvolvido do zero — design system editorial, tema dark refinado, tipografia expressiva, responsividade completa e foco em conversão.",
        "metric": "100% design customizado",
        "tech": ["Streamlit", "Python", "CSS3"],
        "app": None,
        "code": "https://github.com/raphaelcaxias/curriculo"
    }
]

st.markdown('<div class="projects-grid">', unsafe_allow_html=True)
for proj in projects:
    tags_html = ''.join([f'<span class="tag">{t}</span>' for t in proj['tech']])
    app_link = f'<a href="{proj["app"]}" target="_blank">↗ App ao vivo</a>' if proj['app'] else ''
    code_link = f'<a href="{proj["code"]}" target="_blank">↗ Código</a>'

    st.markdown(f"""
    <div class="proj-card">
      <div class="proj-number">{proj['num']}</div>
      <div class="proj-icon">{proj['icon']}</div>
      <div class="proj-title">{proj['title']}</div>
      <p class="proj-desc">{proj['desc']}</p>
      <div class="proj-metric">{proj['metric']}</div>
      <div class="proj-tags">{tags_html}</div>
      <div class="proj-links">{app_link} {code_link}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

# ==============================================================================
# STACK
# ==============================================================================
st.markdown('<div id="stack" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Tecnologias</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Stack técnica</h2>', unsafe_allow_html=True)

stack = {
    "Dados & ETL": ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy"],
    "BI & Visualização": ["Power BI", "Looker Studio", "Plotly", "Streamlit"],
    "Análise & Indicadores": ["KPIs", "Dashboards", "ETL", "Data Modeling"],
    "Automação & Ferramentas": ["Excel / VBA", "Git", "IA Generativa", "CSS / Design"]
}

st.markdown('<div class="stack-section">', unsafe_allow_html=True)
for cat, items in stack.items():
    pills = ''.join([f'<span class="pill">{item}</span>' for item in items])
    st.markdown(f"""
    <div class="stack-block">
      <div class="stack-cat">{cat}</div>
      <div class="stack-pills">{pills}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

# ==============================================================================
# LAB
# ==============================================================================
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Em construção</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Laboratório</h2>', unsafe_allow_html=True)

lab = [
    ("⚡", "Portfólio Premium", "Concluído"),
    ("🤖", "IA para relatórios automáticos", "Em desenvolvimento"),
    ("📈", "Dashboard de fluxo de caixa", "Prototipado")
]

st.markdown('<div class="lab-grid">', unsafe_allow_html=True)
for icon, title, status in lab:
    st.markdown(f"""
    <div class="lab-card">
      <div class="lab-card-icon">{icon}</div>
      <div class="lab-card-title">{title}</div>
      <div class="lab-status">{status}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

# ==============================================================================
# FORMAÇÃO
# ==============================================================================
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Educação</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Formação & Certificações</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="edu-grid">
  <div class="edu-card">
    <div class="edu-icon">🎓</div>
    <div class="edu-degree">Sistemas de Informação</div>
    <div class="edu-school">UniFOA · 2010</div>
    <br>
    <div class="edu-degree">Técnico em Informática</div>
    <div class="edu-school">CIBA · 2005</div>
  </div>
  <div class="edu-card">
    <div class="edu-icon">📜</div>
    <div class="edu-degree">Certificações Hashtag Treinamentos</div>
    <div class="edu-school" style="margin-top:0.75rem;">SQL avançado · Power BI · Python para dados · IA aplicada a negócios</div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# CONTATO
# ==============================================================================
st.markdown('<div id="contato" class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="contact-footer">
  <h3 class="contact-headline">Transformando dados em decisão</h3>
  <p class="contact-sub">Disponível para trabalho remoto ou híbrido · Aberto a novas oportunidades</p>
  <div class="contact-links">
    <a href="mailto:raphael_caxias@hotmail.com">✉ raphael_caxias@hotmail.com</a>
    <a href="tel:+5524992275226">📱 (24) 99227-5226</a>
    <a href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">LinkedIn ↗</a>
    <a href="https://github.com/raphaelcaxias" target="_blank">GitHub ↗</a>
  </div>
  <div class="copyright">© 2026 Raphael Pires · Dados com propósito</div>
</div>
""", unsafe_allow_html=True)

if cv_pdf:
    st.download_button(
        "↓  Baixar currículo (PDF)",
        data=cv_pdf,
        file_name="Raphael_Pires_Curriculo.pdf",
        mime="application/pdf"
    )

st.markdown('</div>', unsafe_allow_html=True)

# Close page wrapper
st.markdown('</div>', unsafe_allow_html=True)
