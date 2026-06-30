import streamlit as st

# ===== TENTA IMPORTAR, MAS SE FALHAR, CRIA UMA FUNÇÃO LOCAL =====
try:
    from config import init_theme, toggle_theme, get_colors
except ImportError:
    # Fallback: define as funções localmente
    def init_theme():
        if "theme" not in st.session_state:
            st.session_state.theme = "dark"
    def toggle_theme():
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
    def get_colors():
        dark = st.session_state.theme == "dark"
        if dark:
            return {
                "primary": "#3B82F6",
                "secondary": "#0EA5E9",
                "bg": "#0B0F1A",
                "text": "#F1F5F9",
                "text_muted": "#94A3B8",
                "card_bg": "rgba(255,255,255,0.04)",
                "border": "rgba(255,255,255,0.08)",
                "tag_bg": "rgba(59,130,246,0.15)",
                "tag_border": "rgba(59,130,246,0.25)",
                "primary_light": "rgba(59,130,246,0.2)",
                "navbar_bg": "rgba(11,15,26,0.75)",
                "navbar_border": "rgba(255,255,255,0.06)",
                "nav_hover": "rgba(255,255,255,0.06)",
                "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(59,130,246,0.08) 0%, transparent 70%)",
                "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(59,130,246,0.15) 0%, transparent 60%)",
                "section_bg": "rgba(11,15,26,0.5)",
                "section_alt_bg": "rgba(255,255,255,0.02)",
                "shadow": "0 8px 32px rgba(0,0,0,0.4)",
                "shadow_hover": "0 12px 40px rgba(59,130,246,0.2)",
                "plotly_template": "plotly_dark",
                "chart_colors": ["#3B82F6","#0EA5E9","#60A5FA","#2563EB","#0284C7"]
            }
        else:
            return {
                "primary": "#1D4ED8",
                "secondary": "#0EA5E9",
                "bg": "#F8FAFC",
                "text": "#0F172A",
                "text_muted": "#475569",
                "card_bg": "rgba(255,255,255,0.7)",
                "border": "rgba(0,0,0,0.06)",
                "tag_bg": "#DBEAFE",
                "tag_border": "#93C5FD",
                "primary_light": "#DBEAFE",
                "navbar_bg": "rgba(248,250,252,0.8)",
                "navbar_border": "rgba(0,0,0,0.04)",
                "nav_hover": "rgba(0,0,0,0.04)",
                "hero_bg": "radial-gradient(ellipse at 50% 30%, rgba(29,78,216,0.04) 0%, transparent 70%)",
                "hero_glow": "radial-gradient(ellipse at 70% 20%, rgba(29,78,216,0.08) 0%, transparent 60%)",
                "section_bg": "rgba(255,255,255,0.5)",
                "section_alt_bg": "rgba(0,0,0,0.01)",
                "shadow": "0 8px 32px rgba(0,0,0,0.06)",
                "shadow_hover": "0 12px 40px rgba(29,78,216,0.1)",
                "plotly_template": "plotly_white",
                "chart_colors": ["#1D4ED8","#0EA5E9","#3B82F6","#2563EB","#0284C7"]
            }

from components import render_footer, get_foto_url, get_pdf_path

