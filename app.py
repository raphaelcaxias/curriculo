import streamlit as st
from config import init_theme, get_colors
from components import render_theme_toggle, render_hero, render_kpis, render_skills_chart, render_footer
from pages.home import render_home

st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_theme()

def load_css():
    colors = get_colors()
    st.markdown(f"""
    <style>
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
        .hero-section {{ text-align: center; padding: 2rem 0 1rem; margin-bottom: 1rem; }}
        .hero-name {{ font-size: 2.8rem; font-weight: 800; color: {colors['text']}; letter-spacing: -0.02em; }}
        .hero-title {{ font-size: 1.1rem; font-weight: 600; color: {colors['primary']}; text-transform: uppercase; letter-spacing: 0.12em; }}
        .hero-subtitle {{ font-size: 1.1rem; color: {colors['text_muted']}; max-width: 720px; margin: 0 auto 1.5rem; line-height: 1.6; }}
        .tech-badge {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.4rem 1rem; border-radius: 999px; font-size: 0.85rem; font-weight: 500;
            color: {colors['text']}; display: inline-block; margin: 0.2rem;
        }}

        /* Seções */
        .section-header {{ text-align: center; margin: 3rem 0 2rem; }}
        .section-label {{
            background: {colors['primary_light']}; padding: 0.3rem 1.2rem; border-radius: 999px;
            font-size: 0.75rem; font-weight: 600; color: {colors['primary']}; display: inline-block;
        }}
        .section-title {{ font-size: 2.2rem; font-weight: 700; margin-top: 0.5rem; color: {colors['text']}; }}

        /* KPIs */
        .kpi-box {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 16px;
            padding: 1.5rem 1rem; text-align: center; transition: 0.3s;
            box-shadow: {colors['shadow']};
        }}
        .kpi-box:hover {{ transform: translateY(-6px); border-color: {colors['primary']}; box-shadow: {colors['shadow_hover']}; }}
        .kpi-value {{ font-size: 2.4rem; font-weight: 700; color: {colors['primary']}; }}
        .kpi-label {{ font-size: 0.9rem; color: {colors['text_muted']}; }}

        /* Timeline */
        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 30px; top: 0; bottom: 0;
            width: 2px; background: linear-gradient(to bottom, {colors['primary']}, {colors['secondary']}, transparent);
        }}
        .timeline-item {{ position: relative; padding-left: 80px; margin-bottom: 2rem; }}
        .timeline-dot {{
            position: absolute; left: 22px; top: 5px; width: 16px; height: 16px;
            border-radius: 50%; background: {colors['primary']}; border: 3px solid {colors['bg']};
            box-shadow: 0 0 0 3px {colors['primary']};
        }}
        .timeline-card {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 16px;
            padding: 1.5rem; transition: 0.3s; box-shadow: {colors['shadow']};
        }}
        .timeline-card:hover {{ border-color: {colors['primary']}; transform: translateX(5px); box-shadow: {colors['shadow_hover']}; }}
        .timeline-date {{ font-size: 0.75rem; font-weight: 600; color: {colors['primary']}; background: {colors['primary_light']}; padding: 0.2rem 0.8rem; border-radius: 999px; display: inline-block; }}
        .timeline-role {{ font-size: 1.2rem; font-weight: 700; margin: 0.3rem 0; color: {colors['text']}; }}
        .timeline-company {{ color: {colors['secondary']}; font-weight: 600; }}
        .timeline-desc {{ color: {colors['text_muted']}; line-height: 1.6; }}
        .timeline-tag {{
            font-size: 0.7rem; background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.2rem 0.6rem; border-radius: 6px; color: {colors['text']}; display: inline-block; margin: 0.2rem;
        }}
        .timeline-badge {{
            background: {colors['primary']}; color: white; font-size: 0.65rem; font-weight: 700;
            padding: 0.15rem 0.6rem; border-radius: 999px; margin-left: 0.5rem; display: inline-block;
        }}

        /* Stack */
        .stack-category {{ font-size: 0.9rem; font-weight: 600; color: {colors['primary']}; margin: 1rem 0 0.5rem; }}
        .stack-chip {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.4rem 1rem; border-radius: 8px; font-size: 0.9rem; font-weight: 500;
            color: {colors['text']}; display: inline-block; margin: 0.2rem;
            transition: 0.2s;
        }}
        .stack-chip:hover {{ background: {colors['primary']}; color: white; transform: translateY(-2px); }}

        /* Depoimentos */
        .testimonial-card {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 16px;
            padding: 1.5rem; text-align: center; box-shadow: {colors['shadow']};
        }}
        .testimonial-text {{ font-size: 1rem; color: {colors['text']}; font-style: italic; line-height: 1.5; }}
        .testimonial-author {{ font-weight: 600; color: {colors['primary']}; margin-top: 0.5rem; }}

        /* Certificação */
        .cert-card {{
            background: linear-gradient(135deg, {colors['primary_light']}, {colors['bg']});
            border: 1px solid {colors['primary']}; border-radius: 16px;
            padding: 1.5rem 2rem; text-align: center; box-shadow: {colors['shadow']};
        }}
        .cert-title {{ font-size: 1.5rem; font-weight: 700; color: {colors['text']}; }}
        .cert-sub {{ font-size: 1rem; color: {colors['text_muted']}; }}
        .cert-badge {{ font-size: 2.5rem; }}

        /* Footer */
        .footer {{
            margin-top: 4rem; padding: 2.5rem 2rem; background: {colors['card_bg']};
            border: 1px solid {colors['border']}; border-radius: 16px; text-align: center;
            box-shadow: {colors['shadow']};
        }}
        .footer-status {{ display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(34,197,94,0.12); border: 1px solid rgba(34,197,94,0.3); padding: 0.4rem 1rem; border-radius: 999px; }}
        .footer-status-dot {{ width: 8px; height: 8px; border-radius: 50%; background: #22C55E; box-shadow: 0 0 10px #22C55E; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
        .footer-status-text {{ font-weight: 600; color: #22C55E; }}
        .footer-title {{ font-size: 1.5rem; font-weight: 700; margin: 1rem 0 0.3rem; }}
        .footer-subtitle {{ color: {colors['text_muted']}; margin-bottom: 1.5rem; }}
        .footer-mode {{ background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']}; padding: 0.3rem 0.8rem; border-radius: 999px; font-size: 0.8rem; display: inline-block; margin: 0.2rem; }}
        .footer-link {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            padding: 0.4rem 1rem; border-radius: 8px; color: {colors['text']}; text-decoration: none;
            font-size: 0.9rem; display: inline-block; margin: 0.2rem; transition: 0.2s;
        }}
        .footer-link:hover {{ background: {colors['primary']}; color: white; transform: translateY(-2px); }}
        .footer-copy {{ color: {colors['text_muted']}; margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid {colors['border']}; }}

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{ gap: 0.5rem; background: transparent; }}
        .stTabs [data-baseweb="tab"] {{
            background: {colors['tag_bg']}; border: 1px solid {colors['tag_border']};
            border-radius: 8px; padding: 0.6rem 1.2rem; color: {colors['text']}; font-weight: 500;
        }}
        .stTabs [aria-selected="true"] {{ background: {colors['primary']} !important; color: white !important; border-color: {colors['primary']} !important; }}
    </style>
    """, unsafe_allow_html=True)

load_css()
render_theme_toggle()

with st.sidebar:
    import os
    if os.path.exists("rapha.jpeg"):
        st.image("rapha.jpeg", width=150)
    else:
        st.image("https://ui-avatars.com/api/?name=Raphael+Pires&size=150&background=3B82F6&color=fff", width=150)
    st.markdown("### Raphael Pires")
    st.markdown("Analista de Dados & BI")
    st.markdown("---")
    page = st.radio(
        "Navegação",
        ["🏠 Início", "📈 Análises", "📊 Dashboard"],
        index=0,
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("© 2026 Raphael Pires")

if page == "🏠 Início":
    render_home()
elif page == "📈 Análises":
    from pages.analytics import render_analytics_dashboard
    render_analytics_dashboard()
else:
    from pages.dashboard import render_dashboard
    render_dashboard()
