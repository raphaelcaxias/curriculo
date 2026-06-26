import streamlit as st

def init_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

def get_colors():
    is_dark = st.session_state.theme == "dark"
    if is_dark:
        return {
            "primary": "#3B82F6", "secondary": "#0EA5E9", "bg": "#0B1120",
            "text": "#E5E7EB", "text_muted": "#94A3B8",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6","#0EA5E9","#60A5FA","#2563EB","#0284C7"],
            "card_bg": "rgba(59,130,246,0.05)", "border": "rgba(59,130,246,0.15)",
            "hover_bg": "rgba(59,130,246,0.1)"
        }
    else:
        return {
            "primary": "#2563EB", "secondary": "#0284C7", "bg": "#F8FAFC",
            "text": "#0F172A", "text_muted": "#64748B",
            "plotly_template": "plotly_white",
            "chart_colors": ["#2563EB","#0284C7","#3B82F6","#1D4ED8","#0369A1"],
            "card_bg": "rgba(59,130,246,0.03)", "border": "rgba(59,130,246,0.1)",
            "hover_bg": "rgba(59,130,246,0.06)"
        }

# Opcional: exportar constantes se precisar
