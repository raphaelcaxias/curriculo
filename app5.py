# -*- coding: utf-8 -*-
"""
Portfolio Premium — Raphael Pires
Versão: 7.0 — Dark/Light toggle, gráficos, sem erros de formatação
"""

import streamlit as st
from PIL import Image
import os
import requests
from io import BytesIO
import base64
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Raphael Pires — Dados & Automação",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# UTILS
# ─────────────────────────────────────────────
def hex_rgba(hex_color: str, alpha: float) -> str:
    """Converte cor hex (#RRGGBB) + alpha float para rgba()"""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

# ─────────────────────────────────────────────
# THEME STATE
# ─────────────────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# ─────────────────────────────────────────────
# IMAGEM E PDF
# ─────────────────────────────────────────────
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
        buf = BytesIO()
        img.save(buf, format="JPEG")
        return base64.b64encode(buf.getvalue()).decode()
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

profile_image  = load_image()
profile_base64 = get_image_base64(profile_image) if profile_image else None
cv_pdf         = load_cv()

# ─────────────────────────────────────────────
# TOKENS DE COR POR TEMA
# ─────────────────────────────────────────────
dark = {
    "bg":         "#0A0A0B",
    "surface":    "#141418",
    "surface2":   "#1E1E24",
    "border":     "#2A2A32",
    "text":       "#EAEAF0",
    "text_dim":   "#9898A8",
    "text_muted": "#5A5A68",
    "gold":       "#C9A84C",
    "gold_light": "#E8C877",
    "gold_dim":   "#4A3A18",
    "teal":       "#2DD4BF",
    "plot_bg":    "#141418",
    "plot_paper": "#141418",
    "plot_grid":  "#2A2A32",
    "plot_font":  "#9898A8",
}
light = {
    "bg":         "#F7F5F0",
    "surface":    "#FFFFFF",
    "surface2":   "#F0EDE6",
    "border":     "#D8D4C8",
    "text":       "#1A1A1E",
    "text_dim":   "#5A5A68",
    "text_muted": "#9898A8",
    "gold":       "#A07830",
    "gold_light": "#C9A84C",
    "gold_dim":   "#F0E4C8",
    "teal":       "#0F766E",
    "plot_bg":    "#FFFFFF",
    "plot_paper": "#F7F5F0",
    "plot_grid":  "#E8E4DC",
    "plot_font":  "#5A5A68",
}

T = dark if st.session_state.dark_mode else light

# ─────────────────────────────────────────────
# CSS DINÂMICO
# ─────────────────────────────────────────────
# Fonts + CSS — split into chunks to avoid Streamlit truncation
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# CSS chunk 1/4
st.markdown(f"""<style>

* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, .stApp {{
    background:{T['bg']} !important;
    font-family:'Inter',system-ui,sans-serif;
    color:{T['text']};
    -webkit-font-smoothing:antialiased;
}}
#MainMenu,footer,header,.stDeployButton,[data-testid="stToolbar"]{{ display:none !important; }}
.block-container {{ padding:0 !important; max-width:100% !important; }}
.stDownloadButton > button {{
    background:{T['gold']};
    color:{T['bg']};
    border:none;
    border-radius:3px;
    font-size:0.8rem;
    font-weight:500;
    letter-spacing:0.08em;
    padding:0.65rem 1.5rem;
    cursor:pointer;
}}
.stDownloadButton > button:hover {{ background:{T['gold_light']}; }}


</style>""", unsafe_allow_html=True)

