import streamlit as st

def render_projects():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Portfólio</span>
        <h2 class="section-title">Cases de sucesso</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>📊 Automação de Relatórios Financeiros</h3>
            <p>Redução de 70% do tempo de geração de relatórios com automação em VBA e integração com Power BI, economizando R$ 500k/ano.</p>
            <a href="#" class="project-link">🔗 Ver Case →</a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="project-card">
            <h3>⛽ Modelo de Previsão de Demanda</h3>
            <p>Previsão de demanda com acurácia de 92% utilizando Python e Machine Learning, otimizando estoques da ANP.</p>
            <a href="#" class="project-link">📊 Ver Dashboard →</a>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>📈 Dashboard de KPIs Operacionais</h3>
            <p>Aumento de 40% na eficiência operacional com dashboards interativos no Power BI e monitoramento em tempo real.</p>
            <a href="#" class="project-link">🔗 Ver Case →</a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="project-card">
            <h3>☁️ Pipeline de Dados em AWS</h3>
            <p>Processamento de mais de 1 milhão de registros por dia com pipeline de dados na AWS (S3, Glue, Athena).</p>
            <a href="#" class="project-link">💻 Ver Arquitetura →</a>
        </div>
        """, unsafe_allow_html=True)

def render_testimonials():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Depoimentos</span>
        <h2 class="section-title">O que dizem sobre meu trabalho</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="testimonial-card">
            <p class="testimonial-quote">"O Raphael transformou nossa área de dados, reduzindo custos operacionais em 30% com automações inteligentes."</p>
            <div class="testimonial-author">— João Silva</div>
            <div class="testimonial-role">Diretor de Operações, NSM</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="testimonial-card">
            <p class="testimonial-quote">"Graças aos dashboards criados pelo Raphael, conseguimos tomar decisões em tempo real, aumentando a eficiência do time comercial."</p>
            <div class="testimonial-author">— Maria Oliveira</div>
            <div class="testimonial-role">Gerente de BI, J Sintonía</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="testimonial-card">
            <p class="testimonial-quote">"O Raphael é um dos analistas mais completos que já trabalhei. Domina desde o tratamento de dados até a visualização e storytelling."</p>
            <div class="testimonial-author">— Carlos Mendes</div>
            <div class="testimonial-role">CTO, Startup de Tecnologia</div>
        </div>
        """, unsafe_allow_html=True)
