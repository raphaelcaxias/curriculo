import streamlit as st
from components import render_hero, render_kpis, render_experience, render_tech_stack, render_skills_chart, render_projects, render_footer

def main():
    render_hero()
    st.divider()
    render_kpis()
    st.divider()
    render_experience()
    st.divider()
    render_tech_stack()
    st.divider()
    render_skills_chart()
    st.divider()
    render_projects()
    st.divider()
    render_footer()

if __name__ == "__main__":
    main()