# CSS chunk 2/4
st.markdown(f"""<style>
/* scrollbar */
::-webkit-scrollbar {{ width:4px; }}
::-webkit-scrollbar-track {{ background:{T['bg']}; }}
::-webkit-scrollbar-thumb {{ background:{T['gold_dim']}; border-radius:2px; }}

/* NAVBAR */
.rp-nav {{
    position:fixed; top:0; left:0; width:100%;
    background:{hex_rgba(T['bg'], 0.93)};
    backdrop-filter:blur(14px);
    border-bottom:1px solid {T['border']};
    z-index:1000;
    height:64px;
    display:flex; align-items:center;
}}
.rp-nav-inner {{
    max-width:1200px; margin:0 auto; width:100%;
    padding:0 2.5rem;
    display:flex; align-items:center; justify-content:space-between;
}}
.rp-logo {{
    font-family:'Playfair Display',serif;
    font-size:1.25rem; color:{T['gold']};
    text-decoration:none; letter-spacing:0.02em;
}}
.rp-nav-links {{ display:flex; gap:2rem; align-items:center; }}
.rp-nav-links a {{
    font-size:0.72rem; letter-spacing:0.14em; text-transform:uppercase;
    color:{T['text_dim']}; text-decoration:none;
    transition:color 0.2s;
}}
.rp-nav-links a:hover {{ color:{T['gold']}; }}

/* PAGE */
.rp-page {{ max-width:1200px; margin:0 auto; padding:88px 2.5rem 4rem; }}

/* SECTION */
.rp-section {{ margin-bottom:6rem; scroll-margin-top:80px; }}
.rp-eyebrow {{
    font-size:0.68rem; letter-spacing:0.22em; text-transform:uppercase;
    color:{T['gold']}; margin-bottom:0.75rem;
    display:flex; align-items:center; gap:0.75rem;
}}
.rp-eyebrow::before {{
    content:'';
    display:inline-block; width:20px; height:1px;
    background:{T['gold']};
}}
.rp-h2 {{
    font-family:'Playfair Display',serif;
    font-size:clamp(1.9rem,3.5vw,3rem);
    font-weight:400; color:{T['text']};
    line-height:1.15; margin-bottom:2.5rem;
    letter-spacing:-0.01em;
}}
.rp-rule {{
    border:none;
    border-top:1px solid {T['border']};
    margin:5rem 0;
}}

/* HERO */
.rp-hero {{
    display:grid;
    grid-template-columns:220px 1fr;
    gap:4rem; align-items:center;
    padding:3rem 0 5rem;
}}
.rp-photo-wrap {{
    width:220px; height:220px;
    border-radius:50%;
    padding:3px;
    background:linear-gradient(135deg,{T['gold']},{T['gold_dim']});
    flex-shrink:0;
}}
.rp-photo-inner {{
    width:100%; height:100%;
    border-radius:50%; overflow:hidden;
    background:{T['surface2']};
    display:flex; align-items:center; justify-content:center;
    font-size:4rem;
}}
.rp-photo-inner img {{ width:100%; height:100%; object-fit:cover; display:block; }}
.rp-hero-eyebrow {{
    font-size:0.7rem; letter-spacing:0.2em; text-transform:uppercase;
    color:{T['gold']}; margin-bottom:1rem;
}}
.rp-hero-name {{
    font-family:'Playfair Display',serif;
    font-size:clamp(2.8rem,5vw,4.5rem);
    font-weight:400; line-height:1; color:{T['text']};
    margin-bottom:0.4rem; letter-spacing:-0.02em;
}}
.rp-hero-name em {{ font-style:italic; color:{T['gold']}; }}
.rp-hero-subtitle {{
    font-size:1.05rem; font-weight:300;
    color:{T['text_dim']}; line-height:1.7;
    max-width:520px; margin-bottom:2rem;
}}
.rp-hero-pitch {{
    font-size:0.9rem; font-weight:400;
    color:{T['text_dim']}; line-height:1.8;
    max-width:560px; margin-bottom:2.5rem;
    padding-left:1rem;
    border-left:2px solid {T['gold']};
}}
.rp-kpis {{ display:flex; gap:3rem; margin-bottom:2.5rem; flex-wrap:wrap; }}
.rp-kpi-val {{
    display:block;
    font-family:'Playfair Display',serif;
    font-size:2.2rem; color:{T['gold']};
    line-height:1;
}}
.rp-kpi-lbl {{
    display:block; font-size:0.66rem;
    letter-spacing:0.14em; text-transform:uppercase;
    color:{T['text_muted']}; margin-top:0.3rem;
}}
.rp-actions {{ display:flex; gap:1rem; flex-wrap:wrap; }}
.rp-btn-primary {{
    display:inline-flex; align-items:center; gap:0.5rem;
    background:{T['gold']}; color:{T['bg']} !important;
    font-size:0.75rem; font-weight:500;
    letter-spacing:0.1em; text-transform:uppercase;
    padding:0.7rem 1.6rem; border-radius:2px;
    text-decoration:none; transition:background 0.2s,transform 0.2s;
}}
.rp-btn-primary:hover {{ background:{T['gold_light']}; transform:translateY(-2px); }}
.rp-btn-ghost {{
    display:inline-flex; align-items:center; gap:0.5rem;
    background:transparent; color:{T['text_dim']} !important;
    font-size:0.75rem; font-weight:400;
    letter-spacing:0.1em; text-transform:uppercase;
    padding:0.7rem 1.6rem; border-radius:2px;
    border:1px solid {T['border']};
    text-decoration:none; transition:border-color 0.2s,color 0.2s,transform 0.2s;
}}
.rp-btn-ghost:hover {{ border-color:{T['gold']}; color:{T['gold']} !important; transform:translateY(-2px); }}


</style>""", unsafe_allow_html=True)

