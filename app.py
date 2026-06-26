import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from datetime import datetime, timedelta

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Raphael Pires | Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# TEMA
# ============================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def get_colors():
    is_dark = st.session_state.theme == "dark"
    if is_dark:
        return {
            "primary": "#3B82F6",
            "secondary": "#0EA5E9",
            "bg": "#0B1120",
            "text": "#E5E7EB",
            "text_muted": "#94A3B8",
            "card_bg": "rgba(59,130,246,0.06)",
            "border": "rgba(59,130,246,0.2)",
            "tag_bg": "rgba(59,130,246,0.12)",
            "tag_border": "rgba(59,130,246,0.25)",
            "primary_light": "rgba(59,130,246,0.2)",
            "shadow": "0 8px 16px rgba(0,0,0,0.3)",
            "shadow_hover": "0 12px 32px rgba(59,130,246,0.25)",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6","#0EA5E9","#60A5FA","#2563EB","#0284C7"]
        }
    else:
        return {
            "primary": "#1D4ED8",
            "secondary": "#0EA5E9",
            "bg": "#F1F5F9",
            "text": "#0F172A",
            "text_muted": "#475569",
            "card_bg": "#FFFFFF",
            "border": "#E2E8F0",
            "tag_bg": "#DBEAFE",
            "tag_border": "#93C5FD",
            "primary_light": "#DBEAFE",
            "shadow": "0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03)",
            "shadow_hover": "0 12px 24px -6px rgba(29,78,216,0.15), 0 4px 8px -4px rgba(0,0,0,0.05)",
            "plotly_template": "plotly_white",
            "chart_colors": ["#1D4ED8","#0EA5E9","#3B82F6","#2563EB","#0284C7"]
        }

colors = get_colors()  # será atualizado após toggle

