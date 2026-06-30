import streamlit as st
import os
from config import get_colors
from components import render_skills_chart, get_foto_url, get_pdf_path

def render_home():
    c = get_colors()

    # ===== FOTO E PDF =====
    foto_url = get_foto_url()
    pdf_path = get_pdf_path()

    # ===== HERO =====
    st.markdown('<section class="hero-full">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    with col1:
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

    # ===== KPIS =====
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

    # ===== EXPERIÊNCIA =====
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

    # ===== PROJETOS =====
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Portfólio</span>
                <h2>Projetos de Analytics</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
                <div class="glass-card">
                    <h3>🇧🇷 Desenrola Brasil</h3>
                    <p style="color:var(--text-muted);">Painel analítico executivo com Python, Pandas, Plotly e Streamlit. Processamento de dados oficiais do Banco Central com KPIs, séries temporais e análise de concentração de mercado (HHI).</p>
                    <a href="https://desenrolabrasil.streamlit.app" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">🔗 Ver App</a>
                </div>
                <div class="glass-card">
                    <h3>🔬 CNPq Analytics</h3>
                    <p style="color:var(--text-muted);">ETL e análise de mais de 213 mil bolsas e R$ 1,2 bi em investimentos públicos, evidenciando desigualdades regionais. Dashboard interativo com filtros dinâmicos.</p>
                    <a href="https://cnpa-analytics.streamlit.app" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">🔗 Ver App</a>
                </div>
                <div class="glass-card">
                    <h3>⛽ Análise de Preços de Combustíveis (ANP)</h3>
                    <p style="color:var(--text-muted);">Dashboard interativo com filtros temporais e regionais utilizando dados oficiais da Agência Nacional do Petróleo.</p>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">📊 Ver Projeto</a>
                </div>
                <div class="glass-card">
                    <h3>💎 Portfólio Premium</h3>
                    <p style="color:var(--text-muted);">Este portfólio construído em Streamlit com design premium, glassmorphism e navegação fixa. Código aberto no GitHub.</p>
                    <a href="https://github.com/raphaelcaxias" target="_blank" class="btn-primary" style="display:inline-block;margin-top:0.5rem;padding:0.4rem 1.2rem;font-size:0.85rem;">💻 Ver Código</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== CERTIFICAÇÕES =====
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Certificações</span>
                <h2>Formação contínua</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5rem;">
                <div class="glass-card" style="text-align:center;">
                    <div style="font-size:2rem;">📘</div>
                    <h4>Hashtag Treinamentos</h4>
                    <p style="color:var(--text-muted);font-size:0.9rem;">SQL Avançado · Power BI · Python para Análise de Dados · Algoritmos e IA Aplicada</p>
                </div>
                <div class="glass-card" style="text-align:center;">
                    <div style="font-size:2rem;">☁️</div>
                    <h4>AWS Educate</h4>
                    <p style="color:var(--text-muted);font-size:0.9rem;">8 módulos concluídos: Cloud Computing, Console, Storage, ML Foundations, Sustainability, Cloud Support</p>
                    <span style="background:var(--primary);color:white;padding:0.2rem 0.8rem;border-radius:999px;font-size:0.7rem;font-weight:600;">40%</span>
                </div>
                <div class="glass-card" style="text-align:center;">
                    <div style="font-size:2rem;">🎯</div>
                    <h4>Meta 2026</h4>
                    <p style="color:var(--text-muted);font-size:0.9rem;">Certificação AWS Cloud Practitioner — em preparação ativa</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== AWS JOURNEY =====
    st.markdown(f"""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Cloud Journey</span>
                <h2>☁️ AWS em progresso</h2>
                <p style="color:var(--text-muted);">Atualmente em trilha de certificação, com foco em arquitetura de dados e machine learning na nuvem.</p>
            </div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;text-align:center;">
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">📘</div><div>Cloud 101</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🖥️</div><div>AWS Console</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">💾</div><div>Storage</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🤖</div><div>ML Foundations</div></div>
                <div class="glass-card" style="padding:1rem;"><div style="font-size:2rem;">🌱</div><div>Sustainability</div></div>
            </div>
            <div style="text-align:center;margin-top:1.5rem;">
                <span style="background:{c['primary_light']};color:{c['primary']};padding:0.2rem 1.2rem;border-radius:999px;font-size:0.8rem;font-weight:600;">🎯 Meta 2026: AWS Cloud Practitioner</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== SKILLS =====
    st.markdown("""
    <div class="section-glass">
        <div class="container">
            <div class="section-header">
                <span class="label">Competências</span>
                <h2>Domínio tecnológico</h2>
            </div>
    """, unsafe_allow_html=True)
    render_skills_chart()
    st.markdown("</div></div>", unsafe_allow_html=True)
