import streamlit as st

def render_projects():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Portfólio</span>
        <h2 class="section-title">Projetos em destaque</h2>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🇧🇷 Desenrola Brasil")
        st.write("Análise de dados do programa governamental, explorando renegociações e perfis de consumidores.")
        st.markdown("[🔗 Acessar Repositório](https://github.com/raphaelcaxias)")
        st.markdown("---")
        st.markdown("### ⛽ Dashboard ANP")
        st.write("Inteligência de dados da ANP com análise de preços e produção de combustíveis.")
        st.markdown("[📊 Ver Dashboard](https://github.com/raphaelcaxias)")
    with col2:
        st.markdown("### 🔬 CNPq Analytics")
        st.write("Dashboard analítico sobre bolsas e fomento do CNPq.")
        st.markdown("[🔗 Acessar Repositório](https://github.com/raphaelcaxias)")
        st.markdown("---")
        st.markdown("### 💎 Portfólio Premium")
        st.write("Este portfólio construído em Streamlit com design premium.")
        st.markdown("[💻 Ver Código](https://github.com/raphaelcaxias)")