# CSS chunk 3/4
st.markdown(f"""<style>
/* IMPACT STRIP */
.rp-strip {{
    display:grid; grid-template-columns:repeat(4,1fr);
    border:1px solid {T['border']}; border-radius:4px;
    overflow:hidden; margin-bottom:5rem;
}}
.rp-strip-cell {{
    padding:2rem 1.5rem;
    border-right:1px solid {T['border']};
    transition:background 0.2s;
}}
.rp-strip-cell:last-child {{ border-right:none; }}
.rp-strip-cell:hover {{ background:{T['surface']}; }}
.rp-strip-num {{
    font-family:'Playfair Display',serif;
    font-size:2.6rem; color:{T['gold']};
    display:block; line-height:1; margin-bottom:0.5rem;
}}
.rp-strip-lbl {{
    font-size:0.7rem; letter-spacing:0.12em; text-transform:uppercase;
    color:{T['text_muted']};
}}

/* METHOD */
.rp-method-grid {{
    display:grid; grid-template-columns:repeat(3,1fr);
    gap:1px; background:{T['border']};
    border-radius:4px; overflow:hidden;
}}
.rp-method-card {{
    background:{T['surface']};
    padding:2.5rem 2rem;
    transition:background 0.25s;
}}
.rp-method-card:hover {{ background:{T['surface2']}; }}
.rp-method-icon {{ font-size:1.75rem; margin-bottom:1.25rem; }}
.rp-method-title {{
    font-family:'Playfair Display',serif;
    font-size:1.2rem; color:{T['text']};
    margin-bottom:0.75rem;
}}
.rp-method-desc {{
    font-size:0.85rem; color:{T['text_dim']};
    line-height:1.75; font-weight:300;
}}

/* TIMELINE */
.rp-timeline {{ position:relative; padding-left:0; }}
.rp-tl-item {{
    display:grid; grid-template-columns:160px 32px 1fr;
    gap:0; margin-bottom:0; position:relative;
}}
.rp-tl-yr {{
    font-size:0.72rem; letter-spacing:0.06em;
    color:{T['text_muted']}; text-align:right;
    padding:4px 1.5rem 0 0; line-height:1.4;
}}
.rp-tl-spine {{
    display:flex; flex-direction:column; align-items:center;
}}
.rp-tl-dot {{
    width:10px; height:10px; border-radius:50%;
    background:{T['bg']}; border:2px solid {T['gold']};
    flex-shrink:0; margin-top:4px;
}}
.rp-tl-line {{
    flex:1; width:1px;
    background:{T['border']};
    min-height:40px;
}}
.rp-tl-body {{ padding:0 0 3rem 1.5rem; }}
.rp-tl-role {{
    font-family:'Playfair Display',serif;
    font-size:1.15rem; color:{T['text']}; margin-bottom:0.2rem;
}}
.rp-tl-company {{
    font-size:0.75rem; letter-spacing:0.1em; text-transform:uppercase;
    color:{T['gold']}; margin-bottom:0.75rem;
}}
.rp-tl-detail {{
    font-size:0.83rem; color:{T['text_dim']}; font-weight:300;
    line-height:1.75; margin-bottom:0.3rem;
    padding-left:0.75rem; border-left:1px solid {T['gold_dim']};
}}

/* PROJECTS */
.rp-proj-grid {{
    display:grid; grid-template-columns:repeat(3,1fr);
    gap:1px; background:{T['border']};
    border-radius:4px; overflow:hidden;
}}
.rp-proj-card {{
    background:{T['surface']};
    padding:2rem 1.75rem;
    display:flex; flex-direction:column;
    position:relative; overflow:hidden;
    transition:background 0.25s;
}}
.rp-proj-card:hover {{ background:{T['surface2']}; }}
.rp-proj-card::after {{
    content:''; position:absolute;
    bottom:0; left:0; right:0; height:2px;
    background:{T['gold']};
    transform:scaleX(0); transform-origin:left;
    transition:transform 0.35s ease;
}}
.rp-proj-card:hover::after {{ transform:scaleX(1); }}
.rp-proj-num {{
    font-family:'Playfair Display',serif;
    font-size:3rem; color:{T['border']};
    line-height:1; margin-bottom:1rem;
}}
.rp-proj-icon {{ font-size:1.75rem; margin-bottom:0.75rem; }}
.rp-proj-title {{
    font-family:'Playfair Display',serif;
    font-size:1.2rem; color:{T['text']};
    margin-bottom:0.65rem; line-height:1.25;
}}
.rp-proj-desc {{
    font-size:0.83rem; color:{T['text_dim']};
    line-height:1.75; font-weight:300;
    flex:1; margin-bottom:1.25rem;
}}
.rp-proj-metric {{
    font-size:0.68rem; letter-spacing:0.14em; text-transform:uppercase;
    color:{T['gold']}; margin-bottom:1rem;
}}
.rp-proj-tags {{ display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1.25rem; }}
.rp-tag {{
    font-size:0.63rem; letter-spacing:0.1em; text-transform:uppercase;
    padding:0.28rem 0.65rem; border-radius:1px;
    border:1px solid {T['border']}; color:{T['text_muted']};
}}
.rp-proj-links {{ display:flex; gap:1.25rem; }}
.rp-proj-links a {{
    font-size:0.7rem; letter-spacing:0.1em; text-transform:uppercase;
    color:{T['text_muted']}; text-decoration:none;
    transition:color 0.2s;
}}
.rp-proj-links a:hover {{ color:{T['gold']}; }}


</style>""", unsafe_allow_html=True)

