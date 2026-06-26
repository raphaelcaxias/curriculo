import streamlit as st
import plotly.express as px
import pandas as pd
from config import get_colors, SOCIAL_LINKS, TECH_STACK, SKILLS_DATA, EXPERIENCES, PROJECTS

# ============================================================================
# COMPONENTES DE UI
# ============================================================================
def render_theme_toggle():
    """Renderiza o botão de alternância de tema"""
    col1, col2, col3 = st.columns([10, 1, 1])
    with col3:
        is_dark = st.session_state.theme == "dark"
        label = "☀️" if is_dark else "🌙"
        st.button(label, on_click=toggle_theme, key="theme_btn", use_container_width=True)

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# ============================================================================
# COMPONENTES DO HEADER
# ============================================================================
def render_hero():
    """Renderiza a seção hero com foto e apresentação"""
    colors = get_colors()
    
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    
    # Foto
    col1, col2, col3 = st.columns([4, 2, 4])
    with col2:
        try:
            st.image("assets/rapha.jpeg", use_container_width=True)
        except:
            st.markdown(f"""
            <div style="
                width: 180px;
                height: 180px;
                border-radius: 50%;
                background: linear-gradient(135deg, {colors['primary']}, {colors['secondary']});
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Playfair Display', serif;
                font-size: 4rem;
                font-weight: 700;
                color: white;
                box-shadow: 0 10px 40px rgba(59, 130, 246, 0.3);
                margin: 0 auto 1.5rem auto;
                border: 3px solid {colors['primary']};
            ">RP</div>
            """, unsafe_allow_html=True)
    
    # Texto
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
    col1, col2, col3 = st.columns([4, 2, 4])
    with col2:
        try:
            with open("assets/Curriculo_Raphael_v2.pdf", "rb") as pdf:
                st.download_button(
                    label="📄 Download Currículo PDF",
                    data=pdf.read(),
                    file_name="Curriculo_Raphael_Pires.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        except:
            st.info("📄 Currículo PDF disponível")

# ============================================================================
# COMPONENTES DE CONTEÚDO
# ============================================================================
def render_kpis():
    """Renderiza os KPIs de impacto"""
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Impacto Mensurável</span>
        <h2 class="section-title">Números que contam histórias</h2>
    </div>
    """, unsafe_allow_html=True)
    
    kpis = [
        ("16+", "anos de experiência"),
        ("70%", "redução operacional"),
        ("213k", "registros processados"),
        ("2h→15m", "análises reduzidas"),
        ("R$50bi", "dados analisados")
    ]
    
    cols = st.columns(5)
    for col, (value, label) in zip(cols, kpis):
        with col:
            st.markdown(f"""
            <div class="kpi-box">
                <div class="kpi-value">{value}</div>
                <div class="kpi-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

def render_experience():
    """Renderiza a timeline de experiências"""
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Trajetória</span>
        <h2 class="section-title">Experiência profissional</h2>
    </div>
    <div class="timeline">
    """, unsafe_allow_html=True)
    
    for exp in EXPERIENCES:
        tags_html = "".join([f'<span class="timeline-tag">{tag}</span>' for tag in exp["tags"]])
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span>
                <h3 class="timeline-role">{exp["role"]}</h3>
                <div class="timeline-company">{exp["company"]}</div>
                <p class="timeline-desc">{exp["description"]}</p>
                <div class="timeline-tags">{tags_html}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_tech_stack():
    """Renderiza a stack tecnológica"""
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Stack</span>
        <h2 class="section-title">Tecnologias</h2>
    </div>
    """, unsafe_allow_html=True)
    
    icons = {
        "Dados": "📊",
        "BI": "📈",
        "Cloud": "☁️",
        "Automação": "⚡"
    }
    
    for category, techs in TECH_STACK.items():
        st.markdown(f'<div class="stack-category">{icons.get(category, "")} {category}</div>', unsafe_allow_html=True)
        chips = "".join([f'<span class="stack-chip">{tech}</span>' for tech in techs])
        st.markdown(f'<div class="stack-chips">{chips}</div>', unsafe_allow_html=True)

def render_skills_chart():
    """Renderiza o gráfico de habilidades"""
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Competências</span>
        <h2 class="section-title">Domínio tecnológico</h2>
    </div>
    """, unsafe_allow_html=True)
    
    colors = get_colors()
    df = pd.DataFrame(SKILLS_DATA)
    
    fig = px.bar(
        df,
        x="Proficiência",
        y="Tecnologia",
        color="Categoria",
        orientation="h",
        color_discrete_sequence=colors["chart_colors"],
        template=colors["plotly_template"],
        text="Proficiência"
    )
    
    fig.update_layout(
        margin=dict(l=20, r=40, t=20, b=40),
        height=380,
        xaxis=dict(range=[0, 105], showgrid=True, gridcolor="rgba(148, 163, 184, 0.1)"),
        yaxis=dict(showgrid=False),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Inter", color=colors["text"]),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    fig.update_traces(textposition="outside", textfont=dict(color=colors["text"], size=11))
    
    st.plotly_chart(fig, use_container_width=True)

def render_projects():
    """Renderiza os projetos sem usar border=True"""
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Portfólio</span>
        <h2 class="section-title">Projetos em destaque</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Organizar em grid 2x2
    for i in range(0, len(PROJECTS), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(PROJECTS):
                proj = PROJECTS[i + j]
                with col:
                    # Usando container sem border e adicionando CSS manualmente
                    st.markdown(f"""
                    <div style="
                        background: rgba(59, 130, 246, 0.03);
                        border: 1px solid rgba(59, 130, 246, 0.1);
                        border-radius: 12px;
                        padding: 1.5rem;
                        margin-bottom: 1rem;
                        transition: all 0.3s ease;
                    ">
                        <h4>{proj['icon']} {proj['title']}</h4>
                        <p style="color: #94A3B8; margin: 0.5rem 0 1rem 0;">{proj['description']}</p>
                        <a href="{proj['link']}" target="_blank" style="
                            display: inline-block;
                            background: rgba(59, 130, 246, 0.1);
                            color: #3B82F6;
                            padding: 0.4rem 1rem;
                            border-radius: 6px;
                            text-decoration: none;
                            font-weight: 500;
                            font-size: 0.9rem;
                        ">🔗 {proj['label']}</a>
                    </div>
                    """, unsafe_allow_html=True)

def render_footer():
    """Renderiza o footer"""
    colors = get_colors()
    
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
            <a href="{SOCIAL_LINKS['linkedin']}" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="{SOCIAL_LINKS['github']}" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="{SOCIAL_LINKS['email']}" class="footer-link">✉️ E-mail</a>
            <a href="{SOCIAL_LINKS['phone']}" class="footer-link">📱 Telefone</a>
        </div>
        
        <p class="footer-copy">© 2026 Raphael Fernando da Silva Pires</p>
    </div>
    """, unsafe_allow_html=True)
