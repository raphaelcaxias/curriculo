# Em pages/home.py, dentro de render_home(), substituir a seção do hero:

def render_home():
    c = get_colors()
    import os

    # ===== HERO =====
    st.markdown('<section class="hero-full"><div class="hero-content">', unsafe_allow_html=True)
    
    # Coluna da foto (usando st.image)
    col1, col2 = st.columns([1, 1])
    with col1:
        if os.path.exists("rapha.jpeg"):
            st.image("rapha.jpeg", width=280)
        elif os.path.exists("assets/rapha.jpeg"):
            st.image("assets/rapha.jpeg", width=280)
        else:
            st.image("https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff", width=280)
    
    with col2:
        st.markdown(f"""
        <div class="hero-text">
            <h1>Raphael <span>Pires</span></h1>
            <p class="subtitle">Analista de Dados &amp; Business Intelligence<br>Mais de <strong>16 anos</strong> transformando dados em decisões estratégicas.</p>
            <div class="badge-group">
                <span class="badge">📊 Power BI</span>
                <span class="badge">🐍 Python</span>
                <span class="badge">🗄️ SQL</span>
                <span class="badge">☁️ AWS</span>
                <span class="badge">🤖 IA Generativa</span>
                <span class="badge">📈 Dashboards</span>
            </div>
            <div class="cta-group">
                <a href="#experiencia" class="btn-primary">Ver trajetória ↓</a>
                <a href="{'Curriculo_Raphael_v2.pdf' if os.path.exists('Curriculo_Raphael_v2.pdf') else '#'}" download class="btn-secondary">📄 Baixar CV</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div></section>', unsafe_allow_html=True)
