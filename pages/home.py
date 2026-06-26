import streamlit as st
from components import render_hero, render_kpis, render_skills_chart, render_footer
from config import get_colors

def render_testimonials():
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

def render_certification():
    colors = get_colors()
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
            <span style="background:{colors['primary']};color:white;padding:0.2rem 1rem;border-radius:999px;font-size:0.8rem;font-weight:600;">Em andamento</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_home():
    render_hero()
    st.divider()
    render_kpis()
    st.divider()

    # Experiência – ordem reordenada (NSM primeiro)
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Trajetória</span>
        <h2 class="section-title">Experiência profissional</h2>
    </div>
    <div class="timeline">
    """, unsafe_allow_html=True)

    experiences = [
        {
            "date": "2014 – Presente · 10+ anos",
            "role": "Analista de Dados & BI",
            "company": "NSM",
            "desc": "Centralização de dados, construção de indicadores estratégicos, automação de relatórios e governança de dados. Redução de 70% do tempo operacional.",
            "tags": ["Dados", "Governança", "Indicadores", "Automação"],
            "badge": "Atual"
        },
        {
            "date": "2012 – Presente · 12+ anos",
            "role": "Fundador & Analista de Dados",
            "company": "Jardim do Éden",
            "desc": "Desenvolvimento de dashboards em Power BI, automações com Python e SQL, uso de IA Generativa para análises preditivas. Redução de 2h para 15min por análise.",
            "tags": ["Power BI", "Python", "SQL", "IA Generativa"],
            "badge": ""
        },
        {
            "date": "2010 – 2014 · 4 anos",
            "role": "Gestão Comercial & BI",
            "company": "J Sintonía",
            "desc": "Implementação de Business Intelligence, criação de KPIs, dashboards gerenciais e análise de viabilidade econômica.",
            "tags": ["BI", "KPIs", "Dashboards"],
            "badge": ""
        },
        {
            "date": "2009 – 2010 · 1 ano",
            "role": "Automação de Processos",
            "company": "Banco do Brasil",
            "desc": "Desenvolvimento de automações em VBA que reduziram o tempo operacional em 70%.",
            "tags": ["VBA", "Automação", "Eficiência"],
            "badge": ""
        }
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

    # Projetos com cases reais
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
    render_testimonials()
    st.divider()

    # Certificação
    render_certification()
    st.divider()

    # Gráfico de habilidades
    render_skills_chart()
    st.divider()

    # Footer
    render_footer()
