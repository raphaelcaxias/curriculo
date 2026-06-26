import streamlit as st
from config import init_theme, get_colors
from components import render_theme_toggle

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# INICIALIZAÇÃO
# ============================================================================
init_theme()

# ============================================================================
# CSS GLOBAL
# ============================================================================
def load_css():
    colors = get_colors()
    
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
    
    /* Reset e Global */
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        background: {colors['bg']};
        color: {colors['text']};
    }}
    
    #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
    .stApp {{ background: {colors['bg']}; }}
    
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
        color: {colors['text']};
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.02em;
    }}
    
    .hero-title {{
        font-size: 1rem;
        font-weight: 600;
        color: {colors['primary']};
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 0 0 1.5rem 0;
    }}
    
    .hero-subtitle {{
        font-size: 1.125rem;
        color: {colors['text_muted']};
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
        color: {colors['text']};
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
        color: {colors['primary']};
        background: rgba(59, 130, 246, 0.1);
        padding: 0.4rem 1rem;
        border-radius: 999px;
        margin-bottom: 1rem;
    }}
    
    .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: {colors['text']};
        margin: 0;
    }}
    
    /* KPIs */
    .kpi-box {{
        background: {colors['card_bg']};
        border: 1px solid {colors['border']};
        border-radius: 12px;
        padding: 1.5rem 1rem;
        text-align: center;
        transition: all 0.3s ease;
    }}
    
    .kpi-box:hover {{
        transform: translateY(-4px);
        border-color: {colors['primary']};
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.15);
    }}
    
    .kpi-value {{
        font-size: 2rem;
        font-weight: 700;
        color: {colors['primary']};
        margin-bottom: 0.5rem;
    }}
    
    .kpi-label {{
        font-size: 0.85rem;
        color: {colors['text_muted']};
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
        background: linear-gradient(180deg, {colors['primary']}, {colors['secondary']}, transparent);
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
        background: {colors['primary']};
        border: 3px solid {colors['bg']};
        box-shadow: 0 0 0 3px {colors['primary']};
    }}
    
    .timeline-card {{
        background: {colors['card_bg']};
        border: 1px solid {colors['border']};
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }}
    
    .timeline-card:hover {{
        border-color: {colors['primary']};
        background: {colors['hover_bg']};
        transform: translateX(4px);
    }}
    
    .timeline-date {{
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 600;
        color: {colors['primary']};
        background: rgba(59, 130, 246, 0.1);
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        margin-bottom: 0.75rem;
    }}
    
    .timeline-role {{
        font-size: 1.15rem;
        font-weight: 600;
        color: {colors['text']};
        margin: 0 0 0.25rem 0;
    }}
    
    .timeline-company {{
        font-size: 0.95rem;
        color: {colors['secondary']};
        font-weight: 500;
        margin-bottom: 0.75rem;
    }}
    
    .timeline-desc {{
        font-size: 0.95rem;
        color: {colors['text_muted']};
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
        color: {colors['text']};
        font-weight: 500;
    }}
    
    /* Stack */
    .stack-category {{
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: {colors['primary']};
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
        color: {colors['text']};
        transition: all 0.2s ease;
    }}
    
    .stack-chip:hover {{
        background: {colors['primary']};
        color: white;
        border-color: {colors['primary']};
        transform: translateY(-2px);
    }}
    
    /* Footer */
    .footer {{
        margin-top: 4rem;
        padding: 3rem 2rem;
        background: {colors['card_bg']};
        border: 1px solid {colors['border']};
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
        color: {colors['text']};
        margin: 0 0 0.5rem 0;
    }}
    
    .footer-subtitle {{
        font-size: 0.95rem;
        color: {colors['text_muted']};
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
        color: {colors['text']};
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
        color: {colors['text']};
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.2s ease;
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
    }}
    
    .footer-link:hover {{
        background: {colors['primary']};
        color: white;
        border-color: {colors['primary']};
        transform: translateY(-2px);
    }}
    
    .footer-copy {{
        font-size: 0.85rem;
        color: {colors['text_muted']};
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
        color: {colors['text']};
        font-weight: 500;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: {colors['primary']} !important;
        color: white !important;
        border-color: {colors['primary']} !important;
    }}
    
    /* Scrollbar */
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: {colors['bg']}; }}
    ::-webkit-scrollbar-thumb {{ background: rgba(59, 130, 246, 0.3); border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: {colors['primary']}; }}
    
    .stMarkdown, h1, h2, h3, h4 {{ color: {colors['text']}; }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# NAVEGAÇÃO
# ============================================================================
def main():
    # Carregar CSS
    load_css()
    
    # Tema toggle
    render_theme_toggle()
    
    # Sidebar com navegação
    with st.sidebar:
        st.markdown("## 📊 Navegação")
        page = st.radio(
            "Selecione uma página:",
            ["🏠 Home", "📈 Análises"],
            index=0,
            label_visibility="collapsed"
        )
    
    # Navegação
    if page == "🏠 Home":
        from pages.home import main as home_main
        home_main()
    else:
        from pages.analytics import main as analytics_main
        analytics_main()

if __name__ == "__main__":
    main()