# CSS chunk 4/4
st.markdown(f"""<style>
/* STACK */
.rp-stack-grid {{
    display:grid; grid-template-columns:repeat(2,1fr); gap:2rem;
}}
.rp-stack-cat {{
    font-size:0.68rem; letter-spacing:0.2em; text-transform:uppercase;
    color:{T['gold']}; margin-bottom:1rem;
    display:flex; align-items:center; gap:0.75rem;
}}
.rp-stack-cat::after {{
    content:''; flex:1; height:1px; background:{T['border']};
}}
.rp-pills {{ display:flex; flex-wrap:wrap; gap:0.5rem; }}
.rp-pill {{
    font-size:0.8rem; font-weight:300;
    padding:0.4rem 0.9rem; border-radius:2px;
    border:1px solid {T['border']}; color:{T['text_dim']};
    transition:border-color 0.2s,color 0.2s,background 0.2s;
    cursor:default;
}}
.rp-pill:hover {{
    border-color:{T['gold']};
    color:{T['gold']};
    background:rgba(74,58,24,0.2);
}}

/* LAB */
.rp-lab-grid {{
    display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem;
}}
.rp-lab-card {{
    padding:1.75rem; border:1px solid {T['border']};
    border-radius:4px;
    transition:border-color 0.25s, transform 0.25s;
}}
.rp-lab-card:hover {{
    border-color:{T['gold_dim']};
    transform:translateY(-4px);
}}
.rp-lab-icon {{ font-size:1.5rem; margin-bottom:0.75rem; }}
.rp-lab-title {{
    font-family:'Playfair Display',serif;
    font-size:1.05rem; color:{T['text']}; margin-bottom:0.35rem;
}}
.rp-lab-status {{
    font-size:0.65rem; letter-spacing:0.14em; text-transform:uppercase;
    color:{T['gold']};
}}

/* EDU */
.rp-edu-grid {{
    display:grid; grid-template-columns:repeat(2,1fr);
    gap:1px; background:{T['border']};
    border-radius:4px; overflow:hidden;
}}
.rp-edu-card {{
    background:{T['surface']};
    padding:2rem;
}}
.rp-edu-icon {{ font-size:1.5rem; margin-bottom:1rem; }}
.rp-edu-degree {{
    font-family:'Playfair Display',serif;
    font-size:1.05rem; color:{T['text']};
    margin-bottom:0.25rem;
}}
.rp-edu-school {{
    font-size:0.72rem; letter-spacing:0.08em; text-transform:uppercase;
    color:{T['text_muted']};
}}

/* CONTACT */
.rp-contact {{
    background:{T['surface']};
    border:1px solid {T['border']};
    border-radius:4px; padding:4rem 3rem;
    text-align:center; position:relative; overflow:hidden;
}}
.rp-contact::before {{
    content:''; position:absolute;
    top:0; left:25%; right:25%; height:1px;
    background:linear-gradient(90deg,transparent,{T['gold']},transparent);
}}
.rp-contact-headline {{
    font-family:'Playfair Display',serif;
    font-size:clamp(1.8rem,3vw,2.75rem);
    font-weight:400; color:{T['text']};
    margin-bottom:0.75rem; line-height:1.2;
}}
.rp-contact-sub {{
    font-size:0.9rem; color:{T['text_dim']};
    font-weight:300; margin-bottom:2.5rem;
    max-width:480px; margin-left:auto; margin-right:auto;
    line-height:1.7;
}}
.rp-contact-links {{
    display:flex; justify-content:center;
    gap:2.5rem; flex-wrap:wrap; margin-bottom:2.5rem;
}}
.rp-contact-links a {{
    font-size:0.75rem; letter-spacing:0.1em; text-transform:uppercase;
    color:{T['text_dim']}; text-decoration:none;
    transition:color 0.2s;
}}
.rp-contact-links a:hover {{ color:{T['gold']}; }}
.rp-copy {{
    font-size:0.68rem; letter-spacing:0.1em; text-transform:uppercase;
    color:{T['text_muted']};
}}

/* RESPONSIVE */
@media(max-width:900px) {{
    .rp-page {{ padding:80px 1.25rem 3rem; }}
    .rp-hero {{ grid-template-columns:1fr; gap:2rem; text-align:center; }}
    .rp-photo-wrap {{ margin:0 auto; }}
    .rp-kpis {{ justify-content:center; }}
    .rp-actions {{ justify-content:center; }}
    .rp-hero-pitch {{ text-align:left; }}
    .rp-strip {{ grid-template-columns:repeat(2,1fr); }}
    .rp-strip-cell:nth-child(2) {{ border-right:none; }}
    .rp-strip-cell:nth-child(3),
    .rp-strip-cell:nth-child(4) {{ border-top:1px solid {T['border']}; }}
    .rp-method-grid {{ grid-template-columns:1fr; }}
    .rp-proj-grid {{ grid-template-columns:1fr; }}
    .rp-stack-grid {{ grid-template-columns:1fr; }}
    .rp-lab-grid {{ grid-template-columns:1fr; }}
    .rp-edu-grid {{ grid-template-columns:1fr; }}
    .rp-contact {{ padding:2.5rem 1.5rem; }}
    .rp-tl-item {{ grid-template-columns:100px 24px 1fr; }}
}}
@media(max-width:600px) {{
    .rp-nav-links a:not(:first-child):not(:last-child) {{ display:none; }}
    .rp-strip {{ grid-template-columns:1fr 1fr; }}
    .rp-tl-item {{ grid-template-columns:80px 20px 1fr; }}
}}

</style>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# NAVBAR  (toggle via Streamlit button inline)
# ─────────────────────────────────────────────
nav_col1, nav_col2 = st.columns([6, 1])
with nav_col1:
    st.markdown(f"""
    <nav class="rp-nav">
      <div class="rp-nav-inner">
        <a href="#inicio" class="rp-logo">Raphael Pires</a>
        <div class="rp-nav-links">
          <a href="#sobre">Sobre</a>
          <a href="#trajetoria">Trajetória</a>
          <a href="#cases">Cases</a>
          <a href="#stack">Stack</a>
          <a href="#contato">Contato</a>
        </div>
      </div>
    </nav>
    """, unsafe_allow_html=True)

# Toggle de tema no topo da página (após a navbar)
st.markdown('<div class="rp-page">', unsafe_allow_html=True)

theme_label = "☀️ Modo claro" if st.session_state.dark_mode else "🌙 Modo escuro"
col_t1, col_t2 = st.columns([10, 1])
with col_t2:
    if st.button(theme_label, key="theme_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)

if profile_base64:
    photo_html = f'<img src="data:image/jpeg;base64,{profile_base64}" alt="Raphael Pires">'
else:
    photo_html = '<span style="font-size:4rem">👤</span>'

st.markdown(f"""
<div class="rp-hero">
  <div>
    <div class="rp-photo-wrap">
      <div class="rp-photo-inner">{photo_html}</div>
    </div>
  </div>
  <div>
    <div class="rp-hero-eyebrow">Dados · Automação · Inteligência Operacional</div>
    <h1 class="rp-hero-name">Raphael <em>Pires</em></h1>
    <p class="rp-hero-subtitle">
      Analista de Dados & Automação com +15 anos transformando operações reais em vantagem competitiva.
    </p>
    <p class="rp-hero-pitch">
      Enquanto a maioria analisa planilhas, eu construo sistemas que<strong style="color:{T['gold']}"> eliminam o trabalho manual</strong>,
      reduzem custos operacionais em até 70% e entregam dashboards que gestores realmente usam para tomar decisões.
      Meu diferencial: entendo o negócio antes de abrir o Python.
    </p>
    <div class="rp-kpis">
      <div><span class="rp-kpi-val">15+</span><span class="rp-kpi-lbl">Anos de operação</span></div>
      <div><span class="rp-kpi-val">−70%</span><span class="rp-kpi-lbl">Redução de tempo</span></div>
      <div><span class="rp-kpi-val">213k</span><span class="rp-kpi-lbl">Registros processados</span></div>
      <div><span class="rp-kpi-val">R$1,2B</span><span class="rp-kpi-lbl">Volume analisado</span></div>
    </div>
    <div class="rp-actions">
      <a href="#contato" class="rp-btn-primary">✉ Falar comigo</a>
      <a href="#cases" class="rp-btn-ghost">→ Ver resultados</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# IMPACT STRIP
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="rp-strip">
  <div class="rp-strip-cell">
    <span class="rp-strip-num">2h→15'</span>
    <span class="rp-strip-lbl">Ciclo de análise</span>
  </div>
  <div class="rp-strip-cell">
    <span class="rp-strip-num">20</span>
    <span class="rp-strip-lbl">Agências automatizadas</span>
  </div>
  <div class="rp-strip-cell">
    <span class="rp-strip-num">R$50B</span>
    <span class="rp-strip-lbl">Dados visualizados</span>
  </div>
  <div class="rp-strip-cell">
    <span class="rp-strip-num">100%</span>
    <span class="rp-strip-lbl">Remoto / Híbrido</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# GRÁFICO 1 — Linha do tempo de impacto
# ─────────────────────────────────────────────
st.markdown('<div id="sobre" class="rp-section">', unsafe_allow_html=True)
st.markdown('<div class="rp-eyebrow">Dados que vendem</div>', unsafe_allow_html=True)
st.markdown('<h2 class="rp-h2">Impacto ao longo da carreira</h2>', unsafe_allow_html=True)

df_impact = pd.DataFrame({
    "Ano":    [2005, 2008, 2010, 2014, 2018, 2021, 2024, 2026],
    "Impacto": [10,   35,   55,   60,   70,   80,   90,   97],
    "Marco": [
        "Início em TI",
        "Automação VBA — BB",
        "Graduação SI",
        "Analista KPIs",
        "Dashboards BI",
        "Python + SQL avançado",
        "IA aplicada",
        "Portfólio público"
    ]
})

fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=df_impact["Ano"],
    y=df_impact["Impacto"],
    mode="lines+markers",
    line=dict(color=T["gold"], width=2.5),
    marker=dict(color=T["gold"], size=9, line=dict(color=T["surface"], width=2)),
    fill="tozeroy",
    fillcolor=hex_rgba(T["gold"], 0.09),
    hovertemplate="<b>%{customdata}</b><extra></extra>",
    customdata=df_impact["Marco"]
))
fig1.update_layout(
    height=260,
    paper_bgcolor=T["plot_paper"],
    plot_bgcolor=T["plot_bg"],
    margin=dict(l=0, r=0, t=10, b=40),
    font=dict(family="Inter", color=T["plot_font"], size=11),
    xaxis=dict(
        showgrid=False, zeroline=False,
        tickfont=dict(color=T["plot_font"], size=10),
        linecolor=T["border"]
    ),
    yaxis=dict(
        showgrid=True, gridcolor=T["plot_grid"],
        zeroline=False, ticksuffix="%",
        tickfont=dict(color=T["plot_font"], size=10),
        title=dict(text="Maturidade técnica", font=dict(color=T["text_muted"], size=10))
    ),
    showlegend=False
)

