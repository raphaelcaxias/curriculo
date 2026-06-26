import streamlit as st
import os
from config import init_theme, get_colors
from components import render_theme_toggle, render_hero, render_kpis, render_skills_chart, render_footer
from pages.home import render_projects
from pages.analytics import render_analytics_dashboard
from pages.dashboard import render_dashboard

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires | Portfólio Analítico",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# INICIALIZAÇÃO DO TEMA
# ============================================================================
init_theme()

# ============================================================================
# CSS GLOBAL MELHORADO
# ============================================================================
def load_css():
    colors = get_colors()
    st.markdown(f"""
    <style>
        /* Fontes e Reset */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            background: {colors['bg']};
            color: {colors['text']};
        }}
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: {colors['bg']}; }}
        .block-container {{ padding: 2rem 3rem; max-width: 1400px; }}

        /* Hero */
        .hero-section {{ text-align: center; padding: 2rem 0 1rem 0; margin-bottom: 1rem; }}
        .hero-name {{ font-size: 2.8rem; font-weight: 800; color: {colors['text']}; letter-spacing: -0.02em; }}
        .hero-title {{ font-size: 1.1rem; font-weight: 600; color: {colors['primary']}; text-transform: uppercase; letter-spacing: 0.12em; margin-top: 0.2rem; }}
        .hero-subtitle {{ font-size: 1.1rem; color: {colors['text_muted']}; max-width: 700px; margin: 0.8rem auto 1.5rem; line-height: 1.7; }}
        .tech-badge {{
            background: rgba(59,130,246,0.12); border: 1px solid rgba(59,130,246,0.25);
            padding: 0.4rem 1.1rem; border-radius: 999px; font-size: 0.85rem; font-weight: 500;
            color: {colors['text']}; display: inline-block; margin: 0.25rem;
            transition: all 0.2s;
        }}
        .tech-badge:hover {{ background: rgba(59,130,246,0.25); transform: translateY(-2px); }}

        /* Seções */
        .section-header {{ text-align: center; margin: 3rem 0 2rem; }}
        .section-label {{ background: rgba(59,130,246,0.12); padding: 0.3rem 1.2rem; border-radius: 999px; font-size: 0.75rem; font-weight: 600; color: {colors['primary']}; display: inline-block; }}
        .section-title {{ font-size: 2.2rem; font-weight: 700; margin-top: 0.5rem; letter-spacing: -0.01em; }}

        /* KPIs */
        .kpi-box {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 16px;
            padding: 1.5rem 1rem; text-align: center; transition: all 0.25s ease;
            backdrop-filter: blur(2px);
        }}
        .kpi-box:hover {{ transform: translateY(-6px); border-color: {colors['primary']}; box-shadow: 0 12px 32px rgba(59,130,246,0.18); }}
        .kpi-value {{ font-size: 2.3rem; font-weight: 700; color: {colors['primary']}; }}
        .kpi-label {{ font-size: 0.85rem; color: {colors['text_muted']}; }}

        /* Timeline */
        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
            width: 2px; background: linear-gradient(to bottom, {colors['primary']}, {colors['secondary']}, transparent);
        }}
        .timeline-item {{ position: relative; padding-left: 80px; margin-bottom: 2.5rem; }}
        .timeline-dot {{
            position: absolute; left: 20px; top: 6px; width: 16px; height: 16px;
            border-radius: 50%; background: {colors['primary']}; border: 3px solid {colors['bg']};
            box-shadow: 0 0 0 3px {colors['primary']};
        }}
        .timeline-card {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 14px;
            padding: 1.5rem 1.8rem; transition: all 0.25s;
        }}
        .timeline-card:hover {{ border-color: {colors['primary']}; transform: translateX(6px); box-shadow: 0 8px 24px rgba(59,130,246,0.08); }}
        .timeline-date {{ font-size: 0.75rem; font-weight: 600; color: {colors['primary']}; background: rgba(59,130,246,0.12); padding: 0.2rem 0.9rem; border-radius: 999px; display: inline-block; }}
        .timeline-role {{ font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0 0.1rem; }}
        .timeline-company {{ color: {colors['secondary']}; font-weight: 500; font-size: 1.05rem; }}
        .timeline-desc {{ color: {colors['text_muted']}; line-height: 1.6; margin: 0.5rem 0; }}
        .timeline-tag {{
            font-size: 0.7rem; background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.15);
            padding: 0.2rem 0.7rem; border-radius: 6px; color: {colors['text']}; display: inline-block; margin: 0.2rem 0.2rem 0 0;
        }}

        /* Stack */
        .stack-category {{ font-size: 0.95rem; font-weight: 600; color: {colors['primary']}; margin: 1.2rem 0 0.6rem; }}
        .stack-chip {{
            background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.15);
            padding: 0.4rem 1.1rem; border-radius: 10px; font-size: 0.9rem; font-weight: 500;
            color: {colors['text']}; display: inline-block; margin: 0.25rem;
            transition: all 0.2s;
        }}
        .stack-chip:hover {{ background: {colors['primary']}; color: white; transform: translateY(-3px); box-shadow: 0 6px 16px rgba(59,130,246,0.25); }}

        /* Footer */
        .footer {{
            margin-top: 4rem; padding: 2.8rem 2rem; background: {colors['card_bg']};
            border: 1px solid {colors['border']}; border-radius: 20px; text-align: center;
        }}
        .footer-status {{ display: inline-flex; align-items: center; gap: 0.6rem; background: rgba(34,197,94,0.12); border: 1px solid rgba(34,197,94,0.3); padding: 0.4rem 1.2rem; border-radius: 999px; }}
        .footer-status-dot {{ width: 8px; height: 8px; border-radius: 50%; background: #22C55E; box-shadow: 0 0 12px #22C55E; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
        .footer-status-text {{ font-weight: 600; color: #22C55E; }}
        .footer-title {{ font-size: 1.6rem; font-weight: 700; margin: 0.8rem 0 0.3rem; }}
        .footer-subtitle {{ color: {colors['text_muted']}; margin-bottom: 1.5rem; font-size: 1.05rem; }}
        .footer-mode {{ background: rgba(59,130,246,0.06); border: 1px solid rgba(59,130,246,0.1); padding: 0.3rem 0.9rem; border-radius: 999px; font-size: 0.8rem; display: inline-block; margin: 0.2rem; }}
        .footer-link {{
            background: rgba(59,130,246,0.06); border: 1px solid rgba(59,130,246,0.15);
            padding: 0.5rem 1.2rem; border-radius: 10px; color: {colors['text']}; text-decoration: none;
            font-size: 0.9rem; display: inline-block; margin: 0.25rem; transition: all 0.2s;
        }}
        .footer-link:hover {{ background: {colors['primary']}; color: white; transform: translateY(-3px); box-shadow: 0 6px 16px rgba(59,130,246,0.2); }}
        .footer-copy {{ color: {colors['text_muted']}; margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(59,130,246,0.08); font-size: 0.9rem; }}

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{ gap: 0.5rem; background: transparent; flex-wrap: wrap; }}
        .stTabs [data-baseweb="tab"] {{
            background: rgba(59,130,246,0.06); border: 1px solid rgba(59,130,246,0.12);
            border-radius: 10px; padding: 0.6rem 1.4rem; color: {colors['text']}; font-weight: 500;
            transition: all 0.2s;
        }}
        .stTabs [data-baseweb="tab"]:hover {{ background: rgba(59,130,246,0.15); }}
        .stTabs [aria-selected="true"] {{ background: {colors['primary']} !important; color: white !important; border-color: {colors['primary']} !important; }}

        /* Sidebar melhorada */
        .css-1d391kg {{ background: {colors['bg']}; }}
        .sidebar-content {{
            text-align: center;
            padding: 0.5rem 0;
        }}
        .sidebar-avatar {{
            border-radius: 50%;
            border: 2px solid {colors['primary']};
            margin-bottom: 0.5rem;
        }}
        .sidebar-name {{
            font-weight: 700;
            font-size: 1.2rem;
            color: {colors['text']};
        }}
        .sidebar-title {{
            font-weight: 400;
            font-size: 0.9rem;
            color: {colors['text_muted']};
        }}
        .sidebar-divider {{
            margin: 1rem 0;
            border: none;
            height: 1px;
            background: {colors['border']};
        }}
        .sidebar-footer {{
            font-size: 0.75rem;
            color: {colors['text_muted']};
            margin-top: 1rem;
        }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# CARREGAR CSS
# ============================================================================
load_css()

# ============================================================================
# SIDEBAR
# ============================================================================
with st.sidebar:
    # Avatar
    avatar_path = None
    if os.path.exists("rapha.jpeg"):
        avatar_path = "rapha.jpeg"
    elif os.path.exists("assets/rapha.jpeg"):
        avatar_path = "assets/rapha.jpeg"
    
    if avatar_path:
        st.image(avatar_path, width=160, use_container_width=False)
    else:
        colors = get_colors()
        st.markdown(f"""
        <div style="width:120px;height:120px;border-radius:50%;background:linear-gradient(135deg,{colors['primary']},{colors['secondary']});
        display:flex;align-items:center;justify-content:center;font-size:3.5rem;font-weight:700;color:white;margin:0 auto 1rem;border:3px solid {colors['primary']};">
        RP</div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="sidebar-content">
        <div class="sidebar-name">Raphael Pires</div>
        <div class="sidebar-title">Analista de Dados & BI</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    # Navegação
    page = st.radio(
        "Navegação",
        ["🏠 Início", "📈 Análises", "📊 Dashboard"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    # Toggle de tema
    render_theme_toggle()
    
    st.markdown("""
    <div class="sidebar-footer">
        © 2026 Raphael Pires<br>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PÁGINAS
# ============================================================================
if page == "🏠 Início":
    render_hero()
    st.divider()
    render_kpis()
    st.divider()
    
    # Experiência (direto aqui para evitar mais imports)
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Trajetória</span>
        <h2 class="section-title">Experiência profissional</h2>
    </div>
    <div class="timeline">
    """, unsafe_allow_html=True)
    experiences = [
        {"date":"Experiência Corporativa","role":"Automação com VBA","company":"Banco do Brasil","desc":"Redução de 70% do tempo operacional.","tags":["VBA","Automação"]},
        {"date":"Fundador & Analista","role":"Fundador","company":"Jardim do Éden","desc":"Dashboards, Power BI, Python, SQL, IA. Redução de 2h para 15min.","tags":["Power BI","Python","SQL","IA"]},
        {"date":"Gestão Comercial","role":"Gestão Comercial & BI","company":"J Sintonía","desc":"Business Intelligence, KPIs, dashboards e análise de viabilidade.","tags":["BI","KPIs","Dashboards"]},
        {"date":"Dados & Operação","role":"Analista de Dados","company":"NSM","desc":"Centralização de dados e controle operacional.","tags":["Dados","Governança","Indicadores"]}
    ]
    for exp in experiences:
        tags_html = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span>
                <h3 class="timeline-role">{exp["role"]}</h3>
                <div class="timeline-company">{exp["company"]}</div>
                <p class="timeline-desc">{exp["desc"]}</p>
                <div>{tags_html}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()
    
    render_skills_chart()
    st.divider()
    render_projects()
    st.divider()
    render_footer()

elif page == "📈 Análises":
    render_analytics_dashboard()

else:  # Dashboard
    render_dashboard()
