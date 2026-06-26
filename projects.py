import streamlit as st

def render_projects():
    """Renderiza os projetos - Versão definitiva sem link_button"""
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Portfólio</span>
        <h2 class="section-title">Projetos em destaque</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Projetos usando HTML puro com links
    st.markdown("""
    <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 250px; background: rgba(59, 130, 246, 0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.1);">
            <h3>🇧🇷 Desenrola Brasil</h3>
            <p>Análise de dados do programa governamental, explorando renegociações e perfis de consumidores.</p>
            <a href="https://github.com/raphaelcaxias" target="_blank" style="display: inline-block; background: #3B82F6; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 500;">🔗 Acessar Repositório</a>
        </div>
        <div style="flex: 1; min-width: 250px; background: rgba(59, 130, 246, 0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.1);">
            <h3>🔬 CNPq Analytics</h3>
            <p>Dashboard analítico sobre bolsas e fomento do CNPq com cruzamento de dados de pesquisa.</p>
            <a href="https://github.com/raphaelcaxias" target="_blank" style="display: inline-block; background: #3B82F6; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 500;">🔗 Acessar Repositório</a>
        </div>
    </div>
    <div style="display: flex; gap: 2rem; flex-wrap: wrap; margin-top: 1rem;">
        <div style="flex: 1; min-width: 250px; background: rgba(59, 130, 246, 0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.1);">
            <h3>⛽ Dashboard ANP</h3>
            <p>Inteligência de dados da ANP com análise de preços e produção de combustíveis.</p>
            <a href="https://github.com/raphaelcaxias" target="_blank" style="display: inline-block; background: #3B82F6; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 500;">📊 Ver Dashboard</a>
        </div>
        <div style="flex: 1; min-width: 250px; background: rgba(59, 130, 246, 0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.1);">
            <h3>💎 Portfólio Premium</h3>
            <p>Este portfólio construído em Streamlit com design premium e visualização de dados.</p>
            <a href="https://github.com/raphaelcaxias" target="_blank" style="display: inline-block; background: #3B82F6; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 500;">💻 Ver Código</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