st.set_page_config(
    page_title="Raphael Pires · Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

init_theme()

def load_css():
    colors = get_colors()
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap');

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, sans-serif;
            background: {colors['bg']};
            color: {colors['text']};
            scroll-behavior: smooth;
        }}
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: {colors['bg']}; }}
        .block-container {{ padding: 0 !important; max-width: 100%; }}

        /* Navbar */
        .navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 999;
            background: {colors['navbar_bg']};
            backdrop-filter: blur(16px) saturate(180%);
            -webkit-backdrop-filter: blur(16px) saturate(180%);
            border-bottom: 1px solid {colors['navbar_border']};
            padding: 0.75rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .navbar-brand {{ font-weight: 700; font-size: 1.25rem; letter-spacing: -0.02em; color: {colors['text']}; text-decoration: none; }}
        .navbar-brand span {{ color: {colors['primary']}; }}
        .navbar-links {{ display: flex; gap: 0.5rem; align-items: center; }}
        .nav-link {{
            padding: 0.4rem 1rem; border-radius: 999px; font-size: 0.875rem;
            font-weight: 500; text-decoration: none; transition: all 0.2s;
            color: {colors['text_muted']}; background: transparent;
            cursor: pointer;
        }}
        .nav-link:hover {{ background: {colors['nav_hover']}; color: {colors['text']}; }}
        .nav-link.active {{
            background: {colors['primary']}; color: white;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
        }}
        .theme-btn-container {{
            display: flex;
            align-items: center;
            margin-left: 1rem;
        }}

        /* Hero – espaçamento reduzido */
        .hero-full {{
            min-height: 70vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 4rem 2rem 2rem;
            background: {colors['hero_bg']};
            position: relative;
            overflow: hidden;
        }}
        .hero-full::before {{
            content: ''; position: absolute; inset: 0;
            background: {colors['hero_glow']};
            opacity: 0.4; pointer-events: none;
        }}
        .hero-content {{
            max-width: 1200px; width: 100%;
            display: grid; grid-template-columns: 1fr 2fr;
            gap: 2rem;
            align-items: center;
            position: relative; z-index: 1;
        }}
        @media (max-width: 768px) {{
            .hero-content {{ grid-template-columns: 1fr; text-align: center; }}
        }}
        .hero-photo img {{
            width: 220px; height: 220px; border-radius: 50%;
            object-fit: cover; border: 4px solid {colors['primary']};
            box-shadow: 0 20px 60px rgba(59,130,246,0.25);
        }}
        .hero-text h1 {{ font-size: 2.8rem; font-weight: 800; letter-spacing: -0.03em; line-height: 1.1; color: {colors['text']}; }}
        .hero-text h1 span {{ color: {colors['primary']}; }}
        .hero-text .subtitle {{ font-size: 1.1rem; color: {colors['text_muted']}; margin: 0.5rem 0 1rem; line-height: 1.6; }}
        .hero-text .badge-group {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }}
        .hero-text .badge {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.3rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 500; color: {colors['text']};
        }}
        .hero-text .cta-group {{ display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem; }}
        .btn-primary {{
            background: {colors['primary']}; color: white;
            padding: 0.6rem 1.5rem; border-radius: 999px;
            font-weight: 600; text-decoration: none; transition: 0.2s;
            display: inline-block; border: none; cursor: pointer;
        }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(59,130,246,0.35); }}
        .btn-secondary {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']};
            padding: 0.6rem 1.5rem; border-radius: 999px;
            font-weight: 500; color: {colors['text']}; text-decoration: none;
            transition: 0.2s; display: inline-block;
        }}
        .btn-secondary:hover {{ background: {colors['nav_hover']}; }}

        /* Seções */
        .section-glass {{
            padding: 3rem 2rem;
            background: {colors['section_bg']};
            backdrop-filter: blur(4px);
            border-top: 1px solid {colors['border']};
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .section-header {{ text-align: center; margin-bottom: 2rem; }}
        .section-header .label {{
            display: inline-block;
            background: {colors['primary_light']};
            padding: 0.2rem 1rem; border-radius: 999px;
            font-size: 0.7rem; font-weight: 600; text-transform: uppercase;
            letter-spacing: 0.08em; color: {colors['primary']};
        }}
        .section-header h2 {{ font-size: 2.2rem; font-weight: 700; margin-top: 0.5rem; color: {colors['text']}; letter-spacing: -0.02em; }}
        .section-header p {{ color: {colors['text_muted']}; max-width: 600px; margin: 0.5rem auto 0; }}

        .glass-card {{
            background: {colors['card_bg']};
            backdrop-filter: blur(8px);
            border: 1px solid {colors['border']};
            border-radius: 24px;
            padding: 1.5rem;
            transition: all 0.25s ease;
            box-shadow: {colors['shadow']};
        }}
        .glass-card:hover {{ transform: translateY(-6px); border-color: {colors['primary']}; box-shadow: {colors['shadow_hover']}; }}

        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 28px; top: 0; bottom: 0;
            width: 2px; background: linear-gradient(to bottom, {colors['primary']}, {colors['secondary']}, transparent);
        }}
        .timeline-item {{ position: relative; padding-left: 80px; margin-bottom: 2rem; }}
        .timeline-dot {{
            position: absolute; left: 20px; top: 6px; width: 18px; height: 18px;
            border-radius: 50%; background: {colors['primary']};
            border: 3px solid {colors['bg']}; box-shadow: 0 0 0 4px {colors['primary']};
        }}
        .timeline-card {{
            background: {colors['card_bg']};
            backdrop-filter: blur(4px);
            border: 1px solid {colors['border']};
            border-radius: 20px; padding: 1.5rem;
            transition: 0.25s;
        }}
        .timeline-card:hover {{ border-color: {colors['primary']}; transform: translateX(6px); }}
        .timeline-date {{
            display: inline-block; font-size: 0.7rem; font-weight: 600;
            background: {colors['primary_light']}; color: {colors['primary']};
            padding: 0.2rem 0.8rem; border-radius: 999px;
        }}
        .timeline-badge {{
            background: {colors['primary']}; color: white;
            font-size: 0.6rem; font-weight: 700; padding: 0.15rem 0.6rem;
            border-radius: 999px; margin-left: 0.5rem; display: inline-block;
        }}
        .timeline-role {{ font-size: 1.1rem; font-weight: 700; margin: 0.3rem 0; }}
        .timeline-company {{ color: {colors['secondary']}; font-weight: 600; }}
        .timeline-desc {{ color: {colors['text_muted']}; line-height: 1.6; }}
        .timeline-tag {{
            font-size: 0.7rem; background: {colors['tag_bg']};
            border: 1px solid {colors['tag_border']}; padding: 0.2rem 0.6rem;
            border-radius: 6px; display: inline-block; margin: 0.2rem;
        }}

        .testimonial-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
        @media (max-width: 768px) {{ .testimonial-grid {{ grid-template-columns: 1fr; }} }}

        .footer {{
            padding: 2.5rem 2rem; text-align: center;
            border-top: 1px solid {colors['border']};
            background: {colors['card_bg']};
            backdrop-filter: blur(4px);
        }}
        .footer .status {{
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.2);
            padding: 0.3rem 1rem; border-radius: 999px;
            font-size: 0.8rem; font-weight: 500; color: #22C55E;
        }}
        .footer .status-dot {{
            width: 8px; height: 8px; border-radius: 50%;
            background: #22C55E; box-shadow: 0 0 12px #22C55E;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} }}
        .footer-links {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 0.5rem; margin: 1.5rem 0; }}
        .footer-link {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.4rem 1rem; border-radius: 999px;
            color: {colors['text']}; text-decoration: none;
            font-size: 0.85rem; transition: 0.2s;
        }}
        .footer-link:hover {{ background: {colors['primary']}; color: white; }}
        .footer-copy {{ color: {colors['text_muted']}; font-size: 0.8rem; }}

        @media (max-width: 768px) {{
            .navbar {{ padding: 0.5rem 1rem; flex-wrap: wrap; }}
            .navbar-links {{ gap: 0.3rem; flex-wrap: wrap; }}
            .hero-full {{ padding: 3rem 1rem 1.5rem; min-height: auto; }}
            .hero-text h1 {{ font-size: 1.8rem; }}
            .hero-photo img {{ width: 140px; height: 140px; }}
            .section-glass {{ padding: 2rem 1rem; }}
        }}
    </style>
    """, unsafe_allow_html=True)

load_css()

# ===== BOTÃO DE TEMA =====
col1, col2, col3 = st.columns([10, 1, 1])
with col3:
    theme_label = "☀️" if st.session_state.theme == "dark" else "🌙"
    st.button(theme_label, on_click=toggle_theme, key="theme_btn", use_container_width=True)

# ===== NAVBAR =====
page = st.query_params.get("page", "home")
st.markdown(f"""
<nav class="navbar">
    <a href="/" class="navbar-brand">Raphael <span>Pires</span></a>
    <div class="navbar-links">
        <a href="?page=home" class="nav-link {'active' if page == 'home' else ''}">Início</a>
        <a href="?page=analytics" class="nav-link {'active' if page == 'analytics' else ''}">Análises</a>
        <a href="?page=dashboard" class="nav-link {'active' if page == 'dashboard' else ''}">Dashboard</a>
    </div>
</nav>
""", unsafe_allow_html=True)

# ===== CONTEÚDO =====
if page == "home":
    from pages.home import render_home
    render_home()
elif page == "analytics":
    from pages.analytics import render_analytics
    render_analytics()
elif page == "dashboard":
    from pages.dashboard import render_dashboard
    render_dashboard()
else:
    from pages.home import render_home
    render_home()

render_footer()