st.plotly_chart(fig1, use_container_width=True, config={"displayModeBar": False})

# ─────────────────────────────────────────────
# GRÁFICO 2 — Radar de competências
# ─────────────────────────────────────────────
categorias = ["Python / ETL", "SQL", "Power BI", "Automação", "Análise de Negócio", "IA Aplicada"]
valores = [90, 88, 85, 92, 95, 78]
valores_full = valores + [valores[0]]
cats_full = categorias + [categorias[0]]

fig2 = go.Figure()
fig2.add_trace(go.Scatterpolar(
    r=valores_full, theta=cats_full,
    fill="toself",
    fillcolor=hex_rgba(T["gold"], 0.13),
    line=dict(color=T["gold"], width=2),
    marker=dict(color=T["gold"], size=7)
))
fig2.update_layout(
    height=320,
    paper_bgcolor=T["plot_paper"],
    plot_bgcolor=T["plot_bg"],
    margin=dict(l=20, r=20, t=20, b=20),
    polar=dict(
        bgcolor=T["plot_bg"],
        radialaxis=dict(
            visible=True, range=[0, 100],
            tickfont=dict(color=T["plot_font"], size=9),
            gridcolor=T["plot_grid"],
            linecolor=T["border"]
        ),
        angularaxis=dict(
            tickfont=dict(color=T["text_dim"], size=10),
            gridcolor=T["plot_grid"],
            linecolor=T["border"]
        )
    ),
    showlegend=False
)

