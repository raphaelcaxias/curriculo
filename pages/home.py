import streamlit as st
import os
from config import get_colors
from components import render_skills_chart, get_pdf_path, get_foto_path

def render_home():
    c = get_colors()

    # ===== FOTO =====
    foto_path = get_foto_path()
    if foto_path:
        foto_url = foto_path
    else:
        foto_url = "https://ui-avatars.com/api/?name=Raphael+Pires&size=280&background=1D4ED8&color=fff"

    # ===== PDF =====
    pdf_path = get_pdf_path()

    # ===== HERO =====
    st.markdown('<section class="hero-full">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        if foto_path:
            st.image(foto_path, width=220)
        else:
            st.image(foto_url, width=220)

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
                {'<a href="' + pdf_path + '" download class="btn-secondary">📄 Baixar CV</a>' if pdf_path else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</section>', unsafe_allow_html=True)

    # ===== KPIs (nativos) =====
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Impacto Mensurável</span>
                <h2>Números que contam histórias</h2>
            </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("16+", "anos de experiência")
    col2.metric("70%", "redução operacional")
    col3.metric("213k", "registros processados")
    col4.metric("2h→15m", "tempo de análise")
    col5.metric("R$50bi", "dados analisados")

    st.markdown("</div></div>", unsafe_allow_html=True)

    # ===== EXPERIÊNCIA (mantida igual) =====
    st.markdown("""
    <div class="section-glass" id="experiencia">
        <div class="container">
            <div class="section-header">
                <span class="label">Trajetória</span>
                <h2>Experiência profissional</h2>
            </div>
            <div class="timeline">
    """, unsafe_allow_html=True)

    experiences = [
        {"date":"2014 – Presente · 10+ anos","role":"Analista de Dados & BI","company":"NSM Comércio","desc":"Centralização de dados, construção de indicadores estratégicos, automação de relatórios e governança. Redução de 70% do tempo operacional.","tags":["Dados","Governança","Indicadores","Automação"],"badge":"Atual"},
        {"date":"2012 – Presente · 12+ anos","role":"Fundador & Analista de Dados","company":"Jardim do Éden (Varejo de Moda)","desc":"Estruturação da base de dados, modelagem, limpeza, integração e desenvolvimento de dashboards gerenciais com SQL, Python, Power BI e Looker Studio — reduzindo ciclo de análise de 2h para 15 min.","tags":["Power BI","Python","SQL","IA Generativa"],"badge":""},
        {"date":"2010 – 2014 · 4 anos","role":"Fundador & Analista de KPIs","company":"J Sintonía (Varejo Especializado)","desc":"Monitoramento de KPIs de vendas, margem e rentabilidade com relatórios automatizados. Análise de viabilidade econômica que fundamentou encerramento estratégico planejado em 2026, evitando prejuízo.","tags":["BI","KPIs","Dashboards"],"badge":""},
        {"date":"2009 – 2010 · 1 ano","role":"Estagiário de Automação e Dados","company":"Banco do Brasil S.A.","desc":"Desenvolvimento de macros VBA em 20 agências, reduzindo 70% do tempo operacional. Saneou e padronizou bases de dados gerenciais internas.","tags":["VBA","Automação","Eficiência"],"badge":""}
    ]

    for exp in experiences:
        tags = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        badge = f'<span class="timeline-badge">{exp["badge"]}</span>' if exp["badge"] else ""
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span> {badge}
                <div class="timeline-role">{exp["role"]}</div>
                <div class="timeline-company">{exp["company"]}</div>
                <div class="timeline-desc">{exp["desc"]}</div>
                <div>{tags}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div></div>", unsafe_allow_html=True)

    # ===== PROJETOS, CERTIFICAÇÕES, AWS JOURNEY, SKILLS (mantidos) =====
    # (coloque o restante do código como estava, não vou repetir para não alongar)
    # Você pode manter a mesma estrutura de projetos, certificações, etc.
