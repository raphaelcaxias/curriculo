import streamlit as st
from config import init_theme, get_colors
from components import render_theme_toggle, render_hero, render_kpis, render_skills_chart, render_footer
from pages.home import render_projects, render_testimonials, render_certification
from pages.analytics import render_analytics_dashboard

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
        .hero-section {{ text-align: center; padding: 2rem 0; margin-bottom: 2rem; }}
        .hero-name {{ font-size: 2.8rem; font-weight: 800; color: {colors['text']}; letter-spacing: -0.02em; }}
        .hero-title {{ font-size: 1.1rem; font-weight: 600; color: {colors['primary']}; text-transform: uppercase; letter-spacing: 0.15em; }}
        .hero-subtitle {{ font-size: 1.1rem; color: {colors['text_muted']}; max-width: 700px; margin: 0 auto 1.5rem; line-height: 1.7; }}
        .hero-badge {{
            background: rgba(59,130,246,0.12); border: 1px solid rgba(59,130,246,0.25);
            padding: 0.3rem 1rem; border-radius: 999px; font-size: 0.85rem; font-weight: 500;
            color: {colors['primary']}; display: inline-block; margin: 0.3rem;
        }}
        .hero-badge strong {{ color: {colors['text']}; }}

        /* Seções */
        .section-header {{ text-align: center; margin: 3rem 0 2rem; }}
        .section-label {{ background: {colors['primary']}15; padding: 0.3rem 1.2rem; border-radius: 999px; font-size: 0.75rem; font-weight: 600; color: {colors['primary']}; display: inline-block; }}
        .section-title {{ font-size: 2.2rem; font-weight: 700; margin-top: 0.5rem; letter-spacing: -0.01em; }}

        /* KPIs */
        .kpi-box {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 14px;
            padding: 1.8rem 1rem; text-align: center; transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        .kpi-box:hover {{ transform: translateY(-6px); border-color: {colors['primary']}; box-shadow: 0 12px 32px rgba(59,130,246,0.12); }}
        .kpi-value {{ font-size: 2.4rem; font-weight: 700; color: {colors['primary']}; line-height: 1.2; }}
        .kpi-label {{ font-size: 0.85rem; color: {colors['text_muted']}; margin-top: 0.2rem; }}

        /* Timeline */
        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 30px; top: 0; bottom: 0;
            width: 3px; background: linear-gradient(to bottom, {colors['primary']}, {colors['secondary']}, transparent);
            border-radius: 999px;
        }}
        .timeline-item {{ position: relative; padding-left: 80px; margin-bottom: 2rem; }}
        .timeline-dot {{
            position: absolute; left: 22px; top: 6px; width: 18px; height: 18px;
            border-radius: 50%; background: {colors['primary']}; border: 3px solid {colors['bg']};
            box-shadow: 0 0 0 4px {colors['primary']}40;
        }}
        .timeline-card {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 14px;
            padding: 1.8rem; transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        .timeline-card:hover {{ border-color: {colors['primary']}; transform: translateX(6px); box-shadow: 0 8px 24px rgba(59,130,246,0.08); }}
        .timeline-date {{ font-size: 0.75rem; font-weight: 600; color: {colors['primary']}; background: {colors['primary']}15; padding: 0.2rem 1rem; border-radius: 999px; display: inline-block; }}
        .timeline-role {{ font-size: 1.3rem; font-weight: 700; margin: 0.4rem 0 0.2rem; }}
        .timeline-company {{ color: {colors['secondary']}; font-weight: 600; font-size: 1rem; }}
        .timeline-desc {{ color: {colors['text_muted']}; line-height: 1.7; margin: 0.5rem 0; }}
        .timeline-tag {{
            font-size: 0.7rem; background: {colors['tag_bg']}; color: {colors['tag_text']};
            padding: 0.2rem 0.7rem; border-radius: 999px; display: inline-block; margin: 0.2rem;
            font-weight: 500;
        }}
        .timeline-tag-current {{
            background: #22C55E20; color: #22C55E; border: 1px solid #22C55E40;
            font-size: 0.7rem; padding: 0.15rem 0.7rem; border-radius: 999px; font-weight: 600;
            display: inline-block; margin-left: 0.5rem;
        }}

        /* Stack */
        .stack-category {{ font-size: 0.9rem; font-weight: 600; color: {colors['primary']}; margin: 1.2rem 0 0.5rem; }}
        .stack-chip {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']};
            padding: 0.4rem 1.2rem; border-radius: 999px; font-size: 0.85rem; font-weight: 500;
            color: {colors['text']}; display: inline-block; margin: 0.25rem;
            transition: all 0.2s ease;
        }}
        .stack-chip:hover {{ background: {colors['primary']}; color: white; border-color: {colors['primary']}; transform: translateY(-2px); }}

        /* Footer */
        .footer {{
            margin-top: 4rem; padding: 2.5rem 2rem; background: {colors['card_bg']};
            border: 1px solid {colors['border']}; border-radius: 16px; text-align: center;
        }}
        .footer-status {{ display: inline-flex; align-items: center; gap: 0.5rem; background: #22C55E15; border: 1px solid #22C55E40; padding: 0.4rem 1.2rem; border-radius: 999px; }}
        .footer-status-dot {{ width: 10px; height: 10px; border-radius: 50%; background: #22C55E; box-shadow: 0 0 12px #22C55E60; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
        .footer-status-text {{ font-weight: 600; color: #22C55E; }}
        .footer-title {{ font-size: 1.6rem; font-weight: 700; margin: 1rem 0 0.3rem; }}
        .footer-subtitle {{ color: {colors['text_muted']}; margin-bottom: 1.5rem; }}
        .footer-mode {{ background: {colors['card_bg']}; border: 1px solid {colors['border']}; padding: 0.3rem 1rem; border-radius: 999px; font-size: 0.8rem; display: inline-block; margin: 0.2rem; }}
        .footer-link {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']};
            padding: 0.4rem 1.2rem; border-radius: 999px; color: {colors['text']}; text-decoration: none;
            font-size: 0.9rem; display: inline-block; margin: 0.2rem; transition: all 0.2s ease;
        }}
        .footer-link:hover {{ background: {colors['primary']}; color: white; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(59,130,246,0.3); }}
        .footer-copy {{ color: {colors['text_muted']}; margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid {colors['border']}; }}

        /* Tabs personalizadas */
        .stTabs [data-baseweb="tab-list"] {{ gap: 0.5rem; background: transparent; }}
        .stTabs [data-baseweb="tab"] {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']};
            border-radius: 999px; padding: 0.5rem 1.5rem; color: {colors['text']}; font-weight: 500;
            transition: all 0.2s ease;
        }}
        .stTabs [aria-selected="true"] {{
            background: {colors['primary']} !important; color: white !important;
            border-color: {colors['primary']} !important;
            box-shadow: 0 4px 12px rgba(59,130,246,0.3);
        }}

        /* Depoimentos */
        .testimonial-card {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 14px;
            padding: 1.8rem; text-align: center; transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        .testimonial-card:hover {{ transform: translateY(-4px); border-color: {colors['primary']}; }}
        .testimonial-quote {{ font-size: 1.1rem; line-height: 1.6; color: {colors['text']}; font-style: italic; }}
        .testimonial-author {{ font-weight: 600; margin-top: 0.8rem; color: {colors['primary']}; }}
        .testimonial-role {{ font-size: 0.8rem; color: {colors['text_muted']}; }}

        /* Certificação */
        .cert-badge {{
            background: linear-gradient(135deg, {colors['primary']}20, {colors['secondary']}10);
            border: 1px solid {colors['primary']}40; border-radius: 14px;
            padding: 1.2rem 2rem; text-align: center; margin: 1.5rem 0;
        }}
        .cert-badge-icon {{ font-size: 2.5rem; }}
        .cert-badge-title {{ font-weight: 700; font-size: 1.2rem; color: {colors['text']}; }}
        .cert-badge-sub {{ color: {colors['text_muted']}; font-size: 0.9rem; }}

        /* Cards de projetos */
        .project-card {{
            background: {colors['card_bg']}; border: 1px solid {colors['border']}; border-radius: 14px;
            padding: 1.5rem; transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        .project-card:hover {{ transform: translateY(-4px); border-color: {colors['primary']}; box-shadow: 0 8px 24px rgba(59,130,246,0.08); }}
        .project-card h3 {{ margin-top: 0; color: {colors['text']}; }}
        .project-card p {{ color: {colors['text_muted']}; line-height: 1.6; }}
        .project-link {{
            display: inline-block; margin-top: 0.5rem; color: {colors['primary']};
            font-weight: 600; text-decoration: none;
        }}
        .project-link:hover {{ text-decoration: underline; }}

    </style>
    """, unsafe_allow_html=True)

load_css()
render_theme_toggle()

with st.sidebar:
    try:
        st.image("rapha.jpeg" if __import__('os').path.exists("rapha.jpeg") else None, width=150)
    except:
        pass
    st.markdown(f"### Raphael Pires")
    st.markdown("Analista de Dados & BI")
    st.markdown("---")
    
    # Certificação na sidebar
    st.markdown("""
    <div style="background: #3B82F615; border: 1px solid #3B82F630; border-radius: 12px; padding: 0.8rem; text-align: center; margin-bottom: 1rem;">
        <span style="font-size: 1.5rem;">🎯</span><br>
        <span style="font-weight: 600;">AWS Cloud Practitioner</span><br>
        <span style="font-size: 0.8rem; color: #94A3B8;">Meta 2026</span>
    </div>
    """, unsafe_allow_html=True)
    
    page = st.radio(
        "Navegação",
        ["🏠 Início", "📈 Análises", "📊 Dashboard"],
        index=0,
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("© 2026 Raphael Pires")

if page == "🏠 Início":
    render_hero()
    st.divider()
    render_kpis()
    st.divider()
    render_certification()
    st.divider()
    
    # Experiência (reordenada)
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Trajetória</span>
        <h2 class="section-title">Experiência profissional</h2>
    </div>
    <div class="timeline">
    """, unsafe_allow_html=True)
    
    experiencias = [
        {
            "date": "2014 – Presente · 10+ anos",
            "role": "Analista de Dados",
            "company": "NSM",
            "desc": "Centralização de dados, construção de indicadores de desempenho e governança de dados. Responsável por dashboards executivos e automação de relatórios.",
            "tags": ["Dados", "Governança", "Indicadores", "Dashboards"],
            "current": True
        },
        {
            "date": "2012 – Presente · 12+ anos",
            "role": "Fundador",
            "company": "Jardim do Éden",
            "desc": "Desenvolvimento de soluções completas em BI: Power BI, Python, SQL, KPIs e IA Generativa. Redução de tempo de análise de 2h para 15min.",
            "tags": ["Power BI", "Python", "SQL", "IA"],
            "current": True
        },
        {
            "date": "2010 – 2014 · 4 anos",
            "role": "Gestão Comercial & BI",
            "company": "J Sintonía",
            "desc": "Implementação de Business Intelligence, criação de KPIs, dashboards e análise de viabilidade econômica para tomada de decisão.",
            "tags": ["BI", "KPIs", "Dashboards"],
            "current": False
        },
        {
            "date": "2009 – 2010 · 1 ano",
            "role": "Automação de Processos com VBA",
            "company": "Banco do Brasil",
            "desc": "Desenvolvimento de automações em VBA que resultaram em redução de 70% do tempo operacional em processos internos.",
            "tags": ["VBA", "Automação", "Eficiência"],
            "current": False
        }
    ]
    
    for exp in experiencias:
        tags_html = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        current_tag = '<span class="timeline-tag-current">● Atual</span>' if exp.get("current") else ''
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span>
                {current_tag}
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
    render_testimonials()
    st.divider()
    render_footer()

elif page == "📈 Análises":
    render_analytics_dashboard()

else:
    from pages.dashboard import render_dashboard
    render_dashboard()