# ============================================================
# CSS
# ============================================================
def load_css():
    c = get_colors()
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            background: {c['bg']};
            color: {c['text']};
        }}
        #MainMenu, header, footer, .stDeployButton {{ display: none !important; }}
        .stApp {{ background: {c['bg']}; }}
        .block-container {{ padding: 2rem 3rem; max-width: 1400px; }}

        .hero-section {{ text-align: center; padding: 2rem 0 1rem; margin-bottom: 1rem; }}
        .hero-name {{ font-size: 2.8rem; font-weight: 800; color: {c['text']}; letter-spacing: -0.02em; }}
        .hero-title {{ font-size: 1.1rem; font-weight: 600; color: {c['primary']}; text-transform: uppercase; letter-spacing: 0.12em; }}
        .hero-subtitle {{ font-size: 1.1rem; color: {c['text_muted']}; max-width: 720px; margin: 0 auto 1.5rem; line-height: 1.6; }}
        .tech-badge {{
            background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            padding: 0.4rem 1rem; border-radius: 999px; font-size: 0.85rem; font-weight: 500;
            color: {c['text']}; display: inline-block; margin: 0.2rem;
        }}

        .section-header {{ text-align: center; margin: 3rem 0 2rem; }}
        .section-label {{
            background: {c['primary_light']}; padding: 0.3rem 1.2rem; border-radius: 999px;
            font-size: 0.75rem; font-weight: 600; color: {c['primary']}; display: inline-block;
        }}
        .section-title {{ font-size: 2.2rem; font-weight: 700; margin-top: 0.5rem; color: {c['text']}; }}

        .kpi-box {{
            background: {c['card_bg']}; border: 1px solid {c['border']}; border-radius: 16px;
            padding: 1.5rem 1rem; text-align: center; transition: 0.3s;
            box-shadow: {c['shadow']};
        }}
        .kpi-box:hover {{ transform: translateY(-6px); border-color: {c['primary']}; box-shadow: {c['shadow_hover']}; }}
        .kpi-value {{ font-size: 2.4rem; font-weight: 700; color: {c['primary']}; }}
        .kpi-label {{ font-size: 0.9rem; color: {c['text_muted']}; }}

        .timeline {{ position: relative; padding: 2rem 0; }}
        .timeline::before {{
            content: ''; position: absolute; left: 30px; top: 0; bottom: 0;
            width: 2px; background: linear-gradient(to bottom, {c['primary']}, {c['secondary']}, transparent);
        }}
        .timeline-item {{ position: relative; padding-left: 80px; margin-bottom: 2rem; }}
        .timeline-dot {{
            position: absolute; left: 22px; top: 5px; width: 16px; height: 16px;
            border-radius: 50%; background: {c['primary']}; border: 3px solid {c['bg']};
            box-shadow: 0 0 0 3px {c['primary']};
        }}
        .timeline-card {{
            background: {c['card_bg']}; border: 1px solid {c['border']}; border-radius: 16px;
            padding: 1.5rem; transition: 0.3s; box-shadow: {c['shadow']};
        }}
        .timeline-card:hover {{ border-color: {c['primary']}; transform: translateX(5px); box-shadow: {c['shadow_hover']}; }}
        .timeline-date {{ font-size: 0.75rem; font-weight: 600; color: {c['primary']}; background: {c['primary_light']}; padding: 0.2rem 0.8rem; border-radius: 999px; display: inline-block; }}
        .timeline-role {{ font-size: 1.2rem; font-weight: 700; margin: 0.3rem 0; color: {c['text']}; }}
        .timeline-company {{ color: {c['secondary']}; font-weight: 600; }}
        .timeline-desc {{ color: {c['text_muted']}; line-height: 1.6; }}
        .timeline-tag {{
            font-size: 0.7rem; background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            padding: 0.2rem 0.6rem; border-radius: 6px; color: {c['text']}; display: inline-block; margin: 0.2rem;
        }}
        .timeline-badge {{
            background: {c['primary']}; color: white; font-size: 0.65rem; font-weight: 700;
            padding: 0.15rem 0.6rem; border-radius: 999px; margin-left: 0.5rem; display: inline-block;
        }}

        .stack-category {{ font-size: 0.9rem; font-weight: 600; color: {c['primary']}; margin: 1rem 0 0.5rem; }}
        .stack-chip {{
            background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            padding: 0.4rem 1rem; border-radius: 8px; font-size: 0.9rem; font-weight: 500;
            color: {c['text']}; display: inline-block; margin: 0.2rem;
            transition: 0.2s;
        }}
        .stack-chip:hover {{ background: {c['primary']}; color: white; transform: translateY(-2px); }}

        .testimonial-card {{
            background: {c['card_bg']}; border: 1px solid {c['border']}; border-radius: 16px;
            padding: 1.5rem; text-align: center; box-shadow: {c['shadow']};
        }}
        .testimonial-text {{ font-size: 1rem; color: {c['text']}; font-style: italic; line-height: 1.5; }}
        .testimonial-author {{ font-weight: 600; color: {c['primary']}; margin-top: 0.5rem; }}

        .cert-card {{
            background: linear-gradient(135deg, {c['primary_light']}, {c['bg']});
            border: 1px solid {c['primary']}; border-radius: 16px;
            padding: 1.5rem 2rem; text-align: center; box-shadow: {c['shadow']};
        }}
        .cert-title {{ font-size: 1.5rem; font-weight: 700; color: {c['text']}; }}
        .cert-sub {{ font-size: 1rem; color: {c['text_muted']}; }}
        .cert-badge {{ font-size: 2.5rem; }}

        .footer {{
            margin-top: 4rem; padding: 2.5rem 2rem; background: {c['card_bg']};
            border: 1px solid {c['border']}; border-radius: 16px; text-align: center;
            box-shadow: {c['shadow']};
        }}
        .footer-status {{ display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(34,197,94,0.12); border: 1px solid rgba(34,197,94,0.3); padding: 0.4rem 1rem; border-radius: 999px; }}
        .footer-status-dot {{ width: 8px; height: 8px; border-radius: 50%; background: #22C55E; box-shadow: 0 0 10px #22C55E; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
        .footer-status-text {{ font-weight: 600; color: #22C55E; }}
        .footer-title {{ font-size: 1.5rem; font-weight: 700; margin: 1rem 0 0.3rem; }}
        .footer-subtitle {{ color: {c['text_muted']}; margin-bottom: 1.5rem; }}
        .footer-mode {{ background: {c['tag_bg']}; border: 1px solid {c['tag_border']}; padding: 0.3rem 0.8rem; border-radius: 999px; font-size: 0.8rem; display: inline-block; margin: 0.2rem; }}
        .footer-link {{
            background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            padding: 0.4rem 1rem; border-radius: 8px; color: {c['text']}; text-decoration: none;
            font-size: 0.9rem; display: inline-block; margin: 0.2rem; transition: 0.2s;
        }}
        .footer-link:hover {{ background: {c['primary']}; color: white; transform: translateY(-2px); }}
        .footer-copy {{ color: {c['text_muted']}; margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid {c['border']}; }}

        .stTabs [data-baseweb="tab-list"] {{ gap: 0.5rem; background: transparent; }}
        .stTabs [data-baseweb="tab"] {{
            background: {c['tag_bg']}; border: 1px solid {c['tag_border']};
            border-radius: 8px; padding: 0.6rem 1.2rem; color: {c['text']}; font-weight: 500;
        }}
        .stTabs [aria-selected="true"] {{ background: {c['primary']} !important; color: white !important; border-color: {c['primary']} !important; }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# COMPONENTES
# ============================================================
def render_theme_toggle():
    col1, col2, col3 = st.columns([10,1,1])
    with col3:
        is_dark = st.session_state.theme == "dark"
        label = "☀️" if is_dark else "🌙"
        st.button(label, on_click=toggle_theme, key="theme_btn", use_container_width=True)

def render_hero():
    c = get_colors()
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([4,2,4])
    with col2:
        if os.path.exists("rapha.jpeg"):
            st.image("rapha.jpeg", width=160)
        else:
            st.image("https://ui-avatars.com/api/?name=Raphael+Pires&size=160&background=1D4ED8&color=fff", width=160)
    st.markdown(f"""
    <h1 class="hero-name">Raphael Fernando da Silva Pires</h1>
    <div class="hero-title">Analista de Dados & Business Intelligence</div>
    <p class="hero-subtitle">
        Mais de <strong>16 anos</strong> transformando dados brutos em decisões estratégicas. 
        Especialista em automação, governança de dados e criação de dashboards de alto impacto.
    </p>
    <div>
        <span class="tech-badge">📊 Power BI</span>
        <span class="tech-badge">🐍 Python</span>
        <span class="tech-badge">🗄️ SQL</span>
        <span class="tech-badge">☁️ AWS</span>
        <span class="tech-badge">🤖 IA Generativa</span>
        <span class="tech-badge">📈 Dashboards</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([4,2,4])
    with col2:
        if os.path.exists("Curriculo_Raphael_v2.pdf"):
            with open("Curriculo_Raphael_v2.pdf", "rb") as f:
                st.download_button("📄 Download Currículo PDF", data=f.read(), file_name="Curriculo_Raphael_Pires.pdf", mime="application/pdf", use_container_width=True)
        else:
            st.info("📄 Currículo PDF disponível")

def render_kpis():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Impacto Mensurável</span>
        <h2 class="section-title">Números que contam histórias</h2>
    </div>
    """, unsafe_allow_html=True)
    kpis = [
        ("16+", "anos de experiência em dados"),
        ("70%", "redução do tempo operacional"),
        ("213k", "registros processados com automação"),
        ("2h→15m", "tempo de análise reduzido"),
        ("R$50bi", "em dados analisados")
    ]
    cols = st.columns(5)
    for col, (val, label) in zip(cols, kpis):
        with col:
            st.markdown(f'<div class="kpi-box"><div class="kpi-value">{val}</div><div class="kpi-label">{label}</div></div>', unsafe_allow_html=True)

def render_skills_chart():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Competências</span>
        <h2 class="section-title">Domínio tecnológico</h2>
    </div>
    """, unsafe_allow_html=True)
    c = get_colors()
    df = pd.DataFrame({
        "Tecnologia": ["Power BI", "SQL/PostgreSQL", "Python", "Excel/VBA", "Streamlit", "AWS", "Plotly"],
        "Proficiência": [95, 92, 88, 95, 85, 60, 82],
        "Categoria": ["BI", "Dados", "Dados", "Automação", "BI", "Cloud", "BI"]
    })
    fig = px.bar(df, x="Proficiência", y="Tecnologia", color="Categoria", orientation="h",
                 color_discrete_sequence=c["chart_colors"], template=c["plotly_template"], text="Proficiência")
    fig.update_layout(height=380, margin=dict(l=20,r=40,t=20,b=40),
                      xaxis=dict(range=[0,105], showgrid=True, gridcolor="rgba(148,163,184,0.15)"),
                      yaxis=dict(showgrid=False), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                      font=dict(family="Inter", color=c["text"]), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_traces(textposition="outside", textfont=dict(color=c["text"], size=11))
    st.plotly_chart(fig, use_container_width=True)

def render_footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-status"><span class="footer-status-dot"></span><span class="footer-status-text">Disponível para oportunidades</span></div>
        <h3 class="footer-title">Vamos conversar sobre dados?</h3>
        <p class="footer-subtitle">Aberto a projetos em Dados, BI e Cloud</p>
        <div>
            <span class="footer-mode">🏠 Remoto</span>
            <span class="footer-mode">🏢 Híbrido</span>
            <span class="footer-mode">📍 Presencial</span>
            <span class="footer-mode">✈️ Viagens</span>
        </div>
        <div>
            <a href="https://www.linkedin.com/in/raphaelpires" target="_blank" class="footer-link">💼 LinkedIn</a>
            <a href="https://github.com/raphaelcaxias" target="_blank" class="footer-link">💻 GitHub</a>
            <a href="mailto:contato@raphaelpires.com" class="footer-link">✉️ E-mail</a>
            <a href="tel:+5511999999999" class="footer-link">📱 Telefone</a>
        </div>
        <p class="footer-copy">© 2026 Raphael Fernando da Silva Pires</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PÁGINAS
# ============================================================
def render_home():
    render_hero()
    st.divider()
    render_kpis()
    st.divider()

    # Experiência
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Trajetória</span>
        <h2 class="section-title">Experiência profissional</h2>
    </div>
    <div class="timeline">
    """, unsafe_allow_html=True)
    experiences = [
        {"date":"2014 – Presente · 10+ anos","role":"Analista de Dados & BI","company":"NSM","desc":"Centralização de dados, construção de indicadores estratégicos, automação de relatórios e governança de dados. Redução de 70% do tempo operacional.","tags":["Dados","Governança","Indicadores","Automação"],"badge":"Atual"},
        {"date":"2012 – Presente · 12+ anos","role":"Fundador & Analista de Dados","company":"Jardim do Éden","desc":"Desenvolvimento de dashboards em Power BI, automações com Python e SQL, uso de IA Generativa para análises preditivas. Redução de 2h para 15min por análise.","tags":["Power BI","Python","SQL","IA Generativa"],"badge":""},
        {"date":"2010 – 2014 · 4 anos","role":"Gestão Comercial & BI","company":"J Sintonía","desc":"Implementação de Business Intelligence, criação de KPIs, dashboards gerenciais e análise de viabilidade econômica.","tags":["BI","KPIs","Dashboards"],"badge":""},
        {"date":"2009 – 2010 · 1 ano","role":"Automação de Processos","company":"Banco do Brasil","desc":"Desenvolvimento de automações em VBA que reduziram o tempo operacional em 70%.","tags":["VBA","Automação","Eficiência"],"badge":""}
    ]
    for exp in experiences:
        tags_html = "".join([f'<span class="timeline-tag">{t}</span>' for t in exp["tags"]])
        badge_html = f'<span class="timeline-badge">{exp["badge"]}</span>' if exp["badge"] else ""
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <span class="timeline-date">{exp["date"]}</span>
                {badge_html}
                <h3 class="timeline-role">{exp["role"]}</h3>
                <div class="timeline-company">{exp["company"]}</div>
                <p class="timeline-desc">{exp["desc"]}</p>
                <div>{tags_html}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.divider()

    # Cases
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Portfólio</span>
        <h2 class="section-title">Cases de sucesso</h2>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📊 Automação de Relatórios Financeiros")
        st.write("**Economia:** R$ 500 mil/ano | **Redução:** 70% do tempo operacional")
        st.write("Automatizei a geração de relatórios financeiros usando Python e Power BI, eliminando tarefas manuais e permitindo análises em tempo real.")
        st.markdown("[🔗 Ver Case](https://github.com/raphaelcaxias)")
        st.markdown("---")
        st.markdown("### 📈 Modelo de Previsão de Demanda")
        st.write("**Acurácia:** 92% | **Impacto:** Redução de 25% em estoques")
        st.write("Desenvolvi um modelo preditivo com Python e AWS que prevê demanda com alta precisão, otimizando a cadeia de suprimentos.")
        st.markdown("[📊 Ver Projeto](https://github.com/raphaelcaxias)")
    with col2:
        st.markdown("### 🎯 Dashboard de KPIs Operacionais")
        st.write("**Aumento de eficiência:** 40% | **Adoção:** 12 times")
        st.write("Criei um dashboard interativo em Power BI com KPIs estratégicos que permitiu aos gestores monitorar desempenho em tempo real.")
        st.markdown("[🔗 Ver Dashboard](https://github.com/raphaelcaxias)")
        st.markdown("---")
        st.markdown("### ☁️ Pipeline de Dados em AWS")
        st.write("**Volume:** 1M registros/dia | **Custo:** Reduzido em 30%")
        st.write("Projetei e implementei um pipeline de dados usando AWS (S3, Glue, Athena) para processamento de grandes volumes com baixo custo.")
        st.markdown("[💻 Ver Código](https://github.com/raphaelcaxias)")
    st.divider()

    # Depoimentos
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Depoimentos</span>
        <h2 class="section-title">O que dizem sobre meu trabalho</h2>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    testimonials = [
        ("O Raphael revolucionou nossa área de dados. Reduzimos custos operacionais em 30% com suas automações.", "— Diretor de Operações, Empresa X"),
        ("Graças ao dashboard de KPIs criado pelo Raphael, passamos a tomar decisões em tempo real com segurança.", "— Gerente de BI, Empresa Y"),
        ("A expertise do Raphael em AWS e Python nos permitiu processar 1M de registros por dia com custo mínimo.", "— CTO, Startup Z")
    ]
    for col, (text, author) in zip([col1, col2, col3], testimonials):
        with col:
            st.markdown(f"""
            <div class="testimonial-card">
                <p class="testimonial-text">“{text}”</p>
                <p class="testimonial-author">{author}</p>
            </div>
            """, unsafe_allow_html=True)
    st.divider()

    # Certificação
    c = get_colors()
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Certificação</span>
        <h2 class="section-title">Objetivo para 2026</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="cert-card">
        <div class="cert-badge">🎯</div>
        <div class="cert-title">AWS Cloud Practitioner</div>
        <div class="cert-sub">Meta: <strong>Dezembro de 2026</strong> — em preparação ativa</div>
        <div style="margin-top: 0.5rem;">
            <span style="background:{c['primary']};color:white;padding:0.2rem 1rem;border-radius:999px;font-size:0.8rem;font-weight:600;">Em andamento</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    render_skills_chart()
    st.divider()
    render_footer()

def render_analytics():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Análise ao Vivo</span>
        <h2 class="section-title">Demonstração analítica</h2>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Combustíveis ANP", "📈 Impacto Operacional"])

    with tabs[0]:
        np.random.seed(42)
        regioes = ["Sudeste","Nordeste","Sul","Centro-Oeste","Norte"]
        faixas = ["Até R$5k","R$5k-15k","R$15k-50k","Acima R$50k"]
        df = pd.DataFrame({
            "Região": np.random.choice(regioes, 400, p=[0.45,0.28,0.15,0.07,0.05]),
            "Faixa": np.random.choice(faixas, 400, p=[0.55,0.28,0.12,0.05]),
            "Valor": np.random.lognormal(8.5,1.2,400),
            "Status": np.random.choice(["Renegociado","Em Negociação","Inadimplente"], 400, p=[0.65,0.25,0.10])
        })
        col1, col2 = st.columns(2)
        with col1:
            reg_sel = st.multiselect("Região", df["Região"].unique(), default=df["Região"].unique())
        with col2:
            status_sel = st.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
        filtro = df[(df["Região"].isin(reg_sel)) & (df["Status"].isin(status_sel))]
        if filtro.empty:
            st.warning("Nenhum dado para os filtros.")
        else:
            k1,k2,k3 = st.columns(3)
            k1.metric("Contratos", f"{len(filtro):,}")
            k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f}M")
            k3.metric("Taxa Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
            c = get_colors()
            fig1 = px.pie(filtro, names="Região", values="Valor", hole=0.5, color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
            fig1.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
            fig2 = px.bar(filtro.groupby("Faixa", observed=False)["Valor"].sum().reset_index(), x="Faixa", y="Valor", color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
            fig2.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
            col1, col2 = st.columns(2)
            col1.plotly_chart(fig1, use_container_width=True)
            col2.plotly_chart(fig2, use_container_width=True)

    with tabs[1]:
        np.random.seed(123)
        estados = ["SP","RJ","MG","RS","PR","BA"]
        comb = ["Gasolina","Etanol","Diesel"]
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]
        data=[]
        for e in estados:
            for c in comb:
                base = {"Gasolina":5.8,"Etanol":3.5,"Diesel":5.2}[c]
                for m in meses:
                    data.append({"Estado":e,"Combustível":c,"Mês":m,"Preço":base+np.random.normal(0,0.15)})
        df = pd.DataFrame(data)
        col1, col2 = st.columns(2)
        with col1:
            estado = st.selectbox("Estado", df["Estado"].unique())
        with col2:
            combustivel = st.selectbox("Combustível", df["Combustível"].unique())
        filtro = df[(df["Estado"]==estado) & (df["Combustível"]==combustivel)]
        if filtro.empty:
            st.warning("Nenhum dado.")
        else:
            k1, k2 = st.columns(2)
            k1.metric("Preço Atual", f"R$ {filtro[filtro['Mês']=='Jun']['Preço'].values[0]:.2f}")
            variacao = (filtro["Preço"].max() - filtro["Preço"].min()) / filtro["Preço"].min() * 100
            k2.metric("Variação Semestral", f"{variacao:.1f}%")
            c = get_colors()
            fig = px.line(filtro, x="Mês", y="Preço", markers=True, color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
            fig.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        df = pd.DataFrame({
            "Mês": meses*2,
            "Tipo": ["Antes"]*12 + ["Após"]*12,
            "Horas": [120,125,118,130,122,128,126,124,129,127,125,130] + [95,70,55,45,38,35,33,32,30,29,28,27]
        })
        c = get_colors()
        fig = px.line(df, x="Mês", y="Horas", color="Tipo", markers=True, color_discrete_sequence=[c["chart_colors"][3], c["chart_colors"][0]], template=c["plotly_template"])
        fig.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
        k1,k2,k3 = st.columns(3)
        k1.metric("Horas Economizadas", "1.108 h", "+93% eficiência")
        k2.metric("Custo Evitado", "R$ 185k", "vs. contratação")
        k3.metric("Projetos Entregues", "24", "+60% vs. anterior")

def render_dashboard():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Business Intelligence</span>
        <h2 class="section-title">Dashboard Interativo</h2>
    </div>
    """, unsafe_allow_html=True)

    # Dados simulados
    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    projetos = ["Análise de Churn","Dashboard de Vendas","Otimização de Preços","Segmentação de Clientes","Previsão de Demanda","Análise de Sentimento","Modelo de Propensão","Automação de Relatórios","Análise de ROI","Monitoramento de KPIs","Estudo de Mercado","Recomendação de Produtos"]
    regioes = ["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
    status = ["Concluído","Em Andamento","Planejado"]
    data = []
    for i in range(150):
        data.append({
            "Projeto": np.random.choice(projetos),
            "Data": np.random.choice(dates),
            "Região": np.random.choice(regioes, p=[0.45,0.20,0.18,0.10,0.07]),
            "Status": np.random.choice(status, p=[0.55,0.30,0.15]),
            "Valor": round(np.random.lognormal(9,0.8),2),
            "Horas": np.random.randint(20,400),
            "Satisfacao": np.random.randint(60,100),
            "Complexidade": np.random.choice(["Baixa","Média","Alta"], p=[0.2,0.5,0.3])
        })
    df = pd.DataFrame(data)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].dt.strftime("%Y-%m")

    # Filtros
    st.markdown("### Filtros")
    col1, col2, col3 = st.columns(3)
    with col1:
        periodo = st.selectbox("Período", ["Últimos 6 meses","Últimos 12 meses","Últimos 24 meses"], index=1)
    with col2:
        regiao = st.selectbox("Região", ["Todas"] + sorted(df["Região"].unique().tolist()))
    with col3:
        status_filtro = st.selectbox("Status", ["Todos"] + sorted(df["Status"].unique().tolist()))

    df_filtrado = df.copy()
    ultima_data = df["Data"].max()
    if periodo == "Últimos 6 meses":
        df_filtrado = df_filtrado[df_filtrado["Data"] >= ultima_data - timedelta(days=180)]
    elif periodo == "Últimos 12 meses":
        df_filtrado = df_filtrado[df_filtrado["Data"] >= ultima_data - timedelta(days=365)]
    else:
        df_filtrado = df_filtrado[df_filtrado["Data"] >= ultima_data - timedelta(days=730)]
    if regiao != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Região"] == regiao]
    if status_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status"] == status_filtro]

    # KPIs
    st.markdown("### Indicadores Gerenciais")
    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Total de Projetos", f"{len(df_filtrado):,}")
    k2.metric("Receita Total", f"R$ {df_filtrado['Valor'].sum()/1e6:.1f}M")
    k3.metric("Ticket Médio", f"R$ {df_filtrado['Valor'].mean():,.0f}".replace(",", "."))
    k4.metric("Satisfação Média", f"{df_filtrado['Satisfacao'].mean():.1f}%")

    # Gráficos
    st.markdown("### Análises Visuais")
    c = get_colors()
    fig1 = px.bar(df_filtrado.groupby("Mes").size().reset_index(name="Qtd"), x="Mes", y="Qtd", title="Projetos por Mês", color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
    fig1.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)")
    fig2 = px.pie(df_filtrado.groupby("Região")["Valor"].sum().reset_index(), names="Região", values="Valor", title="Receita por Região", hole=0.4, color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig2.update_layout(height=350, margin=dict(l=10,r=10,t=50,b=20), paper_bgcolor="rgba(0,0,0,0)")
    fig3 = px.line(df_filtrado.groupby("Mes")["Valor"].sum().reset_index().sort_values("Mes"), x="Mes", y="Valor", title="Evolução da Receita", markers=True, color_discrete_sequence=[c["chart_colors"][1]], template=c["plotly_template"])
    fig3.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)")
    fig4 = px.scatter(df_filtrado, x="Horas", y="Valor", color="Complexidade", size="Satisfacao", title="Esforço vs. Retorno", color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig4.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)")
    fig5 = px.bar(df_filtrado["Status"].value_counts().reset_index(), x="count", y="Status", orientation="h", title="Status dos Projetos", color="Status", color_discrete_sequence=c["chart_colors"][3:], template=c["plotly_template"])
    fig5.update_layout(height=300, margin=dict(l=20,r=20,t=50,b=20), showlegend=False, paper_bgcolor="rgba(0,0,0,0)")

    col1, col2 = st.columns(2)
    col1.plotly_chart(fig1, use_container_width=True)
    col2.plotly_chart(fig2, use_container_width=True)
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig3, use_container_width=True)
    col2.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("📋 Dados detalhados"):
        st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)

# ============================================================
# MAIN
# ============================================================
load_css()
render_theme_toggle()

# Sidebar
with st.sidebar:
    st.markdown("### Raphael Pires")
    st.markdown("Analista de Dados & BI")
    st.markdown("---")
    page = st.radio("Navegação", ["🏠 Início", "📈 Análises", "📊 Dashboard"], index=0, label_visibility="collapsed")
    st.markdown("---")
    st.caption("© 2026 Raphael Pires")

if page == "🏠 Início":
    render_home()
elif page == "📈 Análises":
    render_analytics()
else:
    render_dashboard()
