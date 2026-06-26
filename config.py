import streamlit as st

def init_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

def get_colors():
    is_dark = st.session_state.theme == "dark"
    if is_dark:
        return {
            "primary": "#3B82F6",
            "secondary": "#0EA5E9",
            "bg": "#0B1120",
            "text": "#F1F5F9",
            "text_muted": "#94A3B8",
            "card_bg": "rgba(255,255,255,0.04)",
            "border": "rgba(255,255,255,0.08)",
            "tag_bg": "rgba(59,130,246,0.15)",
            "tag_text": "#93C5FD",
            "plotly_template": "plotly_dark",
            "chart_colors": ["#3B82F6", "#0EA5E9", "#60A5FA", "#2563EB", "#0284C7"]
        }
    else:
        # Layout claro premium
        return {
            "primary": "#1D4ED8",        # Azul mais intenso
            "secondary": "#0EA5E9",      # Ciano vibrante
            "bg": "#F1F5F9",             # Slate-50 (fundo suave)
            "text": "#0F172A",           # Slate-900
            "text_muted": "#475569",     # Slate-600
            "card_bg": "#FFFFFF",        # Branco puro
            "border": "#E2E8F0",         # Slate-200 (borda visível)
            "tag_bg": "#DBEAFE",         # Azul muito claro
            "tag_text": "#1E40AF",       # Azul escuro
            "plotly_template": "plotly_white",
            "chart_colors": ["#1D4ED8", "#0EA5E9", "#3B82F6", "#2563EB", "#0284C7"]
        }