# ─────────────────────────────────────────────
# GRÁFICO 3 — Projetos por tecnologia
# ─────────────────────────────────────────────
techs = ["Python", "SQL", "Streamlit", "Plotly", "Power BI", "VBA"]
usos  = [12, 10, 6, 6, 4, 3]

fig3 = go.Figure(go.Bar(
    x=usos, y=techs,
    orientation="h",
    marker=dict(
        color=usos,
        colorscale=[[0, hex_rgba(T["gold_dim"], 0.55)], [1, T["gold"]]],
        line=dict(width=0)
    ),
    hovertemplate="%{y}: %{x} projetos<extra></extra>"
))
fig3.update_layout(
    height=260,
    paper_bgcolor=T["plot_paper"],
    plot_bgcolor=T["plot_bg"],
    margin=dict(l=0, r=20, t=10, b=20),
    font=dict(family="Inter", color=T["plot_font"], size=11),
    xaxis=dict(
        showgrid=True, gridcolor=T["plot_grid"],
        zeroline=False, tickfont=dict(color=T["plot_font"], size=10)
    ),
    yaxis=dict(
        showgrid=False, tickfont=dict(color=T["text_dim"], size=11)
    ),
    showlegend=False
)

col_r, col_b = st.columns([1, 1], gap="large")
with col_r:
    st.markdown(f'<div style="color:{T["text_muted"]};font-size:0.72rem;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:0.5rem;">Radar de competências</div>', unsafe_allow_html=True)
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
with col_b:
    st.markdown(f'<div style="color:{T["text_muted"]};font-size:0.72rem;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:0.5rem;">Uso por tecnologia</div>', unsafe_allow_html=True)
    st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# METODOLOGIA
# ─────────────────────────────────────────────
st.markdown('<hr class="rp-rule">', unsafe_allow_html=True)
st.markdown('<div class="rp-section">', unsafe_allow_html=True)
st.markdown('<div class="rp-eyebrow">Metodologia</div>', unsafe_allow_html=True)
st.markdown('<h2 class="rp-h2">Como entrego resultado</h2>', unsafe_allow_html=True)

