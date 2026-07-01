"""
app2.py - Arquivo principal do Streamlit
"""
import streamlit as st
from config2 import get_css, get_colors, toggle_theme
from componentes2 import (
    render_navbar, render_pagina_home, render_pagina_curriculo,
    render_pagina_projetos, render_pagina_analytics, render_footer
)

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Raphael Pires · Analista de Dados & BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# INICIALIZAÇÃO DO TEMA
# ============================================================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# ============================================================================
# CARREGA CSS
# ============================================================================
colors = get_colors()
st.markdown(get_css(colors), unsafe_allow_html=True)

# ============================================================================
# NAVEGAÇÃO
# ============================================================================
page = st.query_params.get("page", "home")

if "theme_toggle" in st.query_params:
    toggle_theme()
    params = dict(st.query_params)
    params.pop("theme_toggle", None)
    st.query_params.clear()
    st.query_params.update(params)
    st.rerun()

# ============================================================================
# RENDERIZA CONTEÚDO
# ============================================================================
render_navbar(page)

if page == "home":
    render_pagina_home()
elif page == "curriculo":
    render_pagina_curriculo()
elif page == "projetos":
    render_pagina_projetos()
elif page == "analytics":
    render_pagina_analytics()
else:
    render_pagina_home()

render_footer()