st.markdown(f"""
<div class="rp-method-grid">
  <div class="rp-method-card">
    <div class="rp-method-icon">🔍</div>
    <div class="rp-method-title">1. Entendo o negócio</div>
    <p class="rp-method-desc">
      Nenhum dado existe no vácuo. Antes de qualquer script, mapeio o fluxo operacional real — onde estão as dores, onde estão os pontos cegos e o que realmente importa medir.
    </p>
  </div>
  <div class="rp-method-card">
    <div class="rp-method-icon">⚙️</div>
    <div class="rp-method-title">2. Automatizo o gargalo</div>
    <p class="rp-method-desc">
      Relatório que leva 2 horas é um problema de engenharia, não de Excel. Construo pipelines que transformam entrada de dados em análise pronta — sem intervenção manual.
    </p>
  </div>
  <div class="rp-method-card">
    <div class="rp-method-icon">📊</div>
    <div class="rp-method-title">3. Entrego decisão</div>
    <p class="rp-method-desc">
      Um gráfico bonito que ninguém usa é desperdício. Cada dashboard tem um dono, uma pergunta e uma ação esperada. Dados sem decisão são custo — não investimento.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# EXPERIÊNCIA
# ─────────────────────────────────────────────
st.markdown('<hr class="rp-rule">', unsafe_allow_html=True)
st.markdown('<div id="trajetoria" class="rp-section">', unsafe_allow_html=True)
st.markdown('<div class="rp-eyebrow">Trajetória</div>', unsafe_allow_html=True)
st.markdown('<h2 class="rp-h2">15 anos de operação real</h2>', unsafe_allow_html=True)

experiences = [
    {
        "year": "2014 – 2026",
        "role": "Analista de KPIs & Operações",
        "company": "J Sintonía",
        "items": [
            "Estruturei o sistema de indicadores do zero — vendas, margem, giro e ruptura",
            "Automatizei relatórios semanais que antes consumiam 6h de trabalho manual",
            "Construí dashboards em Power BI e Streamlit usados ativamente pela gestão"
        ]
    },
    {
        "year": "2009 – presente",
        "role": "Gestão Comercial & Dados",
        "company": "Jardim do Éden",
        "items": [
            "Reduzi o ciclo de fechamento analítico de 2 horas para 15 minutos",
            "Implementei automação completa com Python e IA generativa para relatórios",
            "Criei a arquitetura de dados do negócio do zero — da coleta à visualização"
        ]
    },
    {
        "year": "2008 – 2010",
        "role": "Estagiário — Automação & Dados",
        "company": "Banco do Brasil",
        "items": [
            "Desenvolvi macros VBA implantadas em 20 agências simultaneamente",
            "Alcancei 70% de redução no tempo operacional de relatórios de conformidade",
            "Primeira experiência com dados em escala corporativa e processos auditáveis"
        ]
    },
    {
        "year": "2002 – 2009",
        "role": "Suporte Operacional",
        "company": "NSM Comércio",
        "items": [
            "Centralizei dados de 7 unidades em um único sistema de controle",
            "Implementei controle de estoque e indicadores de desempenho por filial"
        ]
    }
]

st.markdown('<div class="rp-timeline">', unsafe_allow_html=True)
for i, exp in enumerate(experiences):
    is_last = (i == len(experiences) - 1)
    details = "".join([f'<div class="rp-tl-detail">{d}</div>' for d in exp["items"]])
    line_html = '' if is_last else '<div class="rp-tl-line"></div>'
    st.markdown(f"""
    <div class="rp-tl-item">
      <div class="rp-tl-yr">{exp['year']}</div>
      <div class="rp-tl-spine">
        <div class="rp-tl-dot"></div>
        {line_html}
      </div>
      <div class="rp-tl-body">
        <div class="rp-tl-role">{exp['role']}</div>
        <div class="rp-tl-company">{exp['company']}</div>
        {details}
      </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CASES
# ─────────────────────────────────────────────
st.markdown('<hr class="rp-rule">', unsafe_allow_html=True)
st.markdown('<div id="cases" class="rp-section">', unsafe_allow_html=True)
st.markdown('<div class="rp-eyebrow">Portfolio</div>', unsafe_allow_html=True)
st.markdown('<h2 class="rp-h2">Cases com resultado mensurável</h2>', unsafe_allow_html=True)

projects = [
    {
        "num": "01", "icon": "📊",
        "title": "Desenrola Brasil",
        "desc": "Dashboard analítico sobre o programa federal de renegociação de dívidas. Visualiza R$50 bilhões em dados abertos do Banco Central por perfil, faixa de renda e modalidade — em tempo real.",
        "metric": "R$ 50 bilhões em dados",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app": "https://desenrolabrasil.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/DESENROLA_BRASIL"
    },
    {
        "num": "02", "icon": "🎓",
        "title": "CNPq Analytics",
        "desc": "Análise completa de 213.735 bolsas científicas, equivalentes a R$1,2 bilhão em fomento. Exploração interativa por área do conhecimento, nível acadêmico, instituição e distribuição geográfica no Brasil.",
        "metric": "213.735 bolsas · R$1,2bi",
        "tech": ["Python", "Pandas", "Plotly", "Streamlit"],
        "app": "https://cnpq-analytics.streamlit.app/",
        "code": "https://github.com/raphaelcaxias/CNPq-Analytics"
    },
    {
        "num": "03", "icon": "⚡",
        "title": "Portfólio Premium",
        "desc": "Produto pessoal construído do zero com design system próprio, tema dark/light, tipografia editorial, gráficos interativos e copy orientado a conversão. Cada linha de CSS foi intencional.",
        "metric": "Design system 100% custom",
        "tech": ["Streamlit", "Python", "Plotly", "CSS3"],
        "app": None,
        "code": "https://github.com/raphaelcaxias/curriculo"
    }
]

st.markdown('<div class="rp-proj-grid">', unsafe_allow_html=True)
for proj in projects:
    tags = "".join([f'<span class="rp-tag">{t}</span>' for t in proj["tech"]])
    app_lnk = f'<a href="{proj["app"]}" target="_blank">↗ App ao vivo</a>' if proj["app"] else ""
    code_lnk = f'<a href="{proj["code"]}" target="_blank">↗ Código</a>'
    st.markdown(f"""
    <div class="rp-proj-card">
      <div class="rp-proj-num">{proj['num']}</div>
      <div class="rp-proj-icon">{proj['icon']}</div>
      <div class="rp-proj-title">{proj['title']}</div>
      <p class="rp-proj-desc">{proj['desc']}</p>
      <div class="rp-proj-metric">{proj['metric']}</div>
      <div class="rp-proj-tags">{tags}</div>
      <div class="rp-proj-links">{app_lnk} {code_lnk}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# STACK
# ─────────────────────────────────────────────
st.markdown('<hr class="rp-rule">', unsafe_allow_html=True)
st.markdown('<div id="stack" class="rp-section">', unsafe_allow_html=True)
st.markdown('<div class="rp-eyebrow">Tecnologias</div>', unsafe_allow_html=True)
st.markdown('<h2 class="rp-h2">Stack técnica</h2>', unsafe_allow_html=True)

stack = {
    "Dados & ETL": ["SQL", "PostgreSQL", "Python", "Pandas", "NumPy"],
    "BI & Visualização": ["Power BI", "Looker Studio", "Plotly", "Streamlit"],
    "Análise & Indicadores": ["KPIs", "Dashboards", "ETL", "Data Modeling"],
    "Automação & Ferramentas": ["Excel / VBA", "Git", "IA Generativa", "CSS Design"]
}

st.markdown('<div class="rp-stack-grid">', unsafe_allow_html=True)
for cat, items in stack.items():
    pills = "".join([f'<span class="rp-pill">{item}</span>' for item in items])
    st.markdown(f"""
    <div>
      <div class="rp-stack-cat">{cat}</div>
      <div class="rp-pills">{pills}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LAB
# ─────────────────────────────────────────────
st.markdown('<hr class="rp-rule">', unsafe_allow_html=True)
st.markdown('<div class="rp-section">', unsafe_allow_html=True)
st.markdown('<div class="rp-eyebrow">Em construção</div>', unsafe_allow_html=True)
st.markdown('<h2 class="rp-h2">Laboratório</h2>', unsafe_allow_html=True)

lab = [
    ("⚡", "Portfólio Premium", "Concluído"),
    ("🤖", "IA para relatórios automáticos", "Em desenvolvimento"),
    ("📈", "Dashboard de fluxo de caixa", "Prototipado")
]

st.markdown('<div class="rp-lab-grid">', unsafe_allow_html=True)
for icon, title, status in lab:
    st.markdown(f"""
    <div class="rp-lab-card">
      <div class="rp-lab-icon">{icon}</div>
      <div class="rp-lab-title">{title}</div>
      <div class="rp-lab-status">{status}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FORMAÇÃO
# ─────────────────────────────────────────────
st.markdown('<hr class="rp-rule">', unsafe_allow_html=True)
st.markdown('<div class="rp-section">', unsafe_allow_html=True)
st.markdown('<div class="rp-eyebrow">Educação</div>', unsafe_allow_html=True)
st.markdown('<h2 class="rp-h2">Formação & Certificações</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="rp-edu-grid">
  <div class="rp-edu-card">
    <div class="rp-edu-icon">🎓</div>
    <div class="rp-edu-degree">Sistemas de Informação</div>
    <div class="rp-edu-school">UniFOA · 2010</div>
    <br>
    <div class="rp-edu-degree">Técnico em Informática</div>
    <div class="rp-edu-school">CIBA · 2005</div>
  </div>
  <div class="rp-edu-card">
    <div class="rp-edu-icon">📜</div>
    <div class="rp-edu-degree">Certificações — Hashtag Treinamentos</div>
    <div class="rp-edu-school" style="margin-top:0.75rem;line-height:2;">
      SQL Avançado &nbsp;·&nbsp; Power BI &nbsp;·&nbsp; Python para Dados &nbsp;·&nbsp; IA Aplicada a Negócios
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONTATO
# ─────────────────────────────────────────────
st.markdown('<div id="contato" class="rp-section">', unsafe_allow_html=True)
st.markdown(f"""
<div class="rp-contact">
  <h3 class="rp-contact-headline">Pronto para transformar dados<br>em resultado para o seu negócio?</h3>
  <p class="rp-contact-sub">
    Disponível para trabalho remoto ou híbrido.<br>
    Respondo em até 24 horas.
  </p>
  <div class="rp-contact-links">
    <a href="mailto:raphael_caxias@hotmail.com">✉ raphael_caxias@hotmail.com</a>
    <a href="tel:+5524992275226">📱 (24) 99227-5226</a>
    <a href="https://linkedin.com/in/raphael-pires-caxias" target="_blank">LinkedIn ↗</a>
    <a href="https://github.com/raphaelcaxias" target="_blank">GitHub ↗</a>
  </div>
  <div class="rp-copy">© 2026 Raphael Pires · Dados com propósito</div>
</div>
""", unsafe_allow_html=True)

if cv_pdf:
    st.download_button(
        "↓  Baixar currículo em PDF",
        data=cv_pdf,
        file_name="Raphael_Pires_Curriculo.pdf",
        mime="application/pdf"
    )

st.markdown('</div>', unsafe_allow_html=True)

# fecha .rp-page
st.markdown('</div>', unsafe_allow_html=True)
